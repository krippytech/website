#!/usr/bin/env python3
"""Validate this dependency-free static site using Python's standard library."""

from __future__ import annotations

import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import struct
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlsplit
import zipfile


ROOT = Path(__file__).resolve().parents[2]
SITE_ORIGIN = "https://krippytech.com"
SITEMAP_URL = f"{SITE_ORIGIN}/sitemap.xml"
SITEMAP_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"
SOCIAL_IMAGE_URL = f"{SITE_ORIGIN}/assets/images/krippytech-social-card.png"
SOCIAL_IMAGE_ALT = "KrippyTech — Practical IT. Real Solutions."
NOINDEX_ROUTES = {
    "/azure-journey/",
    "/downloads/",
    "/powershell/",
    "/tutorials/shared-mailbox/",
}
SOCIAL_METADATA = {
    "/": {
        "title": "KrippyTech | Practical IT. Real Solutions.",
        "description": "KrippyTech brings together MSP University, reviewed tutorials and documented cases, plus consulting for technical assessment, troubleshooting, planning, and defined implementation support.",
        "type": "website",
    },
    "/about/": {
        "title": "About KrippyTech",
        "description": "Learn why KrippyTech exists: practical, reviewed IT guidance for technicians, IT administrators, and MSP professionals.",
        "type": "website",
    },
    "/azure-journey/": {
        "title": "Azure Journey | KrippyTech",
        "description": "Azure Journey is KrippyTech's future home for reviewed Azure learning. No Azure labs, walkthroughs, or resources are currently published.",
        "type": "website",
    },
    "/cases/": {
        "title": "KrippyTech Case Library",
        "description": "Browse KrippyTech technical cases documenting real-world IT problems, investigation paths, root causes, resolutions, and lessons learned.",
        "type": "website",
    },
    "/cases/KT-000001/": {
        "title": "KT-000001 | Shared Mailbox Not Showing in Outlook | KrippyTech",
        "description": "KT-000001 documents a Microsoft 365 shared mailbox that did not appear in Outlook after access was assigned, including investigation, resolution, and lessons learned.",
        "type": "article",
    },
    "/cases/KT-000002/": {
        "title": "KT-000002 | Exchange Online Archive Not Reducing Primary Mailbox | KrippyTech",
        "description": "KT-000002 documents an Exchange Online mailbox whose archive policy appeared correct but was not reducing the primary mailbox, including the evidence that identified a stale retention hold.",
        "type": "article",
    },
    "/consulting/": {
        "title": "KrippyTech Consulting | Practical IT Guidance",
        "description": "Contact KrippyTech for an initial conversation about practical technical assessment, troubleshooting, planning, and implementation guidance.",
        "type": "website",
    },
    "/contact/": {
        "title": "Contact KrippyTech",
        "description": "Contact KrippyTech with general questions, corrections, collaboration ideas, or an initial consulting inquiry.",
        "type": "website",
    },
    "/downloads/": {
        "title": "Downloads | KrippyTech",
        "description": "Download Test-KTDNS v1.0.0, KrippyTech's reviewed read-only DNS troubleshooting release for Windows PowerShell 5.1 and PowerShell 7.",
        "type": "website",
    },
    "/msp-university/": {
        "title": "MSP University | KrippyTech",
        "description": "Practical KrippyTech learning for technicians, solo IT administrators, and MSP professionals working in Microsoft environments.",
        "type": "website",
    },
    "/microsoft-365/": {
        "title": "Microsoft 365 & Identity | KrippyTech",
        "description": "Explore KrippyTech's published Microsoft 365 tutorials and anonymized cases across Exchange Online, identity, permissions, collaboration, and PowerShell.",
        "type": "website",
    },
    "/powershell/": {
        "title": "PowerShell Library | KrippyTech",
        "description": "Download Test-KTDNS v1.0.0, KrippyTech's first public PowerShell release for read-only DNS troubleshooting on Windows.",
        "type": "website",
    },
    "/tutorials/": {
        "title": "Tutorials | KrippyTech",
        "description": "Practical KrippyTech tutorials for Microsoft 365 and Windows troubleshooting, including reviewed procedures and clearly labeled drafts.",
        "type": "website",
    },
    "/tutorials/exchange-online-archive-not-reducing-primary-mailbox/": {
        "title": "Diagnose an Exchange Online Archive Not Reducing Primary Mailbox Usage | KrippyTech",
        "description": "A repeatable Exchange Online PowerShell procedure for diagnosing why an archive mailbox is not reducing primary mailbox usage.",
        "type": "article",
    },
    "/tutorials/dns-active-directory-domain-health/": {
        "title": "Investigating DNS, Active Directory, and Domain Health | KrippyTech",
        "description": "An evidence-first Windows domain investigation guide covering DNS, domain-controller discovery, secure channels, replication, time, services, and event logs.",
        "type": "article",
    },
    "/tutorials/entra-signin-conditional-access-investigation/": {
        "title": "Investigating Microsoft Entra Sign-ins and Conditional Access Results | KrippyTech",
        "description": "An evidence-first guide for investigating Microsoft Entra sign-ins, authentication details, device signals, and Conditional Access results without changing tenant configuration.",
        "type": "article",
    },
    "/tutorials/shared-mailbox/": {
        "title": "Create a Microsoft 365 Shared Mailbox — Draft | KrippyTech",
        "description": "Draft status for a Microsoft 365 shared-mailbox tutorial that is not approved for production use.",
        "type": "website",
    },
    "/tutorials/shared-mailbox-not-showing-outlook/": {
        "title": "Shared Mailbox Not Showing in Outlook | KrippyTech",
        "description": "How to troubleshoot a shared mailbox that does not appear in Outlook after permissions have already been assigned.",
        "type": "article",
    },
    "/tutorials/test-ktdns-v1.0.0/": {
        "title": "Use Test-KTDNS v1.0.0 for Read-Only DNS Troubleshooting | KrippyTech",
        "description": "Learn how to download, verify, review, and run Test-KTDNS v1.0.0 for read-only DNS troubleshooting on Windows.",
        "type": "article",
    },
    "/windows-hybrid/": {
        "title": "Windows & Hybrid | KrippyTech",
        "description": "Explore KrippyTech's Windows and hybrid learning lanes and the published Test-KTDNS read-only DNS troubleshooting tool.",
        "type": "website",
    },
}

