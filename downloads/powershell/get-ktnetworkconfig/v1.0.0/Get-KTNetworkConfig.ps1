#requires -Version 5.1
#requires -Modules NetTCPIP

<#
.SYNOPSIS
Returns a read-only snapshot of active local Windows network configurations.

.DESCRIPTION
Get-KTNetworkConfig queries Get-NetIPConfiguration on the local Windows computer,
keeps configurations whose associated adapter reports a status of Up, and emits
one stable PowerShell object for each retained configuration.

The script does not accept parameters. It does not contact remote computers,
write files, export results, change network settings, collect credentials, launch
external processes, or submit telemetry.

.EXAMPLE
PS> .\Get-KTNetworkConfig.ps1

Returns structured objects for active local network configurations. Review and
redact the results before sharing them outside the organization.

.EXAMPLE
PS> $configuration = .\Get-KTNetworkConfig.ps1
PS> $configuration | Select-Object InterfaceAlias, IPv4Address, IPv4Gateway

Stores the objects and selects a subset of their properties. Formatting is chosen
by the caller; the script does not apply formatting.

.OUTPUTS
KrippyTech.NetworkConfiguration

.NOTES
Version: 1.0.0
License: MIT
Supported environment: Windows with PowerShell 5.1 or PowerShell 7 and the
NetTCPIP module. PowerShell 7 support applies only on Windows where the required
Windows networking cmdlets are available. Administrator rights are not normally
required for ordinary local discovery, although organizational controls can vary.

Provenance: Derived from the approved KrippyTech PowerShell Library v2.0 seed.
Approved seed SHA-256:
26496D1395902B08BDAEE2E3BBFCBDBD8F3D37415680715459F3EDBB869FA0CF

This final release is not Authenticode-signed.

.LINK
https://krippytech.com/powershell/
#>

[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Get-KTOptionalPropertyValue {
    [CmdletBinding()]
    param(
        [AllowNull()]
        [object]$InputObject,

        [Parameter(Mandatory)]
        [string]$Name
    )

    if ($null -eq $InputObject) {
        return $null
    }

    $property = $InputObject.PSObject.Properties[$Name]
    if ($null -eq $property) {
        return $null
    }

    return $property.Value
}

function ConvertTo-KTNullableString {
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [AllowNull()]
        [object]$Value
    )

    if ($null -eq $Value) {
        return $null
    }

    $values = @($Value)
    if ($values.Count -eq 0 -or $null -eq $values[0]) {
        return $null
    }

    $text = [string]$values[0]
    if ([string]::IsNullOrWhiteSpace($text)) {
        return $null
    }

    return $text
}

function ConvertTo-KTStringArray {
    [CmdletBinding()]
    [OutputType([string[]])]
    param(
        [AllowNull()]
        [object]$Collection,

        [string]$PropertyName
    )

    [System.Collections.Generic.List[string]]$values = @()

    foreach ($item in @($Collection)) {
        if ($null -eq $item) {
            continue
        }

        $value = if ([string]::IsNullOrWhiteSpace($PropertyName)) {
            $item
        }
        else {
            Get-KTOptionalPropertyValue -InputObject $item -Name $PropertyName
        }

        foreach ($candidate in @($value)) {
            if ($null -eq $candidate) {
                continue
            }

            $text = [string]$candidate
            if (-not [string]::IsNullOrWhiteSpace($text)) {
                $values.Add($text)
            }
        }
    }

    return [string[]]$values.ToArray()
}

try {
    $configurations = @(Get-NetIPConfiguration -ErrorAction Stop)
}
catch {
    throw [System.InvalidOperationException]::new(
        'Unable to read the local Windows network configuration.',
        $_.Exception
    )
}

foreach ($configuration in $configurations) {
    if ($null -eq $configuration) {
        continue
    }

    $adapter = Get-KTOptionalPropertyValue -InputObject $configuration -Name 'NetAdapter'
    $adapterStatus = ConvertTo-KTNullableString -Value (
        Get-KTOptionalPropertyValue -InputObject $adapter -Name 'Status'
    )

    if ($adapterStatus -ne 'Up') {
        continue
    }

    $interfaceIndexValue = Get-KTOptionalPropertyValue -InputObject $configuration -Name 'InterfaceIndex'
    [Nullable[int]]$interfaceIndex = $null
    if ($null -ne $interfaceIndexValue) {
        try {
            $interfaceIndex = [int]$interfaceIndexValue
        }
        catch {
            throw [System.InvalidDataException]::new(
                'An active network configuration returned an invalid InterfaceIndex value.',
                $_.Exception
            )
        }
    }

    $ipv4 = Get-KTOptionalPropertyValue -InputObject $configuration -Name 'IPv4Address'
    $ipv6 = Get-KTOptionalPropertyValue -InputObject $configuration -Name 'IPv6Address'
    $gateway = Get-KTOptionalPropertyValue -InputObject $configuration -Name 'IPv4DefaultGateway'
    $dns = Get-KTOptionalPropertyValue -InputObject $configuration -Name 'DNSServer'
    $networkProfile = Get-KTOptionalPropertyValue -InputObject $configuration -Name 'NetProfile'

    $result = [pscustomobject][ordered]@{
        InterfaceAlias = ConvertTo-KTNullableString -Value (
            Get-KTOptionalPropertyValue -InputObject $configuration -Name 'InterfaceAlias'
        )
        InterfaceIndex = $interfaceIndex
        Adapter = ConvertTo-KTNullableString -Value (
            Get-KTOptionalPropertyValue -InputObject $adapter -Name 'InterfaceDescription'
        )
        IPv4Address = [string[]]@(
            ConvertTo-KTStringArray -Collection $ipv4 -PropertyName 'IPAddress'
        )
        IPv6Address = [string[]]@(
            ConvertTo-KTStringArray -Collection $ipv6 -PropertyName 'IPAddress'
        )
        IPv4Gateway = [string[]]@(
            ConvertTo-KTStringArray -Collection $gateway -PropertyName 'NextHop'
        )
        DnsServers = [string[]]@(
            ConvertTo-KTStringArray -Collection (
                Get-KTOptionalPropertyValue -InputObject $dns -Name 'ServerAddresses'
            )
        )
        NetProfile = ConvertTo-KTNullableString -Value (
            Get-KTOptionalPropertyValue -InputObject $networkProfile -Name 'Name'
        )
    }

    $result.PSObject.TypeNames.Insert(0, 'KrippyTech.NetworkConfiguration')
    $result
}
