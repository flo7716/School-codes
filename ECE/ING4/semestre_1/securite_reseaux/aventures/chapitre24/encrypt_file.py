import sys
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def derive_key(password: str, salt: bytes) -> bytes:
    """Dérive une clé compatible Fernet à partir d'un mot de passe et d'un sel."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480_000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(file_path: str, password: str):
    if not os.path.exists(file_path):
        print(f"Erreur : Le fichier '{file_path}' n'existe pas.")
        return

    # 1. Génération d'un sel aléatoire de 16 octets
    salt = os.urandom(16)
    key = derive_key(password, salt)
    fernet = Fernet(key)

    # 2. Lecture du fichier original
    with open(file_path, 'rb') as f:
        data = f.read()

    # 3. Chiffrement des données
    encrypted_data = fernet.encrypt(data)

    # 4. Écriture du sel (16 octets) + données chiffrées dans le fichier de sortie
    output_file = file_path + ".enc"
    with open(output_file, 'wb') as f:
        f.write(salt + encrypted_data)

    print(f"[+] Fichier chiffré avec succès : {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 encrypt_file.py <fichier> <mot_de_passe>")
        sys.exit(1)

    encrypt_file(sys.argv[1], sys.argv[2])