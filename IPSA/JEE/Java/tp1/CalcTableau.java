public class CalcTableau {
    public static double somme(double[] tab) {
        double somme = 0;
        for (double e : tab) {
            somme += e;
        }
        return somme;
    }

    public static double[] increment(double[] tab, double val) {
        for (int i = 0; i < tab.length; i++) {
            tab[i] += val;
        }
        return tab;
    }

    public static void main(String[] args) {
        double[] tab = {1.2,5.5,7.1};
        double Resultat = CalcTableau.somme(tab);
        System.out.println(Resultat);

        CalcTableau.increment(tab, 10);
        for (Object e : tab) {
            System.out.println(e);
        }
    }
}
