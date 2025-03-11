public class Materiel {
    private String Designation;
    private float PrixUnitaire;
    private float Quantite;
    private char Nature;

    public Materiel(String designation, float prixUnitaire, float quantite) {
        Designation = designation;
        PrixUnitaire = prixUnitaire;
        Quantite = quantite;
    }

    public String getDesignation() {
        return Designation;
    }

    public void setDesignation(String designation) {
        Designation = designation;
    }

    public float getPrixUnitaire() {
        return PrixUnitaire;
    }

    public void setPrixUnitaire(float prixUnitaire) {
        PrixUnitaire = prixUnitaire;
    }

    public float getQuantite() {
        return Quantite;
    }

    public void setQuantite(float quantite) {
        Quantite = quantite;
    }

    public char getNature() {
        return Nature;
    }

    public void setNature(char nature) {
        Nature = nature;
    }

    

    
}
