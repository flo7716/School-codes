#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

#define NMAX 3

int cpt_int = 0;
int cpt_quit = 0;

void handler_signaux(int sig) {
    if (sig == SIGINT) {
        cpt_int++;
        printf("\nSignal SIGINT reçu (%d/%d)\n", cpt_int, NMAX);
    } else if (sig == SIGQUIT) {
        cpt_quit++;
        printf("\nSignal SIGQUIT reçu (%d/%d)\n", cpt_quit, NMAX);
    }

    if (cpt_int >= NMAX || cpt_quit >= NMAX) {
        printf("Seuil NMAX atteint. Arrêt du programme.\n");
        exit(0);
    }
}

int main() {
    struct sigaction action;
    action.sa_handler = handler_signaux;
    sigemptyset(&action.sa_mask);
    action.sa_flags = 0;

    sigaction(SIGINT, &action, NULL);
    sigaction(SIGQUIT, &action, NULL);

    printf("En attente de signaux (SIGINT ou SIGQUIT)... PID = %d\n", getpid());
    while(1) {
        pause();
    }
    return 0;
}