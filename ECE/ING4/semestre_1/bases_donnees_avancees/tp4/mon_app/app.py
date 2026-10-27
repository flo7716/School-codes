import plotly.express as px
import streamlit as st

from db import get_data

st.set_page_config(page_title="Dashboard des notes", layout="wide")
st.title("Dashboard - Relevé de notes")

# ---- Filtre utilisateur ----
seuil = st.sidebar.slider("Note finale minimale", 0, 20, 0)
p = {"seuil": seuil}

# Table de base filtrée (utilisée dans toutes les requêtes)
BASE = "(SELECT * FROM releve_de_notes WHERE note_finale >= :seuil)"

# ---- Requêtes SQL ----
df = get_data(f"SELECT sname, cc1, cc2, examen, note_finale FROM {BASE} t "
              "ORDER BY note_finale DESC", p)

if df.empty:
    st.warning("Aucun étudiant ne correspond au filtre.")
    st.stop()

df_moy = get_data(f"""
    SELECT 'CC1' AS epreuve, ROUND(AVG(cc1), 2) AS moyenne FROM {BASE} t
    UNION ALL SELECT 'CC2', ROUND(AVG(cc2), 2) FROM {BASE} t
    UNION ALL SELECT 'Examen', ROUND(AVG(examen), 2) FROM {BASE} t
    UNION ALL SELECT 'Note finale', ROUND(AVG(note_finale), 2) FROM {BASE} t""", p)

df_reussite = get_data(f"""
    SELECT CASE WHEN note_finale >= 10 THEN 'Réussite' ELSE 'Échec' END AS resultat,
           COUNT(*) AS nombre
    FROM {BASE} t GROUP BY 1""", p)

df_cc = get_data(f"SELECT sname, (cc1 + cc2) / 2.0 AS moyenne_cc, examen FROM {BASE} t", p)

# ---- Requêtes avec JOINTURE : releve_de_notes (r) + etudiants (e), clé commune : sid ----
JOIN = f"FROM {BASE} r JOIN etudiants e ON r.sid = e.sid"

df_join = get_data(f"""
    SELECT r.sname, e.filiere, e.sexe, r.cc1, r.cc2, r.examen, r.note_finale
    {JOIN} ORDER BY r.note_finale DESC""", p)

df_filiere = get_data(f"""
    SELECT e.filiere, e.sexe, ROUND(AVG(r.note_finale), 2) AS moyenne, COUNT(*) AS effectif
    {JOIN} GROUP BY e.filiere, e.sexe ORDER BY e.filiere, e.sexe""", p)

# ---- Indicateurs ----
c1, c2, c3, c4 = st.columns(4)
c1.metric("Étudiants", len(df))
c2.metric("Moyenne des notes finales", round(df["note_finale"].mean(), 2))
c3.metric("Taux de réussite", f"{round((df['note_finale'] >= 10).mean() * 100)} %")
c4.metric("Meilleure note", df["note_finale"].max())

# ---- Graphiques ----
g1, g2 = st.columns(2)
g1.plotly_chart(
    px.bar(df, x="sname", y="note_finale", text="note_finale",
           title="Note finale par étudiant"),
    width="stretch")
g2.plotly_chart(
    px.bar(df_moy, x="epreuve", y="moyenne", text="moyenne",
           title="Moyenne par épreuve"),
    width="stretch")

g3, g4 = st.columns(2)
g3.plotly_chart(
    px.pie(df_reussite, names="resultat", values="nombre", title="Réussite / Échec",
           color="resultat",
           color_discrete_map={"Réussite": "#2eb398", "Échec": "#c42525"}),
    width="stretch")
g4.plotly_chart(
    px.scatter(df_cc, x="moyenne_cc", y="examen", hover_name="sname",
               title="Contrôle continu vs examen"),
    width="stretch")

# ---- Jointure : notes + informations des étudiants ----
st.subheader("Jointure : notes + filière + sexe")
j1, j2 = st.columns(2)
j1.plotly_chart(
    px.bar(df_filiere, x="filiere", y="moyenne", color="sexe", barmode="group",
           text="moyenne", title="Moyenne par filière et par sexe"),
    width="stretch")
j2.dataframe(df_join, width="stretch")