TEST_KTDNS_RELEASE = ROOT / "downloads/powershell/test-ktdns/v1.0.0"
TEST_KTDNS_HASHES = {
    "LICENSE": "fbbdf22da672c4d3fa5d004c09a2c88e47d0fd66768a83523900df29a236279a",
    "README.md": "7147a9d6285cb1536a06c24830e9d692618a9c740a49b6cee4c0ed7aead5adb8",
    "SHA256SUMS.txt": "7bacb7605b636a0f3acbdf0009af4ff163d1099bb707bee14b8bf432f9732fdb",
    "Test-KTDNS.ps1": "3ba1629a7a8dcf1eb82ce97114a9047529336667bce1fb04f374f028e1340c1f",
    "Test-KTDNS-v1.0.0.zip": "7c0ed40a1ed5803fa97cc365e1439fdde77545246a2d58f0235c763494ec6c86",
    "tests/Test-KTDNS.Tests.ps1": "9abd2ef0ced72f33240c74e7ae8bcca50f51f837dee6a2a5f9dce8b3946d384c",
}
TEST_KTDNS_ZIP_MEMBERS = {
    "LICENSE",
    "README.md",
    "SHA256SUMS.txt",
    "Test-KTDNS.ps1",
    "tests/Test-KTDNS.Tests.ps1",
}

