import java.util.ArrayList;
import java.util.List;
public class Semestre {
    private String nom;
    private List<Module> modules;

    public Semestre(String nom) {
        this.nom = nom;
        this.modules = new ArrayList<>();
    }

    public void ajouterModule(Module module) {
        modules.add(module);
    }

    public void afficherDetails() {
        System.out.println("Semestre: " + nom);
        for (Module m : modules) {
            m.afficherDetails();
        }
    }
}
