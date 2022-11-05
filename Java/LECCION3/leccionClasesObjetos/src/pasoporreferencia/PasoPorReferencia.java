//PASO POR REFERENCIA
/*
Todas las clases en java heredan de la clase object,la herencia de clase object es la clase padre 
de todas las otras clases,que atravez de cada clase se puede crear o istanciar un objeto 
*/
package pasoporreferencia;

import Clases.Persona;


public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();//aca estamos llamando al constructor de esta clase, con new Persona()accedemos a los atributos
        persona1.nombre = "Ester";
        System.out.println("persona1 nombre = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio que hicimos en el nombre es:  "+persona1.nombre);
        persona1 = cambiarElValor(persona1);
        //Persona persona2 = new Persona();
        Persona persona2 = null;
        
        persona2 = cambiarElValor (persona2);
        
   }
    public static void cambiarValor(Persona persona) { //paso por referencia utilizamos la clase persona para aceder al objeto y a la clase el paso por referencia en este caso es
        persona.nombre = "Maria";
        //la clase Persona
    }
   
    //Ahora vamos a crear otro metodo 
    public  static Persona cambiarElValor(Persona persona){ //ahora no va hacer de tipo void, no va hacer vacia,esta va hacer tipo objec, tipo objeto,como lo hacemos poniendo la clase persona
        if(persona == null){
            System.out.println("El valor de persona es invalida : Null");
            return null;
        }
        persona.nombre = "Monica";
        return persona;
    }
    
}
