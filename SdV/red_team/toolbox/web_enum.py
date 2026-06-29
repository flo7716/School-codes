import urllib.request
import urllib.error

def enum_web(ip, port=80):
    """Analyse les endpoints HTTP et affiche les en-têtes."""
    # Chemins obligatoires demandés par le sujet
    endpoints = ["/admin", "/login", "/backup", "/test", "/config", "/.git", "/.env", "/robots.txt", "/login.php", "/index.php" ]
    base_url = f"http://{ip}:{port}"
    
    print(f"[*] Phase 3 : Énumération Web sur {base_url}")
    web_results = {}

    for path in endpoints:
        url = base_url + path
        try:
            # Ajout d'un timeout pour éviter le blocage
            req = urllib.request.Request(url, method="GET")
            with urllib.request.urlopen(req, timeout=1.5) as response:
                status = response.status
                headers = dict(response.headers)
                print(f"    [+] {path} - Status: {status} (Trouvé !)")
                web_results[path] = {"status": status, "headers": headers}
        except urllib.error.HTTPError as e:
            # Même en cas d'erreur 403, 401 ou 404, on capture le status
            print(f"    [-] {path} - Status: {e.code}")
            web_results[path] = {"status": e.code, "headers": dict(e.headers)}
        except Exception:
            # Hôte inaccessible ou pas de serveur web
            pass
            
    print(f"[✓] Énumération Web terminée pour {ip}.\n")
    return web_results