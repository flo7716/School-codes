
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


    
}

