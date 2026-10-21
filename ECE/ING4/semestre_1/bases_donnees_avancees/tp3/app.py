import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def interroger_mysql():
    connexion = None
    try:
        # Étape 1 : Connexion à la base de données avec PyMySQL
        connexion = pymysql.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            charset='utf8mb4'
        )

        print("Connexion réussie à la base de données MySQL !\n")

        # Étape 2 & 3 : Création du curseur et exécution de la requête
        with connexion.cursor() as curseur:
            requete = "SELECT * FROM Epreuve"
            curseur.execute(requete)
            resultats = curseur.fetchall()

            # Étape 4 : Affichage des résultats
            print("Résultats de la requête :")
            for ligne in resultats:
                print(ligne)

    except Exception as e:
        print(f"Erreur lors de la connexion ou de l'exécution MySQL : {e}")

    finally:
        # Étape 5 : Fermeture de la connexion pour libérer les ressources
        if connexion and connexion.open:
            connexion.close()
            print("\nConnexion MySQL fermée.")

if __name__ == "__main__":
    interroger_mysql()