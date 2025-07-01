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
