#include <iostream>
#include "ma_biblio_matrice.h"

using namespace std;
int main() {
    int M[10][10];
    int n, m;
    m = saisir_nb_lignes();
    n = saisir_nb_colonnes();
    saisir_matrice(M, m, n);
    cout << "\n La somme des elements de la matrice M est : " << somme_elements_matrice(M, m, n);
    cout << "\n Le produit des elements de la matrice M est : " << produit_elements_matrice(M, m, n);
    cout << "\n la moyenne des elements de la matrice M est : " << moyenne(M, m, n);
    cout << "\n le plus petit element de la matrice M est : " << minimum_matrice(M, m, n) << " .\n Il est situe en " << pos_minimum_matrice(M, m, n);
    cout << "\n le plus grand element de la matrice M est : " << maximum_matrice(M, m, n) << " .\n Il est situe en " << pos_maximum_matrice(M, m, n);
    somme_matrice(M, m, n);
    produit_matrice(M, m, n);

    return 0;
}