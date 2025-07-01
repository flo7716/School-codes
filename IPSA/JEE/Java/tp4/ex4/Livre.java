import java.util.Date;
import java.util.List;

public class Livre extends Document{
    private List<String> auteurs;
    private String maisonEdition;
    private String isbn;
    private int nombreExemplaires;
    private int numeroInventaire;

    public Livre(String code, String discipline, String theme, String type, Date dateEdition, String langue,
            int nombreExemplaires, List<String> auteurs, String maisonEdition, String isbn, int nombreExemplaires2,
            int numeroInventaire) {
        super(code, discipline, theme, type, dateEdition, langue, nombreExemplaires);
        this.auteurs = auteurs;
        this.maisonEdition = maisonEdition;
        this.isbn = isbn;
        this.nombreExemplaires = nombreExemplaires;
        this.numeroInventaire = numeroInventaire;        
    }

    public List<String> getAuteurs() {
        return auteurs;
    }

    public void setAuteurs(List<String> auteurs) {
        this.auteurs = auteurs;
    }

    public String getMaisonEdition() {
        return maisonEdition;
    }

    public void setMaisonEdition(String maisonEdition) {
        this.maisonEdition = maisonEdition;
    }

    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public int getNombreExemplaires() {
        return nombreExemplaires;
    }

    public void setNombreExemplaires(int nombreExemplaires) {
        this.nombreExemplaires = nombreExemplaires;
    }

    public int getNumeroInventaire() {
        return numeroInventaire;
    }

    public void setNumeroInventaire(int numeroInventaire) {
        this.numeroInventaire = numeroInventaire;
    }

    

    

    
}
