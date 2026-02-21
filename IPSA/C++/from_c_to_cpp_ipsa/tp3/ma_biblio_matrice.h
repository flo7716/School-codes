#include <iostream>

using namespace std;
int mmax, nmax, n, m, s;
int M[10][10];

//Procedure de saisie du nombre de lignes
int saisir_nb_lignes()
{    do
    {        cout << "\nSaisir le nombre de lignes de la matrice entre 1 et 10: ";
        cin >> m;
    } while (m <= 0 || m > 10);
    return m;
}


//Procedure de saisie du nombre de colonnes
int saisir_nb_colonnes()
{    do
    {        cout << "\nSaisir le nombre de colonnes de la matrice entre 1 et 10: ";
        cin >> n;
    } while (n <= 0 || n > 10);
    return n;
}

//Procedure de saisie de la matrice
void saisir_matrice(int M[10][10], int n, int m)
{    int i, j;
    for (i = 0; i < n; i++)
    {        for (j = 0; j < m; j++)
        {            cout << "\nEntrer une valeur dans la ligne " << i << " et colone " << j << " :";
            cin >> M[i][j];
        }
    }
}

//Procedure d'affichage de la matrice
void afficher_matrice(int M[10][10], int n, int m)
{    int i, j;
    for (i = 0; i < n; i++)
    {        for (j = 0; j < m; j++)
        {            cout << "\t" << M[i][j];
        }        cout << "\n";
    }
}

// Fonction somme des elements de la matrice
int somme_elements_matrice(int M[10][10], int m, int n)
{    int s, i, j;
    s = 0;
    for (i = 0; i < m; i++)
    {        for (j = 0; j < n; j++)
        {            s = s + M[i][j];
        }
    }
    return s;
}

// Fonction produit des elements de la matrice
int produit_elements_matrice(int M[10][10], int m, int n)
{    int p, i, j;
    p = 1;
    for (i = 0; i < m; i++)
    {        for (j = 0; j < n; j++)
        {            
            p = p * M[i][j];     
        }   }
    return p;

}

// Fonction moyenne des elements de la matrice
int moyenne(int M[10][10], int m, int n)
{    int moy;
    moy = somme_elements_matrice(M, m, n) / (m * n);
    return moy;
}   

// Fonction minimum
int minimum_matrice(int M[10][10], int m, int n)
{    int mini, i, j;
    mini = M[0][0];
    for (i = 0; i < m; i++)
    {        for (j = 0; j < n; j++)
        {            if (M[i][j] < mini)
            {                mini = M[i][j];
            }        }
    }
    return mini;
}

//----------------------------------
// Fonction position minimum

int pos_minimum_matrice(int M[10][10], int m, int n)
{    int pos_mini, mini, i, j;
    mini = M[0][0];
    pos_mini = 0;
    for (i = 0; i < m; i++)
    {        for (j = 0; j < n; j++)
        {            if (M[i][j] < mini)
            {                mini = M[i][j];
                pos_mini = i, j;
            }        }
    }
    return pos_mini;
}

//----------------------------------
// Fonction maximum
int maximum_matrice(int M[10][10], int m, int n)
{    int maxi, i, j;
    maxi = M[0][0];
    for (i = 0; i < m; i++)
    {        for (j = 0; j < n; j++)
        {            if (M[i][j] > maxi)
            {                maxi = M[i][j];
            }        }
    }
    return maxi;
}


//----------------------------------
// Fonction position maximum
int pos_maximum_matrice(int M[10][10], int m, int n)
{    int pos_maxi, maxi, i, j;
    maxi = M[0][0];
    pos_maxi = 0;
    for (i = 0; i < m; i++)
    {        for (j = 0; j < n; j++)
        {            if (M[i][j] > maxi)
            {                maxi = M[i][j];
                pos_maxi = i, j;
            }        }
    }
    return pos_maxi;
}   

// Fonction somme de 2 matrices
void somme_matrice(int M1[10][10], int M2[10][10], int M3[10][10], int m, int n)
{    int i, j;
    for (i = 0; i < m; i++)
    {        for (j = 0; j < n; j++)
        {            M3[i][j] = M1[i][j] + M2[i][j];
        }    }
}


// Fonction produit de 2 matrices
void produit_matrice(int M1[10][10], int M2[10][10], int M3[10][10], int m, int n)
{    int i, j, k;
    for (i = 0; i < m; i++)
    {        for (j = 0; j < n; j++)
        {            M3[i][j] = 0;
            for (k = 0; k < n; k++)
            {                M3[i][j] = M3[i][j] + M1[i][k] * M2[k][j];
            }        }
    }
}

