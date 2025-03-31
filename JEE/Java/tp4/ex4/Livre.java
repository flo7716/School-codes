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
}
