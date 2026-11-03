#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <signal.h>

void handler_fils(int sig) {
    printf("Fils : Signal %d reçu !\n", sig);
}

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        perror("Erreur fork");
        exit(1);
    }

    if (pid == 0) {
        // Code du fils
        struct sigaction sa;
        sa.sa_handler = handler_fils;
        sigemptyset(&sa.sa_mask);
        sa.sa_flags = 0;
        sigaction(SIGUSR1, &sa, NULL);

        while(1) { pause(); } // Attente d'un signal
    } else {
        // Code du père
        // Test de l'existence du fils (0 n'envoie pas de signal mais teste)[cite: 1, 2]
        if (kill(pid, 0) == 0) {
            printf("Père : Le fils de PID %d existe. Envoi du signal SIGUSR1...\n", pid);
            kill(pid, SIGUSR1);
        } else {
            printf("Père : Le fils n'existe pas.\n");
        }
        sleep(1); // Laisser le temps au fils de traiter le signal avant la fin du père
    }
    return 0;
}