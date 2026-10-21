import os
import pymysql
from dotenv import load_dotenv

# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()

class Epreuve:
    """Classe représentant une épreuve."""
    def __init__(self, row_data):
        # row_data est un dictionnaire représentant une ligne de la base de données
        # Adaptez les clés selon les noms exacts de vos colonnes dans MySQL
        self.id = row_data.get('id')
        self.numepreuve = row_data.get('NumEpreuve')
        self.dateepreuve = row_data.get('DateEpreuve')
        self.Lieu = row_data.get('Lieu')
        # Stockage de l'ensemble des données brutes pour un accès global si besoin
        self.raw_data = row_data

    def __str__(self):
        """Méthode pour afficher proprement l'objet (quand on fait un print)"""
        return f"[Épreuve] ID: {self.id} | Numéro: {self.numepreuve} | Date: {self.dateepreuve} | Lieu: {self.Lieu} | Détails: {self.raw_data}"


def recuperer_epreuves():
    connexion = None
    epreuves_liste = []
    
    try:
        # Étape 1 : Connexion à la base de données
        connexion = pymysql.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor  # Indispensable pour récupérer un dictionnaire par ligne
        )

        print("Connexion réussie à la base de données MySQL !\n")

        # Étape 2 : Exécution de la requête
        with connexion.cursor() as curseur:
            requete = "SELECT * FROM Epreuve"
            curseur.execute(requete)
            resultats = curseur.fetchall()

            # Étape 3 : Conversion des résultats SQL en objets Epreuve
            for ligne in resultats:
                epreuve_obj = Epreuve(ligne)
                epreuves_liste.append(epreuve_obj)

        # Étape 4 : Utilisation des objets
        print(f"Nombre d'épreuves chargées : {len(epreuves_liste)}\n")
        print("Affichage des objets Epreuve :")
        for epreuve in epreuves_liste:
            print(epreuve) # Appelle automatiquement la méthode __str__

    except Exception as e:
        print(f"Erreur lors de la connexion ou de l'exécution MySQL : {e}")

    finally:
        # Étape 5 : Fermeture propre de la connexion
        if connexion and connexion.open:
            connexion.close()
            print("\nConnexion MySQL fermée.")

if __name__ == "__main__":
    recuperer_epreuves()