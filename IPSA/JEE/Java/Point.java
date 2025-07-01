package tp2;
public class Point{
    private float x, y;
    public Point(float x, float y){
        this.x = x;
        this.y = y;
    }

    public static void initialize(Point p){
        p.x = 0;
        p.y = 0;
    }

    public static void deplace(Point p, float dx, float dy){
        p.x += dx;
        p.y += dy;
    }

    public static void affiche(Point p){
        System.out.println("Point: (" + p.x + ", " + p.y + ")");
    }

    public static void main(String[] args) {
        Point p = new Point(0, 0);
        initialize(p);
        deplace(p, 1, 2);
        affiche(p);
    }


}