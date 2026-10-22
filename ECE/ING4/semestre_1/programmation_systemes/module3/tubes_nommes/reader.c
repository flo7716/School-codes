#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
int main() {
    int fd,n;
    char input ;
    fd = open("mypipe", O_RDONLY);
    printf("ici reader[%d] \n",getpid());
    if (fd!= 1){
        printf("Recu par le lecteur:\n");
        while ((n = read(fd,&input ,1)) > 0) {
            printf("%c", input);
        }
        printf("Le lecteur se termine!\n",n);
    }
    else
    printf("desole, le tube n’est pas disponible\n"); close ( fd ) ;
    return 0 ;
}