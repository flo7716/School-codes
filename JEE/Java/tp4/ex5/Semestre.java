import java.util.ArrayList;
import java.util.List;
public class Semestre {
    private String nom;
    private List<Module> modules;
    private int nb_max_modules = 4;

    public Semestre(String nom) {
        this.nom = nom;
        // Initialize the list of modules with a maximum size
        this.modules = new ArrayList<>(nb_max_modules); 

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
