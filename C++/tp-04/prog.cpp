#include "math.h"
#include <iostream>

int test() {
    int factorielle, arr;
    factorielle = fact(5);
    arr = arrangement(2, 5);
    std::cout << "Factorielle de 5 = " << factorielle << std::endl;
    std::cout << "Arrangement de 2 parmi 5 = " << arr << std::endl;
    return 0; // Ajout de l'instruction return
}

int main() {
    int essai = test();
    return 0;
}
