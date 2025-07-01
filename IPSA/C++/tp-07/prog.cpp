#include <iostream>

#include "etudiant.h"
#include "note.h"

int main() {
  // Création de 4 notes
  Note n1(14.5, 2.0), n2(19.0, 1.0), n3(8.0, 0.5), n4(18.0, 2.0);

  // Création d'un étudiant
  Etudiant etudiant("Lucie");

  // Ajout des notes à l'étudiant
  etudiant.ajouter_note(n1);
  etudiant.ajouter_note(n2);
  etudiant.ajouter_note(n3);
  etudiant.ajouter_note(n4);

  // Affichage des informations de l'étudiant
  etudiant.afficher();

  return 0;
}
