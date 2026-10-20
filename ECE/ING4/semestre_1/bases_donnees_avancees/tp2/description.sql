-- Florian ANDRE
-- Ilana VARINOT
-- Adel KHEYAR
-- ING4 - Majeure cybersecurite en apprentissage 
-- TP2 - Bases de données avancées

-- II - Interrogation

use ECE_ING4;

-- 1 : Vérifier la création des 4 tables et leur instanciation (nombre de lignes par table)
SELECT COUNT(*) FROM Etudiant;
SELECT COUNT(*) FROM Matiere;
SELECT COUNT(*) FROM Epreuve;
SELECT COUNT(*) FROM Notation;


-- 2 : Liste des notes supérieures ou égales à 10
SELECT * FROM Notation WHERE Note >= 10;

-- 3 : Liste des épreuves dont la date se trouve entre le 01 janvier et le 01 juin 2016
SELECT * FROM Epreuve WHERE DateEpreuve BETWEEN '2016-01-01' AND '2016-06-01';

-- 4 : Nombre total d'épreuves
SELECT COUNT(*) FROM Epreuve;

-- 5 : Nombre de notes indéterminées (NULL)
SELECT COUNT(*) FROM Notation WHERE Note IS NULL;

-- 6 : Liste des notes en précisant pour chacune le nom et le prénom de l'étudiant qui l'a obtenue,
SELECT E.Note, Et.Nom, Et.Prenom
FROM Notation E
JOIN Etudiant Et ON E.NumEtu = Et.NumEtu;

-- 7 : Moyennes des notes de chaque étudiant (nom, prénom) classés de la meilleure à la moins bonne (les notes NULL sont à considérer comme 0)
SELECT Et.Nom, Et.Prenom, AVG(COALESCE(N.Note, 0)) AS Moyenne
FROM Etudiant Et
LEFT JOIN Notation N ON Et.NumEtu = N.NumEtu
GROUP BY Et.NumEtu
ORDER BY Moyenne DESC;

-- 8 : Liste des étudiants avec la plus petite moyenne en Informatique
SELECT Et.Nom, Et.Prenom, AVG(COALESCE(N.Note, 0)) AS Moyenne
FROM Etudiant Et
JOIN Notation N ON Et.NumEtu = N.NumEtu
JOIN Epreuve E ON N.NumEpreuve = E.NumEpreuve
WHERE E.CodeMat = 'INF'
GROUP BY Et.NumEtu
ORDER BY Moyenne ASC
LIMIT 1;

-- 9 : Liste des étudiants avec la plus grande moyenne générale
SELECT Et.Nom, Et.Prenom, AVG(COALESCE(N.Note, 0)) AS Moyenne
FROM Etudiant Et
JOIN Notation N ON Et.NumEtu = N.NumEtu
GROUP BY Et.NumEtu
ORDER BY Moyenne DESC
LIMIT 1;

-- 10 : Liste des étudiants ayant participé à toutes les épreuves
SELECT Et.Nom, Et.Prenom
FROM Etudiant Et
WHERE NOT EXISTS (
    SELECT E.NumEpreuve
    FROM Epreuve E
    WHERE NOT EXISTS (
        SELECT N.NumEpreuve
        FROM Notation N
        WHERE N.NumEtu = Et.NumEtu AND N.NumEpreuve = E.NumEpreuve
    )
);