USE glace_db;

CREATE TABLE produits (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100),
  description VARCHAR(255)
);
INSERT INTO produits (nom, description) VALUES
 ('Glacon Premium', 'Cube de glace pur, 99.9% H2O'),
 ('Igloo Kit', 'Pret a monter en 10 minutes'),
 ('Pioche Arctique', 'Acier trempe, manche isole'),
 ('Doudoune Polaire', 'Resiste a -40C');

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50),
  password VARCHAR(100)
);
INSERT INTO users (username, password) VALUES
 ('admin', 'Gl4c3!Adm1n#2026'),
 ('guest', 'guest');

CREATE TABLE secrets (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(50),
  valeur VARCHAR(100)
);
-- Flag 2 : stocke en clair (donnee non chiffree, faiblesse volontaire)
INSERT INTO secrets (nom, valeur) VALUES ('flag_2', 'flag{sql1_d4ns_l4_gl4c3}');

-- Compte applicatif utilise par srv-web.
-- NB CTF : ce mot de passe DOIT rester identique a celui ecrit en dur dans
-- ftp/pub/backup/config.php.bak et dans .env (DB_PASSWORD) : c'est le secret
-- que le flag 1 est cense reveler. Ne pas le "securiser" sans mettre a jour
-- les deux autres fichiers, sinon le fil rouge du CTF est casse.
CREATE USER IF NOT EXISTS 'glace_app'@'%' IDENTIFIED BY 'Gl4c3_App_2026';

-- Faiblesse aggravante documentee (CWE-250) : le compte dispose de SELECT sur TOUTE
-- la base (y compris users et secrets) au lieu de la seule table produits.
-- Correctif production : GRANT SELECT ON glace_db.produits TO 'glace_app'@'%';
GRANT SELECT ON glace_db.* TO 'glace_app'@'%';
FLUSH PRIVILEGES;
