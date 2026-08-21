# Test-KTDNS v1.0.0

`Test-KTDNS.ps1` is a read-only Windows PowerShell diagnostic that performs an
explicit DNS query and returns normalized objects suitable for viewing,
filtering, or exporting.

Review and test the release in your environment before use.

## Safety and privacy

The script:

- performs DNS queries only;
- does not use LLMNR or NetBIOS fallback;
- does not change DNS or local/remote configuration;
- does not write files, download content, or launch other programs; and
- does not request, receive, store, or transmit credentials.

DNS resolvers can log query names. Do not send sensitive internal names to an
untrusted or unauthorized resolver. Treat output concerning internal DNS names
as environment data.

## Requirements

- Windows PowerShell 5.1 or PowerShell 7 on Windows
- Windows `DnsClient` module and its `Resolve-DnsName` cmdlet
- No administrator rights are required for ordinary DNS queries

The script is not supported on Linux or macOS because `DnsClient` is a Windows
module.

## Verify before running

Keep `SHA256SUMS.txt` beside the release files. From the release folder, verify
the script against the manifest:

```powershell
$expected = (Select-String -LiteralPath .\SHA256SUMS.txt -Pattern '  Test-KTDNS.ps1$').Line.Split()[0]
$actual = (Get-FileHash -LiteralPath .\Test-KTDNS.ps1 -Algorithm SHA256).Hash
$actual -eq $expected
```

The result must be `True`. If it is not, do not run the script.

Windows may mark a browser-downloaded script as originating from the Internet.
After reviewing the source and verifying its checksum, remove that mark from
this script only:

```powershell
Unblock-File -LiteralPath .\Test-KTDNS.ps1
```

Do not weaken or bypass the computer's global execution policy.

## Usage

Query an A record with the system-configured DNS servers:

```powershell
.\Test-KTDNS.ps1 -Name example.com
```

Query another supported record type:

```powershell
.\Test-KTDNS.ps1 -Name example.com -Type MX
```

Query a synthetic local name:

```powershell
.\Test-KTDNS.ps1 -Name localhost -Type A
```

Use a specifically approved resolver:

```powershell
.\Test-KTDNS.ps1 -Name example.com -Type TXT -Server '<dns-server-ip>'
```

Supported record types are `A`, `AAAA`, `CNAME`, `MX`, `NS`, `SRV`, `TXT`, and
`PTR`.

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `Name` | Yes | DNS name or address to query. Whitespace and control characters are rejected. |
| `Type` | No | Record type. Defaults to `A`. |
| `Server` | No | Approved DNS resolver IP address or host name. Defaults to the Windows interface configuration. |

Parameter values are passed directly to `Resolve-DnsName` through named
parameters. They are not evaluated as PowerShell code.

## Output

Every result has the same properties:

| Property | Meaning |
| --- | --- |
| `Query` | Original requested name |
| `QueryServer` | Requested resolver, or `System default` |
| `RecordName` | Name returned by the resolver |
| `RecordType` | Actual returned record type |
| `TTL` | Time to live, in seconds |
| `Value` | Primary record value, normalized as text |
| `Preference` | MX preference when applicable |
| `Priority` | SRV priority when applicable |
| `Weight` | SRV weight when applicable |
| `Port` | SRV port when applicable |
| `Section` | DNS response section |

Properties that do not apply to a record type are `$null`.

The script emits only objects as functional output and leaves formatting to the
caller. For example:

```powershell
.\Test-KTDNS.ps1 -Name example.com -Type A |
    Format-Table RecordName, RecordType, TTL, Value
```

## Errors and automation

Invalid parameters fail during parameter binding. DNS failures remain
terminating errors because `Resolve-DnsName` runs with `-ErrorAction Stop`. An
automation caller can handle them normally:

```powershell
try {
    $result = .\Test-KTDNS.ps1 -Name example.com -Type A
}
catch {
    Write-Error "DNS query failed: $($_.Exception.Message)"
}
```

## Provenance

This release candidate was prepared from the approved KrippyTech PowerShell
Library v2.0 seed without changing that seed file.

- Approved seed file: `50-Network-Windows/Test-KTDNS.ps1`
- Approved seed SHA-256: `E1C61B20B5888FE21B583C8E5977351F94D346D584A0DF02CF9B08A65B37F2EC`
- Release version: `1.0.0`

Release checksums are generated after all release content is finalized and are
recorded in `SHA256SUMS.txt`.

## License

Copyright (c) 2026 KrippyTech. Released under the MIT License. See `LICENSE`.
