package tp3;

public class VoitureCourse extends Voiture {
    public boolean aileron;
    public VoitureCourse(String marque, int nbchevaux, String[] options, boolean aileron){
        super(marque, nbchevaux, options);
        this.aileron = aileron;
    }
    public void affiche(){
        super.affiche();
        if (aileron){
            System.out.println("Je suis une voiture de course avec aileron");
        }
        else{
            System.out.println("Je suis une voiture de course sans aileron");
        }
    }

    public void demarrrer(){
        super.demarrer();
        System.out.println("Vrouuum");
    }

    public static void main(String[] args) {
        String[] options = {"GPS", "Climatisation", "Vitres electriques"};
        VoitureCourse voiture = new VoitureCourse("Toyota", 250, options, true);
        voiture.affiche();
        voiture.demarrrer();
    }
}
