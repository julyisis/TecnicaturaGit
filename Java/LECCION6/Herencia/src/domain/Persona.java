/*
cuando vamos a  poner un atributo de manera privada esto oeses para el capulamiento
todo lo que es private no se hereda a las clases hijas si queremos que las clases hijas puedan accedeer entonces se utiliza el modificador 
protected, es posible no indicar nada pero recuerden que el atributo al no indicarle nada ningun modificador de acceso va a ser defoult o backage
solo se puede acceder dentro de las clases que esten dentro del mismo paquete 
ahora la ventaja del protected es no importa que las clases hijas esten en otro paquete porque van a poder acceder el protected esta pensado para 
el concepto de herencia 
*/
package domain;


public class Persona {
    //ATRIBUTOS DE HERENCIA /PONGO ATRIBUTOS DE HERENCIA PORQUE LOS ESTAMOS USANDO CON EL MODIFICADOR DE ACCESO PROTECTED YA SABEMOS QUE ES PARA HERENCIA 
    
    protected String nombre;
    protected char genero;
    protected int edad;
    protected String direccion;
    //CREAMOS UN "CONSTRUCTOR"
   // el primero es vacio para crear objetos sin necesidad de inicializar los atributos de la clase 
    //CONSTRUCTOR VACIO:ESTE ES PARA CREAR OBJETOS SIN NECESIDAD DE INICIALIZAR LOS ATRIBUTOS DE LA CLASE
    public Persona(){//CONSTRUCTOR1 VACIO
        
    }
    public Persona(String nombre){ //CONTRUCTOR 2 SOLO PARA NOMBRE 
        this.nombre = nombre;
        
    }

    public Persona(String nombre, char genero, int edad, String direccion) { //constructor3 ES PARA LOS 4 ATRIBUTOS 
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.direccion = direccion;
    }

    public String getDireccion() {
        return this.direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public char getGenero() {
        return this.genero;
    }

    public void setGenero(char genero) {
        this.genero = genero;
    }

    public int getEdad() {
        return this.edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Persona{nombre=").append(nombre);
        sb.append(", genero=").append(genero);
        sb.append(", edad=").append(edad);
        sb.append(", direccion=").append(direccion);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    

   
    
    
    
}
    

