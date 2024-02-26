#include <iostream>
int main() {
    // -------------------------------------------------------------
    // 1.1
    int a = 3;
    int b = 2;
    int superieur;
    std::cout << a << b << std::endl;
    // 1.2
    // -------------------------------------------------------------
    if (a > b)
    {
        superieur = a;
        std::cout << " le plus grand nombre est : " << a << std::endl;
    }
    else
    {
        if(a<b){
                superieur = b;
                std::cout << " le plus grand nombre est : " << b << std::endl;
            }
        else{
            std::cout << "les 2 nombres sont egaux" << std::endl;
        }

    }
     
    int e, f, g;
    e=1;
    f=17;
    g=6;

    if ((e < f) && (e < g)){
        std::cout<<"e est le plus petit nombre. Il vaut e = "<< e <<std::endl;
    }
    else if ((f < e) && (f < g)){
        std::cout<<"f est le plus petit nombre. Il vaut f = "<< f <<std::endl;
    }
    else if ((g < e) && (g < f)){
        std::cout<<"g est le plus petit nombre. Il vaut g = "<< g <<std::endl;
    }
    else
        std::cout<<"2 nombres sont egaux "<<std::endl;
    


    int i;

    
    std::cout << "Entrez un entier entre 1 et 7 : ";
    std::cin >> i;

    
    switch (i) {
        case 1:
            std::cout << "Lundi" << std::endl;
            break;
        case 2:
            std::cout << "Mardi" << std::endl;
            break;
        case 3:
            std::cout << "Mercredi" << std::endl;
            break;
        case 4:
            std::cout << "Jeudi" << std::endl;
            break;
        case 5:
            std::cout << "Vendredi" << std::endl;
            break;
        case 6:
            std::cout << "Samedi" << std::endl;
            break;
        case 7:
            std::cout << "Dimanche" << std::endl;
            break;
        default:
            std::cout << "Erreur : Entrez un nombre entre 1 et 7." << std::endl;
    }


    //Boucles
    int j, k;
    std::cout << "Saisissez un entier j non nul : " <<std::endl;
    std::cin >> j;
    std::cout << "Saisissez un entier k" <<std::endl;
    std::cin >> k;

    if(j!=0){
        int multiple = j;
        while (multiple <= k){
            std::cout << multiple << " ";
            multiple += j;
        }
        std::cout << std::endl;
    }
    else{
        std::cout << "Erreur : j doit etre non nul !" << std::endl;
    }

    int l;

    std::cout << "Entrez un entier l : ";
    std::cin >> l;
    if (l < 0) {
        std::cout << "Erreur : La factorielle n'est pas définie pour les nombres négatifs." << std::endl;
    } 
    else {
        long long factorial = 1;

        for (int i = 1; i <= l; ++i) {
            factorial *= i;
        }

        std::cout << "Factorielle de " << l << " : " << factorial << std::endl;
    }

    int compteur = 1;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            std::cout << compteur;
            compteur++;
        }
        std::cout << std::endl;
    }

    const int lignes = 10;
    const int colonnes = 10;

    for (int i = 0; i < lignes; ++i) {
        for (int j = 0; j < colonnes; ++j) {
            if (j < 10) {
                std::cout << i << "0" << j << " ";
            } else {
                std::cout << i << j << " ";
            }
        }
        std::cout << std::endl;
    }
    
    int m;
    std::cout << "Entrez la valeur de m : ";
    std::cin >> m;

    for (int i = 1; i <= 100; ++i) {
        std::cout << i << " ";

        if (i % m == 0) {
            std::cout << "(jusqu'au premier multiple de " << m << ")";
            break;
        }
    }

    int m1, n;

    std::cout << "Entrez la valeur de m : ";
    std::cin >> m1;

    std::cout << "Entrez la valeur de n : ";
    std::cin >> n;

    for (int i = 1; i <= m1; ++i) {
        if (i % n == 0) {
            // Skip les multiples de n
            continue;
        }
        std::cout << i << " ";
    }
    return 0;
}
