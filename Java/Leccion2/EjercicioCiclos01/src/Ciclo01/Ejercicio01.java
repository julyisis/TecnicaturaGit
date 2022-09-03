/*
EJERCICIO 1: LEER UN NUMERO Y MOSTRAR SU CUADRADO,REPETIR EL PROCESO HASTA QUE 
SE INTRODUZCA UN NUMERO NEGATIVO
*/
package Ciclo01;

import javax.swing.JOptionPane;

        
public class Ejercicio01 {
    public static void main(String[] args) {
         int numero,cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));//la clase JopcionPane trabaja con tipo string,VAMOS A NECESITAR HACER UNA CONVERSION USANDO Integer
        while(numero >= 0){ //EL CICLO WHILE EN ESTA CONDICION MIENTRAS EL NUMERO SEA IGUAL A CERO O POSITIVO
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero "+numero+" elevado al cuadrado es: "+cuadrado);
            
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        System.out.println("El programa a finalizado por un numero negativo");
    
    }
    
}
