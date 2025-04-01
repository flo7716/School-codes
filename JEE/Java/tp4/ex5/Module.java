import java.util.ArrayList;
import java.util.List;

public class Module {
    private String code;
    private String nom;
    private List<ElementModule> elements;

    public Module(String code, String nom) {
        this.code = code;
        this.nom = nom;
        this.elements = new ArrayList<>();
    }

    public void ajouterElement(ElementModule element) {
        elements.add(element);
    }

    public String getNom() {
        return nom;
    }

    public void afficherDetails() {
        System.out.println("Module: " + nom);
        System.out.println("Éléments du module:");
        for (ElementModule e : elements) {
            System.out.println(" - " + e.getNom());
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Module{");
        sb.append("code=").append(code);
        sb.append(", nom=").append(nom);
        sb.append(", elements=").append(elements);
        sb.append('}');
        return sb.toString();
    }

    public static void main(String[] args) {
        Module module = new Module("INFO1", "Informatique 1");
        ElementModule element1 = new ElementModule("Cours 1", 30);
        ElementModule element2 = new ElementModule("TP 1", 20);

        module.ajouterElement(element1);
        module.ajouterElement(element2);

        module.afficherDetails();
    }

    

    
}