EXPECTED_HOME_JSON_LD = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Organization",
            "@id": f"{SITE_ORIGIN}/#organization",
            "name": "KrippyTech",
            "url": f"{SITE_ORIGIN}/",
            "logo": {
                "@type": "ImageObject",
                "url": f"{SITE_ORIGIN}/assets/images/krippytech-icon-512.png",
                "width": 512,
                "height": 512,
            },
            "founder": {
                "@type": "Person",
                "name": "Michael Miller",
                "url": f"{SITE_ORIGIN}/about/",
            },
            "sameAs": ["https://github.com/krippytech"],
        },
        {
            "@type": "WebSite",
            "@id": f"{SITE_ORIGIN}/#website",
            "url": f"{SITE_ORIGIN}/",
            "name": "KrippyTech",
            "publisher": {"@id": f"{SITE_ORIGIN}/#organization"},
            "inLanguage": "en-US",
        },
    ],
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
        self.meta_names: dict[str, list[str]] = {}
        self.meta_properties: dict[str, list[str]] = {}
        self.icon_links: list[dict[str, str]] = []
        self.json_ld_blocks: list[str] = []
        self.current_json_ld: list[str] | None = None

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
        elif tag == "link":
            rel_tokens = (values.get("rel") or "").lower().split()
            if "icon" in rel_tokens or "apple-touch-icon" in rel_tokens:
                self.icon_links.append({key: value or "" for key, value in values.items()})
        elif tag == "meta":
            name = (values.get("name") or "").lower()
            property_name = (values.get("property") or "").lower()
            content = values.get("content") or ""
            if name:
                self.meta_names.setdefault(name, []).append(content)
            if property_name:
                self.meta_properties.setdefault(property_name, []).append(content)
            if name == "robots":
                self.robots_directives.append(content)
        elif tag == "script" and (values.get("type") or "").lower() == "application/ld+json":
            self.current_json_ld = []
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
        if tag == "script" and self.current_json_ld is not None:
            self.json_ld_blocks.append("".join(self.current_json_ld).strip())
            self.current_json_ld = None
        if tag in VOID_TAGS:
            return
        if not self.stack:
            self.errors.append(f"unexpected closing </{tag}>")
            return
        current = self.stack.pop()
        if current != tag:
            self.errors.append(f"expected </{current}> before </{tag}>")

    def handle_data(self, data: str) -> None:
        if self.current_json_ld is not None:
            self.current_json_ld.append(data)

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


def png_dimensions(path: Path) -> tuple[int, int] | None:
    try:
        header = path.read_bytes()[:24]
    except OSError:
        return None
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", header[16:24])


def ico_sizes(path: Path) -> set[tuple[int, int]] | None:
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if len(data) < 6:
        return None
    reserved, image_type, count = struct.unpack("<HHH", data[:6])
    if reserved != 0 or image_type != 1 or len(data) < 6 + (count * 16):
        return None
    sizes: set[tuple[int, int]] = set()
    for offset in range(6, 6 + (count * 16), 16):
        width = data[offset] or 256
        height = data[offset + 1] or 256
        sizes.add((width, height))
    return sizes


def expect_exact_meta(
    relative: Path,
    collection: dict[str, list[str]],
    name: str,
    expected: str,
    failures: list[str],
) -> None:
    actual = collection.get(name, [])
    if actual != [expected]:
        failures.append(
            f"{relative}: expected exactly one {name!r} value {expected!r}; found {actual!r}"
        )


