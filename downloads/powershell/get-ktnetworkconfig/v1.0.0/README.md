# Get-KTNetworkConfig v1.0.0

`Get-KTNetworkConfig.ps1` produces a structured, read-only snapshot of active network configurations on the local Windows computer. It is the reviewed final v1.0.0 release package. It remains unpublished until a separate website-integration authorization is completed.

## Read-only boundary

The script calls `Get-NetIPConfiguration` locally and returns one object for each configuration whose associated adapter reports `Status = Up`.

It does not:

- accept parameters, credentials, computer names, paths, or export destinations;
- contact remote computers or submit results externally;
- write or download files;
- change adapters, addresses, DNS servers, gateways, routes, DHCP leases, profiles, services, the registry, or other configuration;
- launch external processes, create scheduled tasks, execute dynamic code, or send telemetry;
- call `Write-Host` or apply PowerShell formatting commands to functional output.

## Requirements

- A supported Windows environment providing the `NetTCPIP` module and `Get-NetIPConfiguration`.
- Windows PowerShell 5.1, or PowerShell 7 on Windows where the required Windows networking cmdlets are available.
- Ordinary local discovery normally does not require administrator rights. Organizational security controls can still restrict access.

The script is Windows-only. PowerShell 7 on non-Windows systems is not supported.

## Installation and source review

1. Extract the ZIP into a new folder.
2. Confirm that the folder contains only the five documented package members.
3. Open `Get-KTNetworkConfig.ps1`, `README.md`, `LICENSE`, `SHA256SUMS.txt`, and `tests\Get-KTNetworkConfig.Tests.ps1` in a text editor.
4. Verify the checksums before running the script.

This final release is not Authenticode-signed. Review the source and verify SHA-256 before deciding whether it is appropriate under your organization's policy.

## SHA-256 verification

From the extracted release folder:

```powershell
Get-FileHash -LiteralPath .\Get-KTNetworkConfig.ps1 -Algorithm SHA256
Get-FileHash -LiteralPath .\README.md -Algorithm SHA256
Get-FileHash -LiteralPath .\LICENSE -Algorithm SHA256
Get-FileHash -LiteralPath .\tests\Get-KTNetworkConfig.Tests.ps1 -Algorithm SHA256
Get-Content -LiteralPath .\SHA256SUMS.txt
```

Compare every calculated value with `SHA256SUMS.txt`. A mismatch means the extracted member is not byte-identical to the reviewed package and should not be run.

## Execution policy

Do not bypass or globally weaken PowerShell execution policy. If `RemoteSigned` blocks this verified downloaded script because Windows marked it as originating from the Internet, targeted unblocking may be appropriate after source and checksum review:

```powershell
Unblock-File -LiteralPath .\Get-KTNetworkConfig.ps1
```

This command targets only this script. Environments using `Restricted` or `AllSigned` must follow organizational policy; this unsigned final release does not override those controls.

## Usage

```powershell
.\Get-KTNetworkConfig.ps1
```

Store the results without changing their object structure:

```powershell
$configuration = .\Get-KTNetworkConfig.ps1
$configuration | Select-Object InterfaceAlias, IPv4Address, IPv4Gateway, DnsServers
```

The script itself does not format or export results. Any display, filtering, redaction, or export is an explicit caller decision.

## Output contract

Every emitted object has the type name `KrippyTech.NetworkConfiguration` and exactly these properties:

| Property | PowerShell type | Null or empty behavior | Multiple values | Privacy implications |
|---|---|---|---|---|
| `InterfaceAlias` | `System.String` | May be `$null` | No | Can identify interface purpose or organizational naming. |
| `InterfaceIndex` | `System.Int32` | May be `$null` | No | Local identifier; useful only in the observed system context. |
| `Adapter` | `System.String` | May be `$null` | No | Can reveal hardware, driver, VPN, or virtualization products. |
| `IPv4Address` | `System.String[]` | Empty array when unavailable | Yes | Can reveal private or public addressing and network design. |
| `IPv6Address` | `System.String[]` | Empty array when unavailable | Yes | Can reveal host and network addressing. |
| `IPv4Gateway` | `System.String[]` | Empty array when unavailable | Yes | Can reveal local routing design. |
| `DnsServers` | `System.String[]` | Empty array when unavailable | Yes | Can reveal internal resolvers or service providers. |
| `NetProfile` | `System.String` | May be `$null` | No | Can reveal network or organization-specific profile names. |

