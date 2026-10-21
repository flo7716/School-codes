CREATE OR REPLACE PROCEDURE calculer_racine_carree_sec(p_nombre IN NUMBER) IS
    v_resultat NUMBER;
    -- Déclaration d'une exception personnalisée
    e_nombre_negatif EXCEPTION;
BEGIN
    -- Vérification si le nombre est négatif
    IF p_nombre < 0 THEN
        RAISE e_nombre_negatif;
    END IF;
    
    v_resultat := SQRT(p_nombre);
    DBMS_OUTPUT.PUT_LINE('La racine carrée de ' || p_nombre || ' est : ' || v_resultat);
    
EXCEPTION
    WHEN e_nombre_negatif THEN
        DBMS_OUTPUT.PUT_LINE('Erreur : Impossible de calculer la racine carrée d''un nombre négatif (' || p_nombre || ').');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Une erreur inattendue est survenue.');
END;


BEGIN
    calculer_racine_carree_sec(16);
    calculer_racine_carree_sec(-16);
END;
/