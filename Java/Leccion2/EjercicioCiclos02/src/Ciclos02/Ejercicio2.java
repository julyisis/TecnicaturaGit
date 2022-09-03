/*
EJERCICIO2:LEER UN NUMERO E INDICAR SI ES POSITIVO O NEGATIVO
EL PROCESO SE REPETIRA HASTA QUE SE INTRODUZCA UN 0
HACER ESTE JERCICIO CON LA CLASE SCANNER,LUEGO HACERLO NUEVAMENTE CON LA CLASE 
JOptionPane
*/
 
package Ciclos02;

import javax.swing.JOptionPane;
public class Ejercicio2 {
    public static void main(String[] args) {
          var  numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
          while(numero != 0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null,"El numero: "+numero+ "Es POSITIVO");
            }
            else{
                JOptionPane.showMessageDialog(null,"El numero: "+numero+ "Es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null,"El numero "+numero+" FINALIZA EL PROGRAMA");
    }
    
}
