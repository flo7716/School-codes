#ifndef ETUDIANT_H
#define ETUDIANT_H

#include <vector>
#include "note.h"

class Etudiant {
  public:
    std::string nom;
    std::vector<Note> notes;

    // Constructeur avec paramètres
    Etudiant(std::string nom);

    // Ajoute une note à l'étudiant
    void ajouter_note(Note note);

    // Calcule la moyenne des notes de l'étudiant
    double moyenne();

    // Affiche le nom, la moyenne et les notes de l'étudiant
    void afficher();
};

#endif // ETUDIANT_H
