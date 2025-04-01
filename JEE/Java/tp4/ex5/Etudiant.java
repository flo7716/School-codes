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



    public void inscrireModule(Module module) {
        modulesInscrits.add(module);
    }

    public void afficherDetails() {
        System.out.println("Étudiant: " + nom + " " + prenom);
        System.out.println("Modules inscrits:" + getModulesInscrits());
    }

    public static void main(String[] args) {
        Etudiant etudiant = new Etudiant("123", "Dupont", "Jean");
        Module module1 = new Module("INFO1", "Informatique 1");
        Module module2 = new Module("MAT1", "Mathématiques 1");

        etudiant.inscrireModule(module1);
        etudiant.inscrireModule(module2);

        etudiant.afficherDetails();
    }


}
