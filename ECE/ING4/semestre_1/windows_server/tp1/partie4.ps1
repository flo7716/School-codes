# ==========================================
# Script de contrôle de santé et de réplication AD
# Domaine : corp.local
# ==========================================

Write-Host "=== 1. État général du contrôleur de domaine ===" -ForegroundColor Cyan
Dcdiag /v

Write-Host "`n=== 2. État de la réplication Active Directory ===" -ForegroundColor Cyan
repadmin /replsummary
repadmin /showrepl

Write-Host "`n=== 3. Vérification de la résolution DNS et des enregistrements SRV ===" -ForegroundColor Cyan
# Test de résolution du domaine et des contrôleurs
Resolve-DnsName corp.local
# Vérification des enregistrements SRV critiques pour la localisation des DC
Get-DnsServerResourceRecord -ZoneName "corp.local" -Name "_ldap._tcp.dc._msdcs" -ErrorAction SilentlyContinue

Write-Host "`n=== 4. Vérification de la cohérence SYSVOL (DFSR) ===" -ForegroundColor Cyan
Get-CimInstance -Namespace "root\MicrosoftDFS" -ClassName DfsrVolumeConfig | Select-Object VolumeName, ReplicationGroupName

Write-Host "`n=== 5. Test de création et de réplication d'objet (Q4.3) ===" -ForegroundColor Cyan
$testUser = "TestReplUser"

# Création sur le DC local (ou DC1)
if (-not (Get-ADUser -Filter "SamAccountName -eq '$testUser'" -ErrorAction SilentlyContinue)) {
    New-ADUser -Name $testUser -SamAccountName $testUser -UserPrincipalName "$testUser@corp.local" -Path "CN=Users,DC=corp,DC=local" -Enabled $true -AccountPassword (ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force)
    Write-Host "Utilisateur $testUser créé avec succès." -ForegroundColor Green
} else {
    Write-Host "L'utilisateur $testUser existe déjà." -ForegroundColor Yellow
}

# Forcer la synchronisation de réplication
repadmin /syncall /A /e /P | Out-Null
Start-Sleep -Seconds 3

# Vérification de la présence de l'objet
if (Get-ADUser -Identity $testUser) {
    Write-Host "Objet $testUser trouvé et répliqué avec succès." -ForegroundColor Green
} else {
    Write-Warning "L'objet $testUser n'est pas encore visible."
}