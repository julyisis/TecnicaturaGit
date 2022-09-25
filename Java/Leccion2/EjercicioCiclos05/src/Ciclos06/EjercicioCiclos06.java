/*
EJERCICIO06: PEDIR NUMEROS HASTA QUE SE TECLEE UN 0,MOSTRAR LA SUMA DE TODOS LOS 
NUMEROS INTRODUCIDOS
 */
package Ciclos06;

import java.util.Scanner;

public class EjercicioCiclos06 {
    public static void main(String[] args) { //HEMOS CREADO DOS VARIABLES,CON LA INFERENCIA DE TIPO,NO SE PUEDEN CREAR DOS VARIABLES DENTRO DE UNA MISMA LINEA,POR ESO DIRECTAMENTE
        Scanner entrada = new Scanner(System.in);
    
        int numero,suma =0; // LE ASIGNE INT DE TIPO ENTERO
        do{
            System.out.println("digite un numero");
            numero = Integer.parseInt(entrada.nextLine()); //VAMOS A ASIGNARLE EL VALOR QUE HA DIGITADO EL USUARIO
            suma+=numero; //necesitamos que los numeros que a ingresando el usuario se vallan sumando
           
        }while(numero != 0);
        System.out.println("\nLa suma de todos los numeros ingresados es: "+suma);
    }
}
