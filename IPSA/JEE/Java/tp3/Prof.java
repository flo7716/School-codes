package tp3;
public class Prof extends Personne {
    private String matiere;
    
    public Prof(String nom, String prenom, int age, String matiere) {
        super(nom, prenom, age);
        this.matiere = matiere;
    }
    
    @Override
    public void afficher() {
        super.afficher();
        System.out.println("Matière enseignée : " + matiere);
    }

    public static void main(String[] args) {
        Prof p1 = new Prof("Doe", "John", 30, "Mathématiques");
        Prof p2 = new Prof("Smith", "Jane", 35, "Physique");
        p1.afficher();
        p2.afficher();
    }
}
