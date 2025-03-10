package ds1;
public class Robot {
    private String nom;
    public float x;
    public float y;
    private String direction;
    public String getNom() {
        return nom;
    }

    

    public Robot(String nom) {
        this.nom = nom;
        this.x = 0;
        this.y = 0;
        this.direction = "Est";
    }



    public void setNom(String nom) {
        this.nom = nom;
    }
    public float getX() {
        return x;
    }
    public void setX(float x) {
        this.x = x;
    }
    public float getY() {
        return y;
    }
    public void setY(float y) {
        this.y = y;
    }
    public String getDirection() {
        return direction;
    }
    public void setDirection(String direction) {
        this.direction = direction;
    }

    public void avance(){
        if(getDirection() == "Est"){
            this.x++;
        }
        if(getDirection() == "Ouest"){
            this.x--;
        }
        if(getDirection() == "Nord"){
            this.y++;
        }
        else{
            this.y--;
        }
    }

    public void droite(){
        if(getDirection() == "Est"){
            this.setDirection("Sud");
        }
        if(getDirection() == "Ouest"){
            this.setDirection("Nord");
        }
        if(getDirection() == "Nord"){
            this.setDirection("Est");
        }
        else{
            this.setDirection("Ouest");
        }
    }

    public static void main(String[] args) {
        Robot r1 = new Robot("R1");
        Robot r2 = new Robot("R2");
        
        r1.avance();
        r2.avance();
        r1.droite();
        r1.getX();
        r1.getY();
        r2.getX();
        r2.getY();
    }

}
