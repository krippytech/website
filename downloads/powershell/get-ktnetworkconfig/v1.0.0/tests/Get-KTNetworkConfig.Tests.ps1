Describe 'Get-KTNetworkConfig v1.0.0 release contract' {
    BeforeAll {
        $releaseRoot = Split-Path -Parent $PSScriptRoot
        $scriptUnderTest = Join-Path $releaseRoot 'Get-KTNetworkConfig.ps1'
        function Get-KTSyntheticNetworkConfiguration {
            [CmdletBinding()]
            [OutputType([pscustomobject])]
            param(
                [string]$Alias = 'Lab Ethernet',
                [int]$Index = 12,
                [string]$Status = 'Up',
                [object[]]$IPv4 = @([pscustomobject]@{ IPAddress = '192.0.2.20' }),
                [object[]]$IPv6 = @([pscustomobject]@{ IPAddress = '2001:db8::20' }),
                [object[]]$Gateway = @([pscustomobject]@{ NextHop = '192.0.2.1' }),
                [AllowNull()]
                [object]$Dns = [pscustomobject]@{
                    ServerAddresses = @('192.0.2.53', '2001:db8::53')
                },
                [AllowNull()]
                [object]$NetworkProfile = [pscustomobject]@{ Name = 'Synthetic Lab' },
                [AllowNull()]
                [object]$Adapter = $null
            )

            if ($null -eq $Adapter) {
                $Adapter = [pscustomobject]@{
                    Status = $Status
                    InterfaceDescription = 'Synthetic Ethernet Adapter'
                }
            }

            return [pscustomobject]@{
                InterfaceAlias = $Alias
                InterfaceIndex = $Index
                NetAdapter = $Adapter
                IPv4Address = $IPv4
                IPv6Address = $IPv6
                IPv4DefaultGateway = $Gateway
                DNSServer = $Dns
                NetProfile = $NetworkProfile
            }
        }

        function Get-KTScriptAst {
            [CmdletBinding()]
            [OutputType([System.Management.Automation.Language.ScriptBlockAst])]
            param()

            $parseTokens = $null
            $parseErrors = $null
            return [System.Management.Automation.Language.Parser]::ParseFile(
                $scriptUnderTest,
                [ref]$parseTokens,
                [ref]$parseErrors
            )
        }

        function Get-KTScriptCommandName {
            [CmdletBinding()]
            [OutputType([string[]])]
            param()

            $scriptAst = Get-KTScriptAst
            return [string[]]@(
                $scriptAst.FindAll({
                    param($node)
                    $node -is [System.Management.Automation.Language.CommandAst]
                }, $true) |
                    ForEach-Object { $_.GetCommandName() } |
                    Where-Object { $null -ne $_ } |
                    Sort-Object -Unique
            )
        }
    }

    It 'parses successfully under the current engine' {
        $parseTokens = $null
        $parseErrors = $null
        [void][System.Management.Automation.Language.Parser]::ParseFile(
            $scriptUnderTest,
            [ref]$parseTokens,
            [ref]$parseErrors
        )
        $parseErrors.Count | Should -Be 0
    }

    It 'exposes zero script parameters' {
        $scriptAst = Get-KTScriptAst
        $scriptAst.ParamBlock.Parameters.Count | Should -Be 0
    }

    It 'declares the required compatibility boundaries' {
        $sourceText = [System.IO.File]::ReadAllText($scriptUnderTest)
        $sourceText | Should -Match '(?m)^#requires -Version 5\.1$'
        $sourceText | Should -Match '(?m)^#requires -Modules NetTCPIP$'
    }

    Context 'with complete synthetic discovery data' {
        BeforeEach {
            $syntheticConfigurations = @(
                (Get-KTSyntheticNetworkConfiguration -Alias 'Lab Ethernet A' -Index 12),
                (Get-KTSyntheticNetworkConfiguration -Alias 'Lab Ethernet B' -Index 18 -IPv4 @(
                    [pscustomobject]@{ IPAddress = '198.51.100.20' },
                    [pscustomobject]@{ IPAddress = '198.51.100.21' }
                ) -Dns ([pscustomobject]@{
                    ServerAddresses = @('198.51.100.53', '2001:db8::53')
                }))
            )
            Mock Get-NetIPConfiguration { return $syntheticConfigurations }
        }

        It 'calls local discovery once with terminating error behavior' {
            [void]@(& $scriptUnderTest)
            Should -Invoke -CommandName Get-NetIPConfiguration -Times 1 -Exactly
            [System.IO.File]::ReadAllText($scriptUnderTest) |
                Should -Match 'Get-NetIPConfiguration\s+-ErrorAction\s+Stop'
        }

        It 'returns one object for each active synthetic configuration' {
            $results = @(& $scriptUnderTest)
            $results.Count | Should -Be 2
            $results[0].PSObject.TypeNames[0] |
                Should -BeExactly 'KrippyTech.NetworkConfiguration'
        }

        It 'preserves the exact eight-property order on every object' {
            $expectedProperties = @(
                'InterfaceAlias',
                'InterfaceIndex',
                'Adapter',
                'IPv4Address',
                'IPv6Address',
                'IPv4Gateway',
                'DnsServers',
                'NetProfile'
            )
            $results = @(& $scriptUnderTest)
            foreach ($result in $results) {
                @($result.PSObject.Properties.Name) | Should -Be $expectedProperties
            }
        }

        It 'uses stable scalar and array property types' {
            $result = @(& $scriptUnderTest)[0]
            $result.InterfaceAlias | Should -BeOfType [string]
            $result.InterfaceIndex | Should -BeOfType [int]
            $result.Adapter | Should -BeOfType [string]
            ($result.IPv4Address -is [string[]]) | Should -BeTrue
            ($result.IPv6Address -is [string[]]) | Should -BeTrue
            ($result.IPv4Gateway -is [string[]]) | Should -BeTrue
            ($result.DnsServers -is [string[]]) | Should -BeTrue
            $result.NetProfile | Should -BeOfType [string]
        }

        It 'preserves multiple addresses and DNS servers without joining them' {
            $result = @(& $scriptUnderTest)[1]
            $result.IPv4Address | Should -Be @('198.51.100.20', '198.51.100.21')
            $result.DnsServers | Should -Be @('198.51.100.53', '2001:db8::53')
            ($result.IPv4Address -is [string[]]) | Should -BeTrue
            ($result.DnsServers -is [string[]]) | Should -BeTrue
        }
    }

    Context 'with missing or partial synthetic properties' {
        It 'returns an empty string array when IPv4 information is missing' {
            $syntheticConfigurations = @(
                Get-KTSyntheticNetworkConfiguration -IPv4 @()
            )
            Mock Get-NetIPConfiguration { return $syntheticConfigurations }
            $result = @(& $scriptUnderTest)[0]
            $result.IPv4Address.Count | Should -Be 0
            ($result.IPv4Address -is [string[]]) | Should -BeTrue
        }

        It 'returns an empty string array when IPv6 information is missing' {
            $syntheticConfigurations = @(
                Get-KTSyntheticNetworkConfiguration -IPv6 @()
            )
            Mock Get-NetIPConfiguration { return $syntheticConfigurations }
            $result = @(& $scriptUnderTest)[0]
            $result.IPv6Address.Count | Should -Be 0
            ($result.IPv6Address -is [string[]]) | Should -BeTrue
        }

        It 'returns an empty string array when gateway information is missing' {
            $syntheticConfigurations = @(
                Get-KTSyntheticNetworkConfiguration -Gateway @()
            )
            Mock Get-NetIPConfiguration { return $syntheticConfigurations }
            $result = @(& $scriptUnderTest)[0]
            $result.IPv4Gateway.Count | Should -Be 0
            ($result.IPv4Gateway -is [string[]]) | Should -BeTrue
        }

        It 'returns an empty string array when DNS information is missing' {
            $syntheticConfigurations = @(
                Get-KTSyntheticNetworkConfiguration -Dns $null
            )
            Mock Get-NetIPConfiguration { return $syntheticConfigurations }
            $result = @(& $scriptUnderTest)[0]
            $result.DnsServers.Count | Should -Be 0
            ($result.DnsServers -is [string[]]) | Should -BeTrue
        }

        It 'returns null when network profile information is missing' {
            $syntheticConfigurations = @(
                Get-KTSyntheticNetworkConfiguration -NetworkProfile $null
            )
            Mock Get-NetIPConfiguration { return $syntheticConfigurations }
            $result = @(& $scriptUnderTest)[0]
            $result.NetProfile | Should -BeNullOrEmpty
        }

        It 'handles entirely absent optional properties safely' {
            $syntheticConfigurations = @(
                [pscustomobject]@{
                    InterfaceAlias = 'Partial Lab Adapter'
                    InterfaceIndex = 33
                    NetAdapter = [pscustomobject]@{ Status = 'Up' }
                }
            )
            Mock Get-NetIPConfiguration { return $syntheticConfigurations }
            $result = @(& $scriptUnderTest)[0]
            $result.Adapter | Should -BeNullOrEmpty
            $result.NetProfile | Should -BeNullOrEmpty
            ($result.IPv4Address -is [string[]]) | Should -BeTrue
            $result.IPv4Address.Count | Should -Be 0
            ($result.IPv6Address -is [string[]]) | Should -BeTrue
            $result.IPv6Address.Count | Should -Be 0
            ($result.IPv4Gateway -is [string[]]) | Should -BeTrue
            $result.IPv4Gateway.Count | Should -Be 0
            ($result.DnsServers -is [string[]]) | Should -BeTrue
            $result.DnsServers.Count | Should -Be 0
        }
    }

    It 'retains only configurations whose adapter status is exactly Up' {
        $syntheticConfigurations = @(
            (Get-KTSyntheticNetworkConfiguration -Alias 'Up Lab Adapter' -Status 'Up'),
            (Get-KTSyntheticNetworkConfiguration -Alias 'Disconnected Lab Adapter' -Status 'Disconnected'),
            (Get-KTSyntheticNetworkConfiguration -Alias 'Disabled Lab Adapter' -Status 'Disabled'),
            [pscustomobject]@{
                InterfaceAlias = 'No Adapter Evidence'
                InterfaceIndex = 40
            }
        )
        Mock Get-NetIPConfiguration { return $syntheticConfigurations }
        $results = @(& $scriptUnderTest)
        $results.Count | Should -Be 1
        $results[0].InterfaceAlias | Should -BeExactly 'Up Lab Adapter'
    }

    It 'throws a terminating InvalidOperationException when discovery fails' {
        Mock Get-NetIPConfiguration { throw 'Synthetic discovery failure' }
        { & $scriptUnderTest } |
            Should -Throw -ExceptionType ([System.InvalidOperationException]) -ExpectedMessage '*Unable to read the local Windows network configuration.*'
    }

    It 'uses only the approved read-only command inventory' {
        $commandNames = Get-KTScriptCommandName
        $expectedCommands = @(
            'ConvertTo-KTNullableString',
            'ConvertTo-KTStringArray',
            'Get-KTOptionalPropertyValue',
            'Get-NetIPConfiguration',
            'Set-StrictMode'
        )
        $commandNames | Should -Be $expectedCommands
    }

    It 'contains no remote, credential, file-write, process, or dynamic execution behavior' {
        $sourceText = [System.IO.File]::ReadAllText($scriptUnderTest)
        $sourceText | Should -Not -Match '(?i)\bInvoke-Expression\b|\biex\b|&\s*\$|\.Invoke\('

        $forbiddenCommands = @(
            'Add-Content', 'Add-Type', 'Clear-Content', 'Copy-Item', 'Enter-PSSession',
            'Export-Clixml', 'Export-Csv', 'Get-Credential', 'Invoke-Command',
            'Invoke-Expression', 'Invoke-RestMethod', 'Invoke-WebRequest', 'Move-Item',
            'New-CimSession', 'New-Item', 'New-PSSession', 'Out-File', 'Register-ScheduledTask',
            'Remove-Item', 'Restart-Service', 'Set-Content', 'Set-DnsClientServerAddress',
            'Set-NetIPAddress', 'Set-NetIPInterface', 'Set-NetRoute', 'Set-Service',
            'Start-BitsTransfer', 'Start-Process', 'Start-Service', 'Stop-Service',
            'Unregister-ScheduledTask', 'Write-Host', 'cmd.exe', 'powershell.exe', 'pwsh.exe'
        )
        $commandNames = Get-KTScriptCommandName
        foreach ($commandName in $forbiddenCommands) {
            $commandNames | Should -Not -Contain $commandName
        }
    }

    It 'returns ordinary pipeline objects rather than formatting data' {
        $syntheticConfigurations = @(
            Get-KTSyntheticNetworkConfiguration
        )
        Mock Get-NetIPConfiguration { return $syntheticConfigurations }
        $result = @(& $scriptUnderTest)[0]
        $result.GetType().FullName |
            Should -BeExactly 'System.Management.Automation.PSCustomObject'
        $result.PSObject.TypeNames |
            Should -Not -Contain 'Microsoft.PowerShell.Commands.Internal.Format.FormatStartData'
    }
}
