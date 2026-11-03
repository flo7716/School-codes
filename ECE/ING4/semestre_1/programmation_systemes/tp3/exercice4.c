#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>

/*0*/ 
void handler_chld(int sig) {
    // Récupère tous les fils terminés sans bloquer
    while (waitpid(-1, NULL, WNOHANG) > 0);
}

int main(int argc, char *argv[])
{
    /*1*/
    struct sigaction sa;
    sa.sa_handler = handler_chld;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = SA_RESTART;
    sigaction(SIGCHLD, &sa, NULL);

    if (!fork())
    {
        /*2*/
        // Code du fils
        for (int i=0; i<10; i++){
           printf("Fils : %d\n", i); 
        }; // simule un petit calcul[cite: 3]
        /*3*/
        exit(1);
    }
    /*4*/
    
    /*5*/
    while(1) {
        sleep(1); // Simule un calcul infini sans surcharger le CPU
    } 
    /*6*/
    
    return 0;
}