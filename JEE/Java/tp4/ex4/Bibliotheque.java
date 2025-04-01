public class Bibliotheque {
    private Privilege privilege;
    private Adherent[] adherent;
    
    public Bibliotheque(Privilege privilege, Adherent[] adherent) {
        this.privilege = privilege;
        this.adherent = adherent;
    }

    public Privilege getPrivilege() {
        return privilege;
    }

    public void setPrivilege(Privilege privilege) {
        this.privilege = privilege;
    }

    public Adherent[] getAdherent() {
        return adherent;
    }

    public void setAdherent(Adherent[] adherent) {
        this.adherent = adherent;
    }

    public static void main(String[] args) {
        Privilege privilege = new Privilege("Etudiant", 5, 14);
        Adherent[] adherents = new Adherent[1];
        adherents[0] = new Adherent("123", "Dupont", "Jean", "jean.dupont@outlook.com", new Privilege("Eleve",5,14), new Emprunt[1]);
        
        Bibliotheque bibliotheque = new Bibliotheque(privilege, adherents);
        
        System.out.println("Bibliothèque: " + bibliotheque.getPrivilege().getNom());
        for (Adherent adherent : bibliotheque.getAdherent()) {
            System.out.println("Adhérent: " + adherent.getNom() + " " + adherent.getPrenom() + " " + adherent.getEmail() + " " + adherent.getPrivilege().getNom());
        }
    }
}
