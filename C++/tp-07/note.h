#ifndef NOTE_H
#define NOTE_H

#include <iostream>

class Note {
public:
    double valeur;
    double coefficient;

    // Constructeur avec paramètres
    Note(double valeur, double coefficient);

    // Affiche la valeur de la note et son coefficient entre parenthèses
    void afficher() const; // Ajoutez const ici
};

#endif // NOTE_H
