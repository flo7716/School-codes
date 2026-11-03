#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>

char message[] = "Hola mundo";
void* thread_function ( void* arg )
{
    printf("La fonction du thread demarre. L'argument est '%s'\n",(char *) arg);
    sleep(5);
    strcpy(message, "Adios!");
    pthread_exit("Merci par le temps de CPU");
}
int main()
{
    int res ;
    pthread_t a_thread;
    void *thread_result ;
    res = pthread_create(&a_thread,NULL,thread_function,(void*)message);
    if (res != 0)
    {
        perror("Thread creation failed");
        exit(EXIT_FAILURE);
    }
    printf("En attente que le thread termine ...\n");
    res = pthread_join(a_thread, &thread_result);
    if (res != 0)
    {
        perror("Echec dans l'union du thread");
        exit(EXIT_FAILURE);
    }
    printf( "Thread termine %s\n" , (char *)thread_result );
    printf("Le message est %s\n", message);
    exit(EXIT_SUCCESS);
}