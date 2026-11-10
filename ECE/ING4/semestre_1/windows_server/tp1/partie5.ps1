# =========================================================================
# Script d'industrialisation Active Directory - Partie 5
# Domaine : corp.local
# =========================================================================

# 1. Configuration des chemins et de la structure des services
$DomainDN = "DC=corp,DC=local"
$BaseOUName = "Entreprise"
$BaseOUPath = "OU=$BaseOUName,$DomainDN"
$Services = @("Direction", "Finance", "Informatique", "Commercial")

# Chemin vers le fichier CSV (à adapter si nécessaire)
$CsvPath = "C:\temp\collaborateurs.csv"

# Vérification et création de l'OU racine "Entreprise"
if (-not (Get-ADOrganizationalUnit -Filter "Name -eq '$BaseOUName'" -ErrorAction SilentlyContinue)) {
    New-ADOrganizationalUnit -Name $BaseOUName -Path $DomainDN -ProtectedFromAccidentalDeletion $false
    Write-Host "[+] OU racine '$BaseOUName' créée avec succès." -ForegroundColor Green
} else {
    Write-Host "[=] L'OU racine '$BaseOUName' existe déjà." -ForegroundColor Yellow
}

# 2. Création des sous-OU par service (avec séparation Utilisateurs, Groupes, Postes)
foreach ($Service in $Services) {
    $ServiceOUPath = "OU=$Service,$BaseOUPath"
    
    if (-not (Get-ADOrganizationalUnit -Filter "Name -eq '$Service'" -SearchBase $BaseOUPath -ErrorAction SilentlyContinue)) {
        New-ADOrganizationalUnit -Name $Service -Path $BaseOUPath -ProtectedFromAccidentalDeletion $false
        Write-Host "  [+] Sous-OU service '$Service' créée." -ForegroundColor Green
    } else {
        Write-Host "  [=] Sous-OU service '$Service' déjà existante." -ForegroundColor Yellow
    }

    # Sous-conteneurs optionnels pour structurer (Utilisateurs, Groupes, Postes)
    $SubOUs = @("Utilisateurs", "Groupes", "Postes")
    foreach ($Sub in $SubOUs) {
        $SubPath = "OU=$Sub,$ServiceOUPath"
        if (-not (Get-ADOrganizationalUnit -Filter "Name -eq '$Sub'" -SearchBase $ServiceOUPath -ErrorAction SilentlyContinue)) {
            New-ADOrganizationalUnit -Name $Sub -Path $ServiceOUPath -ProtectedFromAccidentalDeletion $false
        }
    }
}

# 3. Création des groupes globaux de sécurité par service
foreach ($Service in $Services) {
    $GroupName = "GG_$Service"
    $GroupPath = "OU=Groupes,OU=$Service,$BaseOUPath"

    if (-not (Get-ADGroup -Filter "Name -eq '$GroupName'" -ErrorAction SilentlyContinue)) {
        New-ADGroup -Name $GroupName -GroupScope Global -GroupCategory Security -Path $GroupPath -Description "Groupe de sécurité pour le service $Service"
        Write-Host "[+] Groupe de sécurité '$GroupName' créé." -ForegroundColor Green
    } else {
        Write-Host "[=] Le groupe '$GroupName' existe déjà." -ForegroundColor Yellow
    }
}

# 4. Importation et traitement des utilisateurs depuis le CSV
if (Test-Path $CsvPath) {
    $Collaborateurs = Import-Csv -Path $CsvPath -Delimiter ";"

    foreach ($Pers in $Collaborateurs) {
        $Prenom = $Pers.Prenom
        $Nom = $Pers.Nom
        $Service = $Pers.Service
        
        # Génération de l'identifiant de connexion unique (ex: p.nom) avec gestion des collisions
        $BaseSam = "$($Prenom.Substring(0,1).ToLower()).$($Nom.ToLower())"
        $SamAccountName = $BaseSam
        $counter = 1

        while (Get-ADUser -Filter "SamAccountName -eq '$SamAccountName'" -ErrorAction SilentlyContinue) {
            $SamAccountName = "$BaseSam$counter"
            $counter++
        }

        $UserPrincipalName = "$SamAccountName@corp.local"
        $UserPath = "OU=Utilisateurs,OU=$Service,$BaseOUPath"
        $DisplayName = "$Prenom $Nom"
        $Password = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force

        # Vérification de l'existence de l'utilisateur par UPN
        if (-not (Get-ADUser -Filter "UserPrincipalName -eq '$UserPrincipalName'" -ErrorAction SilentlyContinue)) {
            try {
                New-ADUser -Name $DisplayName `
                           -GivenName $Prenom `
                           -Surname $Nom `
                           -SamAccountName $SamAccountName `
                           -UserPrincipalName $UserPrincipalName `
                           -Path $UserPath `
                           -AccountPassword $Password `
                           -Enabled $true
                Write-Host "  [+] Utilisateur '$DisplayName' ($SamAccountName) créé dans l'OU $Service." -ForegroundColor Green
            } catch {
                Write-Error "  [!] Erreur lors de la création de l'utilisateur $DisplayName : $_"
            }
        } else {
            Write-Host "  [=] L'utilisateur '$DisplayName' ($SamAccountName) existe déjà." -ForegroundColor Yellow
        }

        # 5. Ajout de l'utilisateur au groupe de sécurité de son service
        $TargetGroup = "GG_$Service"
        $GroupObj = Get-ADGroup -Filter "Name -eq '$TargetGroup'" -ErrorAction SilentlyContinue

        if ($GroupObj) {
            $IsMember = Get-ADGroupMember -Identity $TargetGroup -ErrorAction SilentlyContinue | Where-Object {$_.distinguishedName -eq (Get-ADUser -Identity $SamAccountName).distinguishedName}

            if (-not $IsMember) {
                Add-ADGroupMember -Identity $TargetGroup -Members $SamAccountName
                Write-Host "    [+] Utilisateur $SamAccountName ajouté au groupe $TargetGroup." -ForegroundColor Green
            } else {
                Write-Host "    [=] L'utilisateur $SamAccountName est déjà membre de $TargetGroup." -ForegroundColor Yellow
            }
        }
    }
} else {
    Write-Warning "Le fichier CSV est introuvable à l'emplacement : $CsvPath"
}