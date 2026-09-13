#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main() {
    // display the process ID of the current process
    // simply use any exec call to replace the current process with a new one
    printf("Current process ID: %d\n", getpid());
    // Example exec call (uncomment to use):
    // execl("/bin/ls", "ls", NULL);
    return 0;
}