Describe 'Test-KTDNS' {
    BeforeAll {
        $script:scriptPath = Join-Path (Split-Path -Parent $PSScriptRoot) 'Test-KTDNS.ps1'

        function Get-SyntheticDnsRecord {
            param(
                [Parameter(Mandatory)]
                [string]$RecordType
            )

            $record = [ordered]@{
                Name      = 'example.com'
                QueryType = $RecordType
                Type      = $RecordType
                TTL       = 300
                Section   = 'Answer'
            }

            switch ($RecordType) {
                'A'     { $record.IPAddress = '192.0.2.10' }
                'AAAA'  { $record.IPAddress = '2001:db8::10' }
                'CNAME' { $record.NameHost = 'alias.example.com' }
                'MX'    { $record.NameExchange = 'mail.example.com'; $record.Preference = 10 }
                'NS'    { $record.NameHost = 'ns1.example.com' }
                'PTR'   { $record.NameHost = 'host.example.com' }
                'SRV'   {
                    $record.NameTarget = 'service.example.com'
                    $record.Priority = 10
                    $record.Weight = 20
                    $record.Port = 443
                }
                'TXT'   { $record.Strings = @('synthetic-', 'value') }
            }

            [pscustomobject]$record
        }
    }

    BeforeEach {
        Mock -CommandName Resolve-DnsName -MockWith {
            Get-SyntheticDnsRecord -RecordType ([string]$Type)
        }
    }

    It 'performs a valid default A query through DNS only' {
        $result = & $script:scriptPath -Name 'example.com'

        $result.RecordType | Should -Be 'A'
        $result.Value | Should -Be '192.0.2.10'
        Should -Invoke -CommandName Resolve-DnsName -Times 1 -Exactly -ParameterFilter {
            $Name -eq 'example.com' -and $DnsOnly
        }
    }

    It 'accepts and normalizes every supported record type' {
        $recordTypes = @('A', 'AAAA', 'CNAME', 'MX', 'NS', 'SRV', 'TXT', 'PTR')

        foreach ($recordType in $recordTypes) {
            $result = & $script:scriptPath -Name 'example.com' -Type $recordType
            $result.RecordType | Should -Be $recordType
            $result.Value | Should -Not -BeNullOrEmpty
        }

        Should -Invoke -CommandName Resolve-DnsName -Times 8 -Exactly
    }

    It 'passes a custom resolver as data and reports it' {
        $result = & $script:scriptPath -Name 'example.com' -Server 'resolver.example.com'

        $result.QueryServer | Should -Be 'resolver.example.com'
        Should -Invoke -CommandName Resolve-DnsName -Times 1 -Exactly -ParameterFilter {
            $Server -eq 'resolver.example.com' -and $DnsOnly
        }
    }

    It 'rejects invalid parameter input' {
        { & $script:scriptPath -Name '' } | Should -Throw
        { & $script:scriptPath -Name 'example com' } | Should -Throw
        { & $script:scriptPath -Name 'example.com' -Type 'SOA' } | Should -Throw
        { & $script:scriptPath -Name 'example.com' -Server 'resolver example.com' } | Should -Throw
    }

    It 'preserves DNS failures as terminating errors' {
        Mock -CommandName Resolve-DnsName -MockWith { throw 'Synthetic DNS failure.' }

        { & $script:scriptPath -Name 'does-not-exist.example.com' } |
            Should -Throw -ExpectedMessage '*Synthetic DNS failure*'
    }

    It 'returns a stable property set' {
        $result = & $script:scriptPath -Name 'example.com' -Type 'MX'
        $expectedProperties = @(
            'Query', 'QueryServer', 'RecordName', 'RecordType', 'TTL', 'Value',
            'Preference', 'Priority', 'Weight', 'Port', 'Section'
        )

        @($result.PSObject.Properties.Name) | Should -Be $expectedProperties
        $result.Preference | Should -Be 10
        $result.Priority | Should -BeNullOrEmpty
    }

    It 'passes punctuation as one literal name without evaluating it' {
        $punctuatedName = '_sip._tcp.example.com;Write-Output-safe'
        $result = & $script:scriptPath -Name $punctuatedName -Type 'SRV'

        $result.Query | Should -BeExactly $punctuatedName
        Should -Invoke -CommandName Resolve-DnsName -Times 1 -Exactly -ParameterFilter {
            $Name -ceq '_sip._tcp.example.com;Write-Output-safe'
        }
    }

    It 'contains no commands that write, download, configure, or handle credentials' {
        $tokens = $null
        $parseErrors = $null
        $ast = [System.Management.Automation.Language.Parser]::ParseFile(
            $script:scriptPath,
            [ref]$tokens,
            [ref]$parseErrors
        )
        $parseErrors.Count | Should -Be 0

        $commands = $ast.FindAll({
            param($node)
            $node -is [System.Management.Automation.Language.CommandAst]
        }, $true) | ForEach-Object { $_.GetCommandName() } | Where-Object { $_ }

        $commands | Sort-Object -Unique | Should -Be @(
            'Get-KTDnsPropertyValue',
            'Resolve-DnsName',
            'Set-StrictMode'
        )
    }
}
