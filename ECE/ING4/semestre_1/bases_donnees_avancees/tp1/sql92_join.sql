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