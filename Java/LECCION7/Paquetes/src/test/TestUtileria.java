/*
como podemos importar la clase uteleria manualmente,lo mostraremos en la linea 5 empezando con import ar...asi importamos manualmente
tambien podemos poner import ar.com.codesyatem.*; vamos a mostrar las dos formas uno quedara documentado
*/
package test;
//import ar.com.codesystem.Utileria;
//import ar.com.codesystem.*;
//import static ar.com.codesystem.Utileria.imprimir;//solo aplica para metodos estaticos 
public class TestUtileria {
    public static void main(String[] args) { //estamos utilizando metodos estaticos
       // Utileria.imprimir("Saludos a todos los alumnos de la tecnicatura");
       //imprimir("Terminamos en unos minutos ");//esta es otra sintaxis para trabajar lo que es importar un paquete desde un metodo o atributo statico
       /*
       otra sintaxis es que se comoce con el nombre completamente calificado,podemos utilizar las clase sin necesidad de utilizar ningun import
       esto nos obliga a utilizar el nombre completo de la clase 
       */
       ar.com.codesystem.Utileria.imprimir("Ahora si estamos terminando");//no es recomendable esta sintaxis porque el codigo se hace mas dificil de leer para otros
       /*
       programadores, lo recomendables hacer la importacion de forma normal o estatica lo que esta en la linea 17 no es la forma  
       */
        
    }
    
}
