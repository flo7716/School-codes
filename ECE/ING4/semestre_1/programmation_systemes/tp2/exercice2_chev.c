#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid1, pid2;

    // Création du premier fils
    pid1 = fork();
    if (pid1 < 0) {
        perror("Erreur lors du premier fork");
        exit(1);
    } else if (pid1 == 0) {
        // Code du premier fils : affiche de 1 à 500
        for (int i = 1; i <= 500; i++) {
            printf("%d ", i);
        }
        exit(0);
    }

    // Création du deuxième fils
    pid2 = fork();
    if (pid2 < 0) {
        perror("Erreur lors du deuxième fils");
        exit(1);
    } else if (pid2 == 0) {
        // Code du deuxième fils : affiche de 501 à 1000
        for (int i = 501; i <= 1000; i++) {
            printf("%d ", i);
        }
        exit(0);
    }

    // Le père attend la fin des deux fils
    wait(NULL);
    wait(NULL);
    
    printf("\nFin du programme.\n");

    return 0;
}