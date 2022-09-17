/*
EJERCICIO3:LEER NUMEROS HASTA QUE SE INTRODUZCA UN CERO
PARA CADA UNO INDICAR SI ES PAR O IMPAR.
PRIMERO LO HAREMOS CON LA CLASE SCANNER
LUEGO CON LA CLASE JOptionPane
*/
package Ciclos03;

import java.util.Scanner;

public class Ciclos03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Digite un nemero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if(numero % 2 == 0){
                System.out.println("El numero ingresado "+numero+"Es PAR");
            }
            else{
                System.out.println("El numero ingresao "+numero+"Es IMPAR");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero ingresado es "+numero+"Finaliza el Programa");
    }
    
    
}
