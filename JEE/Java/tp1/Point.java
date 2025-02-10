package tp1;

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


}