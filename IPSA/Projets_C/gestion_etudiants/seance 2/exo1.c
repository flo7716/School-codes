#include <stdio.h>
#include <math.h>
#include <complex.h>
int main()
{
    //Declaration des variables

    float a,b,c;
    float delta,x1,x2;
    printf("Florian ANDRE, Bachelor 2 DIA");
     printf("\n BIn211");
     printf("\n---------------------------------------------");
        printf("\n  Exercice 1 : Equation du 2nd degre " );
        printf("\n---------------------------------------------");
    //Mon programme
    printf("\na :");
    scanf("%f",&a);
    printf("\nb :");
    scanf("%f",&b);
    printf("\nc :");
    scanf("%f",&c);
    if(a==0)
    {
        printf("\nVotre equation n'est pas de degre 2");
    }
    else
    {
        delta = pow(b,2)-4*a*c;
        if(delta==0)
        {
            x1=-b/(2*a);
            printf("\n1 seule racine x1=%f",x1);
        }
        if(delta>0)
        {
            x1=(-b-sqrt(delta))/(2*a);
            x2=(-b+sqrt(delta))/(2*a);
            printf("\n2 racines reelles x1= %f et x2= %f",x1,x2);
        }
        if(delta<0)
        {
            x1=b/(2*a); //partie reelle
            x2=sqrt(-delta)/(2*a); //partie imaginaire pure
            printf("\n2 racines complexes conjuguees z1= %f - %fi et z2= %f + %fi",x1,x2);
        }
    }
    return 0;
}
