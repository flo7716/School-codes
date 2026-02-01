-- Requete r
SELECT CONCAT(s.indIP, '.', p.ad) AS Adresse_IP_Complete
FROM LOGICIEL l
JOIN INSTALLER i ON l.nLog = i.nLog
JOIN POSTE p ON i.nPoste = p.nPoste
JOIN SALLE s ON p.nSalle = s.nSalle
WHERE l.nomLog = 'log6';

-- Requete s
SELECT CONCAT(s.indIP, '.', p.ad) AS Adresse_IP_Complete
FROM LOGICIEL l
JOIN INSTALLER i ON l.nLog = i.nLog
JOIN POSTE p ON i.nPoste = p.nPoste
JOIN SALLE s ON p.nSalle = s.nSalle
WHERE l.nomLog = 'Oracle 8';


-- Requete t
SELECT seg.nomSegment
FROM SEGMENT seg
JOIN SALLE sa ON seg.indIP = sa.indIP
JOIN POSTE p ON sa.nSalle = p.nSalle
WHERE p.typePoste = 'TX'
GROUP BY seg.indIP
HAVING COUNT(p.nPoste) = 3;


-- Requete u
SELECT sa.nomSalle
FROM SALLE sa
JOIN POSTE p ON sa.nSalle = p.nSalle
JOIN INSTALLER i ON p.nPoste = i.nPoste
JOIN LOGICIEL l ON i.nLog = l.nLog
WHERE l.nomLog = 'Oracle 6'
GROUP BY sa.nSalle;


-- Requete w
SELECT CONCAT(s.indIP, '.', p.ad) AS Adresse_IP_Complete
FROM SALLE s
JOIN POSTE p ON s.nSalle = p.nSalle
JOIN INSTALLER i ON p.nPoste = i.nPoste
JOIN LOGICIEL l ON i.nLog = l.nLog
WHERE l.nomLog = 'log6';

-- Requete x
SELECT CONCAT(s.indIP, '.', p.ad) AS Adresse_IP_Complete
FROM SALLE s
JOIN POSTE p ON s.nSalle = p.nSalle
JOIN INSTALLER i ON p.nPoste = i.nPoste
JOIN LOGICIEL l ON i.nLog = l.nLog
WHERE l.nomLog = 'Oracle 8';

-- Requete y
SELECT seg.nomSegment
FROM SEGMENT seg
JOIN SALLE sa ON seg.indIP = sa.indIP
JOIN POSTE p ON sa.nSalle = p.nSalle
WHERE p.typePoste = 'TX'
GROUP BY seg.indIP
HAVING COUNT(p.nPoste) = 3;

-- Requete z
SELECT sa.nomSalle
FROM SALLE sa
JOIN POSTE p ON sa.nSalle = p.nSalle
JOIN INSTALLER i ON p.nPoste = i.nPoste
JOIN LOGICIEL l ON i.nLog = l.nLog
WHERE l.nomLog = 'Oracle 6'
GROUP BY sa.nSalle;

-- Question 2
SELECT p.nPoste, COUNT(DISTINCT l.typeLog) AS Nombre_Types_Logiciels
FROM POSTE p
LEFT JOIN INSTALLER i ON p.nPoste = i.nPoste
LEFT JOIN LOGICIEL l ON i.nLog = l.nLog
GROUP BY p.nPoste;

-- Question 3
SELECT s.nSalle, COUNT(DISTINCT l.typeLog) AS Nombre_Types_Logiciels
FROM SALLE s
LEFT JOIN POSTE p ON s.nSalle = p.nSalle
LEFT JOIN INSTALLER i ON p.nPoste = i.nPoste
LEFT JOIN LOGICIEL l ON i.nLog = l.nLog
GROUP BY s.nSalle;

-- Question 4
SELECT seg.etage, l.nomLog AS Logiciel, COUNT(*) AS Nombre_Installations
FROM LOGICIEL l
JOIN INSTALLER i ON l.nLog = i.nLog
JOIN POSTE p ON i.nPoste = p.nPoste
JOIN SALLE s ON p.nSalle = s.nSalle
JOIN SEGMENT seg ON s.indIP = seg.indIP
GROUP BY seg.etage, l.nLog
ORDER BY seg.etage, Nombre_Installations DESC;

-- Question 5
SELECT p.nPoste, COUNT(i.nLog) AS Nombre_Logiciels
FROM POSTE p
LEFT JOIN INSTALLER i ON p.nPoste = i.nPoste
GROUP BY p.nPoste
ORDER BY COUNT(nLog) DESC


-- Question 6
SELECT COUNT(DISTINCT i.nPoste) AS Nombre_Postes
FROM INSTALLER i
WHERE i.nLog = (
    SELECT nLog
    FROM (
        SELECT nLog, COUNT(*) AS Nombre_Installations
        FROM INSTALLER
        GROUP BY nLog
        LIMIT 1
    ) AS subquery
);


-- Question 7
SELECT seg.nomSegment, sa.nomSalle, CONCAT(seg.indIP, '.', p.ad) AS Adresse_IP_Complete, l.nomLog AS Nom_Logiciel, i.dateIns AS Date_Installation
FROM INSTALLER i
JOIN POSTE p ON i.nPoste = p.nPoste
JOIN SALLE sa ON p.nSalle = sa.nSalle
JOIN SEGMENT seg ON sa.indIP = seg.indIP
JOIN LOGICIEL l ON i.nLog = l.nLog
ORDER BY seg.nomSegment, sa.nomSalle, Adresse_IP_Complete;



