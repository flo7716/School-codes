import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Serveur {
    public static void main(String[] args) {
        int port = 8081;
        try (ServerSocket ss = new ServerSocket(port)) {
            while (true) { 
                try (Socket s = ss.accept();
                     BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
                     PrintWriter out = new PrintWriter(s.getOutputStream(), true)) {
                    System.out.println(in.readLine());
                    System.out.println("Client connected");
                    out.println("Bonjour");
                } catch (IOException ioException) {
                    System.err.println("Error handling client connection: " + ioException.getMessage());
                }
            }
        } catch (IOException ioException) {
            System.err.println("Server error: " + ioException.getMessage());
        }
    }
}
