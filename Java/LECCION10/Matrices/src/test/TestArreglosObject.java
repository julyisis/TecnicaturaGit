/*
TENEMOS DOS MAIN INO EN TestArreglos y el otro en TestArreglosObject
*/
package test;

import domain.Persona;


public class TestArreglosObject {
    public static void main(String[] args) {
        Persona personas[] = new Persona[2]; //es comun que los arreglos se definan en forma plural esto indica que la variable tiene varios elementos, no asi cuando hemos creado un objeto que es uno solo
                                             //no es asi cuando hay variables,SIMPLEMENTE ESTO SE UTILIZA ENFOCADO A LO QUE SON LOS ARREGLOS                   
        personas[0] = new Persona("Ariel");
        personas[1] = new Persona("Osvaldo");
        System.out.println("personas 0 = " + personas[0]);
        System.out.println("personas 1 = " + personas[1]);
        
        /*
        ARREGLOS o ARRAYS: vamos a ver como iterar los elementos de un arreglo de tipo objects
        la iteracion tiene que ver justamente con el ciclo for 
        */
        for(int i = 0; i< personas.length; i++){
            System.out.println("personas"+i+" = " + personas[i]);
        }
        //LA SINTAXIS RESUMIDA PARA TRABAJAR CON ARREGLOS LINEA 26
        String frutas[] = {"Banaba","Pera","Durazno"};
        for(int i = 0; i < frutas.length; i++) {
           System.out.println("frutas" +i+" = "+ frutas[i]);  
        }
        
    }
    
}
