#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/syscall.h>

void *fonction(void *arg)
{
    printf("Thread %ld : PID = %d, TID = %ld\n",
           (long)arg,
           getpid(),
           syscall(SYS_gettid));

    return NULL;
}

int main()
{
    pthread_t threads[3];

    for (long i = 1; i <= 3; i++)
    {
        pthread_create(&threads[i-1], NULL, fonction, (void *)i);
    }

    for (int i = 0; i < 3; i++)
    {
        pthread_join(threads[i], NULL);
    }

    return 0;
}
