#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main(void){
    int i = 5;
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork");
        return EXIT_FAILURE;
    }

    if (pid == 0){
         // I'm the child process
        printf("Je suis le fils, i = %d\n", i);
    }
    else{
        // I'm the parent process
        printf("Je suis le père, i = %d\n", i);
    }
    sleep(3);
    printf("Fin du processus, i = %d\n", i);

    return 0;
}


