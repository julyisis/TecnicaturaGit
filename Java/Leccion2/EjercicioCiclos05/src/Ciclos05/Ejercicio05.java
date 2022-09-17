/*
 EJERCICIO 5:REALIZAR UN JUEGO PARA ADIVINAR UN NUMERO PARA ELLO GENERAR UN 
NUMERO ALEATORIO ENTRE 0-100,Y LUEGO IR PIDIENDO NUMEROS INDICANDO "ES MAYOR"O
"ES MENOR"SEGUN SEA MAYOR O MENOR CON RESPECTO A N, EL PROCESO TERMINA CUANDO EL
USUARIO ACIERTA Y MOSTRAMOS EL NUMERO DE INTENTOS HECHOS JOptionPane
 */
package Ciclos05;

import javax.swing.JOptionPane;


public class Ejercicio05 {
    public static void main(String[] args) {
        int numero, aleatorio,conteo = 0;
        aleatorio = (int)(Math.random()*100); //DE ESTA MANERA CONSEGUIMOS UN NUMERO ALEATORIO,HACEMOS A CONVERCION DE INT Y LA FUNCION MATH.RANDOM *100/ SON NUMEROS ALEATORIOS DE 0 A 100
        do{
            
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));//de esta forma recibimos el dato de parte del usuario
            if(numero < aleatorio){
                JOptionPane.showConfirmDialog(null, "Digite un numero mayor");
            }
            else if(numero > aleatorio){
                JOptionPane.showConfirmDialog(null, "Digite un numero menor");
            }    
            else{
                JOptionPane.showMessageDialog(null,"¡¡¡FELICIDADES!!! Has adivinado el numero: ");
            }
            conteo++;
        }while(numero!= aleatorio);
        JOptionPane.showMessageDialog(null,"ADIVINASTE el numero en: "+conteo+"INTENTOS");
        
        
    }

   
    }

    


 
