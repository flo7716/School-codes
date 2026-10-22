#include <sys/types.h> // types
#include <unistd.h> // fork , pipe , read , write , close
#include <stdio.h>
#include <string.h>
#define R 0
#define W 1
int main(){
    int nboctets, fd[2];
    char message [100] ;
    char* phrase = "message envoye au pere par le fils" ;
    pipe(fd);
    if (fork()==0){
        close ( fd [R ] ) ;
        write(fd[W],phrase, strlen(phrase)+1) ;
        close (fd[W]) ;
    }
    else{
        close(fd[W]) ;
        nboctets = read (fd[R], message,100) ;
        printf ( " Lecture %d octets : %s\n" , nboctets , message ) ;
        close (fd[R]) ;
    }
    return 0 ;
}