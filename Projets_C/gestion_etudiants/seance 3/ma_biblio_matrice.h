#include <stdio.h>
//ANDRE Florian
//2B DIA
int mmax,nmax,n,m,s;
int M[10][10];
//----------------------------------
// Procedure saisie nombre lignes
//----------------------------------
int saisir_nb_lignes( )
{
    do{
        printf("\nSaisir le nombre de lignes de la matrice entre 1 et 10: ");
        scanf("%d",&m);
    }while(m<=0 || m>10);
    return(m);
}
//----------------------------------
// Procedure saisie nombre colonnes
//----------------------------------
int saisir_nb_colonnes( )
{
    do{
        printf("\nSaisir le nombre de colonnes de la matrice entre 1 et 10: ");
        scanf("%d",&n);
    }while(n<=0 || n>10);
    return(n);
}
//----------------------------------
// Procedure saisie matrice
//----------------------------------
void saisir_matrice(int M[10][10],int n,int m){
int i,j;
    for(i=0; i<n; i++){
        for (j=0;j<m;j++){

        printf("\nEntrer une valeur dans la ligne %d et colone %d :",i,j);
        scanf("%d",&M[i][j]);
        }
    }
}
//----------------------------------
// Procedure afficher matrice
//----------------------------------
void afficher_matrice(int M[10][10],int n,int m){
int i,j;
    for(i=0; i<n; i++)
        {
        for (j=0;j<m;j++)
        {
            printf("\t%d",M[i][j]);


        }
        printf("\n");
    }

}

// Fonction somme des elements de la matrice
//----------------------------------

int somme_elements_matrice(int M[10][10],int m, int n )
{  int s,i,j ;
    s=0;
    for(i=0; i<m; i=i+1){
        for(j=0;j<n;j++){
            s+=M[i][j];
        }
    }
     return(s);
}

// Fonction produit des elements de la matrice
//----------------------------------
int produit_elements_matrice(int M[10][10],int m,int n)
{
    int p,i,j;
    p=1;
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            p=p*M[i][j];
        }
    }
    return(p);
}

//----------------------------------
    // Fonction moyenne
    //----------------------------------
    float moyenne( int M[10][10],int m, int n)
    {
        return((float)somme_elements_matrice(M,m,n)/((float)n*(float)m));
    }
    //----------------------------------
    // Fonction minimum
    //----------------------------------
    int minimum_matrice( int M[10][10],int m, int n )
    {  int mini,i,j ;
        mini = M[0][0];
        for(i=0; i<m; i++){
                for(j=0;j<n;j++){
                    if (M[i][j]<mini)
                    {
                        mini = M[i][j];
                    }
                }

            }

         return(mini);
    }
    //----------------------------------
    // Fonction position minimum
    //----------------------------------
    int pos_minimum_matrice( int M[10][10],int m, int n )
    {  int pos_mini,mini,i,j ;
        mini = M[0][0];
        pos_mini = 0;
        for(i=0; i<m; i++){
                for(j=0;j<n;j++){
                    if (M[i][j]<mini)
                    {
                        mini = M[i][j];
                        pos_mini = i,j;
                    }
                }

        }
         return(pos_mini);
    }
    //----------------------------------
    // Fonction maximum
    //----------------------------------
    int maximum_matrice( int M[10][10],int m, int n )
    {  int maxi,i,j ;
        maxi = M[0][0];
        for(i=0; i<m; i++){
                for(j=0;j<n;j++){
                    if (M[i][j]>maxi)
                    {
                        maxi = M[i][j];
                    }
                }

            }

         return(maxi);
    }
    //----------------------------------
    // Fonction position maximum
    //----------------------------------
    int pos_maximum_matrice( int M[10][10],int m, int n )
    {  int pos_maxi,maxi,i,j ;
        maxi = M[0][0];
        pos_maxi = 0;
        for(i=0; i<m; i++){
                for(j=0;j<n;j++){
                    if (M[i][j]>maxi)
                    {
                        maxi = M[i][j];
                        pos_maxi = i,j;
                    }
                }

        }
         return(pos_maxi);
    }
// Fonction somme de 2 matrices
//----------------------------------
    int somme_matrice(int M1[10][10],int m,int n)
    {
        int i,j;
        int M2[10][10];
        int M3[10][10];
        printf("\n Entrez la 2eme matrice : \n");
        for(i=0; i<n; i++){
            for (j=0;j<m;j++){

            printf("\nEntrer une valeur dans la ligne %d et colone %d pour la 2eme matrice :",i,j);
            scanf("%d",&M2[i][j]);
            }
        }
        printf("\n Matrice apres l'addition : \n");
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                M3[i][j]=M1[i][j]+M2[i][j];
                printf("%d\t",M3[i][j]);
            }
            printf("\n");
        }
        return 0;
    }

// Fonction produit de 2 matrices
//----------------------------------
    int produit_matrice(int M1[10][10],int m,int n)
    {
        int i,j;
        int M2[10][10];
        int M3[10][10];
        printf("\n Entrez la 2eme matrice : \n");
        for(i=0; i<n; i++){
            for (j=0;j<m;j++){

            printf("\nEntrer une valeur dans la ligne %d et colone %d pour la 2eme matrice :",i,j);
            scanf("%d",&M2[i][j]);
            }
        }
        printf("\n Matrice apres la multiplication : \n");
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                M3[i][j]+=M1[i][j]*M2[j][i];
                printf("%d\t",M3[i][j]);
            }
            printf("\n");
        }
        return 0;
    }
