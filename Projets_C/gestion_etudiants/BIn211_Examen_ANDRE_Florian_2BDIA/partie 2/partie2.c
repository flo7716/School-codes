//----------------------------------------------
//Florian ANDRE
//2B DIA
//BIn211 Examen
//----------------------------------------------
#include <stdio.h>
#include <string.h>
#define nmax 60


typedef struct {
    int Jour,Mois,Annee;
}Date;

typedef struct {
    int Genre;
    char Nom[20];
    char Prenom[20];
    Date Date_n;
    int Assos;
    int Cursus;
    char Mail[40];
    char Telephone[11];

} Etudiant;

int date_valide(int Jour, int Mois, int Annee) {
    int jour_mois[]={0,31,28,31,30,31,30,31,31,30,31,30,31};
    if(Annee<1||Mois<1||Mois>12||Jour<1)
        return(0);
    if((Annee%4==0)&&(Annee%100!=0)||(Annee%400==0))
        jour_mois[2]=29;
    if(Jour<=jour_mois[Mois])
        return(1);
    else
        return(0);
}

Etudiant saisir_1_etudiant() {
    Etudiant e;
    Date Date_n;
    int validate_date, choix_asso, choix_cursus, val_genre;
    do {
        printf("\nsaisir genre etudiant: 1 = Homme et 2 = Femme :  ");
        scanf("%d", &val_genre);
    } while (val_genre != 1 && val_genre != 2);
    if(val_genre==1)
        e.Genre="Homme";
    else
        e.Genre="Femme";

    do
    {
        printf("\nDonner votre nom: ");
        scanf("%s",&e.Nom);
    }while(strlen(e.Nom)<1||strlen(e.Nom)>20);
    do
    {
        printf("\nDonner votre prenom: ");
        scanf("%s",&e.Prenom);
    }while(strlen(e.Prenom)<1||strlen(e.Prenom)>20);
    do {
        printf("\nDonner votre jour de naissance (seulement le jour!): ");
        scanf("%d", &Date_n.Jour);
        printf("\nDonner votre mois de naissance (seulement le mois!): ");
        scanf("%d", &Date_n.Mois);
        printf("\nDonner votre annee de naissance: ");
        scanf("%d", &Date_n.Annee);
        validate_date = date_valide(Date_n.Jour, Date_n.Mois, Date_n.Annee);
    } while (validate_date == 0);
    e.Date_n=Date_n;
    do
    {
       printf("\nDonner l'asso choisie : 1 = Sportive, 2 = Artistique, 3 = Technique : ");
       scanf("%d",&choix_asso);
    }while(choix_asso<1||choix_asso>3);
    if(choix_asso==1)
        e.Assos="Sportive";
    else if(choix_asso==2)
        e.Assos="Artistique";
    else
        e.Assos="Technique";
    do
    {
        printf("\nSaisissez votre cursus : 1 = Bachelor, 2 = Aero : ");
        scanf("%d",&choix_cursus);
    }while(choix_cursus<1||choix_cursus>2);
    if(choix_cursus==1)
        e.Cursus="Bachelor";
    else
        e.Cursus="Ingenieur";
    do
    {
        printf("\nSaisissez votre mail (40 caracteres maximum) : ");
        scanf("%s",&e.Mail);
    }while(strlen(e.Mail)<1||strlen(e.Mail)>40);

    do
    {
        printf("\nSaisissez votre numero de telephone (11 caracteres maximum): ");
        scanf("%s",&e.Telephone);
    }while(strlen(e.Telephone)<1||strlen(e.Telephone)>11);

    return e;
}



void afficher_1_etudiant(Etudiant e) {
    system("CLS");
    printf("\n-------------------------");
    printf("\n--------ETUDIANT---------");
    printf("\n-------------------------");
    printf("\nGenre            : %s",e.Genre);
    printf("\nNom              : %s", e.Nom);
    printf("\nPrenom           : %s", e.Prenom);

    // Assign the birthdate values to the local date structure
    Date Date_n = e.Date_n;

    printf("\nDate de naissance: %d/%d/%d", Date_n.Jour, Date_n.Mois, Date_n.Annee);
    printf("\nAssos            : %s", e.Assos);
    printf("\nCursus           : %s", e.Cursus);
    printf("\nMail             : %s", e.Mail);
    printf("\nTelephone        : %s", e.Telephone);
    printf("\n-------------------------");
    system("PAUSE");
}

main()
{
    Etudiant e;
    e=saisir_1_etudiant();
    afficher_1_etudiant(e);
}
