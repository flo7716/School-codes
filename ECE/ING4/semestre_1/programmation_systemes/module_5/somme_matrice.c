#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>

#define N 4 // Taille des matrices
#define M 10 // Nb maximum

pthread_t tid[N]; // Vecteurs threads

int A[N][N], B[N][N]; // Matrices
int C[N][N]; // C = A + B
int fila; // La file des 2 matrices

void imprime(int matrice[N][N])
{
    int j, k;
    for(j = 0; j < N; j++)
    {
        printf("\n");
        for(k = 0; k < N; k++)
            printf("%d \t", matrice[j][k]);
    }
}

void* somme_vectorielle(void *arg)
{
    int f, k;
    f = (int)arg;
    printf("Somme de file %d\n", f);
    for(k = 0; k < N; k++)
        C[f][k] = A[f][k] + B[f][k];
    pthread_exit(NULL);
}

int main(void)
{
    int j, k, semilla;
    // Generation des matrices semilla = time(NULL);
    srand(semilla);
    for(j = 0; j < N; j++)
        for(k = 0; k < N; k++)
        {
            A[j][k] = rand() % M; // aleatoire @ M
            B[j][k] = rand() % M; 
        }
    for(j = 0; j < N; j++)
    {
        printf("Thread file%d\n", j);
        pthread_create(&tid[j], NULL, somme_vectorielle, (void*)j);
    }
    for(j = 0; j < N; j++)
    {
        printf("Attendre thread%d\n", j);
        pthread_join(tid[j], NULL);
    }
    printf("\n\nMatrice A ");
    imprime(A);
    printf("\n\nMatrice B ");
    imprime(B);
    printf("\n\nMatrice C=A+B");
    imprime(C);
    return 0;
}