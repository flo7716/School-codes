-- Insertion de données dans la table SEGMENT
INSERT INTO SEGMENT (indIP, nomSegment, etage) VALUES
('130.120.80', 'Brin', 0),
('130.120.81', 'Brin 1er etage', 1),
('130.120.82', 'Brin 2e etage', 2),
('130.120.83', 'Brin 3e etage', 3);

-- Insertion de données dans la table SALLE
INSERT INTO SALLE (nSalle, nomSalle, nbPoste, indIP) VALUES
('S01', 'Salle 1', 3, '130.120.80'),
('S02', 'Salle 2', 2, '130.120.80'),
('S03', 'Salle 3', 2, '130.120.80'),
('S11', 'Salle 11', 2, '130.120.81'),
('S12', 'Salle 12', 1, '130.120.82'),
('S21', 'Salle 21', 2, '130.120.82'),
('S22', 'Salle 22', 0, '130.120.83'),
('S23', 'Salle 23', 0, '130.120.83');

-- Insertion de données dans la table POSTE
INSERT INTO POSTE (nPoste, nomPoste, indIP, ad, typePoste, nSalle) VALUES
('p1', 'Poste 1', '130.120.80', '01', 'TM', 'S01'),
('p2', 'Poste 2', '130.120.80', '02', 'UNIX', 'S01'),
('p3', 'Poste 3', '130.120.80', '03', 'TM', 'S01'),
('p4', 'Poste 4', '130.120.80', '04', 'PCWS', 'S02'),
('p5', 'Poste 5', '130.120.80', '05', 'PCWS', 'S02'),
('p6', 'Poste 6', '130.120.80', '06', 'UNIX', 'S03'),
('p7', 'Poste 7', '130.120.80', '07', 'TM', 'S03'),
('p8', 'Poste 8', '130.120.81', '01', 'UNIX', 'S11'),
('p9', 'Poste 9', '130.120.81', '02', 'TM', 'S11'),
('p10', 'Poste 10', '130.120.81', '03', 'UNIX', 'S12'),
('p11', 'Poste 11', '130.120.82', '01', 'PCNT', 'S21'),
('p12', 'Poste 12', '130.120.82', '02', 'PCWS', 'S21');


-- Insertion de données dans la table LOGICIEL
INSERT INTO LOGICIEL (nLog, nomLog, dateAch, version, typeLog, prix) VALUES
('log1', 'Oracle 6', '1995-05-13', '6.2', 'UNIX', 3000),
('log2', 'Oracle 8', '1999-09-15', '8i', 'UNIX', 5600),
('log3', 'SQL Server', '1998-04-12', '7', 'PCNT', 2700),
('log4', 'Front Page', '1997-06-03', '5', 'PCWS', 500),
('log5', 'WinDev', '1997-05-12', '5', 'PCWS', 750),
('log6', 'SQL*Net', NULL, '2.0', 'UNIX', 500),
('log7', 'I.I.S.', '2002-04-12', '2', 'PCNT', 810),
('log8', 'DreamWeaver', '2003-09-21', '2.0', 'BeOS', 1400);





-- Insertion de données dans la table INSTALLER
INSERT INTO INSTALLER (nPoste, nLog, numIns, dateIns, delai) VALUES
('p2', 'log1', 1, '2003-05-15', NULL),
('p2', 'log2', 2, '2003-09-17', NULL),
('p4', 'log5', 3, NULL, NULL),
('p6', 'log6', 4, '2003-05-20', NULL),
('p6', 'log1', 5, '2003-05-20', NULL),
('p8', 'log2', 6, '2003-05-19', NULL),
('p8', 'log6', 7, '2003-05-20', NULL),
('p11', 'log3', 8, '2003-04-20', NULL),
('p12', 'log4', 9, '2003-04-20', NULL),
('p11', 'log7', 10, '2003-04-20', NULL),
('p7', 'log7', 11, '2002-04-01', NULL);

-- Insertion de données dans la table TYPES
INSERT INTO TYPES (typeLP, nomType) VALUES
('TM', 'Terminal X-Window'),
('UNIX', 'Système Unix'),
('PCNT', 'PC Windows NT'),
('PCWS', 'PC Windows'),
('NC', 'Network Computer');
