public class Produit {
    private static int compteur = 0;
    private int ref;
    private String desig;
    private double pnx;
    private int q;
    
    private Produit(String desig, double pnx, int q) {
        this.ref = compteur++;
        this.desig = desig;
        this.pnx = pnx;
        this.q = q;
    }
    
    public static Produit creerProduit(String desig, double pnx, int q) {
        if (compteur < 10) return new Produit(desig, pnx, q);
        else return null;
    }

    public static void main(String[] args) {
        Produit p1 = Produit.creerProduit("Produit 1", 10.0, 5);
        Produit p2 = Produit.creerProduit("Produit 2", 20.0, 10);
        Produit p3 = Produit.creerProduit("Produit 3", 30.0, 15);
        Produit p4 = Produit.creerProduit("Produit 4", 40.0, 20);
        Produit p5 = Produit.creerProduit("Produit 5", 50.0, 25);
        
        System.out.println("Produit 1: " + p1.ref + " " + p1.desig + " " + p1.pnx + " " + p1.q);
        System.out.println("Produit 2: " + p2.ref + " " + p2.desig + " " + p2.pnx + " " + p2.q);
        System.out.println("Produit 3: " + p3.ref + " " + p3.desig + " " + p3.pnx + " " + p3.q);
        System.out.println("Produit 4: " + p4.ref + " " + p4.desig + " " + p4.pnx + " " + p4.q);
        System.out.println("Produit 5: " + p5.ref + " " + p5.desig + " " + p5.pnx + " " + p5.q);
        
    }
}
