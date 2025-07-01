package ds1;
public class Robot {
    private String nom;
    Position position;
    private String direction;
    public String getNom() {
        return nom;
    }

    

    public Robot(String nom) {
        this.nom = nom;
        this.position = new Position(0, 0);
        this.direction = "Est";
    }

    

    public void setNom(String nom) {
        this.nom = nom;
    }



    public String getDirection() {
        return direction;
    }



    public void setDirection(String direction) {
        this.direction = direction;
    }



    public void avance(){
        if(this.direction == "Est"){
            this.position.setY(this.position.getY() + 1);
        }
        if(this.direction == "Ouest"){
            this.position.setY(this.position.getY() - 1);
        }
        if(this.direction == "Nord"){
            this.position.setX(this.position.getX() + 1);
        }
        else{
            this.position.setX(this.position.getX() - 1);
        }
    }

    public void droite(){
        if(this.direction == "Est"){
            this.direction = "Sud";
        }
        if(this.direction == "Ouest"){
            this.direction = "Nord";
        }
        if(this.direction == "Nord"){
            this.direction = "Est";
        }
        else{
            this.direction = "Ouest";
        }
    }

    @Override
    public String toString() {
        return "Robot [nom=" + nom + ", position=" + position + ", direction=" + direction + "]";
    }



    public static void main(String[] args) {
        Robot r1 = new Robot("R1");
        Robot r2 = new Robot("R2");
        
        r1.avance();
        r2.avance();
        r1.droite();
        r1.position.getX();
        r1.position.getY();
        r2.position.getX();
        r2.position.getY();
    }

}
