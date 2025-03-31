import java.util.Date;
public class Emprunt {
    private String codeDocument;
    private String codeAdherent;
    private Date dateEmprunt;

    public Emprunt(String codeDocument, String codeAdherent, Date dateEmprunt) {
        this.codeDocument = codeDocument;
        this.codeAdherent = codeAdherent;
        this.dateEmprunt = dateEmprunt;
    }

    public String getCodeDocument() {
        return codeDocument;
    }

    public void setCodeDocument(String codeDocument) {
        this.codeDocument = codeDocument;
    }

    public String getCodeAdherent() {
        return codeAdherent;
    }

    public void setCodeAdherent(String codeAdherent) {
        this.codeAdherent = codeAdherent;
    }

    public Date getDateEmprunt() {
        return dateEmprunt;
    }

    public void setDateEmprunt(Date dateEmprunt) {
        this.dateEmprunt = dateEmprunt;
    }

    public static void main(String[] args) {
        Emprunt emprunt = new Emprunt("D001", "A001", new Date());
        System.out.println("Emprunt: Document " + emprunt.getCodeDocument() + " par Adhérent " + emprunt.getCodeAdherent() + " le " + emprunt.getDateEmprunt());
    }
}
