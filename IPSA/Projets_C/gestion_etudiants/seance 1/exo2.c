#include <stdio.h>

int main()
{
    float x,y; //declaration des variables
    printf("donner x : "); //saisie des variables
    scanf("%f",&x);
    printf("donner y : ");
    scanf("%f",&y);
    printf("la somme de %f et %f est egal a %f\n",x,y,x+y); //somme de x et y
    printf("le produit de %f et %f est egal a %f",x,y,x*y); //produit de x et y
    return 0;
}
