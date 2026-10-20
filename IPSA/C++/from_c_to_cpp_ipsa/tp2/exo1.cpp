#include <iostream>
#include "bibliotableau.h"
using namespace std;

int main(){
    int t[nmax];
    int n;
    cout << "Entrez la taille du tableau : ";
    cin >> n;
    for(int i=0; i<n; i++){
        cout << "Entrez l'élément " << i << " : ";
        cin >> t[i];
    }
    cout << "Produit du tableau : " << produit_tableau(t,n) << endl;
    cout << "Somme du tableau : " << somme_tableau(t,n) << endl;
    cout << "Moyenne du tableau : " << moyenne(t,n) << endl;
    cout << "Minimum du tableau : " << minimum_tableau(t,n) << endl;
    cout << "Position du minimum : " << pos_minimum_tableau(t,n) << endl;
    cout << "Maximum du tableau : " << maximum_tableau(t,n) << endl;
    cout << "Position du maximum : " << pos_maximum_tableau(t,n) << endl;
    return 0;
}