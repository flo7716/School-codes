public class Privilege {
    private String nom;
    private int nb_docs_possibles;
    private int nb_jours_max_emprunt;

    public Privilege(String nom, int nb_docs_possibles, int nb_jours_max_emprunt) {
        this.nom = nom;
        this.nb_docs_possibles = nb_docs_possibles;
        this.nb_jours_max_emprunt = nb_jours_max_emprunt;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getNb_docs_possibles() {
        return nb_docs_possibles;
    }

    public void setNb_docs_possibles(int nb_docs_possibles) {
        this.nb_docs_possibles = nb_docs_possibles;
    }

    public int getNb_jours_max_emprunt() {
        return nb_jours_max_emprunt;
    }

    public void setNb_jours_max_emprunt(int nb_jours_max_emprunt) {
        this.nb_jours_max_emprunt = nb_jours_max_emprunt;
    }

    public static void main(String[] args) {
        Privilege privilege = new Privilege("Etudiant", 5, 14);
        System.out.println("Privilege: " + privilege.getNom() + ", Documents possibles: " + privilege.getNb_docs_possibles() + ", Jours max d'emprunt: " + privilege.getNb_jours_max_emprunt());
    }

    
}
