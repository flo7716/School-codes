#include <stdio.h>
#include <G:\Mon Drive\IPSA\Bachelor 2\semestre 1\C\seance 3\ma_biblio_matrice.h>
//ANDRE Florian
//2B DIA
int mmax,nmax,n,m,s;
int M[10][10];

main(){
int M[10][10];
int n,m;
m=saisir_nb_lignes();
n=saisir_nb_colonnes();
saisir_matrice(M,m,n);
printf("\n La somme des elements de la matrice M est : %d",somme_elements_matrice(M,m,n));
printf("\n Le produit des elements de la matrice M est : %d",produit_elements_matrice(M,m,n));
printf("\n la moyenne des elements de la matrice M est : %d",moyenne(M,m,n));
printf("\n le plus petit element de la matrice M est : %d .\n Il est situe en %d",minimum_matrice(M,m,n),pos_minimum_matrice(M,m,n));
printf("\n le plus grand element de la matrice M est : %d .\n Il est situe en %d",maximum_matrice(M,m,n),pos_maximum_matrice(M,m,n));
somme_matrice(M,m,n);
produit_matrice(M,m,n);
}

