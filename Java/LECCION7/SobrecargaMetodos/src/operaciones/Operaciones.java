/*
Vamos a agregar varias veces el metdo sumar, este metodo va a tener diferentes parametros
vamos a crear los metodos pero con el modificador de acceso public y el Static para no tener que estar instanciando
los objetos y el tipo va a ser de tipo int, lo que va a retornar es a + b
*/
package operaciones;


public class Operaciones {
    public static int sumar(int a, int b){ // de la linea 10 a la 14 tenemos el primer metodo
        System.out.println("Metodos para sumar enteros ");
        return a + b; //retorna un entero
        
    }
    /*
    Ahora vamos a crear otro metodo, una de las diferencias que puede haber entre las sobrecargas de metodos es
    el tipo de datos que maneje cada uno
    */
    public static double sumar(double a, double b){
        System.out.println("Metodos para sumar double");
        return a + b; //retorna double
    }
    /*
    de la linea 10 a la 22 tenemos dos metodos, aqui tenemos una sobrecarga de metodos, los dos metodos 
    se llaman igual que es sumar pero son diferentes en el tipo de datos que estan requiriendo 
    en la linea 10 es de tipo entero y el otro que esta en la linea 19 es double y los argumentos van a tener 
    que respetar estos tipos 
    Cuado comenzamos con un metodo public el que sigue tiene que ser tambien de tipo public
    el segundo ya no podria ser de tipo private, protected o default, pero si puede variar el tipo de retorno
    */
    
    
}
