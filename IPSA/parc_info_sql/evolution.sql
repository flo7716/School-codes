-- Ajouter la colonne nbSalle à la table Segment
ALTER TABLE SEGMENT
ADD nbSalle TINYINT(2) DEFAULT 0;

-- Ajouter la colonne nbPoste à la table Segment
ALTER TABLE SEGMENT
ADD nbPoste TINYINT(2) DEFAULT 0;

-- Ajouter la colonne nbInstall à la table Logiciel
ALTER TABLE LOGICIEL
ADD nbInstall TINYINT(2) DEFAULT 0;

-- Ajouter la colonne nbLog à la table Poste
ALTER TABLE POSTE
ADD nbLog TINYINT(2) DEFAULT 0;

-- Ajouter la colonne nbSalle à la table Segment
ALTER TABLE SEGMENT
ADD nbSalle TINYINT(2) DEFAULT 0;

-- Ajouter la colonne nbPoste à la table Segment
ALTER TABLE SEGMENT
ADD nbPoste TINYINT(2) DEFAULT 0;

-- Ajouter la colonne nbInstall à la table Logiciel
ALTER TABLE LOGICIEL
ADD nbInstall TINYINT(2) DEFAULT 0;

-- Ajouter la colonne nbLog à la table Poste
ALTER TABLE POSTE
ADD nbLog TINYINT(2) DEFAULT 0;

-- Augmenter la taille de la colonne nomSalle dans la table Salle
ALTER TABLE SALLE
MODIFY COLUMN nomSalle VARCHAR(30);

-- Diminuer la taille de la colonne nomSegment dans la table Segment
ALTER TABLE SEGMENT
MODIFY COLUMN nomSegment VARCHAR(15);

-- Tenter de diminuer la taille de la colonne nomSegment dans la table Segment à VARCHAR(14)
ALTER TABLE SEGMENT
MODIFY COLUMN nomSegment VARCHAR(14);
