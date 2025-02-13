public class MoyenneTable {
    private double[] tab = new double[2];
    public MoyenneTable(String[] newTab){
        for (int i = 0; i < newTab.length; i++){
            tab[i] = Double.parseDouble(newTab[i]);
        }
    }



    public static void main(String[] args){
        String[] newTab = {"1.1","5.8"};
        MoyenneTable moy = new MoyenneTable(newTab);
        for (double e : moy.tab){
            System.out.println(e);
        }
    }



}
