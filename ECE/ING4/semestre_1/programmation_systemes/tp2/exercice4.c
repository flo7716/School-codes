#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
/* Chasse aux zombies : ’appel waitpid(-1, NULL, WNOHANG) renvoie -1
en cas d’erreur. Si il n’y a pas de fils zombie il renvoie immédiatement 0 (l’appel
est non bloquant) et sinon un fils zombie est choisi, toutes ses ressources sont
libérés et son pid est renvoyé. En déduire (et expérimenter) une maniére pour
un processus de se débarrasser de tous les zombies qu’il a créé. */

int main() {
    pid_t pid;
    int i;

    // Création de 5 processus fils
    for (i = 0; i < 5; i++) {
        pid = fork();
        if (pid < 0) {
            perror("Erreur fork");
            exit(1);
        } else if (pid == 0) {
            // Fils : termine immédiatement pour devenir un zombie
            printf("Fils %d (PID = %d) : Je vais devenir un zombie.\n", i + 1, getpid());
            exit(0);
        }
    }

    // Le père attend un moment pour que les fils deviennent zombies
    sleep(2);

    // Le père se débarrasse de tous les zombies qu'il a créés
    printf("Père (PID = %d) : Je vais me débarrasser des zombies.\n", getpid());
    while ((pid = waitpid(-1, NULL, WNOHANG)) > 0) {
        printf("Père : J'ai récupéré le fils zombie avec PID = %d\n", pid);
    }

    if (pid == -1) {
        perror("Erreur waitpid");
        exit(1);
    }

    printf("Père : Tous les zombies ont été récupérés.\n");

    return 0;
}