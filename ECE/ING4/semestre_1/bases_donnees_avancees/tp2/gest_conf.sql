-- Florian ANDRE
-- Ilana VARINOT
-- Adel KHEYAR
-- ING4 - Majeure cybersecurite en apprentissage 
-- TP2 - Bases de données avancées

-- III - Gestion de la confidentialité (vues et droits d'accès)

use ECE_ING4;

-- 1 : Création d'une vue EtudLyonnais renfermant tous les étudiants lyonnais (la vue obtenue contient tous les champs de la table Etudiant)
CREATE VIEW EtudLyonnais AS
SELECT *
FROM Etudiant
WHERE Ville = 'Lyon';

-- 2 : donner la moyenne en informatique de chacun des étudiants lyonnais
SELECT Nom, Prenom, AVG(Note) AS MoyenneInformatique
FROM EtudLyonnais
JOIN Notation ON EtudLyonnais.NumEtu = Notation.NumEtu
JOIN Epreuve ON Notation.NumEpreuve = Epreuve.NumEpreuve
JOIN Matiere ON Epreuve.CodeMat = Matiere.CodeMat
WHERE Matiere.Libelle = 'Informatique'
GROUP BY EtudLyonnais.NumEtu;

-- 3 : L'etudiant Dupond a quitté l'établissement. Est-il possible de le supprimer depuis la vue EtudLyonnais ? Justifier votre réponse.
DELETE FROM EtudLyonnais WHERE Nom = 'Dupond';
-- Non, il n'est pas possible de supprimer l'étudiant Dupond depuis la vue EtudLyonnais car la vue est basée sur une condition (Ville = 'Lyon') et ne permet pas de modifier directement les données de la table sous-jacente. 

-- 4 : L'etudiant Durand déménage lors de son stage à 1 rue de Lyon, Paris 75002. Est-il possible de mettre à jour ses informations depuis la vue EtudLyonnais ? Justifier votre réponse.
UPDATE EtudLyonnais SET Ville = 'Paris', Rue = '1 rue de Lyon', `CP` = '75002' WHERE Nom = 'Durand';
-- Oui, il est possible de mettre à jour les informations de l'étudiant Durand depuis la vue EtudLyonnais car la vue contient tous les champs de la table Etudiant et permet donc de modifier directement les données de la table sous-jacente.
SELECT * FROM Etudiant WHERE Nom = 'Durand';

-- 5 : Est-il possible d’ajouter l’étudiant (700, Gates, Bill, 1980-09-1, Rue de Paris, 78005, Versailles) depuis la vue EtudLyonnais ?  Vérifier ?
INSERT INTO EtudLyonnais (NumEtu, Nom, Prenom, DateNais, Rue, CP, Ville) VALUES (700, 'Gates', 'Bill', '1980-09-01', 'Rue de Paris', '78005', 'Versailles');
-- Oui, il est possible d'ajouter l'étudiant Bill Gates depuis la vue EtudLyonnais car la vue contient tous les champs de la table Etudiant et permet donc d'insérer directement des données dans la table sous-jacente.


-- 6 : Donner la vue MoyLyonnais contenant la moyenne par matière des étudiants lyonnais.
CREATE VIEW MoyLyonnais AS
SELECT EtudLyonnais.NumEtu, Matiere.Libelle, AVG(Notation.Note) AS Moyenne
FROM EtudLyonnais
JOIN Notation ON EtudLyonnais.NumEtu = Notation.NumEtu
JOIN Epreuve ON Notation.NumEpreuve = Epreuve.NumEpreuve
JOIN Matiere ON Epreuve.CodeMat = Matiere.CodeMat
GROUP BY EtudLyonnais.NumEtu, Matiere.Libelle;

SELECT * FROM `MoyLyonnais`;

-- 7 : Est-il possible de mettre à jour la moyenne en informatique de l’étudiant Dupont depuis la vue MoyLyonnais ?
UPDATE MoyLyonnais SET Moyenne = 15 WHERE NumEtu = 100 AND Libelle = 'Informatique';
-- non il n'est pas possible de mettre à jour la moyenne en informatique de l'étudiant Dupont depuis la vue MoyLyonnais car cette vue est basée sur une agrégation (AVG) et ne permet pas de modifier directement les données de la table sous-jacente.

-- 8 : Donnez un droit d’accès en consultation à la vue EtudLyonnais à votre binôme (Un second compte que vous allez créer si nécessaire sous MySQL). Vérifier le contenu de la vue depuis les 2 comptes.
CREATE USER 'binome'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT ON ECE_ING4.EtudLyonnais TO 'binome'@'localhost';
-- Pour vérifier le contenu de la vue depuis les deux comptes, vous pouvez vous connecter à MySQL avec le compte 'binome' et exécuter la requête suivante
-- SELECT * FROM ECE_ING4.EtudLyonnais;

