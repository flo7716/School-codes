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
    INSERT INTO student VALUES( ‘01‘,‘Leon ‘ ,‘1990−02−01‘ ,‘M’ );
    INSERT INTO student VALUES( ‘02‘, ‘David ‘,‘1990−12−21‘,‘M’ );
    INSERT INTO student VALUES( ‘03‘,‘Lucas ‘,‘1990−12−20‘ ,‘M’ );
    INSERT INTO student VALUES( ‘04‘,‘Paul ‘ ,‘1990−02−06‘ ,‘M’ );
    INSERT INTO student VALUES( ‘05‘, ‘Lea ‘ ,‘1991−02−01‘ ,‘F’ );
    INSERT INTO student VALUES( ‘06‘, ‘Sophie ‘,‘1992−03−01‘,‘F’ );
    INSERT INTO student VALUES( ‘07‘, ‘ Ella ‘ ,‘1989−03−01‘ ,‘F’ );
    INSERT INTO student VALUES( ‘08‘, ‘Zoe ‘ ,‘2007−12−20‘ ,‘F’ );
    INSERT INTO student VALUES( ‘09‘, ‘Anais ‘,‘2007−12−25‘,‘F’ );
    INSERT INTO student VALUES( ‘10‘, ‘Eva ‘,‘2002−06−06‘ ,‘F’ );
    INSERT INTO student VALUES( ‘11‘, ‘Louise ‘,‘2003−06−13‘,‘F’ );
END;