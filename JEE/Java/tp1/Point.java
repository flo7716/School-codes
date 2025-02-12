package tp1;
public class Point{
    private float x, y;
    public Point(float x, float y){
        this.x = x;
        this.y = y;
    }

    public Point(Point p){
        this.x = p.x;
        this.y = p.y;
    }



    public static void initialize(Point p1, Point p2){
        p1.x = 0;
        p1.y = 0;
        p2.x = 0;
        p2.y = 0;
    }

    public static void deplace(Point p, float dx, float dy){
        p.x += dx;
        p.y += dy;
    }

    public static void affiche(Point p){
        System.out.println("Point: (" + p.x + ", " + p.y + ")");
    }

    public void setX(float x){
        this.x = x;
    }

    public void getY(float y){
        this.y = y;
    }

    public static void main(String[] args) {
        Point p1 = new Point(0, 0);
        Point p2 = new Point(0, 0);
        initialize(p1, p2);
        deplace(p1, 1, 2);
        deplace(p2, 3, 4);
        p2.setX(12);
        affiche(p1);
        affiche(p2);
    }


}