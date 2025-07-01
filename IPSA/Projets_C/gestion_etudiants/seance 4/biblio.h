//----------------------------------------------
//Florian ANDRE
//2B DIA
//BIn215 TP4
//----------------------------------------------
#include <stdio.h>
#include <string.h>
#define nmax 60


typedef struct {
    int j,m,a;
}date;

typedef struct {
    char nom[10];
    char prenom[10];
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
        printf("Saisir le nb etudiant entre 1 et %d: ", nmax);
        scanf("%d", &n);
    } while (n < 0 || n > nmax);
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
    system("CLS");
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

void saisir_n_etudiant(etudiant e[nmax], int n) {
    int i;

    for (i = 0; i < n; i++) {
        system("CLS");
        printf("\n------------------------------");
        printf("\n--------ETUDIANT %d---------", i + 1);
        printf("\n------------------------------");
        e[i] = saisir_1_etudiant();
        system("CLS");
    }
}

void afficher_n_etudiant(etudiant e[nmax], int n) {
    int i;
    for (i = 0; i < n; i++) {
        afficher_1_etudiant(e[i], i);
    }
}

void exo_etudiant() {
    int n;
    etudiant e[nmax];
    n = saisir_nb_etudiant();
    saisir_n_etudiant(e, n);
    afficher_n_etudiant(e, n);
}
