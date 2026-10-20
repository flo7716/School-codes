import sys
import os
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

SALT = b'lab_salt_ubuntu_2026'

def derive_key(password: str) -> bytes:
    """Dérive la même clé Fernet à partir du mot de passe fourni."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=480000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def decrypt_file(file_path, password):
    if not os.path.isfile(file_path):
        print(f"Erreur : Le fichier '{file_path}' n'existe pas.")
        sys.exit(1)

    # 1. Régénération de la clé avec le mot de passe saisi
    key = derive_key(password)
    fernet = Fernet(key)

    # 2. Lecture des données chiffrées
    with open(file_path, "rb") as f:
        encrypted_data = f.read()

    # 3. Déchiffrement
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        
        output_file = file_path.replace(".enc", ".dec") if file_path.endswith(".enc") else file_path + ".dec"
        
        with open(output_file, "wb") as f:
            f.write(decrypted_data)

        print(f"[+] Déchiffrement réussi ! Fichier restauré : {output_file}")

    except InvalidToken:
        print("[-] Erreur : Mot de passe incorrect ou fichier corrompu.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 decrypt_file.py <fichier_chiffre> <mot_de_passe>")
        sys.exit(1)

    decrypt_file(sys.argv[1], sys.argv[2])