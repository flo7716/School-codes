#include <iostream>
// Les définitions des fonctions
int f() {
 return 1;
}
// Définition de fonctions
//1.1
int incr(int a) {
    return a + 1 ;
}

//1.2

int f1(int value, bool positive = true) {
    if(positive == true){
        return value;
    }
    else{
        return -value;
    }
}

//1.3

int grid(int row, int column) {
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < column; ++j) {
            if (j < 10) {
                std::cout << i << "0" << j << " ";
            } else {
                std::cout << i << j << " ";
            }
        }
        std::cout << std::endl;
    }
    return 0;
}

//1.4

int copy_plus(int a){
    int b = a + 1;
    return (a , b);
}

void decr(int* ptr) {
    (*ptr)--;
}

void add(int& a, int b) {
    a += b;
}

/*
 Calcul de la factorielle d'un nombre de manière récursive.
  
  n : Le nombre entier non nul pour lequel calculer la factorielle.
  retourne la factorielle de n.
  
  Définition récursive de factorielle :
  - 0! = 1
  - Pour tout entier n > 0, n! = (n – 1)! × n
 */
int fact(int n) {
    if (n == 0)
        return 1;
    else
        return n * fact(n - 1);
}


int main() {
 // Les appels des fonctions à définir
 int x, a, b, increment_a, positif, negatif, tableau;
 x = f();
 a = 3 ;
 increment_a = incr(a);
 std::cout << "Increment de a = " << increment_a << std::endl;
 positif = f1(1, true);
 negatif = f1(1, false);
 std::cout << "Positif = " << positif << std::endl ;
 std::cout << "Negatif = " << negatif << std::endl ;
 tableau = grid(10, 10);
 a, b = copy_plus(a);
 std::cout<<"La valeur a vaut "<< a << " et sa copie b vaut "<< b << std::endl;
 int num = 10;
 std::cout << "Avant appel de decr : " << num << std::endl;
 decr(&num); // Appel de decr avec l'adresse de num comme argument
 std::cout << "Après appel de decr : " << num << std::endl;
 int num1 = 5;
 int num2 = 7;
 std::cout << "Avant appel de add : num1 = " << num1 << ", num2 = " << num2 << std::endl;
 add(num1, num2); // Appel de add avec num1 et num2 comme arguments
 std::cout << "Après appel de add : num1 = " << num1 << ", num2 = " << num2 << std::endl;
 int factorielle_5=fact(5);
 std::cout << " 5! = " << factorielle_5 << std::endl;

 // Affichage si nécessaire
 std::cout << x << std::endl ;
 return 0;
}
