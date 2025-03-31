import java.util.Date;
public class Revue extends Document {
    private String periodicite;

    public Revue(String code, String discipline, String theme, Date dateEdition, String langue, int nombreExemplaires, String periodicite) {
        super(code, discipline, theme, "Revue", dateEdition, langue, nombreExemplaires);
        this.periodicite = periodicite;
    }

    @Override
    public void afficherDetails() {
        System.out.println("Revue: " + theme + " - Périodicité: " + periodicite);
    }

    public String getPeriodicite() {
        return periodicite;
    }

    public void setPeriodicite(String periodicite) {
        this.periodicite = periodicite;
    }

    public static void main(String[] args) {
        Revue revue = new Revue("R001", "Informatique", "Java", new Date(), "Français", 10, "Mensuel");
        revue.afficherDetails();
    }
}

