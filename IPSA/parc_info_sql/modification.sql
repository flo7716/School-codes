
UPDATE SEGMENT
SET etage = 
    CASE indIP
        WHEN '130.120.80' THEN 0
        WHEN '130.120.81' THEN 1
        WHEN '130.120.82' THEN 2
        WHEN '130.120.83' THEN 3
        WHEN '130.120.84' THEN 4
        WHEN '130.120.85' THEN 5
        WHEN '130.120.86' THEN 6
        WHEN '130.120.87' THEN 7
        WHEN '130.120.88' THEN 8
        WHEN '130.120.89' THEN 9
    END;


UPDATE LOGICIEL
SET prix = prix * 0.9
WHERE typeLog = 'PCNT';