Unavailable scalar values are `$null`. Unavailable multivalue fields are empty `System.String[]` arrays. The script does not join arrays into preformatted display strings.

## Interpretation guidance

- An adapter reporting `Up` does not prove Internet, DNS, VPN, domain, or application health.
- An assigned IP address does not prove that DHCP, routing, or duplicate-address detection is healthy.
- A configured gateway does not prove that it is reachable or is the route selected for a particular destination.
- Configured DNS servers do not prove that they respond or return correct answers.
- Missing optional fields can be normal for some adapters and configurations.
- Results describe one local observation and should be correlated with routes, DNS resolution, port tests, application evidence, and organizational design.

## Privacy guidance

Output can reveal interface names and descriptions, local addresses, gateways, DNS servers, and network-profile information. Review and redact results before posting publicly, submitting them to forums, attaching them to tickets, or sharing them outside the organization.

The script deliberately omits computer name, DNS suffix, prefix length, routes, connection state beyond the seed's `Up` filter, and remote information because those fields are not required to preserve the approved seed's narrow output contract.

## Error behavior

A failure of the required `Get-NetIPConfiguration` discovery call produces a terminating `InvalidOperationException`. An invalid interface-index value for a retained active configuration produces a terminating `InvalidDataException`. Missing optional adapter, address, gateway, DNS, or profile properties do not cause failure.

If no configuration has an associated adapter reporting `Up`, the script returns no objects and does not treat that state as proof of a fault.

## Testing

The included Pester tests use only synthetic objects and mocks. They cover parsing, zero exposed parameters, adapter selection, stable output and property order, missing and partial properties, terminating discovery failures, pipeline behavior, and static safety boundaries.

Pester 5.7.1 is the tested release-validation version. If that approved version is already available, run:

```powershell
Invoke-Pester -Path .\tests\Get-KTNetworkConfig.Tests.ps1
```

The package does not install or update Pester and does not alter module repositories, package providers, execution policy, or persistent configuration.

## Known limitations

- Windows-only and dependent on the locally available `NetTCPIP` implementation.
- Reports configuration, not end-to-end connectivity or overall network health.
- Includes only configurations with an associated adapter whose status is exactly `Up`, preserving the seed's intent.
- Does not resolve or validate addresses, contact gateways or DNS servers, inspect routes, or test ports.
- Does not perform remote collection or automatic export.
- Not Authenticode-signed.

## Provenance

Derived from `Get-KTNetworkConfig.ps1` in the approved KrippyTech PowerShell Library v2.0.

Approved seed SHA-256:

`26496D1395902B08BDAEE2E3BBFCBDBD8F3D37415680715459F3EDBB869FA0CF`

Final v1.0.0 is promoted from the approved v1.0.0-rc2 package without functional changes. The approved RC2 hashes are:

- Script: `4197F32EA7CE6BE630D6D1C07C7F63DAC07D9F2A7874B3AE51136C07E3BFD675`
- README: `54E03FFF84CF954B019DA064671DE808BDE3D18139A3BACF790F9F7EC8AAE5A2`
- LICENSE: `FBBDF22DA672C4D3FA5D004C09A2C88E47D0FD66768A83523900DF29A236279A`
- Manifest: `95E65EE65F3E8F7C54C2C209F222FDECDF58F4E168627726EDC818F08B816494`
- Tests: `3CD5DFE824EDDCA95151653D7085AAED2A08D6B63A3F9DD8E23BB777B9BE13A7`
- ZIP: `2D86B2ADFFBD624D11783718D8333DB5968FE93B38133EA8E3B9BBA2F33B40F6`

RC2 renamed the ordinary network-profile variable that collided case-insensitively with PowerShell's automatic `$PROFILE` variable, declared the success output types of both conversion helpers, and replaced the legacy test suite with Pester 5.7.1 lifecycle, assertion, and mock patterns. Final promotion changes only version references, release-status wording, provenance, package naming, and resulting checksums.

Functional differences from the approved seed remain limited to safety, compatibility, documentation, predictable errors, optional-property handling, a stable type name, and consistent array output. The script remains zero-parameter, local-only, and read-only.

## License

MIT. See `LICENSE`.
