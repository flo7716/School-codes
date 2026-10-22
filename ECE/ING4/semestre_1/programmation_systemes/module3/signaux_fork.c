#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>

void trait_sigint (){ 
    printf("bien recu SIGINT, mais je vais l’ignorer\n"); 
}
void trait_sigquit (){ 
    printf("bien recu SIGQUIT, mais je vais l’ignorer\n");
}

int main(){
    int pid;
    pid = fork();
    if (pid==0){
        signal (SIGINT , trait_sigint );
        signal (SIGQUIT, trait_sigquit );
        printf("je suis toujours en vie\n"); sleep (20);
        printf("premier reveil du fils\n"); sleep (120);
        printf("second reveil du fils\n"); sleep (500);
        printf("troisieme reveil du fils\n");
        }
    else{
        sleep (1);
        kill(pid, SIGINT);
        sleep (2);
        kill (pid , SIGQUIT);
        sleep (5);
        kill (pid,SIGKILL);
        };
    return 0 ;
}