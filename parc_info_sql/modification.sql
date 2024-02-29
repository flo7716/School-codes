
UPDATE SEGMENT
SET etage = 
    CASE indIP
        WHEN '130.120.80' THEN 0
        WHEN '130.120.81' THEN 1
        WHEN '130.120.82' THEN 2
    END;


UPDATE LOGICIEL
SET prix = prix * 0.9
WHERE typeLog = 'PCNT';
