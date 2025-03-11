public class Logiciel {
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


    
}
