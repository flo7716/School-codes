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

    public boolean equals(Point p){
        return this.x == p.x && this.y == p.y;
    }

    public static void main(String[] args) {
        int n;
        char last;
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
        String ch = "Bonjour";
        n = ch.length();
        System.out.println(n);
        last = ch.charAt(n-1);
        System.out.println(last);



        String ch1 = "Hello";
        String ch2 = "Hello";

        System.out.println(ch1.equals(ch2));
        System.out.println(ch1.equals("Hello"));

        Point p4 = new Point(10, 20);
        Point p5 = new Point(10, 20);
        System.out.println(p4.equals(p5));


        String ch3 = "Anticonstitutionnellement";
        char tab[] = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'};
        for(char elem : tab){
            int cpt = 0;
            for(int i = 0; i < ch3.length(); i++){
                if(ch3.charAt(i) == elem){
                    cpt++;
                }
            }
            System.out.println(elem + " : " + cpt);
        }

    }


}