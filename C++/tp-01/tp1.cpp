#include <iostream>
#include <cmath>
//Florian ANDRE 2BDIA
//BIn222
int main(){
    //------------------------------------
    int result = 10;
    bool a = true;
    bool b = false;
    bool c = true;
    bool d;

    //Affichage du résultat
    std::cout << "Résultat : " << result << std::endl;

    //Operations logiques
    d=(a||b);
    std::cout << "Valeur de d : " << d << std::endl;

    d=(b||!a);
    std::cout <<"Valeur de d : " << d << std::endl;

    //Operations de comparaisons
    int A;
    int B;
    int C;
    A=1;
    B=2;
    C=3;
    bool D; 
    D=(B<A);
    std::cout <<"Valeur de d (b inferieur a a) : " << D << std::endl;

    //Moyenne ponderee
    float note_1, note_2, note_3,moyenne_ponderee;
    int coeff_1,coeff_2,coeff_3;
    note_1=12.0;
    note_2=14.5;
    note_3=18;
    coeff_1=2;
    coeff_2=3;
    coeff_3=1;
    moyenne_ponderee=(note_1*coeff_1+note_2*coeff_2+note_3*coeff_3)/(coeff_1+coeff_2+coeff_3);
    std::cout <<"Moyenne ponderee = " << moyenne_ponderee << std::endl;

    //Polynome du premier degre ax+b
    float A1, x, B1, y;
    A1=1;
    x=2;
    B1=3;
    y=A1*x+B1;
    std::cout <<"pour A1 = 1, x = 2 et B1 = 3, y = "<< y << std::endl;


    x=-2.2;
    y=A1*x+B1;
    std::cout <<"pour A1 = 1, x = -2.2 et B1 = 3, y = "<< y << std::endl;

    //Polynome du second degre ax^2 + bx + c
    float A2, B2, C2, carreX, X, Y;
    A2=2;
    B2=3;
    C2=6;
    X=1;
    carreX=pow(X,2);
    Y=A2*carreX+B2*X+C2;
    std::cout <<"pour A2 = 2, X = 1, B2 = 3 et C2 = 6, Y = "<< Y << std::endl;

    X=4.2;
    carreX=pow(X,2);
    Y=A2*carreX+B2*X+C2;
    std::cout <<"pour A2 = 2, X = 4.2, B2 = 3 et C2 = 6, Y = "<< Y << std::endl;

    X=-1;
    carreX=pow(X,2);
    Y=A2*carreX+B2*X+C2;
    std::cout <<"pour A2 = 2, X = -1, B2 = 3 et C2 = 6, Y = "<< Y << std::endl;

    //Pointeurs et references
    //Pointeurs
    float v1;
    v1=3.1;
    float* p1 = &v1;
    float valeur = *p1;
    std::cout <<"v1 = "<< valeur << std::endl;

    //References
    float v = 3.2;
    float& ref = v;
    float Valeur = ref;
    std::cout <<"v = "<< Valeur << std::endl;







    return 0;
}