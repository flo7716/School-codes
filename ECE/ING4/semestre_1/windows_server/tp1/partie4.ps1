# 4.1 Vérification de la réplication entre les deux DCs
# Test complet de santé du contrôleur de domaine local
Dcdiag /v

# Résumé de l'état de la réplication entre DC1 et DC2
repadmin /replsummary

# Vérification détaillée des connexions de réplication entrantes/sortantes
repadmin /showrepl

# 4.2 Vérification de la réplication du SYSVOL entre les deux DCs 
#Vérification du bon fonctionnement du service DFSR pour SYSVOL
Get-CimInstance -Namespace "root\MicrosoftDFS" -ClassName DfsrVolumeConfig

# Test d'accès au partage SYSVOL distant depuis l'autre DC
ls \\DC1-FLOADVICIL\SYSVOL\corp.local

##4.3 Test de réplication entre les deux DCs
# Exécuter sur DC1 : Création d'un utilisateur de test
New-ADUser -Name "TestRepl" -SamAccountName "TestRepl" -UserPrincipalName "TestRepl@corp.local" -Path "CN=Users,DC=corp,DC=local" -Enabled $true

# Exécuter sur DC2 : Forcer la réplication immédiate si besoin
repadmin /syncall /A /e /P

# Vérifier la présence de l'objet sur DC2
Get-ADUser -Identity "TestRepl"