package eval;
import java.util.Arrays;

public class Etudiant {
    String nom;
    String prenom;
    int numero;
    static int nbretucrees = 0;
    String [] courssuivis;
    int [] notes;


    public Etudiant(String nom, String prenom, String[] courssuivis) {
        this.nom = nom;
        this.prenom = prenom;
        this.courssuivis = courssuivis;
        nbretucrees = nbretucrees + 1;
        this.numero = nbretucrees;
        this.notes = new int[courssuivis.length];
        Arrays.fill(this.notes, 0);
    }

    
    @Override
    public String toString() {
        return "Etudiant [nom=" + nom + ", prenom=" + prenom + ", numero=" + numero + ", courssuivis="
                + Arrays.toString(courssuivis) + ", notes=" + Arrays.toString(notes) + ", toString()="
                + super.toString() + "]";
    }
    

    public static void main(String[] args) {
        Etudiant e1 = new Etudiant("Dupont", "Jean", new String[]{"Math", "Physique", "Anglais"});
        Etudiant e2 = new Etudiant("André","Florian", new String[]{"SVT", "Français", "Programmation"});
        e1.toString();
        e2.toString();
        System.out.println(e1.nom + " " + e1.prenom + " " + e1.numero);
        System.out.println(e2.nom + " " + e2.prenom + " " + e2.numero);
        
    }


    
}

