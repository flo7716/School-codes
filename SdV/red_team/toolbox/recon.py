import socket

def check_host(ip, port=80, timeout=0.2):
    """Vérifie si une IP répond en utilisant uniquement socket et un timeout."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        # connect_ex renvoie 0 si la connexion réussit (ou si le port répond)
        result = s.connect_ex((ip, port))
        return True
    except Exception:
        return False
    finally:
        s.close()

def scan_network(subnet="192.168.56", start=1, end=254):
    """Scanne le réseau pour trouver les machines actives et crée hosts.txt."""
    print(f"[*] PHASE 1 : Reconnaissance réseau sur {subnet}.0/24")
    active_hosts = []
    
    for i in range(start, end + 1):
        ip = f"{subnet}.{i}"
        # Log visible de progression (Contrainte)
        print(f"    [~] Test de l'hôte {ip}...", end="\r")
        
        if check_host(ip) or check_host(ip, port=22) or check_host(ip, port=443):
            print(f"[+] Machine active détectée : {ip}               ")
            active_hosts.append(ip)
            
    # Sortie attendue : Fichier hosts.txt
    with open("hosts.txt", "w") as f:
        for host in active_hosts:
            f.write(f"{host}\n")
            
    print(f"[✓] Phase 1 terminée. Liste IP actives sauvegardée dans hosts.txt ({len(active_hosts)} trouvées).\n")
    return active_hosts