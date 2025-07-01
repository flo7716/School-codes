public class chaine extends Type{
    private String chaine;
    private int longueur;
    public chaine(String chaine, int longueur) {
        super(chaine); // Call the superclass constructor with the required String argument
        this.chaine = chaine;
        this.longueur = longueur;
    }
    public String getChaine() {
        return chaine;
    }
    public void setChaine(String chaine) {
        this.chaine = chaine;
    }
    public int getLongueur() {
        return longueur;
    }
    public void setLongueur(int longueur) {
        this.longueur = longueur;
    }
}
