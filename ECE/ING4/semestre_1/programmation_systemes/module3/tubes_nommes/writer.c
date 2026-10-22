#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <string.h>
int main(void) {
    int fd;
    char message[26];
    sprintf(message, "bonjour du writer [%d]\n", getpid());
    fd = open("mypipe", O_WRONLY);
    printf (" ici writer[%d] \n" , getpid ());
    if (fd!= 1){
        write(fd, message, strlen(message));
    }
    else
    {
        printf("erreur d'ouverture du tube nommé\n");
    }
    close ( fd ) ;
    return 0 ;
}