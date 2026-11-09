#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *tache(void *arg)
{
    int i = *(int *)arg;

    for (int j = 0; j < 10000; j++)
    {
        // Boucle vide
    }

    printf("Tache %d : thread ID = %lu\n",
           i, (unsigned long)pthread_self());

    return NULL;
}

int main()
{
    pthread_t threads[5];
    int numeros[5];

    for (int i = 0; i < 5; i++)
    {
        numeros[i] = i + 1;

        pthread_create(&threads[i], NULL,
                      tache, &numeros[i]);
    }

    // Le thread initial effectue également la tâche
    int i = 0;
    tache(&i);

    for (int j = 0; j < 5; j++)
    {
        pthread_join(threads[j], NULL);
    }

    return 0;
}
