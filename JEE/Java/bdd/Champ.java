
public class Champ {
    private String nom;
    private String type;
    private int longueur;
    
    public Champ(String nom, String type, int longueur) {
        this.nom = nom;
        this.type = type;
        this.longueur = longueur;
    }
    
    public String getNom() { return nom; }
    public String getType() { return type; }
    public int getLongueur() { return longueur; }
}