#include "biblio.h"
//----------------------------------------------
//Florian ANDRE


int main() {
    int i, j;
    etudiant e;
    i = saisir_nb_etudiant();
    for (j = 0; j < i; j++) {
        cout << "\nSaisie de l'etudiant " << j+1 << ":" << endl;
        e = saisir_1_etudiant();
    afficher_1_etudiant(e, j);
    }
    return 0;
}