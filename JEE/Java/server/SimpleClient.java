
// Source code is decompiled from a .class file using FernFlower decompiler.
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
 
public class SimpleClient {
   public SimpleClient() {
   }
 
   public static void main(String[] var0) {
      String var1 = "localhost";
      short var2 = 8081;
 
      try {
         Socket var3 = new Socket(var1, var2);
 
         try {
            PrintWriter var4 = new PrintWriter(var3.getOutputStream(), true);
 
            try {
               BufferedReader var5 = new BufferedReader(new InputStreamReader(var3.getInputStream()));
 
               try {
                  String var6 = "Hello, Server!";
                  var4.println(var6);
                  System.out.println("Sent to server: " + var6);
                  String var7 = var5.readLine();
                  System.out.println("Received from server: " + var7);
               } catch (Throwable var11) {
                  try {
                     var5.close();
                  } catch (Throwable var10) {
                     var11.addSuppressed(var10);
                  }
 
                  throw var11;
               }
 
               var5.close();
            } catch (Throwable var12) {
               try {
                  var4.close();
               } catch (Throwable var9) {
                  var12.addSuppressed(var9);
               }
 
               throw var12;
            }
 
            var4.close();
         } catch (Throwable var13) {
            try {
               var3.close();
            } catch (Throwable var8) {
               var13.addSuppressed(var8);
            }
 
            throw var13;
         }
 
         var3.close();
      } catch (IOException var14) {
         var14.printStackTrace();
      }
 
   }
}
 
 