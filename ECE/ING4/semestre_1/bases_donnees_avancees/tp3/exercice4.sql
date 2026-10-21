CREATE OR REPLACE FUNCTION calculer_age(p_date_naissance IN DATE) 
RETURN NUMBER IS
    v_age NUMBER;
BEGIN
    -- Vérification si la date de naissance est dans le futur
    IF p_date_naissance > SYSDATE THEN
        RETURN 0; 
    END IF;

    -- Calcul de l'âge en années pleines
    v_age := TRUNC(MONTHS_BETWEEN(SYSDATE, p_date_naissance) / 12);
    
    RETURN v_age;
EXCEPTION
    WHEN OTHERS THEN
        -- Gestion basique des erreurs (ex: date invalide)
        RETURN NULL;
END;
/

SELECT calculer_age(TO_DATE('2002-02-03', 'YYYY-MM-DD')) AS mon_age FROM DUAL;



-- Partie 2 
CREATE TABLE student(
sid VARCHAR2(10) ,
sname VARCHAR2(10),
birthday DATE,
ssex VARCHAR2(10));

BEGIN
    INSERT INTO student VALUES ('01', 'Leon',   TO_DATE('1990-02-01', 'YYYY-MM-DD'), 'M');
    INSERT INTO student VALUES ('02', 'David',  TO_DATE('1990-12-21', 'YYYY-MM-DD'), 'M');
    INSERT INTO student VALUES ('03', 'Lucas',  TO_DATE('1990-12-20', 'YYYY-MM-DD'), 'M');
    INSERT INTO student VALUES ('04', 'Paul',   TO_DATE('1990-02-06', 'YYYY-MM-DD'), 'M');
    INSERT INTO student VALUES ('05', 'Lea',    TO_DATE('1991-02-01', 'YYYY-MM-DD'), 'F');
    INSERT INTO student VALUES ('06', 'Sophie', TO_DATE('1992-03-01', 'YYYY-MM-DD'), 'F');
    INSERT INTO student VALUES ('07', 'Ella',   TO_DATE('1989-03-01', 'YYYY-MM-DD'), 'F');
    INSERT INTO student VALUES ('08', 'Zoe',    TO_DATE('2007-12-20', 'YYYY-MM-DD'), 'F');
    INSERT INTO student VALUES ('09', 'Anais',  TO_DATE('2007-12-25', 'YYYY-MM-DD'), 'F');
    INSERT INTO student VALUES ('10', 'Eva',    TO_DATE('2002-06-06', 'YYYY-MM-DD'), 'F');
    INSERT INTO student VALUES ('11', 'Louise', TO_DATE('2003-06-13', 'YYYY-MM-DD'), 'F');
    
    COMMIT; -- Permet de valider l'insertion dans la base de données
END;
/

-- Ajout age
ALTER TABLE student ADD age NUMBER;

UPDATE student 
SET age = calculer_age(birthday);

SELECT * FROM student;