def validate_trust_and_sharing(
    parsers: dict[Path, SiteParser], failures: list[str]
) -> None:
    favicon_path = ROOT / "favicon.ico"
    master_icon_path = ROOT / "assets/images/krippytech-icon-512.png"
    apple_icon_path = ROOT / "apple-touch-icon.png"
    social_image_path = ROOT / "assets/images/krippytech-social-card.png"

    expected_dimensions = {
        master_icon_path: (512, 512),
        apple_icon_path: (180, 180),
        social_image_path: (1200, 630),
    }
    for path, expected in expected_dimensions.items():
        relative = path.relative_to(ROOT)
        if not path.is_file():
            failures.append(f"{relative}: required image asset is missing")
            continue
        actual = png_dimensions(path)
        if actual != expected:
            failures.append(f"{relative}: expected PNG dimensions {expected}; found {actual}")

    expected_ico_sizes = {(16, 16), (32, 32), (48, 48)}
    actual_ico_sizes = ico_sizes(favicon_path)
    if actual_ico_sizes != expected_ico_sizes:
        failures.append(
            f"favicon.ico: expected embedded sizes {sorted(expected_ico_sizes)}; "
            f"found {sorted(actual_ico_sizes) if actual_ico_sizes else actual_ico_sizes}"
        )

    expected_icon_links = {
        ("icon", "/favicon.ico", "16x16 32x32 48x48", ""),
        ("icon", "/assets/images/krippytech-icon-512.png", "512x512", "image/png"),
        ("apple-touch-icon", "/apple-touch-icon.png", "180x180", ""),
    }
    for path, parser in parsers.items():
        relative = path.relative_to(ROOT)
        actual_icon_links = {
            (
                link.get("rel", "").lower(),
                link.get("href", ""),
                link.get("sizes", ""),
                link.get("type", "").lower(),
            )
            for link in parser.icon_links
        }
        if len(parser.icon_links) != 3 or actual_icon_links != expected_icon_links:
            failures.append(
                f"{relative}: favicon declarations must exactly match the approved three links"
            )

    route_parsers = {
        route: parser
        for path, parser in parsers.items()
        if path.relative_to(ROOT).parts[0] != ".github"
        if (route := public_route(path)) is not None
    }
    if set(route_parsers) != set(SOCIAL_METADATA):
        failures.append(
            "social metadata policy does not exactly cover every non-404 public page"
        )

    for route, expected in sorted(SOCIAL_METADATA.items()):
        parser = route_parsers.get(route)
        if parser is None:
            continue
        relative = parser.path.relative_to(ROOT)
        expected_properties = {
            "og:site_name": "KrippyTech",
            "og:title": expected["title"],
            "og:type": expected["type"],
            "og:description": expected["description"],
            "og:url": canonical_url(route),
            "og:image": SOCIAL_IMAGE_URL,
            "og:image:alt": SOCIAL_IMAGE_ALT,
            "og:image:width": "1200",
            "og:image:height": "630",
            "og:locale": "en_US",
        }
        expected_names = {
            "twitter:card": "summary_large_image",
            "twitter:title": expected["title"],
            "twitter:description": expected["description"],
            "twitter:image": SOCIAL_IMAGE_URL,
            "twitter:image:alt": SOCIAL_IMAGE_ALT,
        }
        for name, value in expected_properties.items():
            expect_exact_meta(relative, parser.meta_properties, name, value, failures)
        for name, value in expected_names.items():
            expect_exact_meta(relative, parser.meta_names, name, value, failures)

        unexpected_og = set(parser.meta_properties) - set(expected_properties)
        unexpected_twitter = {
            name for name in parser.meta_names if name.startswith("twitter:")
        } - set(expected_names)
        if unexpected_og:
            failures.append(f"{relative}: unexpected Open Graph properties {sorted(unexpected_og)}")
        if unexpected_twitter:
            failures.append(f"{relative}: unexpected Twitter/X metadata {sorted(unexpected_twitter)}")
        if "twitter:site" in parser.meta_names:
            failures.append(f"{relative}: twitter:site is not approved")

        og_url = parser.meta_properties.get("og:url", [])
        if route not in NOINDEX_ROUTES and og_url != parser.canonicals:
            failures.append(f"{relative}: og:url must exactly match the canonical URL")
        if route in NOINDEX_ROUTES and og_url != [canonical_url(route)]:
            failures.append(f"{relative}: noindex social URL must use its clean public route")

        image_url = parser.meta_properties.get("og:image", [""])[0]
        parsed_image = urlsplit(image_url)
        if parsed_image.scheme != "https" or parsed_image.netloc != "krippytech.com":
            failures.append(f"{relative}: social image must be an absolute KrippyTech HTTPS URL")
        elif ROOT / parsed_image.path.lstrip("/") != social_image_path:
            failures.append(f"{relative}: social image URL does not map to the approved asset")

        source = parser.path.read_text(encoding="utf-8")
        title_match = re.search(r"<title>\s*(.*?)\s*</title>", source, flags=re.DOTALL)
        title = re.sub(r"\s+", " ", title_match.group(1)).strip() if title_match else ""
        if title != expected["title"]:
            failures.append(
                f"{relative}: browser title must match approved sharing title {expected['title']!r}"
            )

    not_found = parsers.get((ROOT / "404.html").resolve())
    if not_found:
        if any(name.startswith("og:") for name in not_found.meta_properties):
            failures.append("404.html: must not contain Open Graph metadata")
        if any(name.startswith("twitter:") for name in not_found.meta_names):
            failures.append("404.html: must not contain Twitter/X metadata")

    draft = route_parsers.get("/tutorials/shared-mailbox/")
    if draft:
        expect_exact_meta(
            draft.path.relative_to(ROOT),
            draft.meta_names,
            "description",
            SOCIAL_METADATA["/tutorials/shared-mailbox/"]["description"],
            failures,
        )

    approved_authorship = {
        "/tutorials/dns-active-directory-domain-health/": re.compile(
            r'Written by\s*<a href="/about/" rel="author">Michael Miller</a>\s*'
            r'<span aria-hidden="true">·</span>\s*Published\s*'
            r'<time datetime="2026-08-21">August 21, 2026</time>\s*'
            r'<span aria-hidden="true">·</span>\s*Last reviewed\s*'
            r'<time datetime="2026-08-21">August 21, 2026</time>'
        ),
        "/tutorials/entra-signin-conditional-access-investigation/": re.compile(
            r'Written by\s*<a href="/about/" rel="author">Michael Miller</a>\s*'
            r'<span aria-hidden="true">·</span>\s*Published\s*'
            r'<time datetime="2026-08-21">August 21, 2026</time>\s*'
            r'<span aria-hidden="true">·</span>\s*Last reviewed\s*'
            r'<time datetime="2026-08-21">August 21, 2026</time>'
        ),
        "/tutorials/exchange-online-archive-not-reducing-primary-mailbox/": re.compile(
            r'Written by\s*<a href="/about/" rel="author">Michael Miller</a>\s*'
            r'<span aria-hidden="true">·</span>\s*Published\s*'
            r'<time datetime="2026-08-21">August 21, 2026</time>\s*'
            r'<span aria-hidden="true">·</span>\s*Last reviewed\s*'
            r'<time datetime="2026-08-21">August 21, 2026</time>'
        ),
        "/tutorials/shared-mailbox-not-showing-outlook/": re.compile(
            r'Written by\s*<a href="/about/" rel="author">Michael Miller</a>\s*'
            r'<span aria-hidden="true">·</span>\s*Published\s*'
            r'<time datetime="2026-08-09">August 9, 2026</time>\s*'
            r'<span aria-hidden="true">·</span>\s*Last reviewed\s*'
            r'<time datetime="2026-08-16">August 16, 2026</time>'
        ),
        "/tutorials/test-ktdns-v1.0.0/": re.compile(
            r'Written by\s*<a href="/about/" rel="author">Michael Miller</a>\s*'
            r'<span aria-hidden="true">·</span>\s*Published\s*'
            r'<time datetime="2026-08-21">August 21, 2026</time>\s*'
            r'<span aria-hidden="true">·</span>\s*Last reviewed\s*'
            r'<time datetime="2026-08-21">August 21, 2026</time>'
        ),
        "/cases/KT-000001/": re.compile(
            r'Documented by\s*<a href="/about/" rel="author">Michael Miller</a>\s*'
            r'<span aria-hidden="true">·</span>\s*Published\s*'
            r'<time datetime="2026-08-11">August 11, 2026</time>'
        ),
        "/cases/KT-000002/": re.compile(
            r'Documented by\s*<a href="/about/" rel="author">Michael Miller</a>\s*'
            r'<span aria-hidden="true">·</span>\s*Published\s*'
            r'<time datetime="2026-08-21">August 21, 2026</time>'
        ),
    }
    for route, parser in route_parsers.items():
        relative = parser.path.relative_to(ROOT)
        source = parser.path.read_text(encoding="utf-8")
        pattern = approved_authorship.get(route)
        if pattern:
            if not pattern.search(source):
                failures.append(f"{relative}: approved author/date markup has drifted")
            expected_time_count = 2 if route.startswith("/tutorials/") else 1
            if source.count("<time ") != expected_time_count:
                failures.append(f"{relative}: unexpected number of visible time elements")
        elif 'rel="author"' in source or "<time " in source:
            failures.append(f"{relative}: author/date treatment is not approved for this page")

    parsed_json_ld: dict[Path, list[object]] = {}
    for path, parser in parsers.items():
        relative = path.relative_to(ROOT)
        parsed_json_ld[path] = []
        for block in parser.json_ld_blocks:
            try:
                parsed_json_ld[path].append(json.loads(block))
            except json.JSONDecodeError as error:
                failures.append(f"{relative}: invalid JSON-LD ({error})")

    home_path = (ROOT / "index.html").resolve()
    if parsed_json_ld.get(home_path) != [EXPECTED_HOME_JSON_LD]:
        failures.append(
            "index.html: JSON-LD must exactly match the approved Organization/WebSite graph"
        )
    for path, objects in parsed_json_ld.items():
        if path != home_path and objects:
            failures.append(
                f"{path.relative_to(ROOT)}: no structured data is approved on this page in this batch"
            )


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


