package ds1;

public class RobotNG extends Robot {
    private String Mode;
    private int pas;

    public RobotNG(String nom, String mode) {
        super(nom);
        Mode = mode;
    }

    

    public String getMode() {
        return Mode;
    }



    public void setMode(String mode) {
        Mode = mode;
    }



    public void avance(int pas){
        if(getDirection() == "Est"){
            super.x += pas;
        }
        if(getDirection() == "Ouest"){
            super.x -= pas;
        }
        if(getDirection() == "Nord"){
            super.y += pas;
        }
        else{
            super.y -= pas;
        }
    }


    public void gauche(){
        if(getDirection() == "Est"){
            this.setDirection("Nord");
        }
        if(getDirection() == "Ouest"){
            this.setDirection("Sud");
        }
        if(getDirection() == "Nord"){
            this.setDirection("Ouest");
        }
        else{
            this.setDirection("Est");
        }
    }

    public void demiTour(){
        if(getDirection() == "Est"){
            this.setDirection("Ouest");
        }
        if(getDirection() == "Ouest"){
            this.setDirection("Est");
        }
        if(getDirection() == "Nord"){
            this.setDirection("Sud");
        }
        else{
            this.setDirection("Nord");
        }
    }

    public void activation_Turbo(RobotNG robot){
        if(robot.getMode() == "Normal"){
            robot.setMode("Turbo");
            robot.getMode();
        }
    }


    public static void main(String[] args) {
        RobotNG
    }



}
