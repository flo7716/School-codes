CREATE TABLE SEGMENT (
    indIP VARCHAR(11) PRIMARY KEY,
    nomSegment VARCHAR(20) NOT NULL,
    etage TINYINT(1)
);

CREATE TABLE SALLE (
    nSalle VARCHAR(7) PRIMARY KEY,
    nomSalle VARCHAR(20),
    nbPoste TINYINT(2),
    indIP VARCHAR(11),
    FOREIGN KEY (indIP) REFERENCES SEGMENT(indIP)
);

CREATE TABLE POSTE (
    nPoste VARCHAR(7) PRIMARY KEY,
    nomPoste VARCHAR(20) NOT NULL,
    indIP VARCHAR(11),
    ad VARCHAR(3) CHECK (ad >= 0 and ad <= 255),
    typePoste VARCHAR(9),
    nSalle VARCHAR(7),
    FOREIGN KEY (nSalle) REFERENCES SALLE(nSalle)
);

CREATE TABLE LOGICIEL (
    nLog VARCHAR(7) PRIMARY KEY,
    nomLog VARCHAR(20),
    dateAch DATETIME,
    version VARCHAR(7),
    typeLog VARCHAR(9),
    prix DECIMAL(6,2) CHECK (prix >= 0)
);

CREATE TABLE INSTALLER (
    nPoste VARCHAR(7),
    nLog VARCHAR(5),
    numIns INTEGER(5),
    dateIns TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delai SMALLINT,
    PRIMARY KEY (nPoste, nLog, numIns),
    FOREIGN KEY (nPoste) REFERENCES POSTE(nPoste),
    FOREIGN KEY (nLog) REFERENCES LOGICIEL(nLog)
);

CREATE TABLE TYPES (
    typeLP VARCHAR(20) PRIMARY KEY,
    nomType VARCHAR(20)
);


