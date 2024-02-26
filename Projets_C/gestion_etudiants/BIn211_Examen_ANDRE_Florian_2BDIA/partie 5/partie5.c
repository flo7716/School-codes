//----------------------------------------------
//Florian ANDRE
//2B DIA
//BIn211 Examen
//----------------------------------------------
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


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

int Saisir_Nbre_etudiant() {
    int n;
    do {
        printf("Saisir le nb etudiant : ");
        scanf("%d", &n);
    } while (n < 1);
    return n;
}

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

Etudiant Saisir_1_etudiant() {
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



void afficher_1_etudiant(Etudiant e, int i) {
    system("CLS");
    printf("\n-------------------------");
    printf("\n--------ETUDIANT %d---------", i+1);
    printf("\n-------------------------");
    printf("\nGenre            : %s",e.Genre);
    printf("\nNom              : %s", e.Nom);
    printf("\nPrenom           : %s", e.Prenom);


    Date Date_n = e.Date_n;

    printf("\nDate de naissance: %d/%d/%d", Date_n.Jour, Date_n.Mois, Date_n.Annee);
    printf("\nAssos            : %s", e.Assos);
    printf("\nCursus           : %s", e.Cursus);
    printf("\nMail             : %s", e.Mail);
    printf("\nTelephone        : %s", e.Telephone);
    printf("\n-------------------------");
    system("PAUSE");
}

void Saisir_n_etudiants(Etudiant * e, int n) {
    int i;

    for (i = 0; i < n; i++) {
        system("CLS");
        printf("\n------------------------------");
        printf("\n--------ETUDIANT %d---------", i + 1);
        printf("\n------------------------------");
        *(e+i) = Saisir_1_etudiant();
        system("CLS");
    }
}

void Afficher_n_etudiants(Etudiant *e, int n) {
    int i;
    for (i = 0; i < n; i++) {
        afficher_1_etudiant(*(e+i), i);
    }
}

void Saisir_n_etudiant_d_f(Etudiant * e, int d, int f) {
    int i;

    for (i = d; i < f; i++) {
        system("CLS");
        printf("\n------------------------------");
        printf("\n--------ETUDIANT %d---------", i + 1);
        printf("\n------------------------------");
        *(e+i) = Saisir_1_etudiant();
        system("CLS");
    }
}



main()
{
    int n, x;
    Etudiant *e;
    int N;
    e = NULL;
    N = 0;
    do {
        system("CLS");
        printf("\n------------------------------------------------------");
        printf("\n----------------------- MENU -------------------------");
        printf("\n------------------------------------------------------");
        printf("\n              1. Saisir un etudiant");
        printf("\n             2. Afficher tous les etudiants");
        printf("\n                     3. Sortir");
        printf("\n------------------------------------------------------");
        printf("\nChoisissez : ");
        scanf("%d", &x);
        if (x == 1) {
            n = Saisir_Nbre_etudiant();
            if (N == 0) {
                e = (Etudiant *)malloc(n * sizeof(Etudiant));
            } else {
                e = (Etudiant *)realloc(e, (N + n) * sizeof(Etudiant));
            }
            Saisir_n_etudiant_d_f(e, N, N + n);
            N = n + N;
        } else if (x == 2) {
            if (e == NULL) {
                system("CLS");
                printf("Vous n'avez pas encore d'etudiant\n");
                system("PAUSE");
            } else {
                Afficher_n_etudiants(e, N);
                system("CLS");
            }
        }
    } while (x != 3);
    if (x == 3) {
        free(e);
        system("CLS");
        printf("Bonne journee\n");
    }
}

