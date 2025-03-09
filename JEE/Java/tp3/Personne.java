package tp3;
public class Personne {
    private String nom;
    private String prenom;
    private int age;
    
    public Personne(String leNom, String lePrenom, int lAge) {
        this.nom = leNom;
        this.prenom = lePrenom;
        this.age = lAge;
    }
    
    public Personne(Personne p) {
        this.nom = p.nom;
        this.prenom = p.prenom;
        this.age = p.age;
    }
    
    public void afficher() {
        System.out.println("Nom : " + nom);
        System.out.println("Prenom : " + prenom);
        System.out.println("Age : " + age);
    }

    public static void main(String[] args) {
        Personne p1 = new Personne("Doe", "John", 30);
        Personne p2 = new Personne(p1);
        p1.afficher();
        p2.afficher();
    }
}
