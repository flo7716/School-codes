#include <unistd.h> // pour sleep
#include <pthread.h> // pthread_create , pthread_join ...
#include <stdio.h>
void fonction(void *arg) {
    printf("pid du thread fils : %d \n", (int) getpid());
}
int main() {
    pthread_t thread ;
    printf("pid de main=%d \n", (int) getpid());
    pthread_create(&thread , NULL, &fonction , NULL) ;
    pthread_join( thread, NULL) ;
    return 0 ;
}