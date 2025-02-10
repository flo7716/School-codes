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

    public String getNom() {
        return nom;
    }

    public String getPrenom() {
        return prenom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }


    public static void main(String[] args) {
        Employe Em1 = new Employe("Dupont", "Pascal");
        Employe Em2 = new Employe("Durand", "Jacques", 12000);
    }
}





