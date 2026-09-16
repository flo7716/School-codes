-- Florian ANDRE
-- Ilana VARINOT
-- Adel KHEYAR
-- ING4 - Majeure cybersecurite en apprentissage 
-- TP2 - Bases de données avancées



-- Destruction des tables

create database if not exists ECE_ING4;
use ECE_ING4;


DROP TABLE IF EXISTS Etudiant; 
DROP TABLE IF EXISTS Matiere; 
DROP TABLE IF EXISTS Epreuve; 
DROP TABLE IF EXISTS Notation; 


-- Creation de tables

CREATE TABLE Etudiant (
  NumEtu INT(8) PRIMARY KEY,
  Nom VARCHAR(20),
  Prenom VARCHAR(20),
  DateNais DATE,
  Rue VARCHAR(50),
  CP CHAR(5),
  Ville VARCHAR(25)
);


CREATE TABLE Matiere (
  CodeMat CHAR(3) PRIMARY KEY,
  Libelle VARCHAR(20),
  Coef DECIMAL(3,2)
);

CREATE TABLE Epreuve (
  NumEpreuve INT(10) PRIMARY KEY,
  DateEpreuve DATE,
  Lieu VARCHAR(20),
  CodeMat CHAR(3)
);

CREATE TABLE Notation (
  NumEtu INT(8),
  NumEpreuve INT(10),
  Note DECIMAL(4,2),
  PRIMARY KEY (NumEtu,NumEpreuve)
);


-- contraintes de cles etrangeres
ALTER TABLE Epreuve ADD CONSTRAINT FkEpreuve1 FOREIGN KEY(CodeMat) REFERENCES Matiere(CodeMat);
ALTER TABLE Notation ADD CONSTRAINT FkNotation1 FOREIGN KEY(NumEtu) REFERENCES Etudiant(NumEtu);
ALTER TABLE Notation ADD CONSTRAINT FkNotation2 FOREIGN KEY(NumEpreuve) REFERENCES Epreuve(NumEpreuve);

-- Remplissage des tables

INSERT INTO Etudiant VALUES (110,'Dupont','Albert','2002-06-01', 'RuedeCrimée','69001','Lyon');
INSERT INTO Etudiant VALUES (222,'West','James','2003-09-03', 'Studio',NULL,'Hollywood');
INSERT INTO Etudiant VALUES (300,'Martin','Marie','2001-06-05', 'RuedesAcacias','69130','Ecully');
INSERT INTO Etudiant VALUES (421,'Durand','Gaston','2003-11-15', 'RuedelaMeuse','69008','Lyon');
INSERT INTO Etudiant VALUES (575,'Titgoutte','Justine','2000-02-28', 'CheminduChâteau','69630','Chaponost');
INSERT INTO Etudiant VALUES (667,'Dupond','Noémie','2001-01-09', 'RuedeDôle','69007','Lyon');
INSERT INTO Etudiant VALUES (999,'Phantom','Marcel','2000-03-01',NULL,NULL,NULL);

INSERT INTO Matiere VALUES ('STA','Statistique',0.4);
INSERT INTO Matiere VALUES ('INF','Informatique',0.4);
INSERT INTO Matiere VALUES ('ECO','Econométrie',0.2);

INSERT INTO Epreuve VALUES(11031,'2015-12-20','Salle191L','STA');
INSERT INTO Epreuve VALUES(11032,'2016-04-04','AmphiG','STA');
INSERT INTO Epreuve VALUES(21031,'2015-10-30','Salle191L','INF');
INSERT INTO Epreuve VALUES(21032,'2016-06-01','Salle192L','INF');
INSERT INTO Epreuve VALUES(31030,'2016-06-02','Salle05R','ECO');

INSERT INTO Notation VALUES (110,11031,10);
INSERT INTO Notation VALUES (110,11032,11.5);
INSERT INTO Notation VALUES (110,21031,8.5);
INSERT INTO Notation VALUES (110,21032, NULL);
INSERT INTO Notation VALUES (110,31030,13);
INSERT INTO Notation VALUES (222,11031,9);
INSERT INTO Notation VALUES (222,11032,14);
INSERT INTO Notation VALUES (222,21031,12);
INSERT INTO Notation VALUES (222,21032,16);
INSERT INTO Notation VALUES (222,31030,20);
INSERT INTO Notation VALUES (300,11031,14);
INSERT INTO Notation VALUES (300,11032,20);
INSERT INTO Notation VALUES (300,21031,20);
INSERT INTO Notation VALUES (300,21032,13.5);
INSERT INTO Notation VALUES (300,31030,16);
INSERT INTO Notation VALUES (421,11031,5.5);
INSERT INTO Notation VALUES (421,11032,17);
INSERT INTO Notation VALUES (421,21031,1.5);
INSERT INTO Notation VALUES (421,21032, NULL);
INSERT INTO Notation VALUES (421,31030,10);
INSERT INTO Notation VALUES (575,11031,13);
INSERT INTO Notation VALUES (575,11032,9);
INSERT INTO Notation VALUES (575,21031,12.5);
INSERT INTO Notation VALUES (575,21032,14);
INSERT INTO Notation VALUES (575,31030,7);
INSERT INTO Notation VALUES (667,11031,16);
INSERT INTO Notation VALUES (667,11032,20);
INSERT INTO Notation VALUES (667,21031,8.5);
INSERT INTO Notation VALUES (667,21032,9.5);
