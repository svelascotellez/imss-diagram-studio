#
# SddFramework.psd1 - Manifiesto del módulo PowerShell SDD Framework
#

@{
    RootModule = 'setup-sdd-project-v66.ps1'
    ModuleVersion = '6.6.0'
    CompatiblePSEditions = @('Desktop', 'Core')
    GUID = 'b48e3cf2-1b15-4cf8-842c-a29938bb5d1a'
    Author = 'Salvador Velasco & Antigravity (Google DeepMind Team)'
    CompanyName = 'SDD Framework Open Source Initiative'
    Copyright = '(c) 2026 Salvador Velasco. Todos los derechos reservados.'
    Description = 'Marco de Gobernanza Matemática, Candado Criptográfico HMAC-SHA256 y Compliance para Agentes de IA'
    PowerShellVersion = '5.1'
    FunctionsToExport = @('New-SddProject')
    CmdletsToExport = @()
    VariablesToExport = @()
    AliasesToExport = @('sdd-init')
    PrivateData = @{
        PSData = @{
            Tags = @('SDD', 'BDD', 'CleanArchitecture', 'HMAC-SHA256', 'AIAgents', 'Compliance', 'Governance')
            LicenseUri = 'https://github.com/svelascotellez/ssd-projects/blob/main/LICENSE'
            ProjectUri = 'https://github.com/svelascotellez/ssd-projects'
        }
    }
}
