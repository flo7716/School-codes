#include <iostream>
#include <vector>
#include <cmath>

class Point {
private:
    double mX;
    double mY;

public:
    // Constructeur sans arguments
    Point() : mX(0), mY(0) {}

    // Constructeur avec arguments
    Point(double x, double y) : mX(x), mY(y) {}

    // Méthode pour afficher les coordonnées
    void display() {
        std::cout << "(" << mX << "," << mY << ")" << std::endl;
    }

    // Méthode pour calculer la distance à l'origine
    double distance_origine() {
        return sqrt(mX * mX + mY * mY);
    }

    // Méthode pour calculer la distance à un autre point
    double distance(Point& other_point) {
        return sqrt((mX - other_point.mX) * (mX - other_point.mX) + (mY - other_point.mY) * (mY - other_point.mY));
    }
};

int main() {
    // 1.2. Test du constructeur
    Point p1;
    std::cout << "Coordonnées de p1 : ";
    p1.display();

    p1 = Point(3, 4);
    std::cout << "Nouvelles coordonnées de p1 : ";
    p1.display();

    // 1.3. Affichage
    std::cout << "Affichage de p1 : ";
    p1.display();

    // 1.4. Constructeur avec arguments
    Point p2(5, 6);
    std::cout << "Coordonnées de p2 : ";
    p2.display();

    // 1.5. Ensemble de points
    std::vector<Point> points;
    for (int i = 0; i < 10; ++i) {
        points.push_back(Point(i, i));
    }

    std::cout << "Points dans le vecteur : " << std::endl;
    for (auto& point : points) {
        point.display();
    }

    // 1.6. Méthode sans argument avec valeur de retour
    Point p3(1, 1);
    double d1 = p3.distance_origine();
    std::cout << "Distance de p3 à l'origine : " << d1 << std::endl;

    // 1.7. Méthode avec argument de type Point et valeur de retour
    Point p4(10, 1);
    double d2 = p3.distance(p4);
    std::cout << "Distance entre p3 et p4 : " << d2 << std::endl;

    // 1.8. Utilisation du vecteur de points
    double d3 = points.back().distance(points.front());
    std::cout << "Distance entre le premier et le dernier point du vecteur : " << d3 << std::endl;

    return 0;
}
