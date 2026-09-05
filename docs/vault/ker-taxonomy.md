# KrippyTech KER Taxonomy

**Version:** 2.0

## Purpose

KER uses two levels of classification:

1. **Primary Domain**: the stable shelf where a lesson belongs.
2. **Tags**: products, technologies, platforms, vendors, and technical concepts that describe the lesson in more detail.

Every retained lesson should have one primary domain and may have multiple tags.

This prevents the taxonomy from becoming a flat list of hundreds of unrelated product names while preserving detailed searchability.

## Primary Domains

### 01 Identity & Access

Common tags:
- Active Directory
- Entra ID
- Identity
- Users
- Groups
- Permissions
- Authentication
- Passwords
- MFA
- Conditional Access
- SSPR
- Duo
- Delegation
- Account Lifecycle

### 02 Microsoft 365 & Email

Common tags:
- Microsoft 365
- Exchange
- Exchange Online
- Outlook
- Teams
- Shared Mailbox
- Calendar
- Distribution Groups
- Mail Flow
- Message Trace
- Licensing
- Email Security
- Defender for Office 365

### 03 SharePoint & OneDrive

Common tags:
- SharePoint
- OneDrive
- Files On-Demand
- Sync
- Sharing
- Storage
- Migration
- Permissions
- Document Libraries

### 04 Windows & Workstations

Common tags:
- Windows
- Windows 10
- Windows 11
- User Profiles
- Credential Manager
- Office Apps
- Drivers
- Performance
- Disk Space
- Hardware
- QuickBooks
- Application Support

### 05 Remote Access & VPN

Common tags:
- VPN
- WatchGuard
- SonicWall
- Duo
- Remote Desktop
- RDP
- Azure Virtual Desktop
- DNS
- Routes
- Remote Access

### 06 Printers, Scanners & MFP

Common tags:
- Printing
- Printers
- Scanners
- MFP
- Scan to Email
- Scan to Folder
- SMTP
- Drivers
- USB
- PCL
- PostScript

### 07 File Servers & SMB

Common tags:
- File Server
- SMB
- NTFS
- Mapped Drives
- UNC
- Permissions
- Inheritance
- Storage
- DFS

### 08 Servers & Infrastructure

Common tags:
- Windows Server
- Active Directory Infrastructure
- DNS
- DHCP
- Certificates
- Hyper-V
- VMware
- Storage
- Backup
- Veeam
- Replication
- Patching
- Azure
- Networking

### 09 Security & Incident Response

Common tags:
- Security
- SentinelOne
- Microsoft Defender
- Avanan
- Mimecast
- Email Security
- Malware
- Phishing
- Quarantine
- Endpoint Detection
- Incident Response
- Containment
- Sign-in Logs

### 10 Advanced / KER

Common tags:
- PowerShell
- Automation
- Scripting
- Architecture
- Build Guide
- Deep Troubleshooting
- Vendor-Specific
- Documentation
- Migration
- Recovery
- Consulting Reference

## Tag Rules

- Use the most specific useful tag, but do not create cosmetic variations of the same term.
- Product names are tags, not primary domains.
- A lesson may have several tags when multiple systems are genuinely involved.
- Do not assign every possible related tag. Tags should improve retrieval.
- Prefer stable concepts over temporary product branding when both describe the lesson.

## Examples

### Example: Outlook works in the browser but not on the desktop

Primary Domain: `02 Microsoft 365 & Email`

Tags:
- Outlook
- Exchange Online
- User Profiles
- Authentication

### Example: User added to a security group but still receives Access Denied

Primary Domain: `01 Identity & Access`

Tags:
- Active Directory
- Groups
- NTFS
- Access Token
- Effective Access

### Example: VPN connects but mapped drive fails

Primary Domain: `05 Remote Access & VPN`

Tags:
- VPN
- SMB
- DNS
- Mapped Drives
- File Server

### Example: Hyper-V host storage alert affecting virtual machines

Primary Domain: `08 Servers & Infrastructure`

Tags:
- Hyper-V
- Storage
- Windows Server
- Virtualization

## Relationship to Public Content

The taxonomy is an internal knowledge system. Public navigation does not need to mirror it exactly.

Public structure should remain simple for the reader.
Internal taxonomy should remain detailed enough to retrieve and reuse engineering knowledge.

The primary domains provide the bridge between those two goals.
