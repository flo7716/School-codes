import recon
import scanner
import web_enum

def main():
    print("=" * 65)
    print("        PHASE 4 : EXECUTION DU PIPELINE DE PENTEST GLOBAL")
    print("=" * 65)
    
    # Structure globale pour collecter toutes les métriques du rapport final
    pipeline_report = {}

    # Étape 1 : Reconnaissance réseau automatique
    # (Note : Modifiez start=1 et end=25 en lab pour une démonstration ultra rapide)
    active_ips = recon.scan_network(subnet="192.168.56", start=1, end=20)
    
    if not active_ips:
        print("\n[-] Aucune machine active détectée sur le scope. Arrêt du pipeline.")
        return

    # Étape 2 & 3 : Chaînage automatique pour chaque machine trouvée
    for ip in active_ips:
        pipeline_report[ip] = {"ports": {}, "web": {}}
        
        # Lancement automatique du scanner de ports (20-1024)
        open_ports = scanner.scan_host_ports(ip, start_port=20, end_port=1024)
        pipeline_report[ip]["ports"] = open_ports
        
        # Étape 3 Conditionnelle : Si le port 80 (HTTP) ou 443 (HTTPS) est ouvert
        if 80 in open_ports or 443 in open_ports:
            web_port = 80 if 80 in open_ports else 443
            web_data = web_enum.enum_web(ip, port=web_port)
            pipeline_report[ip]["web"] = web_data

    # Étape 4 : Affichage du Résumé Final (Contrainte Clé)
    print("\n" + "=" * 65)
    print("                      RÉSUMÉ FINAL DU PENTEST")
    print("=" * 65)
    
    for ip, data in pipeline_report.items():
        print(f"\n[+] IP ACTIVE : {ip}")
        
        # Affichage des ports et services associés
        if data["ports"]:
            print("    └── 🔓 Ports ouverts détectés :")
            for port, service in data["ports"].items():
                print(f"        ├── Port {port} -> Service: {service}")
        else:
            print("    └── 🔒 Aucun port ouvert trouvé dans la plage 20-1024.")
            
        # Affichage des résultats de l'énumération Web
        if data["web"]:
            print("    └── 🌐 Services Web / Chemins énumérés :")
            for path, details in data["web"].items():
                status_code = details["status"]
                # Formatage visuel pour mettre en évidence les dossiers existants (Hors 404)
                flag = "⚠️  [ALERT]" if status_code in [200, 301, 302, 403] else "[NOT FOUND]"
                print(f"        ├── Path: {path:12} -> Code {status_code} {flag}")
                
    print("\n" + "=" * 65)
    print("[*] Fin de l'audit. Toolbox exécutée avec succès dans le temps imparti.")

if __name__ == "__main__":
    main()