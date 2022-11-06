/*
el public static void main, el modificador de acceso es publico, el static tambien es un modificador
de acceso es de tipo estatico, despues el void que no devuelve nada  y por ultimo esta el main
El main es estatic esto es porque el compilador no va a crear un objeto de la clasepara ejecutar 
la pruebaestamos hablando de la linea 9 class PersonaPrueba, lo que hace es utilizar el nombre de la clase 
y luego en el nombre del metodo main por esto es que es static para no crear objetos de esta clase 
si no para poder acceder directamente al metodo poniendo el nombre de la clase 

vamos a empezar a crear un objeto de la clase Persona
*/
package test;

import domain.Persona;
//no es lo mismo imprimir informacion en consola que egresar informacion  
public class PersonaPrueba {
    private int contador; //aqui tenemos creado un atributo dentro de la clase personaPrueba
    /*
    ahora dentro de aqui lo que es la clase personaPruebase puede crear un atributo de essta clase personaPrueba pues si
    podemos poner private
    */
    /*
    ahora si queremos utilizar el contador dento de la clase main linea 32 nos dice que es una variable 
    que no es estatica da error no se puede referenciar dentro de un contexto estatico
    */
    public static void main(String[] args) {
       
        Persona persona1 = new Persona("Ariel"); //en este objeto vamos anecesitar poner un argumento,este es de tipo string
        System.out.println("persona1 = " + persona1);
        Persona persona2 = new Persona("Naty");
        System.out.println("persona2 = " + persona2);
        imprimir(persona1);
        imprimir(persona2);
        //this.contador = 10;// no se puede referenciar desde un contexto estatico
        PersonaPrueba personaP1 = new PersonaPrueba();
        
        
        System.out.println(personaP1.getContador());
        
    }
     /*VAMOS A CREAR OTRO METODO
    si no le ponemos static a la linea 27 nos va a dar unn   error en la linea 21 y 22 
    porque no se ppuede trabajar dde esta maneera poniendo algo dinamico dentro de algo estatico no es lo mismo
    en el main se puede trabajar con el this,no se puede poner un metodo que no es static dentro de otrrro static
    en este caso ell metodo imprimir se asocia con  objeto de la clase de  tipo personaPrueba, el orrden de los modificadores aqui 
    tambien no importa se puede comenzar con static public .. si esta invertido el orden se ejectuta bien igual
    public static void s solo para imprimir no devuelve absolutamente nada ,Ahora lo que es el tipo de retotno  es void
    la palabra this noo puede ser referenciada dentro de un contexto static
    */
    public static void imprimir(Persona persona){ //NO es ESTATICO, va a trabajar de  forma DINAMICA
        System.out.println("persona = " + persona);
    }
    /*
    si tenemos un atributo dentro de lo que es la clase persona prueba y no podemos trabajar con ese atributo dentro de lo que es el metodo 
    static void, entonces como podemos hacer ahora para solucionar este problema, lo que tenemos que hacer es simplemente 
    crear un metodo
    */
    //una vez que creamos esto,ahora si podemos hacer lo siguiente noss vamos a la linea 34
    public int getContador(){
        imprimir(new Persona("Liliana"));
        return this.contador;
    }
}
