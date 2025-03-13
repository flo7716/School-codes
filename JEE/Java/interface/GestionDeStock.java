public class GestionDeStock {
    private LinkedList<Produit> stock = new LinkedList<>();
    
    public void ajouter(Produit p) {
        stock.add(p);
    }
    
    public void lister() {
        for (Produit p : stock) {
            System.out.println("Désignation: " + p.getDesignation() + ", PU: " + p.getPrixUnitaire() + ", Q: " + p.getQuantite() + ", Nature: " + p.getNature());
            if (p instanceof Logiciel) {
                Logiciel l = (Logiciel) p;
                System.out.println("  Editeur: " + l.getEditeur() + ", Année: " + l.getAnneeEdition());
            }
        }
    }

    public void MaJ(String designation, float prixUnitaire, float quantite, char nature, String editeur, String anneeEdition) {
        for (Produit p : stock) {
            if (p.getDesignation().equals(designation)) {
                p = new Logiciel(designation, prixUnitaire, quantite, nature, editeur, anneeEdition);
                return;
            }
        }
        System.out.println("Produit non trouvé.");
    }

    public void supprimer(String designation) {
        for (Produit p : stock) {
            if (p.getDesignation().equals(designation)) {
                stock.remove(p);
                return;
            }
        }
        System.out.println("Produit non trouvé.");
    }
}
