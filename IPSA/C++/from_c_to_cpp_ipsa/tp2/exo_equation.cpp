#include <iostream>
#include <cmath>
using namespace std;

//Equation du second degre : ax^2 + bx + c = 0
int main(){
    float a,b,c;
    float delta,x1,x2;
    cout << "Entrez a : ";
    cin >> a;
    cout << "Entrez b : ";
    cin >> b;
    cout << "Entrez c : ";
    cin >> c;
    if(a==0){
        cout << "Votre equation n'est pas de degre 2" << endl;
    }
    else{
        delta = pow(b,2)-4*a*c;
        if(delta==0){
            x1=-b/(2*a);
            cout << "1 seule racine x1=" << x1 << endl;
        }
        if(delta>0){
            x1=(-b-sqrt(delta))/(2*a);
            x2=(-b+sqrt(delta))/(2*a);
            cout << "2 racines reelles x1= " << x1 << " et x2= " << x2 << endl;
        }
        if(delta<0){
            x1=b/(2*a); //partie reelle
            x2=sqrt(-delta)/(2*a); //partie imaginaire pure
            cout << "2 racines complexes conjuguees z1= " << x1 << " - " << x2 << "i et z2= " << x1 << " + " << x2 << "i" << endl;
        }
    }
    return 0;
}