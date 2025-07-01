//----------------------------------------------
//Florian ANDRE
//2B DIA
//BIn211 TP6
//----------------------------------------------
#include<stdio.h>
#include"bibliotp5.h"

main()
{
    int x,y,z;
    x=2;
    y=3;
    printf("\nAvant echange, x=%d et y=%d",x,y);

    echange(&x,&y);

    printf("\nApres echange, x=%d et y=%d",x,y);
}
