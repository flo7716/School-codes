import java.util.List;
public class Tuple {
    private List<Object> valeurs;
    
    public Tuple(List<Object> valeurs) {
        this.valeurs = valeurs;
    }
    
    public List<Object> getValeurs() { return valeurs; }
}