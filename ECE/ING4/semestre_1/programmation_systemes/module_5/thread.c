#include <pthread.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

void afficher(int n, char lettre){
    int i,j;
    for(j=1; j<n; j++){
        for(i=1; i<10000000; i++);
        printf("%c", lettre);
        fflush(stdout);
    }
}

void *threadA(void *inutilise){
    afficher(100, 'A');
    printf("\n Fin du thread A\n");
    fflush(stdout);
    pthread_exit(NULL);
}

void *threadC(void *inutilise){
    afficher(150, 'C');
    printf("\n Fin du thread C\n");
    fflush(stdout);
    pthread_exit(NULL);
}

void *threadB(void *inutilise){
    pthread_t thC;
    pthread_create(&thC, NULL, threadC, NULL);
    afficher(100, 'B');
    printf("\n Le thread B attend la fin du thread C\n");
    pthread_join(thC, NULL);
    printf("\n Fin du thread B\n");
    fflush(stdout);
    pthread_exit(NULL);
}

int main(){
    int i;
    pthread_t thA, thB;
    printf("Creation du thread A\n");
    pthread_create(&thA, NULL, threadA, NULL);
    printf("Creation du thread B\n");
    pthread_create(&thB, NULL, threadB, NULL);
    sleep(1);
    printf("Le thread principal attend la fin du thread A\n");
    pthread_join(thA, NULL);
    printf("Le thread principal attend la fin du thread B\n");
    pthread_join(thB, NULL);
    printf("Fin du programme principal\n");
    exit(0);
}