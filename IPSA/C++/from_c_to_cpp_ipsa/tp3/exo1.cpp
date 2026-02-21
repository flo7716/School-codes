#include <iostream>
#include <string>

using namespace std;
int main() {
    string nom;
    string prenom;
    string identite;
    int R;

    cout << "Saisissez votre nom : ";
    getline(cin, nom);
    cout << "Saisissez votre prenom : ";
    getline(cin, prenom);

    identite = nom + " " + prenom;

    //CLEAR SCREEN
    cout << "\033[H\033[J";

    cout << "\n Nom : " << nom;
    cout << "\n Prenom : " << prenom;
    cout << "\n La taille de votre identite est " << identite.length();

    R = (prenom == "Florian") ? 0 : 1;

    if (R == 0) {
        cout << "\n R = " << R;
        cout << "\n Yes c'est bien toi bienvenue ! \n";
    } else {
        cout << "\n R = " << R;
        cout << "\n non ce n'est pas toi casse-toi de la! \n";
    }

    return 0;
}