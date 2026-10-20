--le produit cartésien des tables EMP et DEPT, (b) le THETA-JOIN de EMP et DEPT sur DID, et (c) le NATURAL JOIN de EMP et DEPT.

SELECT * FROM EMP, DEPT;
SELECT * FROM EMP JOIN DEPT ON EMP.DID = DEPT.DID;
SELECT * FROM EMP NATURAL JOIN DEPT;


-- nom et departement des employés travaillant à New York (par jointure naturelle)
SELECT ENAME, DNAME FROM EMP NATURAL JOIN DEPT WHERE DLOC = 'NEW-YORK';

-- nom et département des employés effectuant une mission dans la ville où ils travaillent (par jointure naturelle)
SELECT ENAME FROM EMP NATURAL JOIN DEPT NATURAL JOIN MISSION WHERE DLOC = MLOC;

-- nom des employes et nom de leur manager (par jointure naturelle)
SELECT E1.ENAME AS EMPLOYE, E2.ENAME AS MANAGER FROM EMP E1 LEFT JOIN EMP E2 ON E1.MGR = E2.EID;

-- nom des employés qui ont le même manager qu'Allen
SELECT E1.ENAME AS EMPLOYE, E2.ENAME AS MANAGER FROM EMP E1 LEFT JOIN EMP E2 ON E1.MGR = E2.EID WHERE E2.ENAME = 'ALLEN';

-- nom et date d'embauche des employes embauches avant leur manager (date d'embauche plus ancienne que celle de leur manager)
SELECT E1.ENAME AS EMPLOYE, E1.HIRED AS DATE_EMBAUCHE, E2.ENAME AS MANAGER, E2.HIRED AS DATE_EMBAUCHE_MANAGER FROM EMP E1 LEFT JOIN EMP E2 ON E1.MGR = E2.EID WHERE E1.HIRED < E2.HIRED;

-- nom des employes du departement Sales embauches le meme jour qu'un employe du departement Research
SELECT E1.ENAME AS EMPLOYE_SALES, E1.HIRED AS DATE_EMBAUCHE, E2.ENAME AS EMPLOYE_RESEARCH, E2.HIRED AS DATE_EMBAUCHE_RESEARCH FROM EMP E1 LEFT JOIN EMP E2 ON E1.HIRED = E2.HIRED WHERE E1.DID = 30 AND E2.DID = 20;

-- departements sans employes
SELECT DNAME FROM DEPT LEFT JOIN EMP ON DEPT.DID = EMP.DID WHERE EMP.EID IS NULL;

-- nom des employes avec le salaire le plus eleve de chaque departement (par jointure naturelle)
SELECT E1.ENAME, E1.SAL, E1.DID FROM EMP E1 LEFT JOIN EMP E2 ON E1.DID = E2.DID AND E1.SAL < E2.SAL WHERE E2.EID IS NULL;

-- nom des employes embauches avant tous les employes du departement Sales (par jointure naturelle)
SELECT E1.ENAME, E1.HIRED FROM EMP E1 LEFT JOIN EMP E2 ON E1.HIRED > E2.HIRED AND E2.DID = 30 WHERE E2.EID IS NULL;
