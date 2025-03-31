import java.util.ArrayList;
import java.util.List;

public class Etudiant {
    private String id;
    private String nom;
    private String prenom;
    private List<Module> modulesInscrits;

    public Etudiant(String id, String nom, String prenom) {
        this.id = id;
        this.nom = nom;
        this.prenom = prenom;
        this.modulesInscrits = new ArrayList<>();
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }

    public List<Module> getModulesInscrits() {
        return modulesInscrits;
    }

    public void setModulesInscrits(List<Module> modulesInscrits) {
        this.modulesInscrits = modulesInscrits;
    }

    public static void main(String[] args) {
        Etudiant etudiant = new Etudiant("123", "Doe", "John");
        Module module1 = new Module("M1", "Mathematics", 3);
        Module module2 = new Module("M2", "Physics", 4);

        etudiant.getModulesInscrits().add(module1);
        etudiant.getModulesInscrits().add(module2);

        System.out.println("Etudiant: " + etudiant.getNom() + " " + etudiant.getPrenom());
        System.out.println("Modules inscrits:");
        for (Module module : etudiant.getModulesInscrits()) {
            System.out.println("- " + module.getNom() + " (Code: " + module.getCode() + ", Coefficient: " + module.getCoefficient() + ")");
        }
    }
}
