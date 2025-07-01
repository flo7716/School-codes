#include "math.h"

/**
 * @brief Calcul de la factorielle d'un nombre de manière récursive.
 * 
 * @param n Le nombre entier non nul pour lequel calculer la factorielle.
 * @return La factorielle de n.
 * 
 * Définition récursive de factorielle :
 * - 0! = 1
 * - Pour tout entier n > 0, n! = (n – 1)! × n
 */
int fact(int n) {
    if (n == 0)
        return 1;
    else
        return n * fact(n - 1);
}

/**
 * @brief Calcul du nombre d'arrangements de k éléments parmi n éléments.
 * 
 * @param k Le nombre entier d'éléments à arranger.
 * @param n Le nombre entier total d'éléments.
 * @return Le nombre d'arrangements.
 * 
 * Définition de l'arrangement :
 * - Ank = n! / (n-k)! pour k <= n et 0 pour k > n
 */
int arrangement(int k, int n) {
    if (k <= n)
        return fact(n) / fact(n - k);
    else
        return 0;
}
