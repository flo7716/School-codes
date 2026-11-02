# Plan de Continuité et de Reprise d'Activité — GlaceCorp

Aligné sur la logique PDCA d'ISO 22301, pour l'infrastructure "Le Chemin de la Glace"
(srv-ftp, srv-web, srv-db, srv-logs).

## 1. Contexte et périmètre

- Scénario redouté principal : un attaquant exploite l'anonymat FTP (vulnérabilité 1) pour
  obtenir des indices, puis l'injection SQL de `recherche.php` (vulnérabilité 2) pour lire la
  table `secrets` de `srv-db`, située en zone LAN, normalement inaccessible depuis Internet.
- Scénario secondaire : brute force sur `login.php`.

## 2. Analyse d'impact (BIA simplifiée)

| Actif | Impact si compromis/indisponible | RTO cible | RPO cible |
|---|---|---|---|
| srv-web (catalogue + accès LAN) | Perte de service + porte d'entrée vers srv-db | 1 h | — |
| srv-db (glace_db) | Confidentialité des tables `users`/`secrets` en jeu | 2 h | 4 h |
| srv-ftp | Fuite d'informations internes (identifiants) | 1 h | — |
| srv-logs (zone ADMIN) | Perte de visibilité pendant l'incident | 30 min | — |

## 3. Stratégie de continuité (PCA)

- **Segmentation réseau en profondeur** : `dmz` (seule zone publiée, ports 80/21), `lan` et
  `admin` en `internal: true` (aucune sortie Internet). Seul `srv-web` est autorisé vers
  `srv-db` (flux LAN) ; seuls `srv-web`/`srv-ftp`/les sondes IDS sont autorisés vers
  `srv-logs` (flux ADMIN, à sens unique en pratique).
- **Conteneurs non-root, `cap_drop: ALL`** avec uniquement les capacités strictement
  nécessaires par service.
- **Sauvegardes régulières** de `srv-db` : `scripts/backup.sh` (dump + `sha256sum`,
  rétention 14 jours), à programmer toutes les 4 h → RPO = 4 h.
- **Confinement rapide possible** : en cas de compromission confirmée de `srv-web`,
  le déconnecter du réseau `lan` (`docker network disconnect lan web`) coupe immédiatement
  l'accès à `srv-db` sans arrêter le service public.

## 4. Stratégie de reprise (PRA)

1. **Détection** : alerte Suricata (`ids-ftp`/`ids-web`) ou bannissement fail2ban remonté
   dans les logs centralisés de `srv-logs`.
2. **Confinement** : isoler le conteneur concerné du réseau impliqué (`docker network
   disconnect <reseau> <service>`) sans l'arrêter, pour préserver les preuves.
3. **Preuves** : exporter `/var/log/remote/<hôte>/` depuis `srv-logs` sur la fenêtre
   d'incident, ainsi que `eve.json` des sondes IDS ; horodater.
4. **Éradication** : corriger la cause racine (voir tableau des correctifs dans la
   documentation des vulnérabilités), reconstruire les images (`docker compose build
   --no-cache`).
5. **Reprise** : restauration de `srv-db` depuis la dernière sauvegarde saine
   (`scripts/restore.sh`), vérification d'intégrité (`sha256sum -c`), redéploiement.
6. **Validation** : rejouer `scripts/simulate-attack.sh` sur un environnement de test pour
   confirmer que les vulnérabilités corrigées ne sont plus exploitables et que les alertes
   se déclenchent toujours correctement.
7. **Retour d'expérience** : fiche incident (chronologie, cause racine, actions
   correctives, responsable, échéance) ; mise à jour de ce document.

## 5. Rôles et escalade

| Rôle | Responsabilité |
|---|---|
| Détection (N1) | Surveille les alertes Suricata/fail2ban remontées sur `srv-logs` |
| Réponse (N2) | Confinement, pilotage de l'éradication et de la reprise |
| Décideur | Valide la communication et la remise en production |

Règle d'escalade : toute alerte liée à la vulnérabilité 2 (lecture de `secrets` via
injection SQL) est traitée en moins de 15 min ; les accès au fichier de sauvegarde FTP ou
le brute force en moins d'1 h.

## 6. Tests du plan

- Exercice de table (tabletop) rejouant le scénario FTP anonyme → injection SQL.
- Test de restauration de `srv-db` au moins une fois par cycle de projet.
