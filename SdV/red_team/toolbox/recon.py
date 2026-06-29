import socket

def check_host(ip, port=80, timeout=0.2):
    """Vérifie si une IP est active en tentant une connexion socket rapide."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        s.close()
        return True
    except (socket.timeout, ConnectionRefusedError):
        # Si la connexion est refusée, la machine est quand même active !
        return True
    except Exception:
        return False

def scan_network(subnet="192.168.56", start=1, end=254):
    """Scanne la plage d'IPs et sauvegarde les hôtes actifs."""
    print(f"[*] Phase 1 : Début de la reconnaissance sur {subnet}.0/24...")
    active_hosts = []
    
    for i in range(start, end + 1):
        ip = f"{subnet}.{i}"
        # On log l'avancement de manière visible (Contrainte sujet)
        if check_host(ip):
            print(f"[+] Machine active détectée : {ip}")
            active_hosts.append(ip)
            
    # Sauvegarde obligatoire dans hosts.txt
    with open("hosts.txt", "w") as f:
        for host in active_hosts:
            f.write(f"{host}\n")
            
    print(f"[✓] Phase 1 terminée. {len(active_hosts)} hôtes sauvegardés dans hosts.txt.\n")
    return active_hosts