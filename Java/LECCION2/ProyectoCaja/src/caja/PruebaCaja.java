/*
Proyecto caja:
Ejercicio 1:Crear un proyecto segun las especificaciones
mostradas a continuacion 
la formula es:volumen = ancho * alto * profundidad
*/
package caja;


public class PruebaCaja {
    public static void main(String[] args) { //Metodo main
        //Variables Locales
        int medidaAncho = 3; //Valores ingresados en codigo duro
        int medidaAlto = 2;
        int medidaProf = 6;
        
        Caja caja1 = new Caja(); //Instanciamos el objeto, constructor vacio
        caja1.ancho = medidaAncho; //le pasamos los valores añ objeto
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProf;
        int resultado = caja1.calcularVolumen(); //Llamamos al metodo
        //Primer resultado
        System.out.println("Resultadomvolumen de caja 1: "+ resultado);
        Caja caja2 = new Caja(2 , 4, 6); //Llamamos al contructor 2 con nuevos argumentos
        //Llamamos con el nuevo objeto el metodo para un nuevo calculo 
        System.out.println("resultado volumen de caja 2: " + caja2.calcularVolumen());
    }
    
}
