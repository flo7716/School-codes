import recon
import scanner
import web_enum
import os

def main():
    print("=" * 60)
    print("        TOOLBOX PENTEST PYTHON AUTOMATIQUE")
    print("=" * 60)
    
    # Structure globale pour stocker le rapport final
    report = {}

    # Phase 1: Reconnaissance réseau
    # (Note : Ajustez la plage "start" et "end" si vous voulez tester plus vite en lab)
    active_ips = recon.scan_network(subnet="192.168.56", start=1, end=20)
    
    if not active_ips:
        print("[-] Aucune machine active détectée. Fin du pipeline.")
        return

    # Phase 2 & 3: Boucle sur chaque machine trouvée
    for ip in active_ips:
        report[ip] = {
            "ports": {},
            "web": {}
        }
        
        # Lancement du scan de ports
        open_ports = scanner.scan_host_ports(ip, start_port=20, end_port=1024)
        report[ip]["ports"] = open_ports
        
        # Phase 3 conditionnelle: Si un service web est détecté
        if 80 in open_ports or 443 in open_ports:
            web_port = 80 if 80 in open_ports else 443
            web_info = web_enum.enum_web(ip, port=web_port)
            report[ip]["web"] = web_info

    # Phase 4: Résumé final (Critère important d'évaluation)
    print("\n" + "=" * 60)
    print("                      RÉSUMÉ FINAL")
    print("=" * 60)
    
    for ip, data in report.items():
        print(f"\nHôte : {ip}")
        print(f" └── Ports Ouverts : {list(data['ports'].keys()) or 'Aucun'}")
        
        if data['web']:
            print(" └── Énumération Web :")
            for path, details in data['web'].items():
                print(f"     ├── {path} -> Code {details['status']}")

    # Phase 5: Sauvegarde du rapport dans un fichier
    report_file = "rapport_final.txt"
    with open(report_file, "w") as f:
        f.write("RAPPORT FINAL DE L'OUTIL PENTEST\n")
        f.write("=" * 60 + "\n")
        for ip, data in report.items():
            f.write(f"\nHôte : {ip}\n")
            f.write(f" └── Ports Ouverts : {list(data['ports'].keys()) or 'Aucun'}\n")
            if data['web']:
                f.write(" └── Énumération Web :\n")
                for path, details in data['web'].items():
                    f.write(f"     ├── {path} -> Code {details['status']}\n")
                
    print("\n" + "=" * 60)
    print("[*] Fin du traitement. Rapport généré avec succès.")

if __name__ == "__main__":
    main()