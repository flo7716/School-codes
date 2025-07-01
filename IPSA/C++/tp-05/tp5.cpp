#include <iostream>
#include <string>
#include <vector>
#include <map>

//Florian ANDRE, 2B DIA, BIn222
/*
Les fonctions des parties 1), 2) et 3) seront testées dans des fonctions test1(), test2() et test3()
1.1) Vector
Definit la fonction max qui a un argument nommé v de type vector<double> qui retourne l'indice de son élément le plus grand, avec une boucle for sur les indices.
*/
using namespace std;
int max(vector<double> v) {
    int index = 0;
    for (int i = 1; i < v.size(); i++) {
        if (v[i] > v[index]) {
            index = i;
        }
    }
    return index;
}

/* 1.2) Push_back
Definit la fonction init_vector(size, x) qui retourne un vecteur de taille size dont les éléments ont pour valeur
x en utilisant la méthode push_back.
par exemple, init_vector(3,0) retourne le vecteur [0,0,0]
pour tester, déclarer dans la fonction test1 un vecteur de nombres entiers initialisé avec la fonction init_vector(10)
et avec une boucle for each, afficher les valeurs du vecteur. 
*/
vector<int> init_vector(int size, int x) {
    vector<int> v;
    for (int i = 0; i < size; i++) {
        v.push_back(x);
    }
    return v;
}


/* 1.3) Matrice
3.1) Code
Définit une fonction init_matrix(rows,cols,value) qui retourne une matrice de rows lignes et cols colonnes dont tous les 
éléments ont pour valeur value, en utilisant des vecteurs de vecteurs, des boucles et la méthode push_back.
par exemple, init_matrix(3, 3, 1) retourne la matrice [ [1,1,1], [1,1,1], [1,1,1] ], qui représente la matrice :
111
111
111
*/

vector<vector<int>> init_matrix(int rows, int cols, int value) {
    vector<vector<int>> matrix;
    for (int i = 0; i < rows; i++) {
        vector<int> row;
        for (int j = 0; j < cols; j++) {
            row.push_back(value);
        }
        matrix.push_back(row);
    }
    return matrix;
}

//3.1) Tests
/*
3.2) Tests
Tester la fonction init_matrix en déclarant un vecteur de vecteurs d'entiers dans la fonction test1, initialisé avec init_matrix(20,10,5). Utilisons
ensuite des boucles for imbriquées pour parcourir la matrice et afficher ses valeurs sous forme de matrice
*/

/*
1.4) print_matrix
Definir la fonction print_matrix qui a un argument matrix de type vecteur de vecteurs qui affiche les valeurs 
de matrix avec des boucles for, sous forme de matrice comme-ci dessous:
65475
45685
78998

*/

void print_matrix(vector<vector<int>> matrix) {
    for (vector<int> row : matrix) {
        for (int num : row) {
            cout << num << " ";
        }
        cout << endl;
    }
}


/*
1.5) Passage d'arguments par reference
Definir la fonction set_matrix_at qui a 4 arguments matrix, row, column et value qui modifie la valeur en ligne row
et colonne column de la matrice matrix avec value et qui ne retourne rien

dans test1()
déclarer m1 correspondant à la matrice ci-dessous en utilisant les accolades pour l'initialisation:
33333
33333
33333
33333
33333

modifier la valeur au centre de m1 avec set_matrix_at et afficher m1
*/

void set_matrix_at(vector<vector<int>> &matrix, int row, int column, int value) {
    matrix[row][column] = value;
}


//2) String
/*Définir la fonction print qui prend en argument une chaine de caractères et qui l'affiche avec un retour à la ligne
*/

void print(string s) {
    cout << s << endl;
} 


//3) Map (nous allons utiliser map pour faire un annuaire)
/*
Dans test3, déclarer dir de type map qui associe des noms à des numéros de téléphone. Les noms et numéros sont des chaines de caractères 
*/

void test1() {
    vector<double> numbers = {3.14, 2.71, 6.28, 1.61, 0.0};
    int max_index = max(numbers);
    cout << "The index of the maximum element is: " << max_index << endl;
    vector<int> initial = init_vector(10, 0);
    cout << "Vecteur initialise = ";
    for (int num : initial){
        cout << num << " ";
    }
    cout << endl;

    vector<vector<int>> matrice = init_matrix(20, 10, 5);
    print_matrix(matrice);
    vector<vector<int>> m1 = {{3, 3, 3, 3, 3}, {3, 3, 3, 3, 3}, {3, 3, 3, 3, 3}, {3, 3, 3, 3, 3}, {3, 3, 3, 3, 3}};
    set_matrix_at(m1, 2, 2, 9);
    print_matrix(m1);
}

void test2(){
    string s = "Hello there ! General Kenobi !";
    print(s);
}

void test3() {
    // Déclaration de la map associant des noms à des numéros de téléphone
    std::map<std::string, std::string> dir;

    // Ajout de 3 éléments à la map
    dir["Alice"] = "123456789";
    dir["Bob"] = "987654321";
    dir["Charlie"] = "456789123";

    // Affichage des éléments de la map
    std::cout << "Annuaire :\n";
    for (const auto& entry : dir) {
        std::cout << entry.first << " : " << entry.second << "\n";
    }
}


int main() {
    test1();
    test2();
    test3();
    return 0;
}