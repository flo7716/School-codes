USE glace;

CREATE TABLE products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100), description VARCHAR(255)
);
INSERT INTO products(name, description) VALUES
 ('Glacon Premium','Cube de glace pur, 99.9% H2O'),
 ('Igloo Kit','Prêt à monter en 10 minutes'),
 ('Pioche Arctique','Acier trempé, manche isolé'),
 ('Doudoune Polaire','Résiste à -40°C');

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50), password VARCHAR(100)
);
INSERT INTO users(username, password) VALUES
 ('admin','Gl4c3!Adm1n#2026'),
 ('guest','guest');

CREATE TABLE secrets (
  id INT AUTO_INCREMENT PRIMARY KEY,
  label VARCHAR(50), flag VARCHAR(100)
);
-- Flag stocké en clair (donnée non chiffrée, volontaire)
INSERT INTO secrets(label, flag) VALUES ('flag_1','flag{ic3_p4th_sql1_fr0z3n_d4t4}');

-- Moindre privilège : le compte applicatif ne peut que lire
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'webapp'@'%';
GRANT SELECT ON glace.* TO 'webapp'@'%';
FLUSH PRIVILEGES;
