package ds1;
public class Livre extends Document {
    private String[] liste_auteurs;
    private String code_isbn;
    public String[] getListe_auteurs() {
        return liste_auteurs;
    }
    public void setListe_auteurs(String[] liste_auteurs) {
        this.liste_auteurs = liste_auteurs;
    }
    public String getCode_isbn() {
        return code_isbn;
    }
    public void setCode_isbn(String code_isbn) {
        this.code_isbn = code_isbn;
    }


    public static void main(String[] args) {
        
    }

    
}
