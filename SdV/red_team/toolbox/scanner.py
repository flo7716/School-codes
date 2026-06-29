import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

# Dictionnaire de services connus (Contrainte sujet)
SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 443: "HTTPS", 8080: "HTTP-Proxy"
}

def scan_port(ip, port, timeout=0.5):
    """Scanne un port unique sur une IP donnée."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        result = s.connect_ex((ip, port))
        if result == 0:
            service = SERVICES.get(port, "Inconnu")
            return port, service
    except Exception:
        pass
    finally:
        s.close()
    return None

def scan_host_ports(ip, start_port=20, end_port=1024, max_threads=30):
    """Scanne la plage de ports d'une IP en utilisant le multi-threading."""
    print(f"[*] Phase 2 : Scan des ports pour {ip} ({start_port}-{end_port})...")
    open_ports = {}
    
    ports_to_scan = range(start_port, end_port + 1)
    total_ports = len(ports_to_scan)
    scanned_count = 0

    # Utilisation d'un pool de threads (Bonus technique)
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in ports_to_scan}
        
        for future in as_completed(futures):
            scanned_count += 1
            # Affichage de la progression en pourcentage (Bonus technique)
            if scanned_count % 100 == 0 or scanned_count == total_ports:
                print(f"    Progression {ip} : {scanned_count}/{total_ports} ports vérifiés...", end="\r")
            
            res = future.result()
            if res:
                port, service = res
                print(f"\n    [+] Port Ouvert sur {ip} : {port} ({service})")
                open_ports[port] = service
                
    print(f"\n[✓] Scan de ports terminé pour {ip}.\n")
    return open_ports