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

    public Point(){
        this.x = 1;
        this.y = 2;
    }

    public static void initialize(Point p1, Point p2){
        p1.x = 0;
        p1.y = 0;
        p2.x = 0;
        p2.y = 0;
    }

    public void deplace(float dx, float dy){
        x += dx;
        y += dy;
    }

    public void affiche(){
        System.out.println(((Float)this.x).toString() + " " + ((Float)this.y).toString());
    }

    public void setX(float x){
        this.x = x;
    }

    public float getY(){
        return this.y;
    }

    public static void main(String[] args) {
        Point p1 = new Point(0, 0);
        Point p2 = new Point(p1);
        Point p3 = new Point();
        p1.affiche();
        p2.affiche();
        p3.affiche();
        initialize(p1, p2);
        p1.deplace(1, 2);
        p2.deplace(3, 4);
        p2.setX(12);
        p2.getY();
        p1.affiche();
        p2.affiche();
        p3.affiche();
    }


}