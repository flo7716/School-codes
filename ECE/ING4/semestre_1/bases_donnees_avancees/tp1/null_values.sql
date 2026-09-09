-- NULL VALUES

-- Employes dont la commission est specifiee (meme 0.0)
SELECT * FROM EMP WHERE COMM IS NOT NULL;

-- nombre d'employes dont la commission est specifiee (meme 0.0), en 2 methodes
SELECT COUNT(*) FROM EMP WHERE COMM IS NOT NULL;
SELECT COUNT(COMM) FROM EMP WHERE COMM IS NOT NULL;

-- Nombre d'employes dont la commission n'est pas specifiee en 2 methodes
SELECT COUNT(*) FROM EMP WHERE COMM IS NULL;

