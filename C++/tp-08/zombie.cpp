#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>
#include <ctime>
using namespace std;
class Position{
    public:
        int mX;
        int mY;
    
    void display(){
        cout << "<" << mX << ", " << mY << ">" << endl;
    }

};


/*
Créer une classe GameObject qui a un attribut mPosition initialisé avec l’argument de son constructeur, un attribut
mCode initialisé dans le constructeur avec la valeur G et une méthode display qui affiche le code suivit de ses
coordonnées comme ceci : G<1,1> si le game object est aux cordonnées (1,1), en utilisant display .
*/

class GameObject{
    public:
        Position mPosition;

    GameObject(Position position){
        mPosition = position;
        
    }

    void display(){
        mPosition.display();
    }

};

/*
Création d'une classe Character héritant de GameObject dotée d'un attribut mHealth initialisé à 100
*/

class Character : public GameObject{
    public:
        int mHealth;

    Character(Position position) : GameObject(position), mHealth(100){}

    void display(){
        GameObject::display();
        cout << "Health: " << mHealth << endl;
    }

    void move(string direction){
        if(direction == "left"){
            mPosition.mX--;
        }
        else if(direction == "right"){
            mPosition.mX++;
        }

        else if(direction == "up"){
            mPosition.mY++;
        }
        else if(direction == "down"){
            mPosition.mY--;
        }
    }

};

/*
Création d'une classe Player héritant de Character. Player n'a pas de membre en plus de ceux hérités pour l'instant
*/

class Player : public Character{
    public:
        Player(Position position) : Character(position){}

};

class Zombie : public Character {
public:
    // Ajouter un constructeur par défaut
    Zombie() : Character(Position{0, 0}) {} // Vous pouvez initialiser la position du zombie à (0, 0) par défaut si nécessaire

    // Garder le constructeur existant si nécessaire
    Zombie(Position position) : Character(position) {}
};



class Exit : public GameObject{
    public:
        Exit(Position position) : GameObject(position){}

};

/*
la classe Map représente le terrain du jeu avec un vecteur de vecteurs de tuiles (. : tuile vide)
les game objects sont représentés avec leur attribut code selon l'affichage suivant
Zombie
...........E
............
........S...
............
P...........
LIFE:100
Player move:


la classe Map a un attribut tiles, une méthode void create() affectant à l'attribut tiles
un vecteur de vecteurs de tuiles (. : tuile vide) pour représenter le terrain de 5 lignes et 10 colonnes
une méthode draw(self) affichant les caractères stockés dans tiles et une méthode void_set_title(Position position, char code)
modifiant tiles avec le code en fonction de la position. 
*/
class Map{
    public:
        vector<vector<char>> tiles;

    Map(){
        tiles = vector<vector<char>>(5, vector<char>(10, '.'));
    }

    void create(){
        tiles = vector<vector<char>>(5, vector<char>(10, '.'));
    }

    void draw() {
    // Vérifier que les dimensions du vecteur sont correctes
    if (tiles.empty() || tiles[0].empty()) {
        cout << "La carte est vide." << endl;
        return;
    }

    for (int i = 0; i < tiles.size(); i++) {
        for (int j = 0; j < tiles[i].size(); j++) {
            cout << tiles[i][j];
        }
        cout << endl;
    }
    }

    void set_tile(Position position, char code) {
    // Vérifier si les coordonnées sont valides
    if (position.mY >= 0 && position.mY < tiles.size() &&
        position.mX >= 0 && position.mX < tiles[0].size()) {
        tiles[position.mY][position.mX] = code;
    } else {
        cout << "Erreur : Position en dehors des limites de la carte." << endl;
    }
    }


};


/*
Classe GameManager qui a un attribut mPlayer et mZombie initialisés dans le constructeur. Le player est en (0,0) et le zombie en (5,5)
*/

class GameManager{
    private:
    void placeZombieRandomly() {
        // Initialiser le générateur de nombres aléatoires avec le temps actuel
        srand(time(NULL));

        do {
            // Générer des coordonnées aléatoires pour le zombie
            int randomX = rand() % mMap.tiles[0].size();
            int randomY = rand() % mMap.tiles.size();

            // Vérifier si le zombie respecte la règle
            if (abs(randomX - mPlayer.mPosition.mX) >= 3 && abs(randomY - mPlayer.mPosition.mY) >= 3) {
                // Si les coordonnées respectent la règle, placer le zombie à cet emplacement
                mZombie.mPosition.mX = randomX;
                mZombie.mPosition.mY = randomY;
                break; // Sortir de la boucle do-while
            }
        } while (true);
    }

