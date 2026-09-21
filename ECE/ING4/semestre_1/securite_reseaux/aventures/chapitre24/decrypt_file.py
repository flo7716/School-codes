import sys
import os
import base64
from cryptography.fernet import Fernet, InvalidToken
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

def decrypt_file(file_path: str, password: str):
    if not os.path.exists(file_path):
        print(f"Erreur : Le fichier '{file_path}' n'existe pas.")
        return

    # 1. Lecture du sel (16 premiers octets) et du contenu chiffré
    with open(file_path, 'rb') as f:
        file_content = f.read()

    if len(file_content) <= 16:
        print("Erreur : Fichier chiffré invalide ou corrompu.")
        return

    salt = file_content[:16]
    encrypted_data = file_content[16:]

    # 2. Dérivation de la clé avec le mot de passe fourni
    key = derive_key(password, salt)
    fernet = Fernet(key)

    # 3. Déchiffrement
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        
        # Détermination du nom de fichier de sortie
        output_file = file_path[:-4] if file_path.endswith(".enc") else file_path + ".dec"
        
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)

        print(f"[+] Fichier déchiffré avec succès : {output_file}")

    except InvalidToken:
        print("[-] Erreur : Mot de passe incorrect ou fichier corrompu.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 decrypt_file.py <fichier_chiffré> <mot_de_passe>")
        sys.exit(1)

    decrypt_file(sys.argv[1], sys.argv[2])