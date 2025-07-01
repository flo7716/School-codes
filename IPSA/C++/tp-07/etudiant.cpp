#include <iostream>
#include <vector>

#include "etudiant.h"
#include "note.h"

// Définition de la classe Etudiant

Etudiant::Etudiant(std::string nom) {
  this->nom = nom;
}

void Etudiant::ajouter_note(Note note) {
  notes.push_back(note);
}

double Etudiant::moyenne() {
  if (notes.empty()) {
    return -1.0;
  }

  double total = 0.0;
  for (const Note& note : notes) {
    total += note.valeur * note.coefficient;
  }

  return total / notes.size();
}

void Etudiant::afficher() {
  std::cout << "Nom : " << nom << std::endl;

  double moyenne = this->moyenne();
  if (moyenne == -1.0) {
    std::cout << "Pas de notes" << std::endl;
    return;
  }

  std::cout << "Moyenne : " << moyenne << std::endl;
  std::cout << "Notes :" << std::endl;
  for (const Note& note : notes) {
    note.afficher(); // Utilisez note au lieu de Note
    std::cout << std::endl;
  }
}

