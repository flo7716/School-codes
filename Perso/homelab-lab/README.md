# Homelab — labo Docker (routeur, bastion, Pi-hole, Nextcloud)

Maquette de l'architecture prévue sur le ThinkCentre M920x, à tester sur un laptop avant de la porter sur des VMs Rocky/Alma.

**Deux accès séparés :**
- **Utilisateurs** → `https://nextcloud.localhost`, depuis le navigateur ou les comptes en ligne de GNOME.
- **Administration** → SSH via le bastion uniquement (shell, tunnels vers Pi-hole et Cockpit).

**Hôte cible** : AlmaLinux (ou Rocky) sur le M920x, avec Docker Engine natif, KVM/libvirt et Cockpit. Le même projet tourne sur un laptop Fedora pour les tests.

## Architecture

```
          laptop : 127.0.0.1:443 (HTTPS)      127.0.0.1:2222 (SSH admin)
                          │                         │
                ┌─────────▼─────────────────────────▼──┐
   Internet ◄───┤        ROUTEUR (nftables)             │  WAN 172.31.0.254
                │  DNAT 443 → proxy · DNAT 2222 → bastion│
                └──────┬──────────────────────────┬─────┘
          LAN 10.10.10.0/24                  ADMIN 10.10.20.0/24
 ┌────────┬────────┬─────────┬────────┐        ┌──────────┐
 │Pi-hole │ Caddy  │Nextcloud│ client │        │ BASTION  │ .10
 │  .10   │  .30   │  .20    │  .100  │        │ SSH clé  │
 └────────┴───┬────┴────┬────┴────────┘        └──────────┘
   HTTPS ─────┘ proxy → │ BACKEND 10.10.30.0/24 (non routé)
                   ┌────┴─────┬──────────┐
                   │ MariaDB  │  Redis   │
                   └──────────┴──────────┘
```

Flux autorisés par le routeur (politique par défaut : tout est refusé) :

| De → Vers | Autorisé |
|---|---|
| laptop → reverse proxy Caddy | HTTPS (443) |
| laptop → bastion | SSH (port 2222 publié, puis DNAT vers 22) |
| bastion → LAN | 22, 80, 443, ping |
| LAN → Internet | oui, sauf les réseaux privés (10/8, 172.16/12, 192.168/16) |
| LAN → admin | ❌ |
| admin → Internet | ❌ |
| backend | isolé : seul Nextcloud y est connecté, le routeur ne le voit pas |

## Prérequis

- **Docker Engine natif** (`docker-ce`) avec Compose v2, version 28 ou plus récente (`gw_priority`).
  ⚠️ **Docker Desktop n'est pas pris en charge** : réseau dans une machine virtuelle, pas de port < 1024. Vérifie que `docker context show` affiche `default`.
- `ssh`, `ssh-keygen`, `curl`.
- Le port 443 libre sur le laptop. Sinon, change `HTTPS_PUBLIC_PORT` dans `.env`.
- ~3 Go de RAM libre.

## Utilisation

```bash
chmod +x deploy.sh test.sh
./deploy.sh              # génère .env + clé SSH, build, démarre
./deploy.sh trust-ca     # 1re fois : fait confiance au certificat du labo (sudo)
./deploy.sh test         # vérifie routage, DNS, segmentation, HTTPS
```

### Nextcloud dans le navigateur

Ouvre **https://nextcloud.localhost**. Les identifiants sont dans `.env` (`NEXTCLOUD_ADMIN_*`).

`*.localhost` pointe automatiquement vers 127.0.0.1 dans les navigateurs et avec systemd-resolved. Si ce n'est pas le cas chez toi, ajoute cette ligne à `/etc/hosts` :
```
127.0.0.1  nextcloud.localhost
```

### Nextcloud dans GNOME

1. Lance `./deploy.sh trust-ca`, sinon GNOME refusera le certificat.
2. Dans Nextcloud : **Paramètres personnels → Sécurité → Créer un mot de passe d'application**. C'est mieux que d'utiliser ton mot de passe principal.
3. Dans GNOME : **Paramètres → Comptes en ligne → Nextcloud**
   - Serveur : `https://nextcloud.localhost`
   - Utilisateur : `admin` (ou ton compte)
   - Mot de passe : le mot de passe d'application
4. Fichiers (Nautilus), Agenda, Contacts et Tâches se synchronisent. La découverte CalDAV et CardDAV est assurée par Caddy.

### Administration (SSH)

```bash
ssh -F ssh_config lab-bastion   # shell sur le bastion
./deploy.sh tunnel              # Pi-hole → http://localhost:8080/admin
                                # Cockpit → https://localhost:9090
./deploy.sh status | logs [service] | down | reset
```

## Hôte AlmaLinux + Cockpit

```bash
sudo ./host/setup-host.sh   # une seule fois, idempotent
./deploy.sh
```

Le script installe :
- **Docker Engine** (dépôt officiel), avec rotation des logs et `live-restore` : les conteneurs survivent à un redémarrage du démon Docker ;
- **KVM / libvirt** pour les futures VMs, avec les démons libvirt modulaires ;
- **Cockpit** avec les modules machines virtuelles, stockage, SELinux et fichiers.

