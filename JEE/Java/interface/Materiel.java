public class Materiel implements Produit {
    private String designation;
    private float prixUnitaire;
    private float quantite;
    
    public Materiel(String designation, float prixUnitaire, float quantite) {
        this.designation = designation;
        this.prixUnitaire = prixUnitaire;
        this.quantite = quantite;
    }

    public String getDesignation() { return designation; }
    public float getPrixUnitaire() { return prixUnitaire; }
    public float getQuantite() { return quantite; }
    public char getNature() { return 'M'; }
}