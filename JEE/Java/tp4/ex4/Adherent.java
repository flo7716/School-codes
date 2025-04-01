public class Adherent {
    private String code;
    private String nom;
    private String prenom;
    private String email;
    
    public Adherent(String code, String nom, String prenom, String email) {
        this.code = code;
        this.nom = nom;
        this.prenom = prenom;
        this.email = email;
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

    public void afficherDetails() {
        System.out.println("Adhérent: " + getNom() + " " + getPrenom() + " (" + getEmail() + ")");
    }

    public static void main(String[] args) {
        Adherent adherent = new Adherent("A001", "Doe", "John", "john.doe@example.com");
        adherent.afficherDetails();
    }
}