def validate_test_ktdns_release(failures: list[str]) -> None:
    expected_files = set(TEST_KTDNS_HASHES)
    if not TEST_KTDNS_RELEASE.is_dir():
        failures.append("Test-KTDNS v1.0.0: release directory is missing")
        return

    actual_files = {
        path.relative_to(TEST_KTDNS_RELEASE).as_posix()
        for path in TEST_KTDNS_RELEASE.rglob("*")
        if path.is_file()
    }
    if actual_files != expected_files:
        failures.append(
            "Test-KTDNS v1.0.0: release files differ from the approved set; "
            f"expected {sorted(expected_files)}, found {sorted(actual_files)}"
        )

    for relative, expected_hash in TEST_KTDNS_HASHES.items():
        path = TEST_KTDNS_RELEASE / relative
        if not path.is_file():
            continue
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            failures.append(
                f"Test-KTDNS v1.0.0: SHA-256 mismatch for {relative}; "
                f"expected {expected_hash}, found {actual_hash}"
            )

    manifest_path = TEST_KTDNS_RELEASE / "SHA256SUMS.txt"
    expected_manifest = [
        f"{TEST_KTDNS_HASHES[relative]}  {relative}"
        for relative in (
            "LICENSE",
            "README.md",
            "Test-KTDNS.ps1",
            "tests/Test-KTDNS.Tests.ps1",
        )
    ]
    if manifest_path.is_file():
        actual_manifest = manifest_path.read_text(encoding="utf-8").splitlines()
        if actual_manifest != expected_manifest:
            failures.append(
                "Test-KTDNS v1.0.0: SHA256SUMS.txt does not exactly match approved files"
            )

    zip_path = TEST_KTDNS_RELEASE / "Test-KTDNS-v1.0.0.zip"
    if zip_path.is_file():
        try:
            with zipfile.ZipFile(zip_path) as archive:
                members = {
                    info.filename
                    for info in archive.infolist()
                    if not info.is_dir()
                }
                if members != TEST_KTDNS_ZIP_MEMBERS:
                    failures.append(
                        "Test-KTDNS v1.0.0: ZIP members differ from the approved set; "
                        f"expected {sorted(TEST_KTDNS_ZIP_MEMBERS)}, found {sorted(members)}"
                    )
                for member in members & TEST_KTDNS_ZIP_MEMBERS:
                    expected_hash = TEST_KTDNS_HASHES[member]
                    actual_hash = hashlib.sha256(archive.read(member)).hexdigest()
                    if actual_hash != expected_hash:
                        failures.append(
                            f"Test-KTDNS v1.0.0: ZIP member hash mismatch for {member}"
                        )
        except zipfile.BadZipFile:
            failures.append("Test-KTDNS v1.0.0: release ZIP is invalid")

    script_path = TEST_KTDNS_RELEASE / "Test-KTDNS.ps1"
    if script_path.is_file():
        script = script_path.read_text(encoding="utf-8")
        required_script_text = (
            "#requires -Version 5.1",
            "#requires -Modules DnsClient",
            "Version: 1.0.0",
            "DnsOnly     = $true",
            "E1C61B20B5888FE21B583C8E5977351F94D346D584A0DF02CF9B08A65B37F2EC",
        )
        for required in required_script_text:
            if required not in script:
                failures.append(
                    f"Test-KTDNS v1.0.0: script is missing approved text {required!r}"
                )
        prohibited_commands = re.compile(
            r"(?im)^\s*(Write-Host|Invoke-WebRequest|Invoke-RestMethod|Start-Process|"
            r"Set-Content|Add-Content|Out-File|Export-Csv|New-Item|Remove-Item|"
            r"Set-ExecutionPolicy|Get-Credential|Invoke-Expression)\b"
        )
        match = prohibited_commands.search(script)
        if match:
            failures.append(
                f"Test-KTDNS v1.0.0: prohibited command found: {match.group(1)}"
            )

    readme_path = TEST_KTDNS_RELEASE / "README.md"
    if readme_path.is_file():
        readme = readme_path.read_text(encoding="utf-8")
        required_readme_text = (
            "# Test-KTDNS v1.0.0",
            "Unblock-File -LiteralPath .\\Test-KTDNS.ps1",
            "Do not weaken or bypass the computer's global execution policy.",
            "Approved seed SHA-256: `E1C61B20B5888FE21B583C8E5977351F94D346D584A0DF02CF9B08A65B37F2EC`",
        )
        for required in required_readme_text:
            if required not in readme:
                failures.append(
                    f"Test-KTDNS v1.0.0: README is missing approved text {required!r}"
                )
        if "Set-ExecutionPolicy" in readme or "-ExecutionPolicy Bypass" in readme:
            failures.append(
                "Test-KTDNS v1.0.0: README must not recommend an execution-policy change or bypass"
            )

    public_requirements = {
        ROOT / "powershell/index.html": (
            "/downloads/powershell/test-ktdns/v1.0.0/Test-KTDNS-v1.0.0.zip",
            "/downloads/powershell/test-ktdns/v1.0.0/SHA256SUMS.txt",
            "This release is not Authenticode-signed.",
            "use Unblock-File only on Test-KTDNS.ps1",
        ),
        ROOT / "downloads/index.html": (
            "/downloads/powershell/test-ktdns/v1.0.0/Test-KTDNS-v1.0.0.zip",
            "/downloads/powershell/test-ktdns/v1.0.0/SHA256SUMS.txt",
            "The release is not Authenticode-signed.",
            "use Unblock-File only on the downloaded Test-KTDNS.ps1",
        ),
        ROOT / "tutorials/test-ktdns-v1.0.0/index.html": (
            "/downloads/powershell/test-ktdns/v1.0.0/Test-KTDNS-v1.0.0.zip",
            "/downloads/powershell/test-ktdns/v1.0.0/Test-KTDNS.ps1",
            "/downloads/powershell/test-ktdns/v1.0.0/README.md",
            "/downloads/powershell/test-ktdns/v1.0.0/SHA256SUMS.txt",
            "/powershell/#test-ktdns-v1",
            "/downloads/",
            "/windows-hybrid/",
            "This release is not Authenticode-signed.",
            "Ordinary DNS queries do not require administrator rights.",
            "does not change DNS, write files, download content, modify configuration, or handle credentials",
            "Do not weaken, bypass, or globally change execution policy.",
            "3BA1629A7A8DCF1EB82CE97114A9047529336667BCE1FB04F374F028E1340C1F",
        ),
        ROOT / "tutorials/index.html": (
            "test-ktdns-v1.0.0/",
        ),
        ROOT / "windows-hybrid/index.html": (
            "/tutorials/test-ktdns-v1.0.0/",
            "Published tutorial · DNS",
            "Additional Windows troubleshooting guides",
        ),
    }
    for page, required_text in public_requirements.items():
        source = page.read_text(encoding="utf-8")
        for required in required_text:
            if required not in source:
                failures.append(
                    f"{page.relative_to(ROOT)}: missing Test-KTDNS release text {required!r}"
                )


