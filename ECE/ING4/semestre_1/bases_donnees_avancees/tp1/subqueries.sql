-- employes avec le salaire le plus élevé (2 méthodes)
-- méthode 1 : sous-requête dans la clause WHERE
SELECT *
FROM `EMP`
WHERE SAL = (SELECT MAX(SAL) FROM `EMP`);

-- méthode 2 : sous-requête dans la clause FROM
SELECT E1.*
FROM `EMP` E1, (SELECT MAX(SAL) AS MAX_SAL FROM `EMP`) E2
WHERE E1.SAL = E2.MAX_SAL;