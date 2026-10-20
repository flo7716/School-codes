#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(){
    fork() || (fork() && fork());
    exit(EXIT_SUCCESS);
}