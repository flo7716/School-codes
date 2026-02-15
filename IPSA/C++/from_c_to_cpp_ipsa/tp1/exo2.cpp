#include <iostream>
using namespace std;

int main(){
    float x,y; //déclaration des variables
    cout << "donner x : "; //saisie des variables
    cin >> x;
    cout << "donner y : ";
    cin >> y;
    cout << "la somme de " << x << " et " << y << " est egal a " << x+y << endl; //somme de x et y
    cout << "le produit de " << x << " et " << y << " est egal a " << x*y; //produit de x et y
    return 0;
}