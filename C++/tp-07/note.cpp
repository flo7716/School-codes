#include <iostream>
#include "note.h"

// Définition de la classe Note

Note::Note(double valeur, double coefficient) {
  this->valeur = valeur;
  this->coefficient = coefficient;
}

void Note::afficher() const { // Ajoutez const ici
  std::cout << valeur << "(" << coefficient << ")" << std::endl;
}


