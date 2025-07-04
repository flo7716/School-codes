#include <stdio.h>
#include <math.h>
#define nmax 50


//----------------------------------
// Procedure exo2 complete
// Florian ANDRE
// 2B DIA
//----------------------------------
//------------------------------
// Fonctions utilitaires tableau
//------------------------------
int produit_tableau( int t[nmax], int n )
{  
    int p,i ;
    p =1;
    for(i=0; i<n; i=i+1){
        p = p*t[i];
    }
    return(p);
}
//----------------------------------
// Fonction somme
//----------------------------------
int somme_tableau( int t[nmax], int n )
{  
    int s,i ;
    s=0;
    for(i=0; i<n; i=i+1){
        s+=t[i];
    }
    return(s);
}
//----------------------------------
// Fonction moyenne
//----------------------------------
float moyenne( int t[nmax], int n)
{
    return((float)somme_tableau(t,n)/(float)n);
}
//----------------------------------
// Fonction minimum
//----------------------------------
int minimum_tableau( int t[nmax], int n )
{  
    int mini,i ;
    mini = t[0];
    for(i=0; i<n; i++){
        if (t[i]<mini)
        {
            mini = t[i];
        }
    }
    return(mini);
}
//----------------------------------
// Fonction position minimum
//----------------------------------
int pos_minimum_tableau( int t[nmax], int n )
{  
    int pos_mini,mini,i ;
    mini = t[0];
    pos_mini = 0;
    for(i=0; i<n; i++){
        if (t[i]<mini)
        {
            mini = t[i];
            pos_mini = i;
        }
    }
    return(pos_mini);
}
//----------------------------------
// Fonction maximum
//----------------------------------
int maximum_tableau( int t[nmax], int n )
{  
    int m,i ;
    m = t[0];
    for(i=0; i<n; i++){
        if (t[i]>m)
        {
            m = t[i];
        }
    }
    return(m);
}
//----------------------------------
// Fonction position maximum
//----------------------------------
int pos_maximum_tableau( int t[nmax], int n )
{  
    int pos_m,m,i ;
    m = t[0];
    pos_m = 0;
    for(i=0; i<n; i++){
        if (t[i]>m)
        {
            m = t[i];
            pos_m = i;
        }
    }
    return(pos_m);
}
//----------------------------------
// Fonction dimension
//----------------------------------
int dimension_tableau( )
{
    int n;
    do{
        printf("\nSaisir la dimension du tableau entre 1 et 20: ");
        scanf("%d",&n);
    }while(n<=0 || n>20);
    return(n);
}
//----------------------------------
// Procedure saisie tableau
//----------------------------------
void saisir_tableau(int t[nmax],int n)
{
    int i;
    for(i=0; i<n; i++)
    {
        printf("\nEntrer une valeur dans la case %d :",i);
        scanf("%d",&t[i]);
    }
}
//----------------------------------
// Procedure afficher tableau
//----------------------------------
void afficher_tableau(int t[nmax],int n)
{
    int i;
    printf("\n t : ");
    for(i=0; i<n; i++)
    {
        printf("\t %d",t[i]);
    }
}

//----------------------------------
// Procedure exo2 complete
// Florian ANDRE
// 2B DIA
//----------------------------------
void exo2()
{
    int x,i,a,t1[nmax],S,P,min,max,indmin,indmax;
    float M;

    printf("Florian ANDRE, Bachelor 2 DIA");
    printf("\n BIn211");
    printf("\n---------------------------------------------");
    printf("\n  Exercice 5 : Tableau avec somme, produit, moyenne, minimum, maximum " );
    printf("\n---------------------------------------------");
    do{
        //-------------------------------
        // Saisir la dimension du tableau t1
        //-------------------------------
        x=dimension_tableau();
        printf("\n Dimension : %d \n",x);

        //-------------------------------
        // Saisir les valeurs du tableau
        //-------------------------------
        saisir_tableau(t1,x);
        //-------------------------------
        // Afficher les valeurs du tableau
        //-------------------------------
        afficher_tableau(t1,x);

        //Somme des elements du tableau
        S=somme_tableau(t1, x);

        printf("\n La somme des elements du tableau est egale a %d",S);

        //Produit des elements du tableau
        P=produit_tableau(t1, x);
        printf("\n Le produit des elements du tableau est egale a %d",P);

        //Moyenne des elements du tableau

        M=moyenne(t1,x);
        printf("\n La moyenne des elements du tableau est egale a %f",M);

        //Minimum,maximum et emplacements
        min=minimum_tableau(t1,x);
        indmin=pos_minimum_tableau(t1,x);

        printf("\n La valeur minimum est %d en case %d",min,indmin);

        max=maximum_tableau(t1,x);
        indmax=pos_maximum_tableau(t1,x);
        printf("\n La valeur maximum est %d en case %d",max,indmax);
        printf("\n---------------------------------------------");

        do{
            printf(" \n Voulez vous recommencer ( oui : 1 / non : 0 )  : ");
            scanf("%d",&a);
        }while ( a !=0 && a !=1);

    }while(a!=0);
    system("CLS");
    printf("\n Merci et au revoir " );
}

