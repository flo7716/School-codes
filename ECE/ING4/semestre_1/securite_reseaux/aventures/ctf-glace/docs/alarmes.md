# Détection d'incidents et alarmes

Le service `alerter` interroge Loki toutes les 15 s et déclenche une alarme (log structuré + webhook optionnel) quand une règle dépasse son seuil, avec un délai de répétition (`COOLDOWN`) de 2 min pour éviter le bruit.

| Règle | Sévérité | Déclencheur | Seuil |
|---|---|---|---|
| `SQLI` | HIGH | Motifs d'injection SQL dans les logs web (`UNION SELECT`, `OR 1=1`, `information_schema`, `SLEEP(`, commentaire `--`) | ≥ 1 / min |
| `BRUTEFORCE` | HIGH | Échecs de connexion `/login` (`event=login_fail`) | ≥ 5 / min |
| `SCAN` | MEDIUM | Taux de 404 (scan de répertoires type gobuster) | ≥ 15 / min |
| `WAF` | MEDIUM | Règle ModSecurity/OWASP CRS déclenchée côté proxy | ≥ 1 / min |
| `BACKUP_LEAK` | CRITICAL | Accès au chemin `/backup/...` | ≥ 1 / min |
| `WEB_DOWN` | CRITICAL | Absence totale de logs du service `web` | 2 min sans activité |

## Visualisation

- Grafana (datasource Loki provisionnée) permet d'explorer les logs bruts et de construire un dashboard "Security Overview" (requêtes LogQL identiques à celles de `alerter.py`).
- Les alertes elles-mêmes apparaissent aussi comme des lignes de log JSON du service `alerter` (donc visibles dans Loki/Grafana en plus du webhook).

## Procédure en cas d'alerte

1. Identifier la règle et la sévérité (voir tableau d'escalade dans `plan-continuite-reprise.md` §5).
2. Consulter les logs Loki filtrés sur `service="web"` / `service="proxy"` autour de l'horodatage.
3. Appliquer la procédure de confinement/éradication/reprise du PRA.
