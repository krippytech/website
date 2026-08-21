#requires -Version 5.1
#requires -Modules DnsClient

<#
.SYNOPSIS
Performs a read-only DNS query and returns normalized PowerShell objects.

.DESCRIPTION
Test-KTDNS queries a name by using the Windows DnsClient module. Resolution is
explicitly limited to DNS; LLMNR and NetBIOS fallback are not used.

The script does not modify DNS, write files, download content, change local or
remote configuration, or request credentials. DNS queries may be logged by the
selected resolver, so do not query sensitive internal names through an
untrusted DNS server.

.PARAMETER Name
The DNS name or address to query. Control characters and whitespace are not
accepted. Names containing ordinary DNS punctuation, such as underscores,
hyphens, and periods, are passed to Resolve-DnsName as data.

.PARAMETER Type
The record type to request. Supported values are A, AAAA, CNAME, MX, NS, SRV,
TXT, and PTR. The default is A.

.PARAMETER Server
An optional DNS server IP address or host name. When omitted, Windows uses the
DNS servers configured on the active network interface. The value is passed as
data to Resolve-DnsName and must not contain whitespace or control characters.

.EXAMPLE
PS> .\Test-KTDNS.ps1 -Name example.com

Queries the system-configured DNS resolver for A records for example.com.

.EXAMPLE
PS> .\Test-KTDNS.ps1 -Name example.com -Type MX

Queries MX records and returns each result with a stable property set.

.EXAMPLE
PS> .\Test-KTDNS.ps1 -Name localhost -Type A

Queries the DNS protocol for the synthetic local host name.

.EXAMPLE
PS> .\Test-KTDNS.ps1 -Name example.com -Type TXT -Server '<dns-server-ip>'

Shows the custom-resolver syntax. Replace the placeholder only with an approved
DNS resolver. Do not send internal names to an untrusted resolver.

.INPUTS
None. This script does not accept pipeline input.

.OUTPUTS
System.Management.Automation.PSCustomObject. Each record contains Query,
QueryServer, RecordName, RecordType, TTL, Value, Preference, Priority, Weight,
Port, and Section. Fields that do not apply to a record type are null.

.NOTES
Version: 1.0.0
Requires: Windows PowerShell 5.1 or PowerShell 7 on Windows; DnsClient module
License: MIT
Approved seed SHA-256: E1C61B20B5888FE21B583C8E5977351F94D346D584A0DF02CF9B08A65B37F2EC

.LINK
https://learn.microsoft.com/powershell/module/dnsclient/resolve-dnsname
#>
[CmdletBinding()]
[OutputType([pscustomobject])]
param(
    [Parameter(Mandatory, Position = 0)]
    [ValidateLength(1, 253)]
    [ValidateScript({
        if ([string]::IsNullOrWhiteSpace($_)) {
            throw 'Name cannot be empty or whitespace.'
        }
        if ($_ -match '[\x00-\x20\x7F]') {
            throw 'Name cannot contain whitespace or control characters.'
        }
        $true
    })]
    [string]$Name,

    [ValidateSet('A', 'AAAA', 'CNAME', 'MX', 'NS', 'SRV', 'TXT', 'PTR')]
    [string]$Type = 'A',

    [ValidateLength(1, 253)]
    [ValidateScript({
        if ([string]::IsNullOrWhiteSpace($_)) {
            throw 'Server cannot be empty or whitespace.'
        }
        if ($_ -match '[\x00-\x20\x7F]') {
            throw 'Server cannot contain whitespace or control characters.'
        }
        $true
    })]
    [string]$Server
)

Set-StrictMode -Version 3.0
$ErrorActionPreference = 'Stop'

function Get-KTDnsPropertyValue {
    param(
        [Parameter(Mandatory)]
        [object]$InputObject,

        [Parameter(Mandatory)]
        [string]$PropertyName
    )

    $property = $InputObject.PSObject.Properties[$PropertyName]
    if ($null -ne $property) {
        return $property.Value
    }

    return $null
}

$resolveParameters = @{
    Name        = $Name
    Type        = $Type
    DnsOnly     = $true
    ErrorAction = 'Stop'
}

if ($PSBoundParameters.ContainsKey('Server')) {
    $resolveParameters.Server = $Server
}

$records = @(Resolve-DnsName @resolveParameters)
$queryServer = if ($PSBoundParameters.ContainsKey('Server')) { $Server } else { 'System default' }

foreach ($record in $records) {
    $recordType = [string](Get-KTDnsPropertyValue -InputObject $record -PropertyName 'QueryType')
    if ([string]::IsNullOrWhiteSpace($recordType)) {
        $recordType = [string](Get-KTDnsPropertyValue -InputObject $record -PropertyName 'Type')
    }

    $value = switch ($recordType) {
        'A'     { Get-KTDnsPropertyValue -InputObject $record -PropertyName 'IPAddress' }
        'AAAA'  { Get-KTDnsPropertyValue -InputObject $record -PropertyName 'IPAddress' }
        'CNAME' { Get-KTDnsPropertyValue -InputObject $record -PropertyName 'NameHost' }
        'MX'    { Get-KTDnsPropertyValue -InputObject $record -PropertyName 'NameExchange' }
        'NS'    { Get-KTDnsPropertyValue -InputObject $record -PropertyName 'NameHost' }
        'PTR'   { Get-KTDnsPropertyValue -InputObject $record -PropertyName 'NameHost' }
        'SRV'   { Get-KTDnsPropertyValue -InputObject $record -PropertyName 'NameTarget' }
        'TXT'   {
            $strings = @(Get-KTDnsPropertyValue -InputObject $record -PropertyName 'Strings')
            $strings -join ''
        }
        default { $null }
    }

    [pscustomobject][ordered]@{
        Query       = $Name
        QueryServer = $queryServer
        RecordName  = Get-KTDnsPropertyValue -InputObject $record -PropertyName 'Name'
        RecordType  = $recordType
        TTL         = Get-KTDnsPropertyValue -InputObject $record -PropertyName 'TTL'
        Value       = $value
        Preference  = Get-KTDnsPropertyValue -InputObject $record -PropertyName 'Preference'
        Priority    = Get-KTDnsPropertyValue -InputObject $record -PropertyName 'Priority'
        Weight      = Get-KTDnsPropertyValue -InputObject $record -PropertyName 'Weight'
        Port        = Get-KTDnsPropertyValue -InputObject $record -PropertyName 'Port'
        Section     = [string](Get-KTDnsPropertyValue -InputObject $record -PropertyName 'Section')
    }
}
