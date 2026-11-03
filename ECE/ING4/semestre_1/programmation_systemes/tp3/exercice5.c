#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include<stdio.h>
#include <signal.h>
#define N 5
/*0*/
int main( )
{
    pid_t pid[N];
    int i ;
    /*1*/
    for ( i=0; i<N;i++)
        if ((pid[i]=fork())==0)
        { /*2*/
            while(1)
            printf("ici fils %d ", i);
        }
    /*3*/
}