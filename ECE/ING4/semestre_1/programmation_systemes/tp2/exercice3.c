#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/* Création de 3 processus. un programme qui engendre trois fils. Un fils rentrera dans 
l’état zombie et puis deviendra orphelin. Un deuxième fils deviendra orphelin
avant rentrer dans l’état zombie. Un troisième fils deviendra zombie et il ne
sera jamais orphelin. */

int main() {
    pid_t pid;

    // Création du 1er fils
    pid = fork();
    if (pid < 0){
        perror("Erreur fork");
        exit(1);
    } else if (pid == 0) {
        // Fils 1 : devient zombie après avoir terminé
        printf("Fils 1 (PID = %d) : Je vais devenir un zombie.\n", getpid());
        exit(0); // Terminaison immédiate pour devenir zombie
    }

    // Création du 2ème fils
    pid = fork();
    if (pid < 0){
        perror("Erreur fork");
        exit(1);
    } else if (pid == 0) {
        // Fils 2 : devient orphelin avant de devenir zombie
        printf("Fils 2 (PID = %d) : Je vais devenir orphelin.\n", getpid());
        exit(0);
    }

    // Création du 3ème fils
    pid = fork();
    if (pid < 0){
        perror("Erreur fork");
        exit(1);
    } else if (pid == 0) {
        // Fils 3 : devient zombie et ne devient jamais orphelin
        printf("Fils 3 (PID = %d) : Je vais devenir un zombie.\n", getpid());
        exit(0);
    }

    return 0;
}