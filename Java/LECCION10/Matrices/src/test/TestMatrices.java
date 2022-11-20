/*
UNA MATRIZ ES CONSIDERADA ARREGLO DE ARREGLOS,RENGLONES Y COLUMNAS O FILAS Y COLUMNAS
EN ALGUNOS OTROS LUGARES EN VEZ DE DECIRLES FILAS Y COLUMANS LE DICEN RENGLON Y COLUMNAS
O RENGLONES Y COLUMNAS, NOSOTROS LE VAMOS A LLAMAR FILAS.ESTAS FILAS Y COLUMNAS SE PUEDEN LLENAAR CON 
TIPO PRIMITIVOS O DE TIPO OBJECT/ LA SINTAXIS ES FILA COLUMNA 
PARA EMPEZAR PONEMOS DE QUE TIPO ES LA MATRIZ VA SER DE TIPO INT 
*/
package test;

import domain.Persona;


public class TestMatrices {
    public static void main(String[] args) { //en el primer corchete tiene 3 filas y en el segundo corchete tiene 2 columnas
        int edades[][] = new int[3][2];//del lado izquierdo estamos definiendo la variable hasta aqui es una definicion y del lado derecho es instanciar lo que es la matriz
        System.out.println("edades = " + edades);
        //esta es la parte dos vamos a empezar a hacer modificaciones 
        edades[0][0] = 5;//LLenado manual
        edades[0][1] = 7;//cambiamos el numero porque elegimos difernte columna
        edades[1][0] = 8;
        edades[1][1] = 4;
        edades[2][0] = 2;
        edades[2][1] = 9;
        System.out.println("Recorremos la matriz atravez del ciclo for");
        
        
        System.out.println("edades 0-0  = " + edades [0][0] );
        System.out.println("edades 0-1  = " + edades [0][1]);
        System.out.println("edades 1-0  = " + edades [1][0]);
        System.out.println("edades 1-1  = " + edades [1][1]);
        System.out.println("edades 2-0  = " + edades [2][0]);
        System.out.println("edades 2-1  = " + edades [2][1]);
        
        for (int fila = 0; fila < edades.length; fila++) {
            for (int col = 0; col < edades[fila].length; col++) {
                System.out.println("Edades "+fila+"-"+col+": "+edades[fila][col]);
                
            }
            
        }
        
        //SINTAXIS CLASICA DE MATRICES, del lado izquierdo definimos la variable y del lado derecho instanciamos los arreglos y matrices son de tipo object
      //String frutas[][] = new String[3][2];//esta es la sintaxis clasica
      //SINTAXIS SIMPLIFICADA
      String frutas[][] = {{"Limon","Pomelo"},{"ciruela","kiwi"},{"Banana","Manzana"}};
      imprimir(frutas);
      
       //for (int i = 0; i < frutas.length; i++) {
       //     for (int j = 0; j < frutas[i].length; j++) {
       //         System.out.println("frutas "+i+"-"+j+": "+frutas[i][j]);
                
         //   }
            
        //}
        //VAMOS A COMENZAR CON LA CREACION DE UNA MATRIZ DE OBJETOS 
        Persona persona[][] = new Persona[2][3];
        //ASIGNAMOS VALORES A LA MATRIZ
        /*
        como asinamos objetos, si no es tambien instanciando, necesitamos hacer una instancia para que el valor que se guarde dentro de este 
        indice el elemento sea un objeto,vamos a poner la palabra reservada new Persona aqui estamos acudiendo al contructor de la clase persona
        donde ese constructor nos pide un tipo string que es para el nombre ,asi tenemos un objeto
        */
        persona[0][0] = new Persona("Ariel");
        persona[0][1] = new Persona("Osvaldo"); 
        persona[0][2] = new Persona("Liliana");
        persona[1][0] = new Persona("Natalia");
        persona[1][1] = new Persona("julieta");
        persona[1][2] = new Persona("Marcelo");
        System.out.println("Matriz de Persona");
        imprimir(persona);
        
    }
    /*
    en la linea 75 que sucede entre los parentesis no necesitamos especificar las filas o las colmnas porque la 
    variable va a apuntar a la referencia del objeto matriz que ya hemos creado es como definir la variable del 
    lado izquierdo,ahora vamos a llamar a este metodo en la linea 46
    */
    public static void imprimir(Object matriz[][]){
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.println("matriz "+i+"-"+j+": "+matriz[i][j]);
                
            }
            
        }
    }
}

