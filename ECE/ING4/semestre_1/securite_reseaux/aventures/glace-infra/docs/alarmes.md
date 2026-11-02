# Détection d'incidents et alarmes

Deux mécanismes complémentaires, tous deux centralisés en zone ADMIN (`srv-logs`) :

- **Suricata (IDS réseau)** : une sonde par machine DMZ (`ids-ftp`, `ids-web`), en partage
  de namespace réseau avec `srv-ftp`/`srv-web` — elle voit donc tout le trafic reçu/émis par
  ces conteneurs, y compris un scan de ports ciblant leur IP. Les alertes (`eve.json`) sont
  relayées en temps réel vers `srv-logs:514` (`ids/forward.py`).
- **fail2ban** : tourne sur `srv-logs` et surveille les logs centralisés (reçus via rsyslog
  depuis `srv-web`/`srv-ftp`) pour détecter des motifs répétés.

| Étape d'attaque | Où ça se voit | Règle |
|---|---|---|
| Scan de ports | `eve.json` de `ids-ftp`/`ids-web` | Suricata sid 1000001 (seuil : 10 connexions/5 s depuis une même IP) |
| Connexion FTP anonyme | `eve.json` de `ids-ftp` + `vsftpd.log` sur `srv-logs` | Suricata sid 1000002 ; fail2ban `ftp-anonymous-recon` |
| Téléchargement de `config.php.bak` | `eve.json` de `ids-ftp` | Suricata sid 1000003 |
| Injection SQL sur `recherche.php` | `eve.json` de `ids-web` + `apache-access.log` sur `srv-logs` | Suricata sid 1000004 ; fail2ban `web-sqli-attempt` |
| Scan de répertoires (gobuster) | `eve.json` de `ids-web` | Suricata sid 1000005 (seuil : 15× 404/10 s) |
| Brute force sur `login.php` | `apache-error.log` sur `srv-logs` | fail2ban `web-login-bruteforce` (5 échecs/2 min) |

## Limite assumée (bridge Docker)

Un conteneur attaché simplement au réseau `dmz` ne verrait **pas** le trafic unicast des
autres conteneurs (le bridge Linux se comporte comme un switch). C'est pourquoi chaque sonde
IDS partage directement le namespace réseau de la machine qu'elle surveille
(`network_mode: "service:ftp"` / `"service:web"`) plutôt que d'être simplement raccordée au
réseau `dmz` : elle a ainsi une visibilité réelle, et non simulée, sur le trafic reçu par
chaque service exposé.

## Limite assumée (fail2ban conteneurisé)

Dans ce conteneur de démonstration, `jail.local` utilise l'action par défaut (bannissement
iptables), mais `srv-logs` n'a pas accès aux interfaces réseau de `srv-web`/`srv-ftp` : le
bannissement reste donc local au conteneur `srv-logs` et ne bloque pas réellement
l'attaquant. En production, fail2ban devrait soit tourner sur l'hôte (comme
`firewall/host-firewall.sh`), soit piloter un jeu de règles partagé avec celui-ci.

## Procédure en cas d'alerte

1. Identifier la règle déclenchée et sa gravité (voir `plan-continuite-reprise.md` §5).
2. Consulter `/var/log/remote/<hôte>/` sur `srv-logs` autour de l'horodatage de l'alerte.
3. Appliquer la procédure de confinement/éradication/reprise du PRA.
