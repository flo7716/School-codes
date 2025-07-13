//----------------------------------------------
//Florian ANDRE
//2B DIA
//BIn211 TP7
//----------------------------------------------
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
    int *x;
    x=(int*)malloc(2*sizeof(int));
    *x=1;
    *(x+1)=2;
    printf("\nv1 = %d", *x);
    printf("\nv2 = %d", *(x+1));
    printf("\nA1 = %d",x);
    printf("\nA2 = %d",(x+1));
    scanf("\n%d",x);
    scanf("\n%d",(x+1));
    printf("\nv1 = %d", *x);
    printf("\nv2 = %d", *(x+1));
    printf("\nA1 = %d",x);
    printf("\nA2 = %d",x+1);
    exit(0);
}
