import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Etudiant {
    private String CNE;
    private String CIN;
    private String nom;
    private String prenom;
    private Date dateNaissance;
    private String villeNaissance;
    private String Adresse;
    private String email;
    private List<Module> modulesInscrits;
    //niveau entre 1 et 5
    private int niveau;
    private float[] notes_par_semestre;

    public Etudiant(String cNE, String cIN, String nom, String prenom, Date dateNaissance, String villeNaissance,
            String adresse, String email, List<Module> modulesInscrits, int niveau, float[] notes_par_semestre) {
        CNE = cNE;
        CIN = cIN;
        this.nom = nom;
        this.prenom = prenom;
        this.dateNaissance = dateNaissance;
        this.villeNaissance = villeNaissance;
        Adresse = adresse;
        this.email = email;
        this.modulesInscrits = modulesInscrits;
        this.niveau = niveau;
        this.notes_par_semestre = notes_par_semestre;
    }

    public String getCNE() {
        return CNE;
    }

    public void setCNE(String cNE) {
        CNE = cNE;
    }

    public String getCIN() {
        return CIN;
    }

    public void setCIN(String cIN) {
        CIN = cIN;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }

    public Date getDateNaissance() {
        return dateNaissance;
    }

    public void setDateNaissance(Date dateNaissance) {
        this.dateNaissance = dateNaissance;
    }

    public String getVilleNaissance() {
        return villeNaissance;
    }

    public void setVilleNaissance(String villeNaissance) {
        this.villeNaissance = villeNaissance;
    }

    public String getAdresse() {
        return Adresse;
    }

    public void setAdresse(String adresse) {
        Adresse = adresse;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public List<Module> getModulesInscrits() {
        return modulesInscrits;
    }

    public void setModulesInscrits(List<Module> modulesInscrits) {
        this.modulesInscrits = modulesInscrits;
    }

    public int getNiveau() {
        return niveau;
    }

    public void setNiveau(int niveau) {
        this.niveau = niveau;
    }

    public float[] getNotes_par_semestre() {
        return notes_par_semestre;
    }

    public void setNotes_par_semestre(float[] notes_par_semestre) {
        this.notes_par_semestre = notes_par_semestre;
    }

    public static void main(String[] args) {
        Etudiant e1 = new Etudiant("CNE1", "CIN1", "Nom1", "Prenom1", new Date(), "Ville1", "Adresse1", "Email1", new ArrayList<Module>(), 1, new float[2]);
        Etudiant e2 = new Etudiant("CNE2", "CIN2", "Nom2", "Prenom2", new Date(), "Ville2", "Adresse2", "Email2", new ArrayList<Module>(), 2, new float[2]);
        
    }

    


    
}
