import weaviate
import pandas as pd
import numpy as np
from os import load_dotenv
import os
load_dotenv()

# === CONFIGURATION ===
WEAVIATE_URL = os.getenv("WEAVIATE_URL")
API_KEY = os.getenv("WEAVIATE_API_KEY")
CSV_FILE = os.getenv("CSV_FILE")
CLASS_NAME = "Produit"  # ou n'importe quel nom logique

# === Connexion ===
auth_config = weaviate.AuthApiKey(API_KEY) if API_KEY else None
client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=auth_config,
    additional_headers={"X-OpenAI-Api-Key": "sk-..."}  # si vectorisation via OpenAI
)

# === Création du schéma (si besoin) ===
if not client.schema.contains({"classes": [{"class": CLASS_NAME}]}):
    client.schema.create_class({
        "class": CLASS_NAME,
        "properties": [
            {"name": "nom", "dataType": ["text"]},
            {"name": "description", "dataType": ["text"]},
            {"name": "prix", "dataType": ["number"]},
        ],
        "vectorizer": "text2vec-openai"  # ou "none" si tu fournis les vecteurs
    })

# === Lecture du CSV ===
df = pd.read_csv(CSV_FILE)

# === Upload vers Weaviate ===
with client.batch as batch:
    batch.batch_size = 20
    for i, row in df.iterrows():
        data_object = {
            "nom": row["nom"],
            "description": row["description"],
            "prix": float(row["prix"])
        }
        batch.add_data_object(data_object, CLASS_NAME)

print("Upload terminé.")
