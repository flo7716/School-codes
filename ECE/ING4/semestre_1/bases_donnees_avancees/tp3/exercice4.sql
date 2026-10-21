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