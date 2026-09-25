-- Adel KHEYAR - Florian ANDRE - Ilana Varinot
-- INGE 4 APP Grp 2 
-- TP 2
use ECE_ING4;
-- II

-- 1
SELECT COUNT(*) FROM Etudiant;
SELECT COUNT(*) FROM Matiere;
SELECT COUNT(*) FROM Epreuve;
SELECT COUNT(*) FROM Notation;

-- 2 
SELECT * FROM Notation WHERE Note >= 10;

-- 3
SELECT * FROM Epreuve 
WHERE DateEpreuve BETWEEN '2016-01-01' AND '2016-06-01'; 

-- 4 
SELECT COUNT(*) FROM Epreuve;

-- 5 
SELECT COUNT(*) FROM Notation WHERE Note IS NULL;

-- 6 
SELECT N.NumEtu, E.Nom, E.Prenom, N.NumEpreuve, N.Note
FROM Notation N
JOIN Etudiant E ON N.NumEtu = E.NumEtu;

-- 7 
SELECT E.NumEtu, E.Nom, E.Prenom, AVG(IFNULL(N.Note,0)) AS Moyenne
FROM Etudiant E
JOIN Notation N ON E.NumEtu = N.NumEtu
GROUP BY E.NumEtu, E.Nom, E.Prenom
ORDER BY Moyenne DESC;

-- 8 
SELECT E.NumEtu, E.Nom, E.Prenom, AVG(IFNULL(N.Note,0)) AS MoyInfo
FROM Etudiant E
JOIN Notation N ON E.NumEtu = N.NumEtu
JOIN Epreuve Ep ON N.NumEpreuve = Ep.NumEpreuve
WHERE Ep.CodeMat = 'INF'
GROUP BY E.NumEtu, E.Nom, E.Prenom
ORDER BY MoyInfo ASC
LIMIT 1;

-- 9 
SELECT E.NumEtu, E.Nom, E.Prenom, AVG(IFNULL(N.Note,0)) AS MoyGen
FROM Etudiant E
JOIN Notation N ON E.NumEtu = N.NumEtu
GROUP BY E.NumEtu, E.Nom, E.Prenom
ORDER BY MoyGen DESC
LIMIT 1;

-- 10 
SELECT E.NumEtu, E.Nom, E.Prenom
FROM Etudiant E
JOIN Notation N ON E.NumEtu = N.NumEtu
GROUP BY E.NumEtu, E.Nom, E.Prenom
HAVING COUNT(DISTINCT N.NumEpreuve) = (SELECT COUNT(*) FROM Epreuve);




