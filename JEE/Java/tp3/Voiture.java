package tp3;

public class Voiture {
    public String marque;
    public int nbchevaux;
    public String[] options;

    public Voiture(String marque, int nbchevaux, String[] options) {
        this.marque = marque;
        this.nbchevaux = nbchevaux;
        this.options = options;
    }

    public void affiche() {
        System.out.println("Marque : " + marque);
        System.out.println("Nombre de chevaux : " + nbchevaux);
        System.out.println("Options : ");
        for (String option : options) {
            System.out.println("- " + option);
        }
    }

    public void demarrer() {
        System.out.println("Demarrage OK !");
    }

    public static void main(String[] args) {
        String[] options = {"GPS", "Climatisation", "Vitres electriques"};
        Voiture voiture = new Voiture("Toyota", 200, options);
        voiture.affiche();
        voiture.demarrer();
    }
}