    public:
        Player mPlayer;
        Zombie mZombie;
        bool mGameOver;
        Exit mExit;
        Map mMap;
    

    GameManager() 
    : mPlayer(Position{0, 0}), mGameOver(false), mExit(Position{9, 4}) {
        placeZombieRandomly();
    }

    void player_turn() {
        string direction;
        cout << "Entrez la direction. z : avancer, s : reculer, q : aller a gauche, d : aller a droite : " << endl;
        cin >> direction;
        
        // Variables pour stocker les nouvelles positions du joueur
        int newX = mPlayer.mPosition.mX;
        int newY = mPlayer.mPosition.mY;

        // Déterminer la nouvelle position en fonction de la direction
        if (direction == "z") {
            newY++;
        } else if (direction == "s") {
            newY--;
        } else if (direction == "q") {
            newX--;
        } else if (direction == "d") {
            newX++;
        } else {
            direction = "idle";
        }

        // Vérifier si la nouvelle position est à l'intérieur des limites de la carte
        if (newX >= 0 && newX < mMap.tiles[0].size() && newY >= 0 && newY < mMap.tiles.size()) {
            // La nouvelle position est valide, mettre à jour la position du joueur
            mPlayer.mPosition.mX = newX;
            mPlayer.mPosition.mY = newY;
        } else {
            // La nouvelle position est en dehors des limites, mettre le joueur en mode idle
            direction = "idle";
        }
    }

    


    void zombie_turn() {
        // Calculer les déplacements du zombie en fonction de la position du joueur
        int delta_x = 0;
        int delta_y = 0;

        if (mPlayer.mPosition.mX > mZombie.mPosition.mX) {
            delta_x = 1;
        } else if (mPlayer.mPosition.mX < mZombie.mPosition.mX) {
            delta_x = -1;
        }

        if (mPlayer.mPosition.mY > mZombie.mPosition.mY) {
            delta_y = 1;
        } else if (mPlayer.mPosition.mY < mZombie.mPosition.mY) {
            delta_y = -1;
        }

        // Calculer les nouvelles positions du zombie en maintenant une case de décalage avec le joueur
        int newX = mPlayer.mPosition.mX - delta_x;
        int newY = mPlayer.mPosition.mY - delta_y;

        // Vérifier si la nouvelle position est à l'intérieur des limites de la carte
        if (newX >= 0 && newX < mMap.tiles[0].size() && newY >= 0 && newY < mMap.tiles.size()) {
            // Mettre à jour la position du zombie
            mZombie.mPosition.mX = newX;
            mZombie.mPosition.mY = newY;

            // Vérifier si le joueur est adjacent au zombie après le déplacement
            if ((abs(mPlayer.mPosition.mX - mZombie.mPosition.mX) <= 1) || (abs(mPlayer.mPosition.mY - mZombie.mPosition.mY) <= 1)) {
                // Si le joueur est adjacent au zombie, réduire les points de vie du joueur
                mPlayer.mHealth--;
            }
        }

        // Vérifier si le joueur est mort
        if (mPlayer.mHealth <= 0) {
            cout << "Game over" << endl;
            system("pause");
            mGameOver = true; // Définir le jeu comme terminé
        }
    }
    

    void draw_title(){
        cout << "Zombie" << endl;
    }

    void draw_life(){
        cout << "LIFE: " << mPlayer.mHealth << endl;
    }

    /*méthode game_loop() qui dans une boucle tant que GameOver==false, 
    1. efface l'ecran
    2. affiche le titre
    3. affiche le joueur
    4. affiche le zombie
    5. affiche la sortie
    6. affiche la vie du joueur
    7. appelle player_turn()
    8. appelle zombie_turn()
    */
    void game_loop(){
        while(!mGameOver){
            system("CLS");
            draw_title();
            mMap.draw();
            mPlayer.display();
            mZombie.display();
            mExit.display();
            draw_life();
            player_turn();
            zombie_turn();
            mMap.create();
            mMap.set_tile(mPlayer.mPosition, 'P');
            mMap.set_tile(mZombie.mPosition, 'Z');
            mMap.set_tile(mExit.mPosition, 'E');
            //Vérifier si le joueur a atteint la sortie et afficher "You win !" s'il l'a atteinte
            if(mPlayer.mPosition.mX == mExit.mPosition.mX && mPlayer.mPosition.mY == mExit.mPosition.mY){
                mGameOver = true;
                cout << "You win !" << endl;
                system("pause");
            }
        }
    }
};



int main(){
    GameManager gameManager;
    gameManager.game_loop();
    return 0;
}

