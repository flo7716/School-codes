package tp3;

public class Concession {
    Voiture[] stock;
    public Concession(Voiture[] stock){
        this.stock = stock;
    }

    public void ajoutVoiture(Voiture voiture){
        Voiture[] newStock = new Voiture[stock.length + 1];
        for (int i = 0; i < stock.length; i++){
            newStock[i] = stock[i];
        }
        newStock[stock.length] = voiture;
        stock = newStock;
    }

    public void affiche(){
        for (Voiture voiture : stock){
            voiture.affiche();
        }
    }

    public void rechercheOptions(String option){
        for (Voiture voiture : stock){
            for (String opt : voiture.options){
                if (opt.equals(option)){
                    voiture.affiche();
                }
            }
        }
    }

    public static void main(String[] args){
        String[] op1={"ABS", "GPS"};
        String[] op2={"ABS", "autoradio", "jantes alu"};
        String[] op3={"GPS", "sieges cuir"};
        Voiture v1=new Voiture("Audi", 120, op1);
        Voiture v2=new Voiture("Peugeot", 80, op2);
        VoitureCourse v3=new VoitureCourse("BMW", 250, op3, true);
        v1.demarrer();
        v3.demarrer();
        Concession c=new Concession(new Voiture[]{v1});
        c.ajoutVoiture(v2);
        c.ajoutVoiture(v3);
        c.affiche();
        c.rechercheOptions("GPS");
        }


}