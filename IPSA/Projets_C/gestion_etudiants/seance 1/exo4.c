#include <stdio.h>
#include <math.h>
#include <complex.h>
int main()
{
    //Declaration des variables
    float a,b,c;
    float delta,x1,x2;
    printf("-----------------------\n");
    printf("Exercice 4\n");
    printf("-----------------------\n");
    //Mon programme
    printf("a : ");
    scanf("%f",&a);
    printf("b : ");
    scanf("%f",&b);
    printf("c : ");
    scanf("%f",&c);
    if(a==0)
    {
        printf("Votre equation n'est pas de degre 2");
    }
    else
    {
        delta = pow(b,2)-4*a*c;
        if(delta==0)
        {
            x1=-b/(2*a);
            printf("1 seule racine x1=%f",x1);
        }
        if(delta>0)
        {
            x1=(-b-sqrt(delta))/(2*a);
            x2=(-b+sqrt(delta))/(2*a);
            printf("2 racines reelles x1= %f et x2= %f",x1,x2);
        }
        if(delta<0)
        {
            x1=b/(2*a); //partie reelle
            x2=sqrt(-delta)/(2*a); //partie imaginaire pure
            printf("2 racines complexes conjuguees z1= %f - %fi et z2= %f + %fi \n",x1,x2);
        }
    }
    return 0;
}
