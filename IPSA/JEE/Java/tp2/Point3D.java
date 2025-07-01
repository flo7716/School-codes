package tp2;
public class Point3D extends Point{
    private float z;
    
    public Point3D(float x, float y, float z) {
        
        super(x,y);
        this.z = z;
    }

    public void NouvelleMethode(){
        System.out.println("Nouvelle methode disponible seulement dans Point3D !");
    };

    public static void main(String[] args) {
        Point3D p = new Point3D(0, 0, 0);
        p.NouvelleMethode();
    }


}
