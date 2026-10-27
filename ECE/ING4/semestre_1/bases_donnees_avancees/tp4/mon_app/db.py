import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

# Par défaut : base SQLite dans le fichier notes.db (aucun serveur à installer)
DB_URL = os.getenv("DB_URL", "sqlite:///notes.db")
engine = create_engine(DB_URL)


def note_finale(cc1, cc2, examen):
    cc = (cc1 + cc2) / 2
    return max((cc + examen) / 2, examen)


def init_db():
    """Crée la table releve_de_notes et la remplit si elle est vide."""
    eleves = [
        ("01", "Leon", 10, 20, 8), ("02", "David", 0, 16, 8),
        ("03", "Lucas", 20, 16, 7), ("04", "Paul", 8, 6, 17),
        ("05", "Lea", 3, 4, 12), ("06", "Sophie", 19, 16, 20),
        ("07", "Ella", 11, 14, 12), ("08", "Zoe", 16, 7, 10),
        ("09", "Anais", 13, 7, 10), ("10", "Eva", 20, 8, 17),
        ("11", "Louise", 14, 13, 9),
    ]
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS releve_de_notes (
                sid VARCHAR(10), sname VARCHAR(10),
                cc1 FLOAT, cc2 FLOAT, examen FLOAT, note_finale FLOAT)"""))
        nb = conn.execute(text("SELECT COUNT(*) FROM releve_de_notes")).scalar()
        if nb == 0:
            conn.execute(
                text("INSERT INTO releve_de_notes "
                     "VALUES (:sid, :sname, :cc1, :cc2, :examen, :nf)"),
                [dict(sid=s, sname=n, cc1=a, cc2=b, examen=e, nf=note_finale(a, b, e))
                 for s, n, a, b, e in eleves])


def get_data(query, params=None):
    """Exécute une requête SQL et renvoie un DataFrame pandas."""
    return pd.read_sql(text(query), engine, params=params)


init_db()