def validate_dns_ad_domain_health_tutorial(failures: list[str]) -> None:
    route = "/tutorials/dns-active-directory-domain-health/"
    page = ROOT / "tutorials/dns-active-directory-domain-health/index.html"
    if not page.is_file():
        failures.append(f"{route}: tutorial page is missing")
        return

    source = page.read_text(encoding="utf-8")
    required_text = (
        "Investigating DNS, Active Directory, and Domain Health",
        "This guide collects and correlates evidence. It does not automate repairs",
        "hostname",
        "whoami",
        "ipconfig /all",
        "Get-NetIPConfiguration",
        "Get-DnsClientServerAddress",
        ".\\Test-KTDNS.ps1 -Name DC01.corp.example -Type A",
        ".\\Test-KTDNS.ps1 -Name _ldap._tcp.dc._msdcs.corp.example -Type SRV",
        "Resolve-DnsName -Name _ldap._tcp.dc._msdcs.corp.example -Type SRV -Server 192.0.2.53 -DnsOnly",
        "nltest /dsgetdc:corp.example",
        "nltest /dclist:corp.example",
        "Test-ComputerSecureChannel -Verbose",
        "dcdiag /test:dns /v",
        "dcdiag /test:advertising",
        "dcdiag /test:services",
        "dcdiag /test:sysvolcheck",
        "dcdiag /test:netlogons",
        "repadmin /replsummary",
        "repadmin /showrepl",
        "w32tm /query /status",
        "w32tm /query /source",
        "Get-Service -Name NTDS,DNS,Netlogon,Kdc,W32Time,ADWS,DFSR",
        "Get-WinEvent -FilterHashtable",
        "/tutorials/test-ktdns-v1.0.0/",
        "/downloads/powershell/test-ktdns/v1.0.0/Test-KTDNS.ps1",
        "/powershell/#test-ktdns-v1",
        "/windows-hybrid/",
        "/msp-university/#learning-path",
    )
    for required in required_text:
        if required not in source:
            failures.append(f"{page.relative_to(ROOT)}: missing required guide text {required!r}")

    prohibited_text = (
        "Test-ComputerSecureChannel -Repair",
        "dcdiag /fix",
        "repadmin /syncall",
        "Set-DnsClientServerAddress",
        "Set-ExecutionPolicy",
        "-ExecutionPolicy Bypass",
    )
    for prohibited in prohibited_text:
        if prohibited.lower() in source.lower():
            failures.append(
                f"{page.relative_to(ROOT)}: prohibited remediation command found {prohibited!r}"
            )

    integrations = {
        ROOT / "tutorials/index.html": "dns-active-directory-domain-health/",
        ROOT / "windows-hybrid/index.html": route,
        ROOT / "sitemap.xml": f"{SITE_ORIGIN}{route}",
    }
    for integration, required in integrations.items():
        if required not in integration.read_text(encoding="utf-8"):
            failures.append(
                f"{integration.relative_to(ROOT)}: missing domain-health tutorial integration {required!r}"
            )


