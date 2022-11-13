
package test;

import domain.Cliente;
import domain.Empleado;
import domain.Persona;
import java.util.Date;

/*
Los constructores se heredan es una caracteristica de Java pero podemos acceder
atravez de la palabra super para saber a que contructor queremos utilizar,lo define el numero 
de argumentos que pasemossi no pasamos argumentos utiliza el de la clase padre que esta vacio
si pasamos 1 sera de la clase padre con un argumento
*/
public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Ariel", 57000.00);//Ya creamos un objeto con new y el nombre que elijamos 
        System.out.println("empleado1 = " + empleado1);
        
        Date fecha1 = new Date();   
        Cliente cliente1 = new Cliente(new Date(), true,"Bety",'F',32,"9 de JUlio 1413");
        System.out.println("cliente1 = " + cliente1);
        
        Persona persona1 = new Persona();
    
    /*
    estas clases son un solo objeto la clase padre y la clase hija en memoria que contiene toda la informacion
    de las dos clases 
    */
    
    
       
    
    }


}
