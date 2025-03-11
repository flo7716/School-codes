public class Logiciel implements Produit{
    private String Designation;
    private float PrixUnitaire;
    private float Quantite;
    private String Editeur;
    private String AnneeEdition;
    public Logiciel(String designation, float prixUnitaire, float quantite, String editeur, String anneeEdition) {
        Designation = designation;
        PrixUnitaire = prixUnitaire;
        Quantite = quantite;
        Editeur = editeur;
        AnneeEdition = anneeEdition;
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
    public String getEditeur() {
        return Editeur;
    }
    public void setEditeur(String editeur) {
        Editeur = editeur;
    }
    public String getAnneeEdition() {
        return AnneeEdition;
    }
    public void setAnneeEdition(String anneeEdition) {
        AnneeEdition = anneeEdition;
    }


    public static void main(String[] args) {
        Logiciel logiciel = new Logiciel("Windows 10", 100, 10, "Microsoft", "2015");
        System.out.println("Designation: " + logiciel.getDesignation());
        System.out.println("Prix unitaire: " + logiciel.getPrixUnitaire());
        System.out.println("Quantite: " + logiciel.getQuantite());
        System.out.println("Editeur: " + logiciel.getEditeur());
        System.out.println("Annee d'edition: " + logiciel.getAnneeEdition());
    }
}
