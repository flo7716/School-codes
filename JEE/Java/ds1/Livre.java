package ds1;

import java.util.Date;
import java.util.List;

public class Livre extends Document {
    private String maison_edition;
    private List<Auteur> auteurs;
    private String code_isbn;

    public Livre(String code, String discipline, String theme, String type, Date date_edition, String langue,
            int nombre_exemplaires, int nbex_disponibles, String maison_edition, List<Auteur> auteurs,
            String code_isbn) {
        super(code, discipline, theme, type, date_edition, langue, nombre_exemplaires, nbex_disponibles);
        this.maison_edition = maison_edition;
        this.auteurs = auteurs;
        this.code_isbn = code_isbn;
    }

    public String getMaison_edition() {
        return maison_edition;
    }

    public void setMaison_edition(String maison_edition) {
        this.maison_edition = maison_edition;
    }

    public List<Auteur> getAuteurs() {
        return auteurs;
    }

    public void setAuteurs(List<Auteur> auteurs) {
        this.auteurs = auteurs;
    }

    public String getCode_isbn() {
        return code_isbn;
    }

    public void setCode_isbn(String code_isbn) {
        this.code_isbn = code_isbn;
    }

    
    


    
}
