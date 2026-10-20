#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    // 1. Vérification du paramètre n en ligne de commande
    if (argc != 2) {
        fprintf(stderr, "Usage : %s <nombre_de_processus_n>\n", argv[0]);
        exit(1);
    }

    int n = atoi(argv[1]);
    if (n <= 0) {
        fprintf(stderr, "Erreur : n doit être un entier strictement positif.\n");
        exit(1);
    }

    // 2. Boucle de création des n processus fils
    for (int i = 0; i < n; i++) {
        pid_t pid = fork();

        if (pid < 0) {
            perror("Erreur lors de l'appel système fork");
            exit(1);
        } else if (pid == 0) {
            // Code exécuté par le processus fils
            printf("Je suis le processus fils n°%d (PID = %d, PPID = %d)\n", i + 1, getpid(), getppid());
            exit(0); // Terminaison immédiate du fils pour éviter qu'il ne crée à son tour des processus
        }
    }

    // 3. Le processus père attend la fin de l'exécution de tous ses fils
    for (int i = 0; i < n; i++) {
        wait(NULL);
    }

    printf("Le processus père (PID = %d) a engendré et attendu ses %d fils avec succès.\n", getpid(), n);

    return 0;
}