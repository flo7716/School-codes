#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>


int main() {
    pid_t pid = fork();
    if (pid == 0){
        // Code exécuté par le processus enfant
        printf("Processus enfant : PID = %d\n", getpid());
    } else if (pid > 0) {
        // Code exécuté par le processus parent
        printf("Processus parent : PID = %d, PID de l'enfant = %d\n", getpid(), pid);
    } else {
        // Erreur lors de la création du processus
        fprintf(stderr, "Erreur lors de la création du processus.\n");
        return 1;
    }
    return 0;
}