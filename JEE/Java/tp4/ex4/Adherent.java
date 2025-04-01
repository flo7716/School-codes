public class Adherent {
    private String code;
    private String nom;
    private String prenom;
    private String email;
    private Privilege privilege;
    private Emprunt[] emprunts;

    public Adherent(String code, String nom, String prenom, String email, Privilege privilege, Emprunt[] emprunts) {
        this.code = code;
        this.nom = nom;
        this.prenom = prenom;
        this.email = email;
        this.privilege = privilege;
        this.emprunts = emprunts;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
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

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Privilege getPrivilege() {
        return privilege;
    }

    public void setPrivilege(Privilege privilege) {
        this.privilege = privilege;
    }

    public Emprunt[] getEmprunts() {
        return emprunts;
    }

    public void setEmprunts(Emprunt[] emprunts) {
        this.emprunts = emprunts;
    }
    
    public static void main(String[] args) {
        Adherent adherent = new Adherent("A001", "Doe", "John", "john.doe@example.com", new Privilege("Prof", 10, 14), new Emprunt[0]);
        System.out.println("Adhérent: " + adherent.getNom() + " " + adherent.getPrenom() + " (Code: " + adherent.getCode() + ")" + 
                           ", Email: " + adherent.getEmail() + 
                           ", Privilège: " + adherent.getPrivilege().getNom() + 
                           ", Documents possibles: " + adherent.getPrivilege().getNb_docs_possibles() + 
                           ", Jours max d'emprunt: " + adherent.getPrivilege().getNb_jours_max_emprunt());
    }
    
}
