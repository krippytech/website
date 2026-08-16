#!/usr/bin/env python3
"""Validate this dependency-free static site using Python's standard library."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[2]
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

    if failures:
        print("Static-site validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Validated {len(parsers)} HTML pages: markup, internal links, and accessibility basics passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
