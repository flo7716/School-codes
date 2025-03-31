import java.util.Date;
import java.util.List;

public class Livre extends Document{
    private List<String> auteurs;
    private String maisonEdition;
    private String isbn;

    public Livre(String code, String discipline, String theme, Date dateEdition, String langue, int nombreExemplaires, List<String> auteurs, String maisonEdition, String isbn) {
        super(code, discipline, theme, "Livre", dateEdition, langue, nombreExemplaires);
        this.auteurs = auteurs;
        this.maisonEdition = maisonEdition;
        this.isbn = isbn;
    }

    @Override
    public void afficherDetails() {
        System.out.println("Livre: " + theme + " - " + maisonEdition + " (ISBN: " + isbn + ")");
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

    public static void main(String[] args) {
        Livre livre = new Livre("L001", "Informatique", "Java", new Date(), "Français", 5, List.of("John Doe", "Jane Doe"), "Edition A", "1234567890");
        livre.afficherDetails();
    }
}
