
package EJERCICIO7;

import java.util.Scanner;


public class EJERCICIO7 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        final int salario = 1000;
        int comision = 150, venta;
        float salarioMensual,ventaCarro,porVenta,totalPrecio;
        System.out.println("Digite la cantidad de carros vendidos: ");
        venta = Integer.parseInt(entrada.nextLine());
        System.out.println("Dgite el precio de un carro: ");
        ventaCarro = Float.parseFloat(entrada.nextLine());
        
        comision *= venta;
        totalPrecio = ventaCarro * venta;
        porVenta = totalPrecio * 0.0f;
        salarioMensual = salario + comision + porVenta;
        
        System.out.println("\nEl salario mensual es: "+salarioMensual);
    }
    
}
