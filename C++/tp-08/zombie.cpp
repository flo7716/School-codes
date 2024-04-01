#include <iostream>
#include <vector>
#include <map>
#include <string>
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
        cout << "G<" << mPosition.mX << ", " << mPosition.mY << ">" << endl;
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

class Zombie : public Character{
    public:
        Zombie(Position position) : Character(position){}

};


class Exit : public GameObject{
    public:
        Exit(Position position) : GameObject(position){}

};

/*
Classe GameManager qui a un attribut mPlayer et mZombie initialisés dans le constructeur. Le player est en (0,0) et le zombie en (5,5)
*/

class GameManager{
    public:
        Player mPlayer;
        Zombie mZombie;
        bool mGameOver;
        Exit mExit;
    

    GameManager(){
        mPlayer = Player(Position{0, 0});
        mZombie = Zombie(Position{5, 5});
        mGameOver = false;
        mExit = Exit(Position{9, 4});
    }

    void player_turn(){
        string direction;
        cout << "Entrez la direction. z : avancer, s : reculer, q : aller a gauche, d : aller a droite"<<endl;
        cin >> direction;
        if(direction == "z"){
            mPlayer.move("up");
        }
        else if(direction == "s"){
            mPlayer.move("down");
        }
        else if(direction == "q"){
            mPlayer.move("left");
        }
        else if(direction == "d"){
            mPlayer.move("right");
        }
        else{
            direction="idle";
        }
    }

    void zombie_turn(){
        int delta_x;
        int delta_y;

        if(mPlayer.mPosition.mX > mZombie.mPosition.mX){
            delta_x = 1;
            mZombie.move("right");
        }
        if(mPlayer.mPosition.mX < mZombie.mPosition.mX){
            delta_x = -1;
            mZombie.move("left");
        }
        if(mPlayer.mPosition.mY > mZombie.mPosition.mY){
            delta_y = 1;
            mZombie.move("down");
        }
        if(mPlayer.mPosition.mY < mZombie.mPosition.mY){
            delta_y = -1;
            mZombie.move("up");
        }
        if(mPlayer.mPosition.mX == mZombie.mPosition.mX && mPlayer.mPosition.mY == mZombie.mPosition.mY){
            mPlayer.mHealth--;
        }
        if(mPlayer.mHealth <= 0){
            mGameOver = true;
        }
    }
    void draw_title(){
        cout << "Zombie" << endl;
    }

    void draw_life(){
        cout << "LIFE: " << mPlayer.mHealth << endl;
    }

    void game_loop(){
        while(mGameOver==False){
            system("cls");
            draw_title();
            
        }
    }
};

