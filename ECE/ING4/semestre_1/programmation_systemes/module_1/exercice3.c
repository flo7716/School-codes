#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(){
    int i, n=5;
    int childpid;
    for(i=0; i<n; i++){
        if((childpid = fork()) <= 0){
            break;
        }
        printf("Parent process %d created child process %d\n", getpid(), childpid);
    }
    return 0;
}

