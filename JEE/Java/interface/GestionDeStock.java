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
}
