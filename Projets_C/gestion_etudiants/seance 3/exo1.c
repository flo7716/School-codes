#include <stdio.h>
//ANDRE Florian
//2B DIA

main(){
    int longueur;
    char nom[15];
    char prenom[15];
    char identite[30];
    int R;
    printf("Saisissez votre nom : ");
    gets(nom);
    printf("Saisissez votre prenom : ");
    gets(prenom);
    strcpy(identite,"");
    strcat(identite,nom);
    strcat(identite,"");
    strcat(identite,prenom);
    system("CLS");
    printf("\n Nom : %s",nom);
    printf("\n Prenom : %s",prenom);
    printf("\n La taille de votre identite est %d",strlen(identite));
    R=strcmp(prenom,"Mehdi");

    if(R==0){
        printf("\n R = %d",R);
        printf("\n Yes c'est bien toi bienvenue ! \n");
        }
    else{
        printf("\n R = %d",R);
        printf("\n non ce n'est pas toi casse-toi de la! \n");
        }
}
