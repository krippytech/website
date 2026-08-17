#!/usr/bin/env python3
"""Validate this dependency-free static site using Python's standard library."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[2]
SITE_ORIGIN = "https://krippytech.com"
SITEMAP_URL = f"{SITE_ORIGIN}/sitemap.xml"
SITEMAP_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"
NOINDEX_ROUTES = {
    "/azure-journey/",
    "/downloads/",
    "/powershell/",
    "/tutorials/shared-mailbox/",
}
VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}


class SiteParser(HTMLParser):
    def __init__(self, path: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.path = path
        self.stack: list[str] = []
        self.links: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.errors: list[str] = []
        self.h1_count = 0
        self.has_title = False
        self.html_has_lang = False
        self.canonicals: list[str] = []
        self.robots_directives: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag not in VOID_TAGS:
            self.stack.append(tag)
        if tag == "html":
            self.html_has_lang = bool(values.get("lang"))
        elif tag == "title":
            self.has_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "img" and not values.get("alt"):
            self.errors.append("image is missing non-empty alt text")
        elif tag == "link" and "canonical" in (values.get("rel") or "").lower().split():
            self.canonicals.append(values.get("href") or "")
        elif tag == "meta" and (values.get("name") or "").lower() == "robots":
            self.robots_directives.append(values.get("content") or "")
        if values.get("id"):
            self.ids.add(values["id"] or "")
        for attr in ("href", "src"):
            if values.get(attr):
                self.links.append((attr, values[attr] or ""))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS:
            self.stack.pop()

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID_TAGS:
            return
        if not self.stack:
            self.errors.append(f"unexpected closing </{tag}>")
            return
        current = self.stack.pop()
        if current != tag:
            self.errors.append(f"expected </{current}> before </{tag}>")

    def finish(self) -> None:
        if self.stack:
            self.errors.append("unclosed tags: " + ", ".join(self.stack))
        if not self.html_has_lang:
            self.errors.append("<html> is missing a lang attribute")
        if not self.has_title:
            self.errors.append("document is missing a <title>")
        if self.h1_count != 1:
            self.errors.append(f"expected exactly one <h1>; found {self.h1_count}")


def resolve_target(source: Path, raw_url: str) -> tuple[Path | None, str]:
    parsed = urlsplit(raw_url)
    if parsed.scheme or parsed.netloc or raw_url.startswith(("mailto:", "tel:")):
        return None, ""
    fragment = unquote(parsed.fragment)
    if not parsed.path:
        return source, fragment
    relative = Path(unquote(parsed.path.lstrip("/"))) if parsed.path.startswith("/") else source.parent / unquote(parsed.path)
    target = (ROOT / relative).resolve() if not relative.is_absolute() else relative.resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        return Path("__outside_site__"), fragment
    if target.is_dir() or parsed.path.endswith("/"):
        target /= "index.html"
    return target, fragment


def public_route(path: Path) -> str | None:
    relative = path.resolve().relative_to(ROOT)
    if relative.parts[0] == ".github" or relative == Path("404.html"):
        return None
    if relative == Path("index.html"):
        return "/"
    if relative.name == "index.html":
        return f"/{relative.parent.as_posix()}/"
    return None


def canonical_url(route: str) -> str:
    return f"{SITE_ORIGIN}{route}"


def sitemap_target(raw_url: str) -> Path | None:
    parsed = urlsplit(raw_url)
    if parsed.scheme != "https" or parsed.netloc != "krippytech.com":
        return None
    if parsed.query or parsed.fragment or not parsed.path.endswith("/"):
        return None
    if parsed.path == "/":
        return ROOT / "index.html"
    return ROOT / parsed.path.lstrip("/") / "index.html"


def validate_crawl_baseline(
    parsers: dict[Path, SiteParser], failures: list[str]
) -> None:
    public_parsers = {
        path: parser
        for path, parser in parsers.items()
        if path.relative_to(ROOT).parts[0] != ".github"
    }
    route_parsers = {
        route: parser
        for path, parser in public_parsers.items()
        if (route := public_route(path)) is not None
    }

    robots_path = ROOT / "robots.txt"
    if not robots_path.is_file():
        failures.append("robots.txt: file is missing")
    else:
        robots_lines = [
            line.strip() for line in robots_path.read_text(encoding="utf-8").splitlines()
        ]
        if not any(line.lower() == "user-agent: *" for line in robots_lines):
            failures.append("robots.txt: missing User-agent: *")
        if not any(line.lower() == "allow: /" for line in robots_lines):
            failures.append("robots.txt: missing Allow: /")
        blocked_paths = [
            line for line in robots_lines
            if line.lower().startswith("disallow:") and line.partition(":")[2].strip()
        ]
        if blocked_paths:
            failures.append(
                "robots.txt: public crawling must not be blocked; found "
                + ", ".join(blocked_paths)
            )
        if not any(line.lower() == f"sitemap: {SITEMAP_URL}".lower() for line in robots_lines):
            failures.append(f"robots.txt: missing Sitemap: {SITEMAP_URL}")

    sitemap_path = ROOT / "sitemap.xml"
    sitemap_urls: list[str] = []
    if not sitemap_path.is_file():
        failures.append("sitemap.xml: file is missing")
    else:
        try:
            sitemap_root = ET.parse(sitemap_path).getroot()
        except ET.ParseError as error:
            failures.append(f"sitemap.xml: invalid XML ({error})")
        else:
            if sitemap_root.tag != f"{{{SITEMAP_NAMESPACE}}}urlset":
                failures.append("sitemap.xml: root must be the standard sitemap urlset")
            sitemap_urls = [
                (element.text or "").strip()
                for element in sitemap_root.findall(
                    f"{{{SITEMAP_NAMESPACE}}}url/{{{SITEMAP_NAMESPACE}}}loc"
                )
            ]

    if len(sitemap_urls) != len(set(sitemap_urls)):
        failures.append("sitemap.xml: contains duplicate URLs")

    sitemap_routes: set[str] = set()
    for url in sitemap_urls:
        parsed = urlsplit(url)
        target = sitemap_target(url)
        if parsed.scheme != "https":
            failures.append(f"sitemap.xml: URL must use HTTPS: {url!r}")
        if parsed.netloc != "krippytech.com":
            failures.append(f"sitemap.xml: URL must use apex domain krippytech.com: {url!r}")
        if parsed.query or parsed.fragment:
            failures.append(f"sitemap.xml: URL must not contain a query or fragment: {url!r}")
        if not parsed.path.endswith("/"):
            failures.append(f"sitemap.xml: URL must use a trailing slash: {url!r}")
        if target is None or not target.is_file() or public_route(target) is None:
            failures.append(f"sitemap.xml: URL does not map to a public page: {url!r}")
        else:
            sitemap_routes.add(parsed.path)

    expected_indexable_routes = set(route_parsers) - NOINDEX_ROUTES
    missing_routes = expected_indexable_routes - sitemap_routes
    extra_routes = sitemap_routes - expected_indexable_routes
    for route in sorted(missing_routes):
        failures.append(f"sitemap.xml: missing indexable page {canonical_url(route)}")
    for route in sorted(extra_routes):
        failures.append(f"sitemap.xml: must not include {canonical_url(route)}")

    all_canonicals: list[tuple[str, Path]] = []
    for route, parser in sorted(route_parsers.items()):
        relative = parser.path.relative_to(ROOT)
        robots_tokens = [
            {
                token.lower()
                for token in directive.replace(",", " ").split()
                if token
            }
            for directive in parser.robots_directives
        ]
        if route in NOINDEX_ROUTES:
            if len(robots_tokens) != 1 or robots_tokens[0] != {"noindex", "follow"}:
                failures.append(
                    f"{relative}: expected exactly one robots directive with noindex, follow"
                )
            if route in sitemap_routes:
                failures.append(f"{relative}: noindex page appears in sitemap.xml")
        else:
            if any("noindex" in tokens for tokens in robots_tokens):
                failures.append(f"{relative}: indexable page must not contain noindex")
            expected_canonical = canonical_url(route)
            if parser.canonicals != [expected_canonical]:
                failures.append(
                    f"{relative}: expected exactly one canonical {expected_canonical!r}; "
                    f"found {parser.canonicals!r}"
                )
        all_canonicals.extend((value, parser.path) for value in parser.canonicals)

    canonical_sources: dict[str, list[Path]] = {}
    for value, path in all_canonicals:
        canonical_sources.setdefault(value, []).append(path)
    for value, paths in canonical_sources.items():
        if len(paths) > 1:
            sources = ", ".join(str(path.relative_to(ROOT)) for path in paths)
            failures.append(f"canonical URL {value!r} is duplicated by: {sources}")

    not_found_parser = public_parsers.get((ROOT / "404.html").resolve())
    if not_found_parser and not_found_parser.canonicals:
        failures.append("404.html: must not contain a canonical URL")
    if "/404.html" in sitemap_routes or f"{SITE_ORIGIN}/404.html" in sitemap_urls:
        failures.append("sitemap.xml: 404.html must be excluded")


def main() -> int:
    parsers: dict[Path, SiteParser] = {}
    failures: list[str] = []

    for path in sorted(ROOT.rglob("*.html")):
        parser = SiteParser(path)
        parser.feed(path.read_text(encoding="utf-8"))
        parser.close()
        parser.finish()
        parsers[path.resolve()] = parser
        failures.extend(f"{path.relative_to(ROOT)}: {error}" for error in parser.errors)

    for source, parser in parsers.items():
        for attr, raw_url in parser.links:
            target, fragment = resolve_target(source, raw_url)
            if target is None:
                continue
            if not target.exists():
                failures.append(
                    f"{source.relative_to(ROOT)}: broken {attr}={raw_url!r}"
                )
                continue
            if fragment and target.suffix.lower() == ".html":
                target_parser = parsers.get(target.resolve())
                if target_parser and fragment not in target_parser.ids:
                    failures.append(
                        f"{source.relative_to(ROOT)}: missing fragment #{fragment} in "
                        f"{target.relative_to(ROOT)}"
                    )

    validate_crawl_baseline(parsers, failures)

    if failures:
        print("Static-site validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        f"Validated {len(parsers)} HTML pages: markup, internal links, accessibility basics, "
        "robots.txt, sitemap.xml, canonical URLs, and indexability directives passed."
    )
    print("Warnings: none.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
