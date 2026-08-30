#!/usr/bin/env python3
"""Validate this dependency-free static site using Python's standard library."""

from __future__ import annotations

import hashlib
import html
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
    "/everyday-it/": {
        "title": "Everyday IT | KrippyTech",
        "description": "Real-world guidance for the IT work people actually get asked to do every day.",
        "type": "website",
    },
    "/everyday-it/active-directory/": {
        "title": "Active Directory Basics | Everyday IT | KrippyTech",
        "description": "Practical Active Directory guidance for everyday IT work: OUs, users, groups, logon issues, lockouts, safe changes, and what not to touch casually.",
        "type": "article",
    },
    "/everyday-it/groups-permissions/": {
        "title": "Groups & Permissions | Everyday IT | KrippyTech",
        "description": "Plain-English guidance for security groups, distribution lists, NTFS and share permissions, access denied troubleshooting, and role-based access.",
        "type": "article",
    },
    "/everyday-it/microsoft-365-email/": {
        "title": "Microsoft 365 & Email Basics | Everyday IT | KrippyTech",
        "description": "Practical Microsoft 365 and email guidance for licensing, user and shared mailboxes, distribution lists, mail flow, and basic message trace troubleshooting.",
        "type": "article",
    },
    "/everyday-it/new-user-setup/": {
        "title": "New User Setup | Everyday IT | KrippyTech",
        "description": "A practical new-user onboarding guide for office IT: Active Directory, Microsoft 365 licensing, groups, email, access, devices, verification, and common mistakes.",
        "type": "article",
    },
    "/everyday-it/office-it-admin-survival-guide/": {
        "title": "Office IT Admin Survival Guide | KrippyTech",
        "description": "A practical real-world course outline covering new-user onboarding, Active Directory, permissions, Microsoft 365, printers, SharePoint, OneDrive, MFA, troubleshooting, and escalation.",
        "type": "article",
    },
    "/everyday-it/passwords-mfa/": {
        "title": "Passwords, Lockouts & MFA | Everyday IT | KrippyTech",
        "description": "A practical guide to password resets, account lockouts, cached credentials, Microsoft MFA issues, device-specific symptoms, verification, and safe escalation.",
        "type": "article",
    },
    "/everyday-it/printers/": {
        "title": "Printer Troubleshooting | Everyday IT | KrippyTech",
        "description": "A practical office printer troubleshooting guide covering drivers, ports, queues, spooler issues, test prints, network checks, and safe escalation.",
        "type": "article",
    },
    "/everyday-it/sharepoint-onedrive/": {
        "title": "SharePoint & OneDrive Basics | Everyday IT | KrippyTech",
        "description": "Practical SharePoint and OneDrive guidance for permissions, sync issues, browser-vs-Explorer problems, and common access complaints.",
        "type": "article",
    },
    "/everyday-it/troubleshooting-escalation/": {
        "title": "Troubleshooting & Escalation | Everyday IT | KrippyTech",
        "description": "A practical troubleshooting framework for everyday IT: scope the issue, ask what changed, test one layer at a time, verify the fix, and know when to escalate.",
        "type": "article",
    },
    "/everyday-it/onedrive-free-up-space/": {
        "title": "Recover Disk Space with OneDrive Files On-Demand | Everyday IT | KrippyTech",
        "description": "Use OneDrive Files On-Demand to release local cached copies without deleting the cloud files.",
        "type": "article",
    },
    "/everyday-it/outlook-profile-rebuild/": {
        "title": "Rebuild an Outlook Profile | Everyday IT | KrippyTech",
        "description": "Rebuild a Classic Outlook profile safely when the desktop client is misbehaving but the mailbox itself is healthy.",
        "type": "article",
    },
    "/everyday-it/scan-to-email/": {
        "title": "Scan to Email Troubleshooting | Everyday IT | KrippyTech",
        "description": "Use timestamps and evidence to prove whether a scan-to-email delay occurred before or after Microsoft 365 received the message.",
        "type": "article",
    },
    "/everyday-it/scanner-troubleshooting/": {
        "title": "Scanner Troubleshooting | Everyday IT | KrippyTech",
        "description": "Troubleshoot a scanner by separating the physical connection, Windows detection, vendor software, and workstation performance layers.",
        "type": "article",
    },
    "/everyday-it/vpn-troubleshooting/": {
        "title": "VPN Troubleshooting | Everyday IT | KrippyTech",
        "description": "Prove where a VPN connection fails before reinstalling clients or changing firewall settings.",
        "type": "article",
    },
    "/everyday-it/windows-temp-cleanup/": {
        "title": "Clear Windows Temp Files Safely | Everyday IT | KrippyTech",
        "description": "Clear common Windows Temp locations safely, skip files that are in use, and avoid deleting the Temp folders themselves.",
        "type": "article",
    },
    "/everyday-it/mapped-drives-access/": {
        "title": "Mapped Drives & File Access | Everyday IT | KrippyTech",
        "description": "A practical guide to missing mapped drives, UNC paths, SMB shares, permissions, SharePoint and OneDrive confusion, and safe file-access troubleshooting.",
        "type": "article",
    },
    "/everyday-it/scan-to-folder/": {
        "title": "Scan to Folder Troubleshooting | Everyday IT | KrippyTech",
        "description": "A practical guide to setting up and troubleshooting scan-to-folder with SMB shares, UNC paths, permissions, service accounts, and copier testing.",
        "type": "article",
    },
    "/everyday-it/vpn-mapped-drive/": {
        "title": "VPN Works but the Drive Does Not | Everyday IT | KrippyTech",
        "description": "A practical guide for troubleshooting mapped drives and internal file access after a VPN tunnel connects successfully.",
        "type": "article",
    },
    "/everyday-it/new-pc-setup/": {
        "title": "New PC Setup Checklist | Everyday IT | KrippyTech",
        "description": "Set up a replacement workstation by validating identity, data, apps, peripherals, updates, and the user's real workflow.",
        "type": "article",
    },
    "/everyday-it/office-account-licensing/": {
        "title": "Office Account & Licensing Problems | Everyday IT | KrippyTech",
        "description": "Separate Office activation, account ownership, and Microsoft 365 licensing before reinstalling applications.",
        "type": "article",
    },
    "/everyday-it/outlook-vs-web/": {
        "title": "Outlook vs Outlook on the Web | Everyday IT | KrippyTech",
        "description": "Use Outlook on the web to prove whether an email problem is in Microsoft 365 or the local Outlook client.",
        "type": "article",
    },
    "/everyday-it/when-to-replace-workstation/": {
        "title": "When to Replace a Workstation | Everyday IT | KrippyTech",
        "description": "Use repeat failures, severe slowness, failing storage, constant resource pressure, and repair history to decide when to stop troubleshooting.",
        "type": "article",
    },
    "/everyday-it/former-employee-mailbox/": {
        "title": "Former Employee Mailbox Handling | Everyday IT | KrippyTech",
        "description": "Handle a departing employee's mailbox safely by separating account access, mailbox retention, shared-mailbox use, delegation, and verification.",
        "type": "article",
    },
    "/everyday-it/message-trace-delivery/": {
        "title": "Message Trace: Prove Delivery | Everyday IT | KrippyTech",
        "description": "Use exact timestamps and message trace to prove whether Microsoft 365 received, delayed, delivered, rejected, or quarantined a message.",
        "type": "article",
    },
    "/everyday-it/outlook-signature-troubleshooting/": {
        "title": "Outlook Signature Troubleshooting | Everyday IT | KrippyTech",
        "description": "Use Outlook-versus-web comparison and a clean test signature to separate client formatting, roaming signature, and mail-flow causes.",
        "type": "article",
    },
    "/everyday-it/shared-mailbox-permissions/": {
        "title": "Shared Mailbox Permissions | Everyday IT | KrippyTech",
        "description": "Understand Full Access, Send As, Send on Behalf, propagation, and shared mailbox verification without guessing.",
        "type": "article",
    },
    "/everyday-it/calendar-sharing-troubleshooting/": {
        "title": "Calendar Sharing Troubleshooting | Everyday IT | KrippyTech",
        "description": "Identify the mailbox, tenant, sharing policy, and recipient domain before changing calendar permissions.",
        "type": "article",
    },
    "/everyday-it/mobile-exchange-sync/": {
        "title": "Mobile Exchange Sync Troubleshooting | Everyday IT | KrippyTech",
        "description": "Separate mailbox health from stale Apple Mail authentication and token state after Microsoft security changes.",
        "type": "article",
    },
    "/everyday-it/outlook-profile-creation-fails/": {
        "title": "Outlook Profile Creation Fails | Everyday IT | KrippyTech",
        "description": "Use web sign-in, connectivity, Office state, cached credentials, and Autodiscover evidence before repeatedly rebuilding Outlook.",
        "type": "article",
    },
    "/everyday-it/sharepoint-sync-troubleshooting/": {
        "title": "SharePoint Sync Troubleshooting | Everyday IT | KrippyTech",
        "description": "Separate SharePoint library sync, OneDrive shortcuts, browser access, and local File Explorer state before rebuilding anything.",
        "type": "article",
    },
    "/about/": {
        "title": "About KrippyTech",
        "description": "Learn why KrippyTech exists: practical, reviewed IT guidance for technicians, IT administrators, and MSP professionals.",
        "type": "website",
    },
    "/azure-journey/": {
        "title": "Azure Journey | KrippyTech",
        "description": "Azure Journey connects KrippyTech's published Azure VM connectivity guide and companion lab with developing Azure foundations, identity, networking, and hybrid learning.",
        "type": "website",
    },
    "/azure-journey/labs/map-azure-vm-network-path/": {
        "title": "Map the Network Path to an Azure VM | KrippyTech",
        "description": "A self-contained synthetic lab for mapping an Azure VM network path, correlating evidence, and writing an escalation-quality finding.",
        "type": "article",
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
        "description": "Practical KrippyTech tutorials for Microsoft 365, Windows, and Azure troubleshooting, including reviewed procedures and clearly labeled drafts.",
        "type": "website",
    },
    "/tutorials/azure-vm-connectivity-investigation/": {
        "title": "Investigating Azure VM Connectivity | KrippyTech",
        "description": "An evidence-first guide for investigating Azure virtual-machine connectivity before changing network, platform, or guest configuration.",
        "type": "article",
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
    "/tutorials/dhcp-scope-capacity-investigation/": {
        "title": "Investigating DHCP Scope Capacity and Address Exhaustion | KrippyTech",
        "description": "Investigate DHCP scope utilization, leases, reservations, exclusions, failover, and monitoring evidence before planning a capacity change.",
        "type": "article",
    },
    "/tutorials/entra-signin-conditional-access-investigation/": {
        "title": "Investigating Microsoft Entra Sign-ins and Conditional Access Results | KrippyTech",
        "description": "An evidence-first guide for investigating Microsoft Entra sign-ins, authentication details, device signals, and Conditional Access results without changing tenant configuration.",
        "type": "article",
    },
    "/tutorials/onedrive-sharepoint-sync-investigation/": {
        "title": "Investigating OneDrive and SharePoint Sync Problems | KrippyTech",
        "description": "An evidence-first guide for investigating OneDrive and SharePoint synchronization problems before changing accounts, relationships, files, or permissions.",
        "type": "article",
    },
    "/tutorials/windows-server-low-disk-space-investigation/": {
        "title": "Investigating Low Disk Space on Windows Server | KrippyTech",
        "description": "An evidence-first guide for investigating low disk space on Windows Server before deleting data, changing retention, or expanding storage.",
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
    "/tutorials/get-ktnetworkconfig-v1.0.0/": {
        "title": "Inspecting Local Windows Network Configuration with Get-KTNetworkConfig | KrippyTech",
        "description": "Learn how to verify, run, and interpret Get-KTNetworkConfig v1.0.0 before choosing the next Windows network diagnostic step.",
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

GET_KTNETWORKCONFIG_RELEASE = ROOT / "downloads/powershell/get-ktnetworkconfig/v1.0.0"
GET_KTNETWORKCONFIG_HASHES = {
    "Get-KTNetworkConfig.ps1": "eada2bbdde5c0b62bb97d82d4db4a70259cb8cc8dc9d65ca9d52e9384ff2c5c1",
    "README.md": "48b4ee70ac398ea5ac6ba070614d10dce8c6b69de5117528b776b4896cf9b3e1",
    "LICENSE": "fbbdf22da672c4d3fa5d004c09a2c88e47d0fd66768a83523900df29a236279a",
    "SHA256SUMS.txt": "72c7d8b381bd83f48228bf822c77e4f23b88d87e44724cf3d18ecb13f12de8a8",
    "tests/Get-KTNetworkConfig.Tests.ps1": "d0fde152de0a6c79e1601ebf3ec3aadb5735ad193cdb8ad6b76deaec3b1c31b1",
    "Get-KTNetworkConfig-v1.0.0.zip": "8b93938eef5ab39bcff393330b5666d1a52d45e95933500b75934e0b520f0fda",
}
GET_KTNETWORKCONFIG_ZIP_MEMBERS = {
    "Get-KTNetworkConfig.ps1",
    "README.md",
    "LICENSE",
    "SHA256SUMS.txt",
    "tests/Get-KTNetworkConfig.Tests.ps1",
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
        title = html.unescape(re.sub(r"\s+", " ", title_match.group(1)).strip()) if title_match else ""
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
        "/tutorials/windows-server-low-disk-space-investigation/": re.compile(
            r'Written by\s*<a href="/about/" rel="author">Michael Miller</a>\s*'
            r'<span aria-hidden="true">·</span>\s*Published\s*'
            r'<time datetime="2026-08-22">August 22, 2026</time>\s*'
            r'<span aria-hidden="true">·</span>\s*Last reviewed\s*'
            r'<time datetime="2026-08-22">August 22, 2026</time>'
        ),
        "/tutorials/dhcp-scope-capacity-investigation/": re.compile(
            r'Written by\s*<a href="/about/" rel="author">Michael Miller</a>\s*'
            r'<span aria-hidden="true">·</span>\s*Published\s*'
            r'<time datetime="2026-08-22">August 22, 2026</time>\s*'
            r'<span aria-hidden="true">·</span>\s*Last reviewed\s*'
            r'<time datetime="2026-08-22">August 22, 2026</time>'
        ),
        "/tutorials/onedrive-sharepoint-sync-investigation/": re.compile(
            r'Written by\s*<a href="/about/" rel="author">Michael Miller</a>\s*'
            r'<span aria-hidden="true">·</span>\s*Published\s*'
            r'<time datetime="2026-08-22">August 22, 2026</time>\s*'
            r'<span aria-hidden="true">·</span>\s*Last reviewed\s*'
            r'<time datetime="2026-08-22">August 22, 2026</time>'
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
        "/tutorials/get-ktnetworkconfig-v1.0.0/": re.compile(
            r'Written by\s*<a href="/about/" rel="author">Michael Miller</a>\s*'
            r'<span aria-hidden="true">·</span>\s*Published\s*'
            r'<time datetime="2026-08-22">August 22, 2026</time>\s*'
            r'<span aria-hidden="true">·</span>\s*Last reviewed\s*'
            r'<time datetime="2026-08-22">August 22, 2026</time>'
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


def validate_get_ktnetworkconfig_release(failures: list[str]) -> None:
    expected_files = set(GET_KTNETWORKCONFIG_HASHES)
    if not GET_KTNETWORKCONFIG_RELEASE.is_dir():
        failures.append("Get-KTNetworkConfig v1.0.0: release directory is missing")
        return

    actual_files = {
        path.relative_to(GET_KTNETWORKCONFIG_RELEASE).as_posix()
        for path in GET_KTNETWORKCONFIG_RELEASE.rglob("*")
        if path.is_file()
    }
    if actual_files != expected_files:
        failures.append(
            "Get-KTNetworkConfig v1.0.0: release files differ from the approved set; "
            f"expected {sorted(expected_files)}, found {sorted(actual_files)}"
        )

    for relative, expected_hash in GET_KTNETWORKCONFIG_HASHES.items():
        path = GET_KTNETWORKCONFIG_RELEASE / relative
        if not path.is_file():
            continue
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            failures.append(
                f"Get-KTNetworkConfig v1.0.0: SHA-256 mismatch for {relative}; "
                f"expected {expected_hash}, found {actual_hash}"
            )

    manifest_path = GET_KTNETWORKCONFIG_RELEASE / "SHA256SUMS.txt"
    expected_manifest = [
        f"{GET_KTNETWORKCONFIG_HASHES[relative].upper()}  {relative}"
        for relative in (
            "Get-KTNetworkConfig.ps1",
            "README.md",
            "LICENSE",
            "tests/Get-KTNetworkConfig.Tests.ps1",
        )
    ]
    if manifest_path.is_file():
        actual_manifest = manifest_path.read_text(encoding="utf-8").splitlines()
        if actual_manifest != expected_manifest:
            failures.append(
                "Get-KTNetworkConfig v1.0.0: SHA256SUMS.txt does not exactly match approved files"
            )

    zip_path = GET_KTNETWORKCONFIG_RELEASE / "Get-KTNetworkConfig-v1.0.0.zip"
    if zip_path.is_file():
        try:
            with zipfile.ZipFile(zip_path) as archive:
                members = {
                    info.filename
                    for info in archive.infolist()
                    if not info.is_dir()
                }
                if members != GET_KTNETWORKCONFIG_ZIP_MEMBERS:
                    failures.append(
                        "Get-KTNetworkConfig v1.0.0: ZIP members differ from the approved set; "
                        f"expected {sorted(GET_KTNETWORKCONFIG_ZIP_MEMBERS)}, found {sorted(members)}"
                    )
                for member in members & GET_KTNETWORKCONFIG_ZIP_MEMBERS:
                    expected_hash = GET_KTNETWORKCONFIG_HASHES[member]
                    actual_hash = hashlib.sha256(archive.read(member)).hexdigest()
                    if actual_hash != expected_hash:
                        failures.append(
                            f"Get-KTNetworkConfig v1.0.0: ZIP member hash mismatch for {member}"
                        )
        except zipfile.BadZipFile:
            failures.append("Get-KTNetworkConfig v1.0.0: release ZIP is invalid")

    script_path = GET_KTNETWORKCONFIG_RELEASE / "Get-KTNetworkConfig.ps1"
    if script_path.is_file():
        script = script_path.read_text(encoding="utf-8")
        required_script_text = (
            "#requires -Version 5.1",
            "#requires -Modules NetTCPIP",
            "Version: 1.0.0",
            "Get-NetIPConfiguration -ErrorAction Stop",
            "26496D1395902B08BDAEE2E3BBFCBDBD8F3D37415680715459F3EDBB869FA0CF",
        )
        for required in required_script_text:
            if required not in script:
                failures.append(
                    f"Get-KTNetworkConfig v1.0.0: script is missing approved text {required!r}"
                )
        prohibited_commands = re.compile(
            r"(?im)^\s*(Write-Host|Invoke-WebRequest|Invoke-RestMethod|Start-Process|"
            r"Set-Content|Add-Content|Out-File|Export-Csv|New-Item|Remove-Item|"
            r"Set-ExecutionPolicy|Get-Credential|Invoke-Expression|Invoke-Command|"
            r"Set-DnsClientServerAddress|Set-NetIPAddress|Set-NetIPInterface|Set-NetRoute)\b"
        )
        match = prohibited_commands.search(script)
        if match:
            failures.append(
                f"Get-KTNetworkConfig v1.0.0: prohibited command found: {match.group(1)}"
            )

    readme_path = GET_KTNETWORKCONFIG_RELEASE / "README.md"
    if readme_path.is_file():
        readme = readme_path.read_text(encoding="utf-8")
        required_readme_text = (
            "# Get-KTNetworkConfig v1.0.0",
            "Unblock-File -LiteralPath .\\Get-KTNetworkConfig.ps1",
            "Do not bypass or globally weaken PowerShell execution policy.",
            "Approved seed SHA-256:",
            "26496D1395902B08BDAEE2E3BBFCBDBD8F3D37415680715459F3EDBB869FA0CF",
        )
        for required in required_readme_text:
            if required not in readme:
                failures.append(
                    f"Get-KTNetworkConfig v1.0.0: README is missing approved text {required!r}"
                )
        if "Set-ExecutionPolicy" in readme or "-ExecutionPolicy Bypass" in readme:
            failures.append(
                "Get-KTNetworkConfig v1.0.0: README must not recommend an execution-policy change or bypass"
            )

    public_requirements = {
        ROOT / "powershell/index.html": (
            "Get-KTNetworkConfig v1.0.0 is a read-only Windows PowerShell tool for discovering the local network configuration of active adapters.",
            "It returns structured PowerShell objects containing the interface alias and index, adapter description, IPv4 and IPv6 addresses, IPv4 gateways, DNS servers, and network profile.",
            "The script performs local discovery only. It does not change network settings, write files, contact remote systems, test connectivity, modify configuration, or handle credentials.",
            "Network configuration can contain internal IP addresses, gateways, DNS servers, adapter names, and network-profile information.",
            "This release is not Authenticode-signed.",
            "use Unblock-File only on Get-KTNetworkConfig.ps1",
            "Do not bypass or globally change execution policy.",
            "/downloads/powershell/get-ktnetworkconfig/v1.0.0/Get-KTNetworkConfig-v1.0.0.zip",
            "/downloads/powershell/get-ktnetworkconfig/v1.0.0/Get-KTNetworkConfig.ps1",
            "/downloads/powershell/get-ktnetworkconfig/v1.0.0/README.md",
            "/downloads/powershell/get-ktnetworkconfig/v1.0.0/SHA256SUMS.txt",
        ),
        ROOT / "downloads/index.html": (
            "Get-KTNetworkConfig v1.0.0 is KrippyTech’s second downloadable PowerShell release.",
            "Verify the package. Review the script. Run only what you understand.",
            "This release is not Authenticode-signed.",
            "use Unblock-File only on Get-KTNetworkConfig.ps1",
            "Do not bypass or globally change execution policy.",
            "/downloads/powershell/get-ktnetworkconfig/v1.0.0/Get-KTNetworkConfig-v1.0.0.zip",
            "/downloads/powershell/get-ktnetworkconfig/v1.0.0/Get-KTNetworkConfig.ps1",
            "/downloads/powershell/get-ktnetworkconfig/v1.0.0/README.md",
            "/downloads/powershell/get-ktnetworkconfig/v1.0.0/SHA256SUMS.txt",
            "/powershell/#get-ktnetworkconfig-v1",
        ),
    }
    for page, required_text in public_requirements.items():
        source = page.read_text(encoding="utf-8")
        for required in required_text:
            if required not in source:
                failures.append(
                    f"{page.relative_to(ROOT)}: missing Get-KTNetworkConfig release text {required!r}"
                )


def validate_get_ktnetworkconfig_tutorial(failures: list[str]) -> None:
    route = "/tutorials/get-ktnetworkconfig-v1.0.0/"
    page = ROOT / "tutorials/get-ktnetworkconfig-v1.0.0/index.html"
    if not page.is_file():
        failures.append(f"{route}: tutorial page is missing")
        return

    source = page.read_text(encoding="utf-8")
    required_text = (
        "Inspecting Local Windows Network Configuration with Get-KTNetworkConfig",
        "Real symptom",
        "Local evidence",
        "The script accepts no parameters.",
        "performs local discovery only",
        "associated adapter reports <code>Up</code>",
        "returns one structured PowerShell object",
        "Windows PowerShell 5.1 or PowerShell 7 on Windows",
        "Administrator rights are normally unnecessary",
        "built-in <code>NetTCPIP</code> module",
        "does not modify network configuration, write files, test connectivity, contact remote systems",
        "$networkConfig = &amp; .\\Get-KTNetworkConfig.ps1",
        "InterfaceAlias",
        "InterfaceIndex",
        "Adapter",
        "IPv4Address",
        "IPv6Address",
        "IPv4Gateway",
        "DnsServers",
        "NetProfile",
        "System.String[]",
        "empty array",
        "<code>$null</code>",
        "192.0.2.20",
        "2001:db8::20",
        "does not prove that DNS resolution, routing, Internet access, domain health, DHCP, VPN connectivity, or application connectivity works",
        "Do not paste raw output into public channels",
        "Do not bypass or globally change PowerShell execution policy.",
        "Unblock-File -LiteralPath .\\Get-KTNetworkConfig.ps1",
        "EADA2BBDDE5C0B62BB97D82D4DB4A70259CB8CC8DC9D65CA9D52E9384FF2C5C1",
        "/downloads/powershell/get-ktnetworkconfig/v1.0.0/Get-KTNetworkConfig-v1.0.0.zip",
        "/downloads/powershell/get-ktnetworkconfig/v1.0.0/Get-KTNetworkConfig.ps1",
        "/downloads/powershell/get-ktnetworkconfig/v1.0.0/README.md",
        "/downloads/powershell/get-ktnetworkconfig/v1.0.0/SHA256SUMS.txt",
        "/powershell/#get-ktnetworkconfig-v1",
        "/downloads/#get-ktnetworkconfig-v1",
        "/tutorials/test-ktdns-v1.0.0/",
        "/tutorials/dns-active-directory-domain-health/",
        "/windows-hybrid/",
        "/msp-university/#learning-path",
        "https://learn.microsoft.com/en-us/powershell/module/nettcpip/get-netipconfiguration?view=windowsserver2025-ps",
        "https://learn.microsoft.com/en-us/powershell/module/netadapter/get-netadapter?view=windowsserver2022-ps",
        "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-7.6",
        "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/unblock-file?view=powershell-7.5",
        "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.5",
    )
    for required in required_text:
        if required not in source:
            failures.append(
                f"{route}: missing required Get-KTNetworkConfig tutorial text {required!r}"
            )

    forbidden = (
        "Set-ExecutionPolicy",
        "-ExecutionPolicy Bypass",
        "Set-NetIPAddress",
        "Set-NetIPInterface",
        "Set-DnsClientServerAddress",
        "New-NetRoute",
        "Remove-NetRoute",
        "Restart-NetAdapter",
        "Disable-NetAdapter",
        "Enable-NetAdapter",
        "ipconfig /release",
        "ipconfig /renew",
        "netsh winsock reset",
    )
    for prohibited in forbidden:
        if prohibited in source:
            failures.append(
                f"{route}: prohibited configuration-changing guidance found: {prohibited!r}"
            )

    integrations = {
        ROOT / "tutorials/index.html": "get-ktnetworkconfig-v1.0.0/",
        ROOT / "windows-hybrid/index.html": "/tutorials/get-ktnetworkconfig-v1.0.0/",
        ROOT / "sitemap.xml": "https://krippytech.com/tutorials/get-ktnetworkconfig-v1.0.0/",
    }
    for integration, required in integrations.items():
        if required not in integration.read_text(encoding="utf-8"):
            failures.append(
                f"{integration.relative_to(ROOT)}: missing Get-KTNetworkConfig tutorial integration {required!r}"
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


def validate_windows_server_low_disk_tutorial(failures: list[str]) -> None:
    route = "/tutorials/windows-server-low-disk-space-investigation/"
    page = ROOT / "tutorials/windows-server-low-disk-space-investigation/index.html"
    if not page.is_file():
        failures.append(f"{route}: tutorial page is missing")
        return

    source = page.read_text(encoding="utf-8")
    required_text = (
        "Investigating Low Disk Space on Windows Server",
        "This is an investigation guide, not an automated cleanup or remediation procedure",
        "Do not invent one universal threshold",
        "Large does not mean unnecessary",
        "Old does not automatically mean safe to delete",
        "Get-Volume",
        "Get-PSDrive -PSProvider FileSystem",
        "Get-CimInstance -ClassName Win32_LogicalDisk",
        "fsutil volume diskfree C:",
        "DISM /Online /Cleanup-Image /AnalyzeComponentStore",
        "Get-WinEvent -ListLog *",
        "vssadmin list shadowstorage",
        "vssadmin list shadows",
        "Recursive scans can be expensive",
        "Observation",
        "What it may indicate",
        "What it does not prove",
        "Safest next investigation step",
        "This guide does not provide cleanup or remediation procedures",
        "/msp-university/#learning-path",
        "/windows-hybrid/",
        "/tutorials/dns-active-directory-domain-health/",
        "/tutorials/test-ktdns-v1.0.0/",
        "https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-volume",
        "https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/determine-the-actual-size-of-the-winsxs-folder",
        "https://learn.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service",
    )
    for required in required_text:
        if required not in source:
            failures.append(f"{page.relative_to(ROOT)}: missing required guide text {required!r}")

    prohibited_text = (
        "Remove-Item",
        "/StartComponentCleanup",
        "/ResetBase",
        "vssadmin delete",
        "vssadmin resize",
        "Clear-EventLog",
        "Resize-Partition",
        "Restart-Computer",
    )
    for prohibited in prohibited_text:
        if prohibited.lower() in source.lower():
            failures.append(
                f"{page.relative_to(ROOT)}: prohibited remediation command found {prohibited!r}"
            )

    integrations = {
        ROOT / "tutorials/index.html": "windows-server-low-disk-space-investigation/",
        ROOT / "windows-hybrid/index.html": route,
        ROOT / "sitemap.xml": f"{SITE_ORIGIN}{route}",
    }
    for integration, required in integrations.items():
        if required not in integration.read_text(encoding="utf-8"):
            failures.append(
                f"{integration.relative_to(ROOT)}: missing Windows Server storage tutorial integration {required!r}"
            )


def validate_dhcp_scope_capacity_tutorial(failures: list[str]) -> None:
    route = "/tutorials/dhcp-scope-capacity-investigation/"
    page = ROOT / "tutorials/dhcp-scope-capacity-investigation/index.html"
    if not page.is_file():
        failures.append(f"{route}: tutorial page is missing")
        return

    source = page.read_text(encoding="utf-8")
    required_text = (
        "Investigating DHCP Scope Capacity and Address Exhaustion",
        "High utilization does not automatically prove exhaustion",
        "Percentage and free-address count answer different questions",
        "LAB-DHCP-01.example.test",
        "192.0.2.0/24",
        "Get-DhcpServerv4Scope -ComputerName $dhcpServer -ScopeId $scopeId",
        "Get-DhcpServerv4ScopeStatistics -ComputerName $dhcpServer",
        "Get-DhcpServerv4Lease -ComputerName $dhcpServer",
        "Get-DhcpServerv4Reservation -ComputerName $dhcpServer -ScopeId $scopeId",
        "Get-DhcpServerv4ExclusionRange -ComputerName $dhcpServer",
        "Get-DhcpServerv4OptionValue -ComputerName $dhcpServer -ScopeId $scopeId",
        "Get-DhcpServerv4Failover -ComputerName $dhcpServer -ScopeId $scopeId",
        "Get-DhcpServerv4Superscope -ComputerName $dhcpServer",
        "Observation",
        "Possible interpretation",
        "Unknown",
        "Required next check",
        "Change requiring approval",
        "This guide authorizes evidence collection only",
        "/tutorials/get-ktnetworkconfig-v1.0.0/",
        "/tutorials/test-ktdns-v1.0.0/",
        "/windows-hybrid/",
        "/msp-university/#learning-path",
        "https://learn.microsoft.com/en-us/powershell/module/dhcpserver/?view=windowsserver2025-ps",
        "https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-scopes",
        "https://learn.microsoft.com/en-us/powershell/module/dhcpserver/get-dhcpserverv4scope?view=windowsserver2025-ps",
        "https://learn.microsoft.com/en-us/powershell/module/dhcpserver/get-dhcpserverv4scopestatistics?view=windowsserver2025-ps",
        "https://learn.microsoft.com/en-us/powershell/module/dhcpserver/get-dhcpserverv4lease?view=windowsserver2025-ps",
        "https://learn.microsoft.com/en-us/powershell/module/dhcpserver/get-dhcpserverv4reservation?view=windowsserver2025-ps",
        "https://learn.microsoft.com/en-us/powershell/module/dhcpserver/get-dhcpserverv4exclusionrange?view=windowsserver2025-ps",
        "https://learn.microsoft.com/en-us/powershell/module/dhcpserver/get-dhcpserverv4optionvalue?view=windowsserver2025-ps",
        "https://learn.microsoft.com/en-us/powershell/module/dhcpserver/get-dhcpserverv4failover?view=windowsserver2025-ps",
        "https://learn.microsoft.com/en-us/powershell/module/dhcpserver/get-dhcpserverv4superscope?view=windowsserver2025-ps",
    )
    for required in required_text:
        if required not in source:
            failures.append(f"{page.relative_to(ROOT)}: missing required guide text {required!r}")

    prohibited_text = (
        "Set-DhcpServer",
        "Add-DhcpServer",
        "Remove-DhcpServer",
        "Clear-DhcpServer",
        "Restart-Service",
        "Stop-Service",
        "Start-Service",
    )
    for prohibited in prohibited_text:
        if prohibited.lower() in source.lower():
            failures.append(
                f"{page.relative_to(ROOT)}: prohibited DHCP change command found {prohibited!r}"
            )

    synthetic_boundaries = (
        "LAB-DHCP-01.example.test",
        "192.0.2.0",
        "Every value below is invented and documentation-safe",
    )
    for required in synthetic_boundaries:
        if required not in source:
            failures.append(
                f"{page.relative_to(ROOT)}: missing synthetic-example boundary {required!r}"
            )

    forbidden_environment_markers = (
        "10.0.",
        "10.1.",
        "172.16.",
        ".local",
        "contoso.com",
        "fabrikam.com",
    )
    for marker in forbidden_environment_markers:
        if marker.lower() in source.lower():
            failures.append(
                f"{page.relative_to(ROOT)}: non-approved environment marker found {marker!r}"
            )

    integrations = {
        ROOT / "tutorials/index.html": "dhcp-scope-capacity-investigation/",
        ROOT / "windows-hybrid/index.html": route,
        ROOT / "sitemap.xml": f"{SITE_ORIGIN}{route}",
    }
    for integration, required in integrations.items():
        if required not in integration.read_text(encoding="utf-8"):
            failures.append(
                f"{integration.relative_to(ROOT)}: missing DHCP capacity tutorial integration {required!r}"
            )


def validate_onedrive_sharepoint_sync_tutorial(failures: list[str]) -> None:
    route = "/tutorials/onedrive-sharepoint-sync-investigation/"
    page = ROOT / "tutorials/onedrive-sharepoint-sync-investigation/index.html"
    if not page.is_file():
        failures.append(f"{route}: tutorial page is missing")
        return

    source = page.read_text(encoding="utf-8")
    required_text = (
        "Investigating OneDrive and SharePoint Sync Problems",
        "This is an investigation guide, not a repair, migration, or data-reconciliation procedure",
        "Synchronization is not a backup",
        "Synchronization cannot decide ownership",
        "A file visible locally does not prove it reached OneDrive or SharePoint",
        "A file visible in the browser does not prove it synchronized",
        "Matching filenames do not prove matching content",
        "Modified timestamps alone should not determine",
        "Add shortcut to OneDrive",
        "Known Folder Move",
        "It does not redirect Windows Documents directly into a SharePoint document library",
        "Online-only",
        "Locally available",
        "Always available",
        "Sync pending",
        "Sync error",
        "Duplicate organization folders",
        "Bulk overwrite is unsafe",
        "Observation",
        "What it may indicate",
        "What it does not prove",
        "Safest next investigation step",
        "This guide does not provide repair or reconciliation procedures",
        "/msp-university/#learning-path",
        "/microsoft-365/",
        "/tutorials/entra-signin-conditional-access-investigation/",
        "https://support.microsoft.com/en-us/onedrive/save-disk-space-with-onedrive-files-on-demand-for-windows",
        "https://support.microsoft.com/en-us/office/restrictions-and-limitations-in-onedrive-and-sharepoint-64883a5d-228e-48f5-b3d2-eb39e07630fa",
        "https://learn.microsoft.com/en-us/sharepoint/redirect-known-folders",
    )
    for required in required_text:
        if required not in source:
            failures.append(f"{page.relative_to(ROOT)}: missing required guide text {required!r}")

    prohibited_text = (
        "OneDrive.exe /reset",
        "cmdkey /delete",
        "reg delete",
        "Remove-Item",
        "Stop-Process",
        "taskkill",
        "Unlink this PC",
        "Start-Process",
        "Set-ItemProperty",
    )
    for prohibited in prohibited_text:
        if prohibited.lower() in source.lower():
            failures.append(
                f"{page.relative_to(ROOT)}: prohibited remediation instruction found {prohibited!r}"
            )

    integrations = {
        ROOT / "tutorials/index.html": "onedrive-sharepoint-sync-investigation/",
        ROOT / "microsoft-365/index.html": route,
        ROOT / "sitemap.xml": f"{SITE_ORIGIN}{route}",
    }
    for integration, required in integrations.items():
        if required not in integration.read_text(encoding="utf-8"):
            failures.append(
                f"{integration.relative_to(ROOT)}: missing OneDrive and SharePoint tutorial integration {required!r}"
            )


def validate_azure_vm_connectivity_tutorial(failures: list[str]) -> None:
    route = "/tutorials/azure-vm-connectivity-investigation/"
    page = ROOT / "tutorials/azure-vm-connectivity-investigation/index.html"
    if not page.is_file():
        failures.append(f"{route}: tutorial page is missing")
        return

    source = page.read_text(encoding="utf-8")
    required_text = (
        "Investigating Azure VM Connectivity",
        "Evidence should be collected before changing the network path",
        "Running is a power-state observation, not an application-health result",
        "Effective security rules",
        "Effective routes",
        "Connection troubleshoot",
        "IP flow verify",
        "Next hop",
        "This guide does not provide connectivity repair or deployment procedures",
        "Observation",
        "What it may indicate",
        "What it does not prove",
        "Safest next investigation step",
        "ipconfig /all",
        "route print",
        "Get-NetIPConfiguration -Detailed",
        "Test-NetConnection -ComputerName app.example.com -Port 443 -InformationLevel Detailed",
        "Get-NetTCPConnection -LocalPort 443 -State Listen",
        "Resolve-DnsName -Name app.example.com -Type A -DnsOnly",
        "Get-NetFirewallProfile -PolicyStore ActiveStore",
        "Get-NetFirewallRule -PolicyStore ActiveStore -Enabled True -Direction Inbound",
        "198.51.100.24",
        "/azure-journey/",
        "/msp-university/#learning-path",
        "https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing",
        "https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview",
        "https://learn.microsoft.com/en-us/azure/network-watcher/effective-security-rules-overview",
        "https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview",
        "https://learn.microsoft.com/en-us/azure/network-watcher/ip-flow-verify-overview",
        "https://learn.microsoft.com/en-us/azure/network-watcher/next-hop-overview",
        "https://learn.microsoft.com/en-us/azure/network-watcher/connection-troubleshoot-overview",
        "https://learn.microsoft.com/en-us/azure/network-watcher/required-rbac-permissions",
    )
    for required in required_text:
        if required not in source:
            failures.append(f"{page.relative_to(ROOT)}: missing required guide text {required!r}")

    prohibited_commands = (
        "New-AzNetworkSecurityRuleConfig",
        "Set-AzNetworkSecurityGroup",
        "Remove-AzNetworkSecurityRuleConfig",
        "New-AzRouteConfig",
        "Set-AzRouteTable",
        "Restart-AzVM",
        "Disable-NetFirewallRule",
        "Set-NetFirewallProfile",
        "New-NetFirewallRule",
        "Set-NetIPInterface",
        "ipconfig /renew",
        "az network nsg rule create",
        "az network route-table route create",
    )
    for prohibited in prohibited_commands:
        if prohibited.lower() in source.lower():
            failures.append(
                f"{page.relative_to(ROOT)}: prohibited configuration-changing command found {prohibited!r}"
            )

    integrations = {
        ROOT / "tutorials/index.html": "azure-vm-connectivity-investigation/",
        ROOT / "azure-journey/index.html": route,
        ROOT / "sitemap.xml": f"{SITE_ORIGIN}{route}",
    }
    for integration, required in integrations.items():
        if required not in integration.read_text(encoding="utf-8"):
            failures.append(
                f"{integration.relative_to(ROOT)}: missing Azure VM connectivity tutorial integration {required!r}"
            )


def validate_azure_vm_network_path_lab(failures: list[str]) -> None:
    route = "/azure-journey/labs/map-azure-vm-network-path/"
    page = ROOT / "azure-journey/labs/map-azure-vm-network-path/index.html"
    if not page.is_file():
        failures.append(f"{route}: lab page is missing")
        return

    source = page.read_text(encoding="utf-8")
    required_text = (
        "Map the Network Path to an Azure VM",
        "No Azure subscription, deployment, payment, tenant access, or production environment is required.",
        "1 · Learning objectives",
        "2 · Prerequisite knowledge",
        "3 · Investigation rules",
        "4 · Synthetic environment",
        "5 · Defined traffic flow",
        "6 · Topology and inventory",
        "7 · Evidence packet",
        "8 · Learner tasks",
        "9 · Network-path worksheet",
        "10 · Interpretation questions",
        "11 · Final conclusion template",
        "12 · Expandable answer key",
        "13 · Escalation-quality sample",
        "14 · What the evidence does not prove",
        "15 · Related resources",
        "LAB-ADMIN-01",
        "LAB-WEB-01",
        "app.lab.example",
        "10.20.1.4",
        "10.20.2.4",
        "DenyAdminHttps",
        "nsg-lab-app",
        "VirtualNetwork",
        "Access denied",
        "Supported / Contradicted / Unknown",
        "earliest demonstrated point blocking the defined flow",
        "/tutorials/azure-vm-connectivity-investigation/",
        "/azure-journey/",
        "/msp-university/#learning-path",
        "https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing",
        "https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview",
        "https://learn.microsoft.com/en-us/azure/network-watcher/effective-security-rules-overview",
        "https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview",
        "https://learn.microsoft.com/en-us/azure/network-watcher/ip-flow-verify-overview",
    )
    for required in required_text:
        if required not in source:
            failures.append(f"{page.relative_to(ROOT)}: missing required lab text {required!r}")

    if source.count("<details>") != 9 or source.count("<summary>") != 9:
        failures.append(
            f"{page.relative_to(ROOT)}: answer key must contain exactly nine native details/summary disclosures"
        )

    prohibited_commands = (
        "New-AzNetworkSecurityRuleConfig",
        "Set-AzNetworkSecurityGroup",
        "Remove-AzNetworkSecurityRuleConfig",
        "New-AzRouteConfig",
        "Set-AzRouteTable",
        "Restart-AzVM",
        "Disable-NetFirewallRule",
        "Set-NetFirewallProfile",
        "New-NetFirewallRule",
        "Set-NetIPInterface",
        "ipconfig /renew",
        "az network nsg rule create",
        "az network route-table route create",
        "Start-AzNetworkWatcherPacketCapture",
    )
    for prohibited in prohibited_commands:
        if prohibited.lower() in source.lower():
            failures.append(
                f"{page.relative_to(ROOT)}: prohibited configuration-changing command found {prohibited!r}"
            )

    if re.search(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b", source, re.I):
        failures.append(f"{page.relative_to(ROOT)}: GUID-like identifier found in synthetic lab")
    if "/subscriptions/" in source.lower():
        failures.append(f"{page.relative_to(ROOT)}: Azure subscription resource path found in synthetic lab")

    integrations = {
        ROOT / "azure-journey/index.html": route,
        ROOT / "tutorials/azure-vm-connectivity-investigation/index.html": route,
        ROOT / "sitemap.xml": f"{SITE_ORIGIN}{route}",
    }
    for integration, required in integrations.items():
        if required not in integration.read_text(encoding="utf-8"):
            failures.append(
                f"{integration.relative_to(ROOT)}: missing Azure VM network-path lab integration {required!r}"
            )


def validate_grouped_navigation(failures: list[str]) -> None:
    navigation_script = ROOT / "navigation.js"
    stylesheet = ROOT / "styles.css"

    if not navigation_script.is_file():
        failures.append("navigation.js: shared navigation behavior is missing")
        return
    if not stylesheet.is_file():
        failures.append("styles.css: shared navigation styling is missing")
        return

    script_source = navigation_script.read_text(encoding="utf-8")
    style_source = stylesheet.read_text(encoding="utf-8")

    required_script = (
        'document.documentElement.classList.add("js")',
        'event.key === "Escape"',
        'event.key === "ArrowDown"',
        'event.key === "ArrowUp"',
        'event.target.closest("[data-dropdown]")',
        'group.addEventListener("pointerenter"',
        'group.addEventListener("pointerleave"',
        'mobileToggle.setAttribute("aria-expanded"',
        'mobileToggle.focus()',
        "window.innerWidth > 840",
    )
    for required in required_script:
        if required not in script_source:
            failures.append(f"navigation.js: missing required behavior {required!r}")

    required_style = (
        "html:not(.js) .dropdown-group:hover .dropdown-menu",
        "html:not(.js) .dropdown-group:focus-within .dropdown-menu",
        ".js .mobile-panel.is-open",
        "@media (max-width: 840px)",
        "@media (prefers-reduced-motion: reduce)",
        ':where(a, button):focus-visible',
        '.nav-link[aria-current="page"]',
        ".contact-link",
    )
    for required in required_style:
        if required not in style_source:
            failures.append(f"styles.css: missing grouped-navigation style {required!r}")
    if re.search(r"transition\s*:\s*all(?:\s|;)", style_source, re.IGNORECASE):
        failures.append("styles.css: grouped navigation must not use transition: all")

    required_links = {
        "/": 1,
        "/consulting/": 2,
        "/everyday-it/": 2,
        "/msp-university/": 2,
        "/azure-journey/": 2,
        "/tutorials/": 2,
        "/cases/": 2,
        "/powershell/": 2,
        "/downloads/": 2,
        "/about/": 2,
        "/contact/": 2,
    }

    def expected_active(route: str | None) -> str | None:
        if route == "/":
            return "/"
        if route and route.startswith("/everyday-it/"):
            return "/everyday-it/"
        if route in {"/msp-university/", "/microsoft-365/", "/windows-hybrid/"}:
            return "/msp-university/"
        if route and route.startswith("/azure-journey/labs/"):
            return "/azure-journey/"
        if route and route.startswith("/tutorials/"):
            return "/tutorials/"
        if route and route.startswith("/cases/"):
            return "/cases/"
        if route in {
            "/consulting/",
            "/azure-journey/",
            "/powershell/",
            "/downloads/",
            "/about/",
            "/contact/",
        }:
            return route
        return None

    navigation_pages = [
        ROOT / "404.html",
        *sorted(ROOT.glob("**/index.html")),
        ROOT / ".github/templates/case-template.html",
    ]
    for page in navigation_pages:
        source = page.read_text(encoding="utf-8")
        route = public_route(page)
        relative = page.relative_to(ROOT)
        header_match = re.search(
            r'<header class="site-header">.*?</header>', source, re.DOTALL
        )
        if not header_match:
            failures.append(f"{relative}: grouped site header is missing")
            continue
        header_source = header_match.group(0)

        required_markup = (
            '<nav class="site-nav" aria-label="Primary navigation">',
            '<ul class="desktop-nav">',
            'class="dropdown-menu" id="learn-menu"',
            'class="dropdown-menu" id="solutions-menu"',
            'class="dropdown-menu" id="tools-menu"',
            'aria-controls="learn-menu"',
            'aria-controls="solutions-menu"',
            'aria-controls="tools-menu"',
            'aria-haspopup="true"',
            'aria-controls="mobile-navigation"',
            'aria-label="Open navigation menu"',
            'class="mobile-panel" id="mobile-navigation"',
            'id="mobile-learn-label"',
            'id="mobile-solutions-label"',
            'id="mobile-tools-label"',
            'class="nav-link contact-link"',
        )
        for required in required_markup:
            if required not in header_source:
                failures.append(f"{relative}: missing navigation markup {required!r}")

        if 'class="nav-links"' in header_source:
            failures.append(f"{relative}: legacy flat navigation remains")
        if source.count('<script src="/navigation.js"></script>') != 1:
            failures.append(
                f"{relative}: must load shared navigation.js exactly once"
            )

        for href, count in required_links.items():
            actual = header_source.count(f'href="{href}"')
            if actual != count:
                failures.append(
                    f"{relative}: navigation href {href!r} appears {actual} times; expected {count}"
                )

        active_hrefs = re.findall(
            r'href="([^"]+)"[^>]*\saria-current="page"', header_source
        )
        expected = (
            "/cases/"
            if relative.as_posix() == ".github/templates/case-template.html"
            else expected_active(route)
        )
        expected_count = 1 if expected == "/" else 2 if expected else 0
        if active_hrefs != ([expected] * expected_count if expected else []):
            failures.append(
                f"{relative}: active navigation is {active_hrefs!r}; expected "
                f"{([expected] * expected_count if expected else [])!r}"
            )

        expected_group = None
        if expected in {"/everyday-it/", "/msp-university/", "/azure-journey/"}:
            expected_group = "learn-menu"
        elif expected in {"/tutorials/", "/cases/"}:
            expected_group = "solutions-menu"
        elif expected in {"/powershell/", "/downloads/"}:
            expected_group = "tools-menu"

        current_groups = re.findall(
            r'<li class="dropdown-group has-current" data-dropdown>\s*'
            r'<button[^>]+aria-controls="([^"]+)"',
            header_source,
        )
        if current_groups != ([expected_group] if expected_group else []):
            failures.append(
                f"{relative}: current group is {current_groups!r}; expected "
                f"{([expected_group] if expected_group else [])!r}"
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
    validate_get_ktnetworkconfig_release(failures)
    validate_get_ktnetworkconfig_tutorial(failures)
    validate_dns_ad_domain_health_tutorial(failures)
    validate_entra_signin_ca_tutorial(failures)
    validate_windows_server_low_disk_tutorial(failures)
    validate_dhcp_scope_capacity_tutorial(failures)
    validate_onedrive_sharepoint_sync_tutorial(failures)
    validate_azure_vm_connectivity_tutorial(failures)
    validate_azure_vm_network_path_lab(failures)
    validate_grouped_navigation(failures)

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
