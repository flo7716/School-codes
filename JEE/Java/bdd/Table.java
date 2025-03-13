import java.util.ArrayList;
import java.util.List;
public class Table {
    private String nom;
    private List<Champ> champs;
    private List<Tuple> tuples;
    
    public Table(String nom) {
        this.nom = nom;
        this.champs = new ArrayList<>();
        this.tuples = new ArrayList<>();
    }
    
    public void ajouterChamp(Champ champ) {
        champs.add(champ);
    }
    
    public void ajouterTuple(Tuple tuple) {
        tuples.add(tuple);
    }
    
    public void afficherStructure() {
        System.out.println("Table: " + nom);
        for (Champ champ : champs) {
            System.out.println("Champ: " + champ.getNom() + ", Type: " + champ.getType() + ", Longueur: " + champ.getLongueur());
        }
    }
    
    public void afficherDonnees() {
        for (Tuple tuple : tuples) {
            System.out.println(tuple.getValeurs());
        }
    }
}