**Comment Cockpit est protégé :**
- Il n'écoute que sur `10.10.20.1:9090`, l'IP de l'hôte sur le réseau Docker `admin`. Il n'est **pas** joignable depuis le LAN de la maison.
- Le service `cockpit` est retiré de la zone firewalld par défaut.
- Accès : laptop → bastion (SSH) → `10.10.20.1:9090`, avec `./deploy.sh tunnel`.
- Connexion avec ton compte Linux (groupe `wheel`) ; `root` est interdit. Déconnexion automatique après 15 minutes d'inactivité.

**Dans Cockpit** : Docker n'apparaît pas, car le module conteneurs de Cockpit (`cockpit-podman`) ne gère que Podman. Utilise `docker` en SSH, ou passe à Podman plus tard. En revanche, Cockpit gère très bien les VMs, le stockage, les journaux, les mises à jour, SELinux et firewalld.

### Passer du laptop au serveur

Dans le `.env` du serveur :
```
BIND_IP=192.168.1.50                 # IP LAN du M920x (et non 127.0.0.1)
NEXTCLOUD_DOMAIN=nextcloud.home.arpa # *.localhost ne marche que sur la machine elle-même
```
Ensuite :
1. sur le serveur : `./deploy.sh down && ./deploy.sh`, puis `./deploy.sh nextcloud-domain` ;
2. sur chaque appareil client, faire pointer le nom vers le serveur (`/etc/hosts` ou un enregistrement DNS local) et faire confiance à la CA du labo. Copie `secrets/homelab-ca.crt` du serveur, puis `./deploy.sh trust-ca` sur un laptop Linux.

Docker ouvre lui-même les ports publiés dans firewalld (zone `docker`). Vérifie avec `sudo ss -ltnp` que seuls 443 et 2222 écoutent sur l'IP LAN.

### Instance installée avec une version précédente du labo

Les domaines approuvés de Nextcloud ne sont lus qu'à l'installation. Deux solutions :
- `./deploy.sh nextcloud-domain` met à jour l'instance existante ;
- `./deploy.sh reset` puis `./deploy.sh` repart de zéro.

## Points techniques

- **HTTPS** : Caddy génère sa propre autorité de certification (`tls internal`), conservée dans le volume `caddy-data`. Tant que ce volume existe, le certificat installé par `trust-ca` reste valable. Un `reset` le supprime : relance alors `trust-ca`.
- **Nextcloud derrière le proxy** : `TRUSTED_PROXIES`, `OVERWRITEPROTOCOL` et `OVERWRITECLIURL` sont relus à chaque démarrage. Nextcloud ne génère donc que des URL en `https://`.
- **Routes par défaut** : un petit conteneur `*-gw` partage le namespace réseau de chaque service et y remplace la route par défaut Docker par `default via <routeur>`. Les services eux-mêmes n'ont donc pas besoin de `NET_ADMIN`.
- **Pourquoi `lan` et `admin` ne sont pas `internal`** : sur un réseau `internal`, Docker ajoute sur l'hôte des règles qui jettent tout paquet dont la source ou la destination est hors du sous-réseau. Cela bloquait tout le trafic routé par le routeur (NAT vers Internet, DNAT vers le bastion et le proxy). Seul `backend` reste `internal`.
- **Si tu redémarres un service seul**, redémarre aussi son `*-gw`, sinon la route disparaît. Le plus simple : `./deploy.sh down && ./deploy.sh`.
- **Le routeur** ne gère que ses propres tables `labfw` et `labnat`, sans effacer tout le jeu de règles (`flush ruleset`), pour ne pas casser le DNS interne de Docker.
- **Le bastion** n'autorise que l'authentification par clé, un seul utilisateur, et uniquement des redirections locales vers les destinations listées dans `PermitOpen` (`bastion/sshd_config`).

## Limites (c'est un labo)

- Les accès ne sont exposés que sur `127.0.0.1` (le laptop lui-même). Pour y accéder depuis d'autres appareils, il faudrait publier sur l'IP réseau du laptop et utiliser un vrai nom de domaine.
- Les conteneurs voient l'adresse de l'hôte sur leur réseau Docker (10.10.10.1, 10.10.20.1). C'est inhérent aux bridges Docker : sur le M920x, avec de vrais VLANs, ce point disparaît.
- Pas encore de WireGuard.
- Les images `latest` / `stable` sont à figer sur des versions précises avant un usage réel.
- Podman rootless n'est pas supporté. Podman en root devrait fonctionner avec `podman compose`.
- Docker n'active pas le confinement SELinux des conteneurs par défaut (`selinux-enabled: false`). L'hôte reste en Enforcing, mais les conteneurs ne sont pas confinés : c'est une piste de durcissement, à tester (NET_ADMIN, nftables).

## Passage sur le M920x

| Labo Docker | Cible |
|---|---|
| conteneur `router` (nftables) | VM OPNsense ou VM Rocky + nftables, avec la carte réseau Intel en passthrough |
| conteneur `bastion` | VM Rocky minimale, VLAN admin, tlog + auditd |
| conteneur `proxy` (Caddy) | Caddy ou Nginx avec Podman, dans une DMZ ; certificat Let's Encrypt (DNS-01) ou CA interne |
| réseaux Docker | VLANs (switch manageable) ou bridges libvirt |
| Pi-hole / Nextcloud | conteneurs **Podman + Quadlet** |
| `nextcloud.localhost` | `nextcloud.home.arpa` résolu par Pi-hole (enregistrement DNS local) |
| `*-gw` | inutile : la route par défaut vient du DHCP du routeur |
