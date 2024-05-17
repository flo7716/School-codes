#include <stdio.h>

main()
{
    float x,y; //declaration des variables
    printf("donner x et y:"); //saisie des variables
    scanf("%f %f",&x,&y);
    printf("la somme de %f et %f est egal a %f\n",x,y,x+y); //somme de x et y
    printf("le produit de %f et %f est egal a %f",x,y,x*y); //produit de x et y
}
