/*
EJERCICIO3:LEER NUMEROS HASTA QUE SE INTRODUZCA UN CERO
PARA CADA UNO INDICAR SI ES PAR O IMPAR.
PRIMERO LO HAREMOS CON LA CLASE SCANNER
LUEGO CON LA CLASE JOptionPane
*/
package Ciclos03;

import javax.swing.JOptionPane;


public class Ejercicio03 {
    public static void main(String[] args) {
    int numero;//HEMOS CREADO UNA VARIABLE DE TIPO ENTERA,QUE ESTA TOTALMENTE VACIA
    numero = Integer.parseInt(JOptionPane.showInputDialog("DIGITE UN NUMERO"));
        while(numero != 0){//(WHILE ES MIENTRAS,REPETIR UNA ACCION EN UN BUCLE SIEMPRE  CUANDO SE CUMPLA LA CONDICION 
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null,"El numero ingresado "+numero+"Es PAR");
            }
            else{
                JOptionPane.showMessageDialog(null,"El numero ingresado "+numero+"Es IMPAR");
            }
            
            numero = Integer.parseInt(JOptionPane.showInputDialog("DIGITE OTRO NUMERO"));
        }
        JOptionPane.showMessageDialog(null,"El numero ingresado es "+numero+"Finaliza el Programa");
    }
    
    }

