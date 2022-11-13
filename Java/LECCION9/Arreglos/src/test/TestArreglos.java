/*
DEFINICION DE ARREGLOS CON TIPOS ENTEROS EN LA SINTAXIS DE JAVA LO QUE NOS INDICA QUE ESTAMOS 
CREANDO LOS ARREGLOS SON LOS "CORCHETES" ESTOS CORCHETES VAN DESPUES DEL IDENTIFICADOR PUEDE IR PEGADO O NO EJ DIA[] O DIA []
LUEGO ASIGNAMOS Y COLOCAMOS LA PALABRA RESERVADA NEW PORQUE LOS ARREGLOS SON UN TIPO OBJECT,al final un ARREGLO hereda de la clase 
object despues del new poner el tipo de dato volvemos a poner []y dentro de los parentesis le indicamos la cantidad de elementos 
ACLARACION: en la linea 14 antes del igual seria el lado izquierdo estamos declarando la variable edades y del lado derecho
estamos instanciando un objeto de tipo arreglo

*/
package test;


public class TestArreglos {
    public static void main(String[] args) { //lado derecho instanciamos un object de tipo object
        int edades[] = new int [3];//el lado izq. declaramos la variable 
        System.out.println("edades = " + edades);
        
        edades[0]= 17;
        System.out.println("edades 0 = " + edades[0]);
        edades[1] = 22;
        System.out.println("edades 1 = " + edades[1]);
        edades[2] = 18;
        System.out.println("edades 2 = " + edades[2]);
       // edades[3]= 7; //fuera de rango, error en tiempo de ejecucion
       
       for(int i = 0; i < edades.length; i++){
           System.out.println("Edades y sus elementos "+i+": "+edades[i]);
       }
    }
    
}
