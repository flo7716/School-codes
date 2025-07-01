import java.util.Date;

// Classe de base pour un Document
public abstract class Document {
    protected String code;
    protected String discipline;
    protected String theme;
    protected String type;
    protected Date dateEdition;
    protected String langue;
    protected int nombreExemplaires;
    protected int exemplairesDisponibles;
    
    public Document(String code, String discipline, String theme, String type, Date dateEdition, String langue, int nombreExemplaires) {
        this.code = code;
        this.discipline = discipline;
        this.theme = theme;
        this.type = type;
        this.dateEdition = dateEdition;
        this.langue = langue;
        this.nombreExemplaires = nombreExemplaires;
        this.exemplairesDisponibles = nombreExemplaires;
    }
}
