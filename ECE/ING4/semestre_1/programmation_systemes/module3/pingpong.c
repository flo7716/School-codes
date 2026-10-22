#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>


/*le code simule un ping-pong entre deux processus (1 pere et 1 fils)*/


int main(){
    int pid;
    pid = fork();
    if (pid==0){
        while(1){
            printf("fils : ping\n");
            sleep(1);
        }
    }
    else{
        while(1){
            printf("pere : pong\n");
            sleep(1);
        }
    };
    return 0 ;
}