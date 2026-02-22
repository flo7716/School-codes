#include <iostream>
#include <string>
#define nmax 60

using namespace std;

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
        cout << "Saisir le nb etudiant entre 1 et " << nmax << ": ";
        cin >> n;
    } while (n < 0 || n > nmax);
    return n;
}

etudiant saisir_1_etudiant() {
    etudiant e;
    date ddn;
    int validate_date;

    cout << "\nDonner votre nom: ";
    cin >> e.nom;
    cout << "Donner votre prenom: ";
    cin >> e.prenom;
    do {
        cout << "Donner votre jour de naissance (seulement le jour!): ";
        cin >> ddn.j;
        cout << "Donner votre mois de naissance (seulement le mois!): ";
        cin >> ddn.m;
        cout << "Donner votre annee de naissance: ";
        cin >> ddn.a;
        validate_date = date_valide(ddn.j, ddn.m, ddn.a);
    } while (validate_date == 0);
    e.ddn=ddn;

    return e;
}

void afficher_1_etudiant(etudiant e, int i) {
    cout << "\nEtudiant " << i+1 << ": " << e.nom << " " << e.prenom << endl;
    cout << "Date de naissance: " << e.ddn.j << "/" << e.ddn.m << "/" << e.ddn.a << endl;
    cout << "Note 1: " << e.note1 << endl;
    cout << "Note 2: " << e.note2 << endl;
    cout << "Note 3: " << e.note3 << endl;
    cout << "Moyenne: " << e.moy << endl;
}


void saisir_n_etudiant(etudiant t[], int n) {
    for (int i = 0; i < n; i++) {
        cout << "\nSaisie de l'etudiant " << i+1 << ":" << endl;
        t[i] = saisir_1_etudiant();
    }
}

void afficher_n_etudiant(etudiant t[], int n) {
    for (int i = 0; i < n; i++) {
        afficher_1_etudiant(t[i], i);
    }
}

void exo_etudiant() {
    int n = saisir_nb_etudiant();
    etudiant t[n];
    saisir_n_etudiant(t, n);
    afficher_n_etudiant(t, n);
}