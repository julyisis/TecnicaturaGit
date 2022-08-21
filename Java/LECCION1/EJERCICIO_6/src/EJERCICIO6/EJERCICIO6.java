
package EJERCICIO6;

import java.util.Scanner;


public class EJERCICIO6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        float guillermo ,luis,juan, total;
        System.out.println("Digite la cantidad de dinero de Guillermo: ");
        guillermo = Float.parseFloat(entrada.nextLine());
        
       luis = guillermo / 2;
       juan = (luis + guillermo)/ 2;
       total = + guillermo + juan;
        System.out.println("\nEl inero de Luis es : U$$"+luis);
        System.out.println("\nEl dinero de Juan  es: U$$"+juan);
        System.out.println("El total de dinero entre los tres es: U$$"+total);
    }
    
}
