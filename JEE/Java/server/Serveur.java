
import java.net.ServerSocket;

public class Serveur {
    public static void main(String[] args) {
        int port = 8080;
        try {
            ServerSocket ss = new ServerSocket(port);
            System.out.println("Serveur en attente de connexion sur le port " + port);
        } catch (Exception e) {
        }
    }
}
