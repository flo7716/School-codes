CREATE TABLE releve_de_notes (
    sid        VARCHAR2(10),
    cc1        NUMBER(4, 2),
    cc2        NUMBER(4, 2),
    examen     NUMBER(4, 2),
    note_finale NUMBER(4, 2)
);


CREATE OR REPLACE FUNCTION calculer_note_finale (
    p_cc1    IN NUMBER,
    p_cc2    IN NUMBER,
    p_examen IN NUMBER
) RETURN NUMBER IS
    v_cc          NUMBER;
    v_moyenne     NUMBER;
    v_note_finale NUMBER;
BEGIN
    -- Calcul du CC : moyenne de cc1 et cc2
    v_cc := (NVL(p_cc1, 0) + NVL(p_cc2, 0)) / 2;
    
    -- Calcul de la moyenne globale
    v_moyenne := (v_cc + NVL(p_examen, 0)) / 2;
    
    -- La note finale est le Max entre la moyenne globale et la note d'examen
    v_note_finale := GREATEST(v_moyenne, NVL(p_examen, 0));
    
    RETURN v_note_finale;
EXCEPTION
    WHEN OTHERS THEN
        RETURN NULL;
END;
/

CREATE OR REPLACE TRIGGER trg_before_insert_releve
BEFORE INSERT ON releve_de_notes
FOR EACH ROW
BEGIN
    :NEW.note_finale := calculer_note_finale(:NEW.cc1, :NEW.cc2, :NEW.examen);
END;
/

BEGIN
    -- Exemple donné dans la question (CC1=12, CC2=15, Examen=16) -> Note finale = 16
    INSERT INTO releve_de_notes (sid, cc1, cc2, examen) VALUES ('01', 12, 15, 16);
    
    -- Autre exemple (CC1=10, CC2=14, Examen=10) -> CC = 12, Moyenne = 11, Max(11, 10) = 11
    INSERT INTO releve_de_notes (sid, cc1, cc2, examen) VALUES ('02', 10, 14, 10);
    
    COMMIT;
END;
/

SELECT * FROM releve_de_notes;