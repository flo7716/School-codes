import java.util.ArrayList;
import java.util.List;
public class BaseDeDonnees {
    private List<Table> tables;
    
    public BaseDeDonnees() {
        this.tables = new ArrayList<>();
    }
    
    public void ajouterTable(Table table) {
        tables.add(table);
    }
    
    public void afficherStructure() {
        for (Table table : tables) {
            table.afficherStructure();
        }
    }
    
    public void afficherDonnees() {
        for (Table table : tables) {
            table.afficherDonnees();
        }
    }

    public static void main(String[] args) {
        BaseDeDonnees bd = new BaseDeDonnees();
        
        Table t1 = new Table("Personne");
        t1.ajouterChamp(new Champ("nom", "String", 50));
        t1.ajouterChamp(new Champ("age", "int", 0));
        t1.ajouterTuple(new Tuple(List.of("Alice", 25)));
        t1.ajouterTuple(new Tuple(List.of("Bob", 30)));
        
        Table t2 = new Table("Adresse");
        t2.ajouterChamp(new Champ("rue", "String", 100));
        t2.ajouterChamp(new Champ("ville", "String", 50));
        t2.ajouterTuple(new Tuple(List.of("rue de la Paix", "Paris")));
        t2.ajouterTuple(new Tuple(List.of("rue de la Joie", "Lyon")));
        
        bd.ajouterTable(t1);
        bd.ajouterTable(t2);
        
        bd.afficherStructure();
        bd.afficherDonnees();
    }
}