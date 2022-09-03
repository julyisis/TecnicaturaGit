/*
EJERCICIO2:LEER UN NUMERO E INDICAR SI ES POSITIVO O NEGATIVO
EL PROCESO SE REPETIRA HASTA QUE SE INTRODUZCA UN 0
HACER ESTE JERCICIO CON LA CLASE SCANNER,LUEGO HACERLO NUEVAMENTE CON LA CLASE 
JOptionPane
*/
package Ciclos02;

import java.util.Scanner;


public class Ejercicio02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("digite un numero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if(numero > 0){
                System.out.println("El numero" +numero+ " Es POSITIVO");
            }
            else{
                System.out.println("El numero " +numero+ "Es NEGATIVO");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero "+numero+" FINALIZA EL PROGRAMA");
    }
    
}
