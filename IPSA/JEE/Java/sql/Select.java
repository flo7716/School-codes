
import java.util.List;

public class Select extends Requete{
    private List<Champ> champs;
    private Table table;
    private Condition condition;
    public Select(String nom, List<Champ> champs, Table table, Condition condition) {
        super(nom);
        this.champs = champs;
        this.table = table;
        this.condition = condition;
    }
    public List<Champ> getChamps() {
        return champs;
    }
    public void setChamps(List<Champ> champs) {
        this.champs = champs;
    }
    public Table getTable() {
        return table;
    }
    public void setTable(Table table) {
        this.table = table;
    }
    public Condition getCondition() {
        return condition;
    }
    public void setCondition(Condition condition) {
        this.condition = condition;
    }

    public static void main(String[] args) {
        Champ champ1 = new Champ("nom");
        Champ champ2 = new Champ("prenom");
        Table table = new Table("personne");
        Condition condition = new Condition("nom", "prenom", "=");
        Select select = new Select("SELECT", List.of(champ1, champ2), table, condition);
        System.out.println(select.getNom() + " " + select.getChamps() + " FROM " + select.getTable() + " WHERE " + select.getCondition() + ";");
    }

    
}