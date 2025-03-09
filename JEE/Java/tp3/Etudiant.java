package tp3;
public class Etudiant extends Personne {
    private String section;
    private int joursAbsence;
        
    public Etudiant(String nom, String prenom, int age, String section, int joursAbsence) {
        super(nom, prenom, age); // Ensure the Personne class has a matching constructor
        this.section = section;
        this.joursAbsence = joursAbsence;
    }
        
    @Override
    public void afficher() {
        super.afficher();
        System.out.println("Section : " + section);
        System.out.println("Jours d'absence : " + joursAbsence);
    }

    public static void main(String[] args) {
        Etudiant e1 = new Etudiant("Doe", "John", 30, "Mathématiques", 5);
        Etudiant e2 = new Etudiant("Smith", "Jane", 35, "Physique", 10);
        e1.afficher();
        e2.afficher();
    }
}
