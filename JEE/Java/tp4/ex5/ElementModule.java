public class ElementModule {
    private String nom;
    private int coefficient;

    public ElementModule(String nom, int coefficient) {
        this.nom = nom;
        this.coefficient = coefficient;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getCoefficient() {
        return coefficient;
    }

    public void setCoefficient(int coefficient) {
        this.coefficient = coefficient;
    }
    
    public static void main(String[] args) {
        Module module = new Module("INFO1", "Informatique 1");
        ElementModule element1 = new ElementModule("Java", 3);
        ElementModule element2 = new ElementModule("BDD", 2);

        module.ajouterElement(element1);
        module.ajouterElement(element2);

        module.afficherDetails();
    }
}