def validate_entra_signin_ca_tutorial(failures: list[str]) -> None:
    route = "/tutorials/entra-signin-conditional-access-investigation/"
    page = ROOT / "tutorials/entra-signin-conditional-access-investigation/index.html"
    if not page.is_file():
        failures.append(f"{route}: tutorial page is missing")
        return

    source = page.read_text(encoding="utf-8")
    required_text = (
        "Investigating Microsoft Entra Sign-ins and Conditional Access Results",
        "This is an investigation guide. It does not change users",
        "Reports Reader as the least-privileged role for activity logs",
        "Interactive user sign-ins",
        "Non-interactive user sign-ins",
        "Service principal sign-ins",
        "Managed identity sign-ins",
        "Previously satisfied claims",
        "A successful MFA event does not automatically prove the entire sign-in succeeded",
        "Not applied",
        "Report-only records potential impact without enforcing access",
        "A successful sign-in does not prove the device is correctly managed or compliant",
        "A blank field does not automatically prove the device is unknown, unmanaged, or malicious",
        "Observation",
        "What it may indicate",
        "What it does not prove",
        "Safest next investigation step",
        "Excluded actions include disabling users",
        "/msp-university/#learning-path",
        "/microsoft-365/",
        "/tutorials/shared-mailbox-not-showing-outlook/",
        "/tutorials/exchange-online-archive-not-reducing-primary-mailbox/",
        "https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-ins",
        "https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only",
        "https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-reports-data-retention",
    )
    for required in required_text:
        if required not in source:
            failures.append(f"{page.relative_to(ROOT)}: missing required guide text {required!r}")

    prohibited_text = (
        "Revoke-MgUserSignInSession",
        "Update-MgIdentityConditionalAccessPolicy",
        "Remove-MgDevice",
        "Set-MgUserAuthenticationMethod",
        "Set-MgPolicyIdentitySecurityDefaultEnforcementPolicy",
        "New-MgRoleManagementDirectoryRoleAssignment",
    )
    for prohibited in prohibited_text:
        if prohibited.lower() in source.lower():
            failures.append(
                f"{page.relative_to(ROOT)}: prohibited tenant-changing command found {prohibited!r}"
            )

    integrations = {
        ROOT / "tutorials/index.html": "entra-signin-conditional-access-investigation/",
        ROOT / "microsoft-365/index.html": route,
        ROOT / "sitemap.xml": f"{SITE_ORIGIN}{route}",
    }
    for integration, required in integrations.items():
        if required not in integration.read_text(encoding="utf-8"):
            failures.append(
                f"{integration.relative_to(ROOT)}: missing Entra tutorial integration {required!r}"
            )


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
    validate_trust_and_sharing(parsers, failures)
    validate_test_ktdns_release(failures)
    validate_dns_ad_domain_health_tutorial(failures)
    validate_entra_signin_ca_tutorial(failures)

    if failures:
        print("Static-site validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        f"Validated {len(parsers)} HTML pages: markup, internal links, accessibility basics, "
        "robots.txt, sitemap.xml, canonical URLs, indexability directives, favicons, social "
        "metadata, authorship dates, and structured data passed."
    )
    print("Warnings: none.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
