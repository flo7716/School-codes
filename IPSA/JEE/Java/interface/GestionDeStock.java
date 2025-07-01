import java.util.LinkedList;
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
                System.out.println("  Editeur: " + l.getEditeur() + ", Année: " + l.getAE());
            }
        }
    }

    public void updater(Produit p, Produit updatedProduit) {
        for (int i = 0; i < stock.size(); i++) {
            if (stock.get(i).equals(p)) {
                stock.set(i, updatedProduit);
                break;
            }
        }
    }

    public void supprimer(Produit p) {
        stock.remove(p);
    }

    public static void main(String[] args) {
        GestionDeStock gds = new GestionDeStock();
        gds.ajouter(new Materiel("Souris", 10, 100));
        gds.ajouter(new Materiel("Clavier", 20, 50));
        gds.ajouter(new Logiciel("Windows", 100, 10, "Microsoft", 2018));
        gds.ajouter(new Logiciel("Office", 200, 5, "Microsoft", 2019));
        gds.updater(new Materiel("Souris", 10, 100), new Materiel("Souris", 10, 200));
        gds.supprimer(new Materiel("Clavier", 20, 50));
        gds.lister();
    }
}