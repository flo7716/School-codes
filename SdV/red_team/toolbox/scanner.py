import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

# Association des services connus (Contrainte)
SERVICES_CONNUS = {
    20: "FTP-Data", 21: "FTP", 22: "SSH", 23: "Telnet", 
    25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3", 
    143: "IMAP", 443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S"
}

def scan_port(ip, port, timeout=0.5):
    """Contrainte : Fonction dédiée à l'analyse d'un port unique."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        result = s.connect_ex((ip, port))
        if result == 0:
            return port, SERVICES_CONNUS.get(port, "Service Inconnu")
    except Exception:
        pass
    finally:
        s.close()
    return None

def scan_host_ports(ip, start_port=20, end_port=1024, max_threads=30):
    """Scanne la plage 20-1024 en multithreading avec affichage de progression."""
    print(f"[*] PHASE 2 : Scan des ports de {ip} (Plage {start_port} à {end_port})")
    open_ports = {}
    
    ports_to_scan = range(start_port, end_port + 1)
    total_ports = len(ports_to_scan)
    scanned_count = 0

    # Utilisation du Multithreading (Bonus Threads x30)
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in ports_to_scan}
        
        for future in as_completed(futures):
            scanned_count += 1
            # Bonus : Affichage dynamique de la progression
            if scanned_count % 50 == 0 or scanned_count == total_ports:
                print(f"    [~] Progression {ip} : {scanned_count}/{total_ports} ports scannés...", end="\r")
            
            result = future.result()
            if result:
                port, service = result
                print(f"\n    [+] Port Ouvert détecté : {port} ({service})")
                open_ports[port] = service
                
    print(f"\n[✓] Phase 2 terminée pour l'hôte {ip}.\n")
    return open_ports