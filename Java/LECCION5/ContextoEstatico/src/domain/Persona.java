
package domain;


public class Persona { 

//vamos a cargar nuestros atributos de tipo private 
    //CARGAMOS LOS ATRIBUTOS 
    private int idPersona;
    private  static int contadorPersona;
    private String nombre;
    
    //ARMAMOS EL "CONTRUCTOR"
    /*
    no vamos a utilizar el contructor vacio,cuando armamos un contructor cuando ponemos un contructor en nuestra clase 
    ya no se va a crear automaticamente el contructor vacio si vamos a necesitar el contructor vacio  hay qye colocarlo
    si no simpre va a recurrir al unico constructor que hemos cargado en nuestra clase
    En este caso no vamos a utilizar constructor vacio,vamos a poner un parametro
    */
    public Persona(String nombre){ //Este parametro es el Parametro nombre 
        this.nombre = nombre;
        //INCREMENTAR EL CONTADOR POR CADA OBJETO NUEVO
        /*
        NO se utiliza el operador this para un atributo statico si no se va a 
        utilizar el mismo nombre de la clase
        */
        Persona.contadorPersona++; //NO UTILIZAR EL OPERADOR THIS, LA REFERENCIA TIENE QUE SER ATRAVEZ DE LA CLASE 
        //VAMOS A ASIGNAR UN NUEVO VALOR A LA VARIABLE idPersona
        
        this.idPersona = Persona.contadorPersona;
    }
    public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int aContadorPersona) {
        contadorPersona = aContadorPersona;
    }
    
    public int getIdPersona() {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
     /*
    la anotacion override agrega informacion extra al metodo que estamos definiendo que es el
    metodo toString,primero la anotacion luego el metodo, la anotacion esta indicando que estamos sobre escribiendo el 
    metodo toString
    que significa sobre escribir el metodo toString? en la herencia en la clase object se 
    hereda este metodo toString
    aqui lo estamos sobre escribiendo este metodo que recibimos por herencia de la clase 
    object,lo estamos sobre escribiendo para mostrarlo como se ve en la linea 65
    */
    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
    
    
}
