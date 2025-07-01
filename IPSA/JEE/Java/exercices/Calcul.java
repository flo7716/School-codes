public class Calcul {
    public static int factoriel(int n) {
        if (n == 0) return 1;
        int result = 1;
        for (int i = 1; i <= n; i++) result *= i;
        return result;
    }
    
    public static double puissance(double base, int exposant) {
        return Math.pow(base, exposant);
    }
    
    public static double racineCarree(double nombre) {
        return Math.sqrt(nombre);
    }
    
    public static int partieEntiere(double nombre) {
        return (int) nombre;
    }

    public static void main(String[] args) {
        System.out.println("Factoriel de 5: " + factoriel(5));
        System.out.println("2^3: " + puissance(2, 3));
        System.out.println("Racine carrée de 9: " + racineCarree(9));
        System.out.println("Partie entière de 3.14: " + partieEntiere(3.14));
    }
}