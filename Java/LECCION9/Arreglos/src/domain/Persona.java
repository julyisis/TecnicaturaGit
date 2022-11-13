/*
ARREGLOS DE TIPO OBJECT VAMOS A PONER UN ATRIBUTO QUE VA A SER ENCAPSULADO(PRIVATE)
*/
package domain;

public class Persona {
    private String nombre;

    public Persona(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + '}'+","+super.toString();
    }
    
    
    
    
    
}
