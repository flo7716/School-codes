-- NULL VALUES

-- Employes dont la commission est specifiee (meme 0.0)
SELECT * FROM EMP WHERE COMM IS NOT NULL;

-- nombre d'employes dont la commission est specifiee (meme 0.0), en 2 methodes
SELECT COUNT(*) FROM EMP WHERE COMM IS NOT NULL;
SELECT COUNT(COMM) FROM EMP WHERE COMM IS NOT NULL;

-- Nombre d'employes dont la commission n'est pas specifiee en 2 methodes
SELECT COUNT(*) FROM EMP WHERE COMM IS NULL;

-- la commission la plus basse, la moyenne et la plus élevée (on écarte les NULL)
SELECT MIN(COMM), AVG(COMM), MAX(COMM) FROM EMP WHERE COMM IS NOT NULL;

-- Commission moyenne de tous les employés, en considérant que les NULL sont des 0.0
SELECT AVG(COALESCE(COMM, 0.0)) FROM EMP;

-- Nom et commission de tous les employés en euros (1€ = 1.2$)
SELECT ENAME, COALESCE(COMM, 0.0) / 1.2 AS COMM_EURO FROM EMP;

-- Nom et salaire total (salaire + commission) de tous les employés, en considérant que les NULL sont des 0.0
SELECT ENAME, SAL + COALESCE(COMM, 0.0) AS SAL_TOTAL FROM EMP;

-- Nom des plus hauts responsables de l'entreprise (ceux qui n'ont pas de supérieur hiérarchique)
SELECT ENAME FROM EMP WHERE MGR IS NULL;

-- Employes dont la commission est inférieure à 25% de leur salaire (avec et sans NULL)
SELECT * FROM EMP WHERE COMM < 0.25 * SAL;
SELECT * FROM EMP WHERE COMM IS NOT NULL AND COMM < 0.25 * SAL;