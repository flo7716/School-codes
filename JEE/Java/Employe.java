public class Employe{
    private String nom, prenom;
    private double salaire;

    // Constructeurs
    public Employe() {}

    public Employe(String n, String p){
        nom = n;
        prenom = p;
    }

    public Employe(String n, String p, double s){
        nom = n;
        prenom = p;
        salaire = s;
    }

    public static void main(String[] args) {
        Em1 = Employe("Dupont", "Pascal");
        Em2 = Employe("Durand", "Jacques", 12000);
    }
}





