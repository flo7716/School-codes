#include <stdio.h>
#include <math.h>

int main()

{   //-------------------------------
    // Declaration des variables
    //-------------------------------
    int x,i,t1[21];
    printf("Florian ANDRE, Bachelor 2 DIA");
     printf("\n BIn211");
     printf("\n---------------------------------------------");
        printf("\n  Exercice 4 : Tableau " );
        printf("\n---------------------------------------------");
    //-------------------------------
    // Saisir la dimension du tableau t1
    //-------------------------------
    do{
        printf("\nSaisir la dimension du tableau entre 1 et 20: ");
        scanf("%d",&x);
    }while(x<=0 || x>20);
    //-------------------------------
    // Saisir les valeur du tableau
    //-------------------------------
    for(i=0; i<x; i=i+1)
    {
       printf("entrer une valeur dans la case %d :",i);
       scanf("%d",&t1[i]);
    }
    //-------------------------------
    // Afficher les valeur du tableau
    //-------------------------------
    printf(" \n tableau t1 : ");
    for(i=0; i<x; i=i+1)
    {
       printf(" %d ",t1[i]);

    }
return 0;

}
