//----------------------------------------------
//Florian ANDRE
//2B DIA
//BIn215 TP4
//----------------------------------------------
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


typedef struct {
    int j,m,a;
}date;

typedef struct {
    char nom[20];
    char prenom[20];
    float note1;
    float note2;
    float note3;
    float moy;
    date ddn;
} etudiant;



int date_valide(int j, int m, int a) {
    int jour_mois[]={0,31,28,31,30,31,30,31,31,30,31,30,31};
    if(a<1||m<1||m>12||j<1)
        return(0);
    if((a%4==0)&&(a%100!=0)||(a%400==0))
        jour_mois[2]=29;
    if(j<=jour_mois[m])
        return(1);
    else
        return(0);
}

int saisir_nb_etudiant() {
    int n;
    do {
        printf("Saisir le nb etudiant : ");
        scanf("%d", &n);
    } while (n < 0 );
    return n;
}

etudiant saisir_1_etudiant() {
    etudiant e;
    date ddn;
    int validate_date;

    printf("\nDonner votre nom: ");
    scanf("%s", e.nom);
    printf("Donner votre prenom: ");
    scanf("%s", e.prenom);
    do {
        printf("Donner votre jour de naissance (seulement le jour!): ");
        scanf("%d", &ddn.j);
        printf("Donner votre mois de naissance (seulement le mois!): ");
        scanf("%d", &ddn.m);
        printf("Donner votre annee de naissance: ");
        scanf("%d", &ddn.a);
        validate_date = date_valide(ddn.j, ddn.m, ddn.a);
    } while (validate_date == 0);
    e.ddn=ddn;
    printf("Donner votre note1: ");
    scanf("%f", &e.note1);
    printf("Donner votre note2: ");
    scanf("%f", &e.note2);
    printf("Donner votre note3: ");
    scanf("%f", &e.note3);
    e.moy = (e.note1 + e.note2 + e.note3) / 3;
    return e;
}

void afficher_1_etudiant(etudiant e, int i) {
    printf("\033[H\033[J");
    printf("\n-------------------------");
    printf("\n--------ETUDIANT %d---------", i + 1);
    printf("\n-------------------------");
    printf("\nNom: %s", e.nom);
    printf("\nPrenom: %s", e.prenom);

    // Assign the birthdate values to the local date structure
    date ddn = e.ddn;

    printf("\nDate de naissance: %d/%d/%d", ddn.j, ddn.m, ddn.a);
    printf("\nNote1: %.2f", e.note1);
    printf("\nNote2: %.2f", e.note2);
    printf("\nNote3: %.2f", e.note3);
    printf("\nMoyenne: %.2f", e.moy);
    printf("\n-------------------------");
    system("PAUSE");
}

void saisir_n_etudiant(etudiant * e, int n) {
    int i;

    for (i = 0; i < n; i++) {
        printf("\033[H\033[J");
        printf("\n------------------------------");
        printf("\n--------ETUDIANT %d---------", i + 1);
        printf("\n------------------------------");
        *(e+i) = saisir_1_etudiant();
        printf("\033[H\033[J");
    }
}

void afficher_n_etudiant(etudiant *e, int n) {
    int i;
    for (i = 0; i < n; i++) {
        afficher_1_etudiant(*(e+i), i);
    }
}

void saisir_n_etudiant_d_f(etudiant * e, int d, int f) {
    int i;

    for (i = d; i < f; i++) {
        printf("\033[H\033[J");
        printf("\n------------------------------");
        printf("\n--------ETUDIANT %d---------", i + 1);
        printf("\n------------------------------");
        *(e+i) = saisir_1_etudiant();
        printf("\033[H\033[J");
    }
}

int chercher_etudiant(etudiant *e, int n, char nom[], char prenom[]) {
    for (int i = 0; i < n; i++) {
        if (strcmp(e[i].nom, nom) == 0 && strcmp(e[i].prenom, prenom) == 0) {
            return i; // Retourne l'index de l'�tudiant trouv�
        }
    }
    return -1; // Retourne -1 si l'�tudiant n'est pas trouv�
}

void supprimer_etudiant(etudiant *e, int *n, char nom[], char prenom[]) {
    int index = chercher_etudiant(e, *n, nom, prenom);
    if (index != -1) {
        // Remplace l'�tudiant � supprimer par le dernier �tudiant dans le tableau
        e[index] = e[*n - 1];
        // R�duit la taille du tableau
        *n = *n - 1;
        // R�alloue la m�moire pour le tableau
        e = (etudiant *)realloc(e, (*n) * sizeof(etudiant));
        printf("Etudiant supprime avec succes.\n");
    } else {
        printf("Etudiant non trouve.\n");
    }
    system("PAUSE");
}

void exo_etudiant() {
    int n, x;
    etudiant *e;
    int N;
    e = NULL;
    N = 0;
    do {
        printf("\033[H\033[J");
        printf("\n------------------------------------------------------");
        printf("\n----------------------- MENU -------------------------");
        printf("\n------------------------------------------------------");
        printf("\n             1. Saisir un etudiant");
        printf("\n             2. Afficher tous les etudiants");
        printf("\n             3. Chercher un etudiant");
        printf("\n             4. Supprimer un etudiant");
        printf("\n             5. Sortir");
        printf("\n------------------------------------------------------");
        printf("\nChoisissez : ");
        scanf("%d", &x);
        if (x == 1) {
            n = saisir_nb_etudiant();
            if (N == 0) {
                e = (etudiant *)malloc(n * sizeof(etudiant));
            } else {
                e = (etudiant *)realloc(e, (N + n) * sizeof(etudiant));
            }
            saisir_n_etudiant_d_f(e, N, N + n);
            N = n + N;
        } else if (x == 2) {
            if (e == NULL) {
                printf("\033[H\033[J");
                printf("Vous n'avez pas encore d'etudiant\n");
                system("PAUSE");
            } else {
                afficher_n_etudiant(e, N);
                printf("\033[H\033[J");
            }
        } else if (x == 3) {
            if (e == NULL) {
                printf("\033[H\033[J");
                printf("Vous n'avez pas encore d'etudiant\n");
                system("PAUSE");
            } else {
                char nom[20];
                char prenom[20];
                printf("Entrez le nom de l'etudiant : ");
                scanf("%s", nom);
                printf("Entrez le prenom de l'etudiant : ");
                scanf("%s", prenom);
                int index = chercher_etudiant(e, N, nom, prenom);
                if (index != -1) {
                    afficher_1_etudiant(e[index], index);
                } else {
                    printf("Etudiant non trouve.\n");
                    system("PAUSE");
                }
            }
        } else if (x == 4) {
            if (e == NULL) {
                printf("\033[H\033[J");
                printf("Vous n'avez pas encore d'etudiant\n");
                system("PAUSE");
            } else {
                char nom[20];
                char prenom[20];
                printf("Entrez le nom de l'etudiant a supprimer : ");
                scanf("%s", nom);
                printf("Entrez le prenom de l'etudiant a supprimer : ");
                scanf("%s", prenom);
                supprimer_etudiant(e, &N, nom, prenom);
            }
        }
    } while (x != 5);
    if (x == 5) {
        free(e);
        printf("\033[H\033[J");
        printf("Bonne journee\n");
    }
}
