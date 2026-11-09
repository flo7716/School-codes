#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int n, m, p;
int **A, **B, **C;

typedef struct
{
    int i;
    int j;
} Parametre;

void *calcul(void *arg)
{
    Parametre *param = (Parametre *)arg;

    int i = param->i;
    int j = param->j;

    C[i][j] = 0;

    for (int k = 0; k < m; k++)
    {
        C[i][j] += A[i][k] * B[k][j];
    }

    return NULL;
}

int main()
{
    printf("Dimensions de A (n m) : ");
    scanf("%d %d", &n, &m);

    printf("Nombre de colonnes de B (p) : ");
    scanf("%d", &p);

    A = malloc(n * sizeof(int *));
    B = malloc(m * sizeof(int *));
    C = malloc(n * sizeof(int *));

    for (int i = 0; i < n; i++)
        A[i] = malloc(m * sizeof(int));

    for (int i = 0; i < m; i++)
        B[i] = malloc(p * sizeof(int));

    for (int i = 0; i < n; i++)
        C[i] = malloc(p * sizeof(int));

    printf("Saisie de la matrice A :\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            scanf("%d", &A[i][j]);

    printf("Saisie de la matrice B :\n");
    for (int i = 0; i < m; i++)
        for (int j = 0; j < p; j++)
            scanf("%d", &B[i][j]);

    pthread_t threads[n][p];
    Parametre params[n][p];

    // Création d'un thread pour chaque élément C[i][j]
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < p; j++)
        {
            params[i][j].i = i;
            params[i][j].j = j;

            pthread_create(&threads[i][j], NULL,
                           calcul, &params[i][j]);
        }
    }

    // Attente de tous les threads
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < p; j++)
        {
            pthread_join(threads[i][j], NULL);
        }
    }

    printf("Matrice résultat C :\n");

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < p; j++)
            printf("%d ", C[i][j]);

        printf("\n");
    }

    return 0;
}
