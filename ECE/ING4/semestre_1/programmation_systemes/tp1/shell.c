#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>


/*
Write a program that displays the following menu in a loop :
1- run a program
2- kill a process (hint : lookup the kill
manual)
3- list the files in the current folder (hint :
lookup the ls manual)
4- quit
Use the «mySystem » function to implement the
different options of your menu (except for quit of
course).

*/

int mySystem(const char *command) {
    pid_t pid = fork();
    if (pid < 0) {
        perror("fork");
        return -1;
    }
    if (pid == 0) {
        // Child process
        execl("/bin/sh", "sh", "-c", command, (char *)NULL);
        perror("execl");
        exit(EXIT_FAILURE);
    } else {
        // Parent process
        int status;
        waitpid(pid, &status, 0);
        return status;
    }
}

int main() {
    int choice;
    char command[256];

    while (1) {
        printf("Menu:\n");
        printf("1- Run a program\n");
        printf("2- Kill a process\n");
        printf("3- List the files in the current folder\n");
        printf("4- Quit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter the command to run: ");
                scanf("%s", command);
                mySystem(command);
                break;
            case 2:
                printf("Enter the PID of the process to kill: ");
                int pid;
                scanf("%d", &pid);
                if (kill(pid, SIGKILL) == -1) {
                    perror("kill");
                } else {
                    printf("Process %d killed successfully.\n", pid);
                }
                break;
            case 3:
                mySystem("ls");
                break;
            case 4:
                exit(0);
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}