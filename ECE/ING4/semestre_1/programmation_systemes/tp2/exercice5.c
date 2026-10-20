#include <unistd.h>
#include <stdlib.h>
#include<stdio.h>
#include <sys/wait.h>
void jouer(int NumJoueur); //NumJoueur est le numero du joueur 0..MaxJoueurs-1
#define MaxJoueurs 4
/*0*/
int main()
{
    // creer MaxJoueurs processus fils du processus principal
    // chaque joueur execute la fonction jouer puis se termine
    /*1*/
    pid_t pid;
    for(int i=0;i<MaxJoueurs;i++){
        pid=fork();
        if(pid<0){
            perror("Erreur fork");
            exit(1);
        }
        else if(pid==0){
            jouer(i);
            exit(0);
        }
    }
    while(1){
    // attendre la fin d’un joueur
    //lorsqu’un joueur se termine, un autre joueur de meme numero est cree
    /*3*/
        
    }
return 0;
}