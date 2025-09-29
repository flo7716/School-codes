#include <stdio.h>
#include <stdlib.h>
int main()
{     //declaration des variables
    int x,i,a;
    printf("Florian ANDRE, Bachelor 2 DIA");
    printf("\n BIn211");
     printf("\n---------------------------------------------");
        printf("\n  Exercice 3 : Table de Multiplication " );
        printf("\n---------------------------------------------");
    do{
        do{

            printf("\nSaisissez un entier entre 1 et 10 svp: ");
            scanf("%d",&x);
            system("CLS");

        }while(1>x||x>10);


        printf("\n---------------------------------------------");
        printf("\nTable de multiplication de %d ",x);
        printf("\n---------------------------------------------");
        for (i=1;i<=10;i++)
        {

            printf("\n%d * %d = %d",x,i,x*i);
        }
        printf("\n---------------------------------------------");
        do{
            printf(" \n Voulez vous recommencer ( oui : 1 / non : 0 )  : ");
            scanf("%d",&a);
        }while ( a !=0 && a !=1);
    }while(a!=0);
system("CLS");
printf("\n Merci et au revoir " );
return 0;
}
