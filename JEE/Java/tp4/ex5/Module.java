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
}

