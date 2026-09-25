-- III
use tp2;
-- 1 
CREATE VIEW EtudLyonnais AS
SELECT * FROM Etudiant WHERE Ville = 'Lyon';

SELECT * FROM EtudLyonnais;

-- 2 
SELECT EL.NumEtu, EL.Nom, EL.Prenom, AVG(IFNULL(N.Note,0)) AS MoyInfo
FROM EtudLyonnais EL
JOIN Notation N ON EL.NumEtu = N.NumEtu
JOIN Epreuve Ep ON N.NumEpreuve = Ep.NumEpreuve
WHERE Ep.CodeMat = 'INF'
GROUP BY EL.NumEtu, EL.Nom, EL.Prenom;

-- 3 
DELETE FROM EtudLyonnais WHERE Nom = 'Dupond';
-- la suppression échoue à cause de la contrainte de clé étrangère

-- 4 
UPDATE EtudLyonnais 
SET Rue = '1, Rue de Lyon', CP = '75002', Ville = 'Paris'
WHERE Nom = 'Durand';
SELECT * FROM EtudLyonnais; -- il n'est plus la car plus lyonnais, ca marche 

-- 5 
INSERT INTO EtudLyonnais VALUES 
(700, 'Gates', 'Bill', '1980-09-01', 'Rue de Paris', '78005', 'Versailles');
SELECT * FROM Etudiant WHERE NumEtu=700;
-- il a bien été ajoute


-- 6
CREATE VIEW MoyLyonnais AS
SELECT EL.NumEtu, EL.Nom, EL.Prenom, Ep.CodeMat, AVG(IFNULL(N.Note,0)) AS Moyenne
FROM EtudLyonnais EL
JOIN Notation N ON EL.NumEtu = N.NumEtu
JOIN Epreuve Ep ON N.NumEpreuve = Ep.NumEpreuve
GROUP BY EL.NumEtu, EL.Nom, EL.Prenom, Ep.CodeMat;

SELECT * FROM MoyLyonnais;

-- 7 
UPDATE MoyLyonnais SET Moyenne = 15 WHERE Nom='Dupont' AND CodeMat='INF';
-- non cela echoue 

-- 8 
CREATE USER 'binome'@'localhost' IDENTIFIED BY 'motdepasse';
GRANT SELECT ON tp2.EtudLyonnais TO 'binome'@'localhost';
FLUSH PRIVILEGES;

SHOW GRANTS FOR 'binome'@'localhost';
-- c'est bien visible sur les 2 comptes 

-- 9 
UPDATE EtudLyonnais SET Rue='Rue de la Meuse', CP='69008', Ville='Lyon' WHERE Nom='Dupont';
COMMIT;

SELECT * FROM EtudLyonnais WHERE Nom='Dupont';
-- ca marche aussi sur l'autre compte 

-- 10
-- l doit faire un COMMIT après son INSERT. Tant qu'il n'a pas validé sa transaction, les autres connexions ne voient pas la nouvelle ligne
-- Une fois le COMMIT effectué, un SELECT * FROM EtudLyonnais, depuis le compte devrait afficher le nouvel étudian

-- 11 
-- par exemple  : 
START TRANSACTION;
UPDATE Notation SET Note = 15 WHERE NumEtu=110 AND NumEpreuve=11031; -- exemple
UPDATE Notation SET Note = 10 WHERE NumEtu=421 AND NumEpreuve=11031; -- exemple
COMMIT;

-- 12 
-- Utiliser des transactions avec verrouillage explicite
-- Définir une répartition claire des droits (qui a le droit d'écrire sur quoi).
-- Mettre enplace un contrôle applicati
-- Communiquer/synchroniser entre binômes avant modification concurrente d'une même donnée