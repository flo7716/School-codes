#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>

pthread_t pth_id [4] ;
int A[2][2]={{0, 1}, {2, 3}};
int B[2][2]={{4, 5}, {6, 7}};
int C[2][2];

/* Fonction pour la multiplication de deux matrices carres (2x2)*/
void* multipl_thr(void * i){
    int j ;
    printf("Thread numero = %d\n", (int)i);
    for(j=0;j<2;j++)
        C[(int)i/2][(int)i%2] = C[(int)i/2][(int)i%2] + A[(int)i/2][j]* B[j][(int)i%2];
    pthread_exit(0);
}

int main ( ) {
    int i,j ;
    void * statut = NULL;
    for(i=0; i<4; i++)
    {
        if(pthread_create(pth_id+i, 0 , (void*) &multipl_thr, (void*)i) == -1)
        {
            fprintf(stderr, "Erreur de creation du thread \n") ;
        }
    }
    printf("Join des thread crees \n");
    for(i=0;(i<4 && pthread_join(pth_id[i],NULL) == 0); i++);
    printf("Fin des thread \n");
    printf("Affichage de la matrice produit \n");
    for(i=0;i<2;i++)
    {
        for(j=0;j<2;j++)
            printf("%d ",C[i][j]);
        printf("\n");
    }
    return 0;
}