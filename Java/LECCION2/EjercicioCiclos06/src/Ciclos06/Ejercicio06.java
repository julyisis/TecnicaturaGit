/*
EJERCICIO06: PEDIR NUMEROS HASTA QUE SE TECLEE UN 0,MOSTRAR LA SUMA DE TODOS LOS 
NUMEROS INTRODUCIDOS
 */
package Ciclos06;

import javax.swing.JOptionPane;


public class Ejercicio06 {
    
    public static void main(String[] args) { //HEMOS CREADO DOS VARIABLES,CON LA INFERENCIA DE TIPO,NO SE PUEDEN CREAR DOS VARIABLES DENTRO DE UNA MISMA LINEA,POR ESO DIRECTAMENTE
        
    
        int numero,suma =0; // LE ASIGNE INT DE TIPO ENTERO
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un nemero: ")); //VAMOS A ASIGNARLE EL VALOR QUE HA DIGITADO EL USUARIO
            suma+=numero; //necesitamos que los numeros que a ingresando el usuario se vallan sumando
           
        }while(numero != 0);
        JOptionPane.showMessageDialog(null,"La suma de todos los numeros ingresados es: "+suma);
    }

    
        
    }



