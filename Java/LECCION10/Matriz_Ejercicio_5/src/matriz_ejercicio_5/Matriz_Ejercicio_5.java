/*
Ejercicio5: crear y cargar una matriz de tamaño nxm mostrar la suma de cada fila y de cada columna
*/
package matriz_ejercicio_5;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class Matriz_Ejercicio_5 {
    
        public static void main(String[] args) {
               Scanner entrada = new Scanner(System.in);
               int matriz[][],nFilas,nCol,sumaFilas,sumaCol;//CREAMOS UNA MATRIZ DE TIPO ENTERA/DESPUES CREAMOS UNA VARIABLE DE FILAS Y VARIABLE DE COLUMNAS,SUMAf..Y SUMAC..
               int posFila,posCol;//CONTINUAMOS DE TIPO ENTERA CREAMOS LA VARIABLE POSf..Y POSC..
        
               nFilas = Integer.parseInt(JOptionPane.showInputDialog("Digite el numero de filas: ")); //nFilas le asignamos x JOptionP..hacemos una salida de inf.que el usuario digite eln de filas
               nCol = Integer.parseInt(JOptionPane.showInputDialog("Digite el numero de columnas: ")); //y despues para que digite el numero de columnas para la matriz,se debe usar el Integer para la conversion
        
               matriz = new int [nFilas][nCol];//instanciamos la matriz es ya un objeto le asignamos un valor que se ingreso para filas y para columanas 
               int filas[] = new int[nFilas];//aqui tenemos un arreglo
               int columnas[] = new int[nCol];//otro arreglo
        
               System.out.println("Rellenado de la matriz: ");
               for(int i=0; i<nFilas; i++) {
                       for(int j=0; j<nCol; j++) {
                               System.out.println("Matriz ["+i+"] ["+j+"]: ");
                               matriz[i][j] = entrada.nextInt();
                
                        }
            
                }
                System.out.println("\nMatriz Original: ");//atravez de los ciclos anidados vamos a pedir que nos muestre la matriz 
                for(int i=0; i<nFilas;i++) {
                        for(int j=0; j<nCol ; j++) {
                                System.out.print(matriz[i][j]+" ");
                
                        }
                        System.out.println("");    
                //SUMANDO LAS FILAS //donde creamos dos arreglos 
                posFila=0; //hemos inicializado lo que son contadores
             
                        sumaFilas = 0; //UTILIZAMOS UNA VARIABLE PARA HACER LA SUMA ITERATIVA AQUI GUARDAMOS LA SUMA 
                        for(int j=0; j<nCol; j++){
                                sumaFilas += matriz[i][j];    
                        }
                        filas[posFila] = sumaFilas; 
                        posFila++;
                }
            //SUMANDO LAS COLUMNAS
                posCol = 0;
                for(int j=0; j<nCol;j++){  //aqui pomenos primero el recorrido para columnas y despues con el siguiente for ponemos el reccorrido de filas
                        sumaCol = 0;
                        for(int i=0; i< nFilas;i++){
                                sumaCol += matriz[i][j];
                        }
                        columnas[posCol] = sumaCol;
                        posCol++;
                    
                }
            
                System.out.println("\nLa suma de las filas es: ");
                for(int i=0; i<nFilas;i++){ //con este ciclo for recorremos lo que son las filas 
                        System.out.print(filas[i]+" - ");//vamos a mostrar el arreglo donde se guardaron todas las sumas de filas 
                
                }
                System.out.println("");
            
                System.out.println("\nLa suma de las columnas es: ");
                for(int i=0; i<nCol; i++){
                        System.out.print(columnas[i]+" - ");
                }
                System.out.println("");
                
            
        }
        
    }
    

