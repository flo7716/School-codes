-- Vues
-- Vue_Poste_UNIX_TX
CREATE VIEW Vue_Poste_UNIX_TX AS
SELECT p.nomPoste, CONCAT(p.indIP, '.', p.ad) AS adresse_IP, p.nSalle
FROM POSTE p
WHERE p.typePoste IN ('UNIX', 'TX');

-- Vue_Logiciel_UNIX_TX
CREATE VIEW Vue_Logiciel_UNIX_TX AS
SELECT l.nLog, l.nomLog, l.version, l.typeLog, COUNT(i.nPoste) AS nbInstall
FROM LOGICIEL l
JOIN INSTALLER i ON l.nLog = i.nLog
WHERE l.typeLog IN ('UNIX', 'TX')
GROUP BY l.nLog, l.nomLog, l.version, l.typeLog
ORDER BY l.nomLog, l.version;

-- Utilisateurs
CREATE USER 'user_reader'@'localhost' IDENTIFIED BY 'password';
CREATE USER 'user_modifier'@'localhost' IDENTIFIED BY 'password';

-- Droits
-- user_reader
GRANT SELECT ON parc_informatique.Vue_Poste_UNIX_TX TO 'user_reader'@'localhost';
GRANT SELECT ON parc_informatique.Vue_Logiciel_UNIX_TX TO 'user_reader'@'localhost';

-- user_modifier
GRANT SELECT, DROP ON parc_informatique.Vue_Poste_UNIX_TX TO 'user_modifier'@'localhost';
GRANT SELECT, DROP ON parc_informatique.Vue_Logiciel_UNIX_TX TO 'user_modifier'@'localhost';


--Triggers 
-- Trig_AD_Installer (AFTER DELETE)
CREATE TRIGGER Trig_AD_Installer AFTER DELETE ON INSTALLER
FOR EACH ROW
BEGIN
    UPDATE POSTE SET nbLog = nbLog - 1 WHERE nPoste = OLD.nPoste;
    UPDATE LOGICIEL SET nbInstall = nbInstall - 1 WHERE nLog = OLD.nLog;
END;

-- Trig_AI_Installer (AFTER INSERT)
CREATE TRIGGER Trig_AI_Installer AFTER INSERT ON INSTALLER
FOR EACH ROW
BEGIN
    UPDATE POSTE SET nbLog = nbLog + 1 WHERE nPoste = NEW.nPoste;
    UPDATE LOGICIEL SET nbInstall = nbInstall + 1 WHERE nLog = NEW.nLog;
END;


-- Trig_AI_Poste (AFTER INSERT)
CREATE TRIGGER Trig_AI_Poste AFTER INSERT ON POSTE
FOR EACH ROW
BEGIN
    UPDATE SALLE SET nbPoste = nbPoste + 1 WHERE nSalle = NEW.nSalle;
END;

-- Trig_AD_Poste (AFTER DELETE)
CREATE TRIGGER Trig_AD_Poste AFTER DELETE ON POSTE
FOR EACH ROW
BEGIN
    UPDATE SALLE SET nbPoste = nbPoste - 1 WHERE nSalle = OLD.nSalle;
END;

-- Trig_AU_Salle (AFTER UPDATE)
CREATE TRIGGER Trig_AU_Salle AFTER UPDATE ON SALLE
FOR EACH ROW
BEGIN
    UPDATE SEGMENT s
    SET s.nbPoste = (SELECT SUM(nbPoste) FROM SALLE WHERE indIP = s.indIP);
END;
