#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid1, pid2;

    // 1. Création du premier fils pour afficher de 1 à 50
    pid1 = fork();
    if (pid1 < 0) {
        perror("Erreur fork");
        exit(1);
    } else if (pid1 == 0) {
        for (int i = 1; i <= 50; i++) {
            printf("%d ", i);
        }
        fflush(stdout); // Vide le tampon pour forcer l'affichage immédiat
        exit(0);
    }

    // Le père attend impérativement que le premier fils ait terminé son affichage
    wait(NULL);

    // 2. Création du deuxième fils pour afficher de 51 à 100
    pid2 = fork();
    if (pid2 < 0) {
        perror("Erreur fork");
        exit(1);
    } else if (pid2 == 0) {
        for (int i = 51; i <= 100; i++) {
            printf("%d ", i);
        }
        fflush(stdout);
        exit(0);
    }

    // Le père attend la fin du deuxième fils
    wait(NULL);
    printf("\n"); // Pour un affichage propre après les nombres
    printf("Fin du programme\n");

    return 0;
}