//----------------------------------------------
//Florian ANDRE
//2B DIA
//BIn211 TP6
//----------------------------------------------

//Exo 1


void echange(int *a,int *b)
{
    int z;
    printf("\n-------------------------");
    z=*a;
    *a=*b;
    *b=z;
    printf("\n-------------------------");
    printf("\nApres echange, x=%d et y=%d",*a,*b);
    printf("\n-------------------------");
}

//Exo 2

void min_max(int a,int b,int*maxi,int*mini)
{
    if(a<b)
    {
        *maxi=b;
        *mini=a;
    }
    else
    {
        *maxi=a;
        *mini=b;
    }
}

//Exo 3
void saisir_n(int*n)
{
    do
    {
        printf("\nDonnez n : ");
        scanf("%d",n);
    }while(*n<=0);
}

//Exo 4

