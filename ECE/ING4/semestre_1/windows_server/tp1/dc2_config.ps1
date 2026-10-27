##Etape 1 : Renommer le DC2 et configurer l'adresse IP fixe
# Renommer le DC2 avec le nom "DC2-FLOADVICIL" et redémarrer le serveur
Rename-Computer -NewName "DC2-FLOADVICIL" -Restart

# Affichez les cartes réseaux pour récupérer le nom exact (ex: "Ethernet0")
Get-NetAdapter

# Attribuez l'adresse IP fixe (ex: 192.168.100.11) sans passerelle puisque le réseau est isolé
New-NetIPAddress -InterfaceAlias "Ethernet0" -IPAddress "192.168.100.11" -PrefixLength 24

# Indiquez DC1 (192.168.100.10) comme serveur DNS principal pour qu'il puisse résoudre le domaine existant
Set-DnsClientServerAddress -InterfaceAlias "Ethernet0" -ServerAddresses ("192.168.100.10")

# Test connectivité avec DC1
Test-Connection 192.168.100.10


##Etape 2 : Promouvoir le DC2 en tant que contrôleur de domaine supplémentaire
# Installer le rôle AD DS (Active Directory Domain Services)
Install-WindowsFeature AD-Domain-Services -IncludeManagementTools

# couper le parefeu pour permettre la communication entre les deux DCs (sur DC1)
Set-NetFirewallProfile -Enabled False

# Promouvoir le DC2 en tant que contrôleur de domaine supplémentaire dans le domaine "corp.local", avec installation de DNS et en utilisant les chemins par défaut pour la base de données, les journaux et SYSVOL. Le serveur sera redémarré automatiquement après l'installation.
Install-ADDSDomainController `
    -NoGlobalCatalog:$false `
    -CreateDnsDelegation:$false `
    -CriticalReplicationOnly:$false `
    -DatabasePath "C:\Windows\NTDS" `
    -DomainName "corp.local" `
    -InstallDns:$true `
    -LogPath "C:\Windows\NTDS" `
    -NoRebootOnCompletion:$false `
    -SiteName "Default-First-Site-Name" `
    -SysvolPath "C:\Windows\SYSVOL" `
    -Force