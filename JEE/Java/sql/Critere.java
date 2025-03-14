
import java.util.List;

public class Critere {
    private List<Condition> conditions;

    public Critere(List<Condition> conditions) {
        this.conditions = conditions;
    }

    public List<Condition> getConditions() {
        return conditions;
    }

    public void setConditions(List<Condition> conditions) {
        this.conditions = conditions;
    }

    public String toString() {
        return conditions.toString();
    }
    
}
