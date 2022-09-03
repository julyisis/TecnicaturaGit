/*
EJERCICIO 1: LEER UN NUMERO Y MOSTRAR SU CUADRADO,REPETIR EL PROCESO HASTA QUE 
SE INTRODUZCA UN NUMERO NEGATIVO
*/
package Ciclo01;

import java.util.Scanner;


public class Ciclos01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int numero,cuadrado;
        System.out.println("Digite un numero");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){ //EL CICLO WHILE EN ESTA CONDICION MIENTRAS EL NUMERO SEA IGUAL A CERO O POSITIVO
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero "+numero+"elevado al cuadrado es: "+cuadrado);
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa a finalizado por un numero negativo");
    }
    
}
