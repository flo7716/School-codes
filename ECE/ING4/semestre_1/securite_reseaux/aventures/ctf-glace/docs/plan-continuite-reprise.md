# Plan de Continuité et de Reprise d'Activité — GlaceCorp (infra "Le Chemin de la Glace")

Aligné sur la logique PDCA d'ISO 22301 (cohérent avec les livrables MSI-4-26 : TD02 TechSecure et le mini-projet logistique/séisme).

## 1. Contexte et périmètre

- Système concerné : infrastructure Docker GlaceCorp (proxy/WAF, app web, MariaDB, supervision Loki/Grafana, alerter).
- Scénario redouté principal : compromission de la base de données via l'injection SQL exposée en `/search` et `/login`, avec exfiltration du flag/secret et possible rebond.
- Scénario secondaire : fuite de fichier de configuration (`/backup/db_config.bak`) menant à une divulgation d'informations.

## 2. Analyse d'impact (BIA simplifiée)

| Actif | Impact si indisponible | RTO cible | RPO cible |
|---|---|---|---|
| Service web (catalogue) | Perte de visibilité commerciale | 1 h | — |
| Base de données | Perte de ventes, intégrité des données en jeu | 2 h | 4 h (fréquence des sauvegardes) |
| Supervision (Loki/Grafana/alerter) | Perte de détection pendant l'incident, aggravant l'impact | 30 min | — |

## 3. Stratégie de continuité (PCA)

- **Redondance logique minimale** : conteneurs stateless (`web`, `proxy`) redémarrables instantanément (`restart: unless-stopped`, healthchecks) ; seule `db` porte un état persistant.
- **Isolation réseau par défaut** : `front`/`back`/`monitoring` sont `internal`, limitant la propagation latérale en cas de compromission de `proxy`.
- **Sauvegardes régulières** : `scripts/backup.sh` (dump logique + `sha256sum`, rétention 14 jours), programmable via cron toutes les 4 h → RPO = 4 h.
- **Procédure de bascule en mode dégradé** : en cas de compromission confirmée de `web`, couper son accès réseau (`docker network disconnect front web`) tout en conservant `proxy` pour servir une page de maintenance statique.

## 4. Stratégie de reprise (PRA)

1. **Détection** : alerte `alerter` (SQLI/BRUTEFORCE/BACKUP_LEAK/WEB_DOWN) ou remontée manuelle.
2. **Confinement** : isoler le conteneur compromis du réseau concerné (`docker network disconnect <net> <service>`), ne pas l'arrêter (préservation des preuves).
3. **Preuves** : export des logs Loki sur la fenêtre d'incident, `docker diff` et `docker export` du conteneur suspect, horodatage.
4. **Éradication** : identifier la vulnérabilité exploitée (ici : injection SQL / fichier exposé), corriger le code (`app.py` → requêtes préparées, suppression de `/backup`), reconstruire l'image (`docker compose build --no-cache`).
5. **Reprise** : restauration depuis la dernière sauvegarde saine via `scripts/restore.sh`, vérification d'intégrité (`sha256sum -c`), redéploiement (`docker compose up -d`).
6. **Validation** : rejouer `scripts/simulate-attack.sh` pour confirmer que la vulnérabilité est corrigée et que l'alerte correspondante se déclenche correctement si on force le test sur un environnement de rejeu.
7. **Retour d'expérience (post-mortem)** : fiche incident (chronologie, cause racine, actions correctives, responsable, échéance), mise à jour de ce document.

## 5. Rôles et escalade

| Rôle | Responsabilité |
|---|---|
| Détection (N1) | Surveille les alertes `alerter`/Grafana, qualifie la sévérité |
| Réponse (N2) | Applique le confinement, pilote l'éradication/reprise |
| Décideur | Valide la communication et la remise en production |

Règle d'escalade : toute alerte de sévérité `CRITICAL` (ex. `BACKUP_LEAK`, `WEB_DOWN`) déclenche une notification immédiate (webhook) et doit être traitée en moins de 15 min ; `HIGH` en moins d'1 h ; `MEDIUM` en moins de 4 h.

## 6. Tests du plan

- Exercice de table (tabletop) : rejouer le scénario d'injection SQL en environnement de test.
- Test de restauration : exécuter `scripts/restore.sh` sur une sauvegarde de test au moins une fois par cycle de projet, et vérifier le flag/les données restaurées.
