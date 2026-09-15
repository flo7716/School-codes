#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(void){
    pid_t pid;
    int a = 20;
    switch(pid = fork()){
        case -1:
            perror("fork failed");
            exit(EXIT_FAILURE);
        case 0:
            a += 10;
            printf("Child process: a = %d\n", a);
            break;
        default:
            a -= 5;
            printf("Parent process: a = %d\n", a);
            break;
    }
    printf("Fin du processus %d avec a = %d\n", getpid(), a);
    return 0;
}