public class Logiciel implements Produit {
    private String designation;
    private float prixUnitaire;
    private float quantite;
    private String editeur;
    private int anneeEdition;

    public Logiciel(String designation, float prixUnitaire, float quantite, String editeur, int anneeEdition) {
        this.designation = designation;
        this.prixUnitaire = prixUnitaire;
        this.quantite = quantite;
        this.editeur = editeur;
        this.anneeEdition = anneeEdition;
    }

    public String getDesignation() { return designation; }
    public float getPrixUnitaire() { return prixUnitaire; }
    public float getQuantite() { return quantite; }
    public char getNature() { return 'L'; }
    public String getEditeur() { return editeur; }
    public int getAE() { return anneeEdition; }
}