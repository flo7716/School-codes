import urllib.request
import urllib.error

def enum_web(ip, port=80):
    """Détecte le serveur HTTP, affiche le status code, les headers et brute-force les chemins."""
    # Chemins obligatoires (Contrainte)
    endpoints = ["/admin", "/login", "/backup", "/test"]
    
    # Chemins supplémentaires (Bonus Mini brute-force de chemins)
    wordlist_bonus = ["/robots.txt", "/.git", "/config.php", "/secret", "/uploads"]
    
    all_paths = endpoints + wordlist_bonus
    base_url = f"http://{ip}:{port}"
    
    print(f"[*] PHASE 3 : Énumération Web & Mini Brute-force sur {base_url}")
    web_results = {}

    for path in all_paths:
        url = base_url + path
        try:
            # On forge la requête
            req = urllib.request.Request(url, method="GET")
            with urllib.request.urlopen(req, timeout=1.5) as response:
                status = response.status
                headers = dict(response.headers)
                print(f"    [+] {path} -> Code {status} (Trouvé !)")
                web_results[path] = {"status": status, "headers": headers}
        except urllib.error.HTTPError as e:
            # On capture le code même si c'est une erreur (ex: 403 Forbidden ou 404 Not Found)
            print(f"    [-] {path} -> Code {e.code}")
            web_results[path] = {"status": e.code, "headers": dict(e.headers)}
        except Exception:
            # Hôte inaccessible ou pas de service web actif
            pass
            
    print(f"[✓] Phase 3 terminée pour {ip}.\n")
    return web_results