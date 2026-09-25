import sys
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Sel fixe partagé pour dériver la clé de façon déterministe
SALT = b'lab_salt_ubuntu_2026'

def derive_key(password: str) -> bytes:
    """Dérive une clé Fernet valide à partir d'un mot de passe texte."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=480000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(file_path, password):
    if not os.path.isfile(file_path):
        print(f"Erreur : Le fichier '{file_path}' n'existe pas.")
        sys.exit(1)

    # 1. Génération de la clé Fernet à partir du mot de passe
    key = derive_key(password)
    fernet = Fernet(key)

    # 2. Lecture du fichier original
    with open(file_path, "rb") as f:
        data = f.read()

    # 3. Chiffrement
    encrypted_data = fernet.encrypt(data)

    # 4. Sauvegarde du fichier chiffré
    output_file = file_path + ".enc"
    with open(output_file, "wb") as f:
        f.write(encrypted_data)

    print(f"[+] Fichier chiffré avec succès : {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 encrypt_file.py <fichier_a_chiffrer> <mot_de_passe>")
        sys.exit(1)

    encrypt_file(sys.argv[1], sys.argv[2])