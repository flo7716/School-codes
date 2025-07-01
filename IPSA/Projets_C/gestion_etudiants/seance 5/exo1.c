#include <stdio.h>
/*int a;

int annee_bissextile()
{
    printf("Saisissez une annee : ");
    scanf("%d",&a);
    if((a%4==0)&&(a%100!=0))||(a%400==0)
        printf("%d est une annee bissextile",a);
    else
        printf("%d n'est pas une annee bissextile",a);
}*/

main()
{ int a,m,j,a_bissextile,date_correcte ;

     printf("Saisissez une annee : ");
    scanf("%d",&a);
    if((a%4==0)&&(a%100!=0)||(a%400==0))
        {printf("%d est une annee bissextile",a);
        a_bissextile=1;
        }
    else
        {printf("%d n'est pas une annee bissextile",a);
        a_bissextile=0;
        }

    printf("\nSaisissez un mois : ");
    scanf("%d",&m);
    if(m<1||m>12)
        printf("%d est un numero de mois incorrect : ",m);
    else
        printf("%d est un numero de mois correct : ",m);

    printf("\nSaisissez un jour : ");
    scanf("%d",&j);
    if (m==2)
        {if (a_bissextile==1)
            if(j<1||j>29)
                date_correcte=0;
            else
                date_correcte=1;

        else
            if(j<1||j>28)
                date_correcte=0;
            else
                date_correcte=1;
        }
    if(m==1||m==3||m==5||m==7||m==8||m==10||m==12)
        {if(j<1||j>31)
                date_correcte=0;
        else
                date_correcte=1;
        }
    else
        if(j<1||j>30)
                date_correcte=0;
        else
                date_correcte=1;
    if (date_correcte==1)
        printf("\nDate correcte : %d/%d/%d",j,m,a);
    else
        printf("\nDate incorrecte : %d/%d/%d",j,m,a);
}
