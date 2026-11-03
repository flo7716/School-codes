#include <stdio.h>
#include <unistd.h> //sleep
#include <pthread.h> //pthread_create , pthread_join , pthread_exit

int glob=0;

void* increment(void *arg)
{
    int inc =2;
    sleep(10);
    glob+=inc ;
    printf("ici increment[%d], glob = %d\n",(int)pthread_self(), glob);
    pthread_exit(NULL) ;
}

void* decrement(void *arg)
{
    int dec=1;
    sleep (1);
    glob-=dec ;
    printf("ici decrement[%d], glob = %d\n", (int) pthread_self(), glob);
    pthread_exit(NULL) ;
}

int main()
{
    pthread_t tid1, tid2;
    printf("ici main[%d], glob = %d\n", (int) getpid(),glob);

    // cération d'un thread pour increment
    if (pthread_create(&tid1,NULL,increment,NULL)!=0)
        return 1;
    printf(" ici main : creation du thread[%d] avec succès\n", (int) tid1 );
    
    // cération d'un thread pour decrement
    if (pthread_create(&tid2, NULL, decrement, NULL)!=0)
        return 1;
    printf ( " ici main : creation du thread [%d] avec succès\n" , (int) tid2 );
    
    // attendre la fin des threads
    pthread_join ( tid1 ,NULL) ;
    pthread_join ( tid2 ,NULL) ;
    printf("ici main : fin des threads, glob=%d\n",glob);
    return 0 ;
}