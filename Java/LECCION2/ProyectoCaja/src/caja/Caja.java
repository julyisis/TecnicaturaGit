
package caja;


public class Caja { //Clase publica caja 
    //Atributos (caracteristicas )
    int ancho;
    int alto;
    int profundo;
    //Metodo y Constructores (acciones)
    public Caja(){ //Constructor 1 vacio
    }
    //Constructor con Parametros
    public Caja(int ancho, int alto ,int profundo) { //constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    public int calcularVolumen() { //Metodo para calcular 
        return ancho * alto * profundo;
    }
}
