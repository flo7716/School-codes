package ds1;

import java.util.Date;
public class Bibliotheque {
    Document[] stock;
    public Bibliotheque(Document[] stock){
        this.stock = stock;
    }
    public Document[] getStock() {
        return stock;
    }
    public void setStock(Document[] stock) {
        this.stock = stock;
    }

    public void ajouterDoc(Document doc){
        Document[] newStock = new Document[stock.length + 1];
        for (int i = 0; i < stock.length; i++) {
            newStock[i] = stock[i];
        }
        newStock[stock.length] = doc;
        stock = newStock;
    }

    public void emprunterDoc(Document doc){
        for (int i = 0; i < stock.length; i++) {
            if (stock[i].equals(doc)) {
                stock[i].setNbex_disponibles(stock[i].getNbex_disponibles() - 1);
            }
        }
    }
    public void rendreDoc(Document doc){
        for (int i = 0; i < stock.length; i++) {
            if (stock[i].equals(doc)) {
                stock[i].setNbex_disponibles(stock[i].getNbex_disponibles() + 1);
            }
        }
    }
    public void afficherStock(){
        for (int i = 0; i < stock.length; i++) {
            System.out.println(stock[i].toString());
        }
    }

    public static void main(String[] args) {
        Document[] stock = new Document[3];
        stock[0] = new Document("D1", "Mathematiques", "Algebre", "Livre", new Date(2020, 10, 10), "Francais", 5, 5);
        stock[1] = new Document("D2", "Informatique", "Programmation", "Livre", new Date(2020, 10, 10), "Francais", 5, 5);
        stock[2] = new Document("D3", "Mathematiques", "Analyse", "Livre", new Date(2020, 10, 10), "Francais", 5, 5);
        Bibliotheque b = new Bibliotheque(stock);
        b.afficherStock();
        Document doc = new Document("D1", "Mathematiques", "Algebre", "Livre", new Date(2020, 10, 10), "Francais", 5, 5);
        b.emprunterDoc(doc);
        b.afficherStock();
        b.rendreDoc(doc);
        b.afficherStock();
    }
}
