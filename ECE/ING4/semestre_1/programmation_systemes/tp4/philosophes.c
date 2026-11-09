#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

pthread_mutex_t *baguettes;
int N;

void *philosophe(void *arg)
{
    int i = *(int *)arg;

    int gauche = i;
    int droite = (i + 1) % N;

    while (1)
    {
        printf("Philosophe %d discute...\n", i);
        sleep(1);

        // Le dernier philosophe prend les baguettes
        // dans l'ordre inverse pour éviter le deadlock.
        if (i == N - 1)
        {
            pthread_mutex_lock(&baguettes[droite]);
            pthread_mutex_lock(&baguettes[gauche]);
        }
        else
        {
            pthread_mutex_lock(&baguettes[gauche]);
            pthread_mutex_lock(&baguettes[droite]);
        }

        printf("Philosophe %d mange...\n", i);
        sleep(1);

        pthread_mutex_unlock(&baguettes[gauche]);
        pthread_mutex_unlock(&baguettes[droite]);

        printf("Philosophe %d repose ses baguettes.\n", i);
    }

    return NULL;
}

int main()
{
    printf("Nombre de philosophes : ");
    scanf("%d", &N);

    if (N < 2)
    {
        printf("Il faut au moins 2 philosophes.\n");
        return 1;
    }

    pthread_t threads[N];
    int ids[N];

    baguettes = malloc(N * sizeof(pthread_mutex_t));

    for (int i = 0; i < N; i++)
        pthread_mutex_init(&baguettes[i], NULL);

    for (int i = 0; i < N; i++)
    {
        ids[i] = i;
        pthread_create(&threads[i], NULL,
                       philosophe, &ids[i]);
    }

    for (int i = 0; i < N; i++)
        pthread_join(threads[i], NULL);

    return 0;
}
