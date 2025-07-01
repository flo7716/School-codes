package ds1;

public class RobotNG extends Robot {
    private boolean turbo;

    public RobotNG(String nom, boolean turbo) {
        super(nom);
        this.turbo = turbo;
    }

    public boolean isTurbo() {
        return turbo;
    }

    public void setTurbo(boolean turbo) {
        this.turbo = turbo;
    }

    public void avance(int pas){
        if (turbo) {
            pas *= 3;
        }
        for(int i = 0; i < pas; i++){
            super.avance();
        }
    }

    public void gauche(){
        for (int i = 0; i < 3; i++) {
            super.droite();
        }
    }


    public void demiTour(){
        for (int i = 0; i < 2; i++) {
            super.droite();
        }
    }


    public static void main(String[] args) {
        RobotNG r = new RobotNG("R2D2", true);
        r.avance(3);
        System.out.println(r);
        r.gauche();
        System.out.println(r);
        r.demiTour();
        System.out.println(r);
    }

}
