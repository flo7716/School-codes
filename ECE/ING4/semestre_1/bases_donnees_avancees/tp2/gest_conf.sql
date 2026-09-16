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

-- 2 : donner la moyenne en informatique des étudiants lyonnais
SELECT AVG(Note) AS MoyenneInformatique
FROM Notation N
JOIN Epreuve E ON N.NumEpreuve = E.NumEpreuve
WHERE E.CodeMat = 'INF' AND N.NumEtu IN (SELECT NumEtu FROM EtudLyonnais);

-- 3 : L'etudiant Dupond a quitté l'établissement. Est-il possible de le supprimer depuis la vue EtudLyonnais ? Justifier votre réponse.
DELETE FROM EtudLyonnais WHERE Nom = 'Dupond';
-- Non, il n'est pas possible de supprimer l'étudiant Dupond depuis la vue EtudLyonnais car la vue est basée sur une condition (Ville = 'Lyon') et ne permet pas de modifier directement les données de la table sous-jacente. 

-- 4 : L'etudiant Durand déménage lors de son stage à 1 rue de Lyon, Paris 75002. Est-il possible de mettre à jour ses informations depuis la vue EtudLyonnais ? Justifier votre réponse.
UPDATE EtudLyonnais SET Ville = 'Paris', Rue = '1 rue de Lyon', `CP` = '75002' WHERE Nom = 'Durand';
-- Oui, il est possible de mettre à jour les informations de l'étudiant Durand depuis la vue EtudLyonnais car la vue contient tous les champs de la table Etudiant et permet donc de modifier directement les données de la table sous-jacente.
SELECT * FROM Etudiant WHERE Nom = 'Durand';

-- 

