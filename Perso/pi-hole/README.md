# Pi-hole – Déploiement et gestion avec Docker et Ansible

## 1. Présentation du projet

Ce projet permet de déployer et de gérer **Pi-hole** sur une machine Fedora à l'aide de Docker Compose et Ansible.

L'objectif est de disposer d'un service DNS filtrant, pilotable à travers quatre actions Ansible :

- `install` : installer et démarrer Pi-hole.
- `enable` : activer Pi-hole comme serveur DNS du système.
- `disable` : arrêter Pi-hole et restaurer la configuration DNS du réseau.
- `uninstall` : supprimer les ressources Docker tout en conservant les données persistantes.

La configuration DNS est gérée dynamiquement grâce à NetworkManager et systemd-resolved. Aucune interface réseau ni aucun profil Wi-Fi n'est codé en dur.

## 2. Architecture

```text
pi-hole/
├── docker-compose.yml
├── etc-pihole/                  # Données persistantes
├── scripts/
│   ├── pihole-networkmanager.sh
│   ├── pihole-dns-reload.sh
│   ├── pihole-dns-restore.sh
│   └── pihole-dns-stop.sh
└── ansible/
    ├── ansible.cfg
    ├── inventory.ini
    ├── group_vars/
    │   └── all.yml
    ├── playbook.yml
    └── roles/
        ├── install/
        │   └── tasks/main.yml
        ├── enable/
        │   └── tasks/main.yml
        ├── disable/
        │   └── tasks/main.yml
        └── uninstall/
            └── tasks/main.yml
```

### Technologies utilisées

| Technologie | Rôle |
|---|---|
| Fedora | Système hôte |
| Docker Engine | Exécution des conteneurs |
| Docker Compose | Définition et gestion du service |
| Pi-hole | Filtrage DNS |
| Ansible | Automatisation des opérations |
| NetworkManager | Gestion des connexions réseau |
| systemd-resolved | Résolution DNS du système |
| Bash | Scripts de gestion DNS |

## 3. Prérequis

Les composants suivants doivent être disponibles sur le système :

- Fedora avec NetworkManager et systemd-resolved.
- Docker Engine opérationnel.
- Docker Compose V2.
- Ansible.
- `dig` (fourni notamment par le paquet `bind-utils` sur Fedora).
- `resolvectl`.

Vérification des principaux composants :

```bash
docker --version
docker compose version
ansible --version
dig -v
resolvectl status
```

Le contexte Docker utilisé par le projet est `default`.

Vérification :

```bash
docker context show
```

## 4. Configuration

Les variables principales sont centralisées dans :

```text
ansible/group_vars/all.yml
```

| Variable | Fonction |
|---|---|
| `docker_context` | Contexte Docker utilisé |
| `pihole_project_dir` | Répertoire du projet |
| `docker_compose_file` | Fichier Docker Compose |
| `pihole_scripts_dir` | Répertoire des scripts Shell |
| `pihole_container_name` | Nom du conteneur |
| `pihole_data_dir` | Répertoire des données persistantes |
| `pihole_dns_address` | Adresse DNS locale |
| `pihole_dns_port` | Port DNS |
| `pihole_web_port` | Port de l'interface Web |

L'interface réseau active et le profil NetworkManager sont détectés dynamiquement par les scripts.

## 5. Utilisation avec Ansible

Toutes les commandes suivantes sont à exécuter depuis le répertoire `ansible/`.

### Installer Pi-hole

```bash
ansible-playbook playbook.yml \
  -e "pihole_action=install" \
  --ask-become-pass
```

Cette action :

1. Vérifie Docker et Docker Compose.
2. Vérifie la configuration Compose.
3. Prépare le répertoire des données.
4. Télécharge l'image Pi-hole.
5. Démarre le conteneur.
6. Vérifie son état.

L'installation ne modifie pas le DNS du système.

### Activer Pi-hole

```bash
ansible-playbook playbook.yml \
  -e "pihole_action=enable" \
  --ask-become-pass
```

Cette action :

1. Démarre Pi-hole si nécessaire.
2. Attend que son service DNS soit disponible.
3. Vérifie sa réponse sur `127.0.0.1:53`.
4. Configure systemd-resolved pour utiliser Pi-hole.
5. Détecte l'interface réseau active.

### Désactiver Pi-hole

```bash
ansible-playbook playbook.yml \
  -e "pihole_action=disable" \
  --ask-become-pass
```

Cette action :

1. Arrête le conteneur Pi-hole.
2. Identifie l'interface réseau active.
3. Réactive le profil NetworkManager correspondant.
4. Restaure le DNS fourni par le réseau.

Le service DNS revient ainsi à sa configuration réseau précédente.

### Désinstaller Pi-hole

```bash
ansible-playbook playbook.yml \
  -e "pihole_action=uninstall" \
  --ask-become-pass
```

Cette action :

1. Arrête Pi-hole.
2. Restaure la configuration DNS réseau.
3. Supprime les conteneurs et réseaux créés par Compose.
4. Conserve le répertoire `etc-pihole`.

**Important :** les données persistantes ne sont pas supprimées. La commande `docker compose down` est utilisée sans option `--volumes` (`-v`).

## 6. Vérifications

### Vérifier l'état du conteneur

```bash
docker --context default ps -a
```

### Tester directement le DNS Pi-hole

Lorsque Pi-hole est actif :

```bash
dig @127.0.0.1 example.com
```

Une réponse `NOERROR` indique que le serveur DNS répond correctement.

### Vérifier le DNS système

```bash
resolvectl status
```

Lorsque Pi-hole est activé, l'adresse DNS attendue est :

```text
127.0.0.1
```

### Tester la résolution système

```bash
resolvectl query example.com
```

Après désactivation, le DNS fourni par le réseau doit être de nouveau utilisé.

### Vérifier les données persistantes

```bash
du -sh ../etc-pihole/
ls -lah ../etc-pihole/
```

## 7. Gestion des données

Les données de Pi-hole sont conservées dans :

```text
etc-pihole/
```

Ce répertoire contient notamment :

- `gravity.db` : base de données des listes de blocage.
- `pihole-FTL.db` : base de données FTL.
- `pihole.toml` : configuration Pi-hole.
- `adlists.list` : listes de blocage configurées.
- Les sauvegardes et fichiers associés.

La désinstallation du service ne supprime pas ces données. Elles peuvent donc être réutilisées lors d'une nouvelle installation.

## 8. Validation fonctionnelle

Les quatre actions ont été exécutées et testées sur Fedora.

| Action | Résultat |
|---|---|
| Installation | Conteneur en état `running` |
| Activation DNS | Résolution via `127.0.0.1:53` |
| Désactivation DNS | Retour au DNS DHCP |
| Désinstallation | Conteneur et réseau Compose supprimés |
| Conservation des données | Répertoire `etc-pihole` conservé |
| Résolution après désinstallation | Fonctionnelle |

## 9. Évolutions envisagées

Les évolutions possibles du projet sont :

- Intégration de Jenkins pour piloter les actions Ansible.
- Création d'un pipeline avec paramètres pour sélectionner l'action.
- Centralisation des journaux d'exécution.
- Gestion des sauvegardes du répertoire `etc-pihole`.
- Ajout d'une procédure de restauration.

---

**Projet personnel – Automatisation du déploiement et de la gestion d'un service DNS filtrant avec Docker, Bash et Ansible.**