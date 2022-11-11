/*
extends es la palabrita que hace que trabajemos en la herencia al lado de la palabrita pondremos 
el nombre de la clase Padre
*/
package domain;

/*
En la linea 10 estamos indicando que la clase empleados es na clase hija de la clase Persona 
si no se coloca no se podra acceder a ninguna de las propiedades metodos directamente de la 
clase persona ,porque no seria hija la clase empleado no seria hija si no ponemos el 
extends Persona
en java son herencias simples no se puede indicar que de varias clases
*/
/*
vamos a definir si esta clase empleado va atener sus clases, si ya no va a tener entonces sus atributos
van a estar encapsulados de manera private,o sea el modificador de acceso debe ser private
ya no protected ,el protected es para acceder en lo que es la herencia a los atributos que una 
clase hija pueda acceder auna clase padre,en este caso la clase empleado no va a heredarle  a nadie 
vamos a trabajar con el modificador de acceso de forma private
*/
public class Empleado extends Persona{
    private int idEmpleado;
    private double sueldo;
    /*ahora vamos a necesitar trabajar con el atributo idEmpleado,lo vamos hacer a travez de uno tipo static que este asociado directamente a la clase para 
    trabajar en lo que es el aumento de uno en uno.
    */
    private static int contadorEmpleados;//es para incrementar 
    //vamos a comenzar con lo que son los CONTRUCTORES 

    public Empleado(String nombre,double sueldo) { //
        super(nombre);
        this.idEmpleado = ++Empleado.contadorEmpleados;
        this.sueldo = sueldo;
    }

    public int getIdEmpleado() {
        return this.idEmpleado;
    }


    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
    
    
    
    
    
    
}
