import sys
import socket
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

# Dictionnaire global pour l'association des services (Contrainte Phase 2)
SERVICES_CONNUS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 3389: "RDP"
}

# =====================================================================
# PHASE 1 : RECONNAISSANCE RÉSEAU
# =====================================================================
def check_host(ip, port=80, timeout=0.2):
    """Vérifie si une IP répond rapidement (Contraintes: socket + timeout)."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        result = s.connect_ex((ip, port))
        return result == 0
    except Exception:
        return False
    finally:
        s.close()

def parse_target(target_input):
    """Analyse l'argument d'entrée pour générer la liste des IPs à scanner."""
    ips_to_scan = []
    
    # Cas d'un sous-réseau au format CIDR (ex: 192.168.56.0/24)
    if "/" in target_input:
        try:
            base_ip = target_input.split("/")[0]
            ip_parts = base_ip.split(".")
            subnet = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}"
            # On génère la plage complète .1 à .20
            for i in range(1, 20):
                ips_to_scan.append(f"{subnet}.{i}")
        except Exception:
            print(f"[-] Erreur de formatage du sous-réseau : {target_input}")
            sys.exit(1)
    else:
        # Cas d'une IP unique (ex: 192.168.56.10)
        ips_to_scan.append(target_input)
        
    return ips_to_scan

def run_reconnaissance(target_list):
    """Scanne la liste des cibles générées et écrit le fichier hosts.txt."""
    print(f"[*] PHASE 1 : Début de la reconnaissance réseau...")
    active_hosts = []
    
    for ip in target_list:
        # Logs visibles de progression (Contrainte)
        print(f"    [~] Test de la machine : {ip}...", end="\r")
        
        # On teste le port 80 ou le port 22 pour maximiser la détection
        if check_host(ip, port=80) or check_host(ip, port=22):
            print(f"[+] Machine active détectée : {ip}               ")
            active_hosts.append(ip)
            
    # Sauvegarde obligatoire dans hosts.txt (Contrainte)
    with open("hosts.txt", "w") as f:
        for host in active_hosts:
            f.write(f"{host}\n")
            
    print(f"[✓] Phase 1 terminée. {len(active_hosts)} hôte(s) sauvegardé(s) dans hosts.txt.\n")
    return active_hosts


# =====================================================================
# PHASE 2 : SCAN DE PORTS
# =====================================================================
def scan_port(ip, port, timeout=0.5):
    """Contrainte : Fonction dédiée à l'analyse d'un port unique."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        result = s.connect_ex((ip, port))
        if result == 0:
            return port, SERVICES_CONNUS.get(port, "Inconnu")
    except Exception:
        pass
    finally:
        s.close()
    return None

def run_port_scan(ip, start_port=20, end_port=1024, max_threads=30):
    """Scanne une IP en utilisant du multithreading (Bonus Threads x30)."""
    print(f"[*] PHASE 2 : Scan des ports 20-1024 pour l'hôte {ip}...")
    open_ports = {}
    
    ports = range(start_port, end_port + 1)
    total_ports = len(ports)
    scanned = 0

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in ports}
        
        for future in as_completed(futures):
            scanned += 1
            # Bonus : Affichage de la progression dynamique
            if scanned % 100 == 0 or scanned == total_ports:
                print(f"    [~] Progression {ip} : {scanned}/{total_ports} ports vérifiés...", end="\r")
            
            res = future.result()
            if res:
                port, service = res
                print(f"\n    [+] Port Ouvert : {port} ({service})")
                open_ports[port] = service
                
    print(f"\n[✓] Phase 2 terminée pour {ip}.\n")
    return open_ports


# =====================================================================
# PHASE 3 : ÉNUMÉRATION WEB
# =====================================================================
def run_web_enumeration(ip, port=80):
    """Analyse les endpoints HTTP, lit les status codes et fait un brute-force."""
    # Chemins obligatoires demandés par le sujet
    mandatory_paths = ["/admin", "/login", "/backup", "/test"]
    # Bonus : Chemins additionnels (Mini brute-force)
    bonus_paths = ["/robots.txt", "/config.php", "/secret", "/.git"]
    
    all_paths = mandatory_paths + bonus_paths
    base_url = f"http://{ip}:{port}"
    
    print(f"[*] PHASE 3 : Énumération Web / Brute-force sur {base_url}")
    web_results = {}

    for path in all_paths:
        url = base_url + path
        try:
            req = urllib.request.Request(url, method="GET")
            with urllib.request.urlopen(req, timeout=1.5) as response:
                # Enregistrement du status code et des headers (Contraintes)
                web_results[path] = {"status": response.status, "headers": dict(response.headers)}
                print(f"    [+] {path} -> Code {response.status} (Trouvé)")
        except urllib.error.HTTPError as e:
            # On capture le code même si c'est une erreur HTTP (ex: 403 ou 401)
            web_results[path] = {"status": e.code, "headers": dict(e.headers)}
            print(f"    [-] {path} -> Code {e.code}")
        except Exception:
            pass
            
    print(f"[✓] Phase 3 terminée pour {ip}.\n")
    return web_results


# =====================================================================
# PHASE 4 : PIPELINE PRINCIPAL ET RENDU
# =====================================================================
def main():
    # Vérification de l'argument en ligne de commande
    if len(sys.argv) < 2:
        print("[-] Erreur : argument manquant.")
        print(f"Usage   : python {sys.argv[0]} <IP_ou_CIDR>")
        print(f"Exemple : python {sys.argv[0]} 192.168.56.0/24")
        print(f"Exemple : python {sys.argv[0]} 192.168.56.10")
        sys.exit(1)

    target_input = sys.argv[1]
    
    print("=" * 65)
    print("           PENTEST TOOLBOX AUTOMATIQUE - SCRIPT PYTHON")
    print("=" * 65)
    
    # Structure de stockage pour le rapport de fin
    report = {}

    # Étape 1 : Interprétation de l'entrée et Reconnaissance réseau
    potential_ips = parse_target(target_input)
    active_ips = run_reconnaissance(potential_ips)
    
    if not active_ips:
        print("[-] Aucune machine active détectée sur la cible indiquée. Fin du pipeline.")
        return

    # Étape 2 & 3 : Boucle automatisée sur chaque cible valide
    for ip in active_ips:
        report[ip] = {"ports": {}, "web": {}}
        
        # Lancement du scan de ports
        open_ports = run_port_scan(ip)
        report[ip]["ports"] = open_ports
        
        # Détection conditionnelle de serveurs HTTP/HTTPS pour la Phase 3
        if 80 in open_ports or 443 in open_ports:
            web_port = 80 if 80 in open_ports else 443
            web_info = run_web_enumeration(ip, port=web_port)
            report[ip]["web"] = web_info

    # Étape 4 : Rendu du résumé final structuré
    print("\n" + "=" * 65)
    print("                         RÉSUMÉ FINAL")
    print("=" * 65)
    
    for ip, data in report.items():
        print(f"\nHôte Actif : {ip}")
        print(f" └── Ports ouverts : {list(data['ports'].keys()) or 'Aucun (20-1024)'}")
        if data['ports']:
            for p, svc in data['ports'].items():
                print(f"     ├── [{p}] -> {svc}")
                
        if data['web']:
            print(" └── Énumération Chemins Web :")
            for path, details in data['web'].items():
                status = details["status"]
                alert = "🔥 (Intéressant)" if status in [200, 403, 301] else ""
                print(f"     ├── {path:12} -> Code {status} {alert}")
                
    print("\n" + "=" * 65)
    print("[*] Fin du traitement de la Toolbox.")

if __name__ == "__main__":
    main()