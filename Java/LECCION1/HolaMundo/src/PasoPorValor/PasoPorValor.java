/*
El paso por valor es una copia que se toma con funciones y sabemos que los metodos
es lo mismo que funciones 
*/
package PasoPorValor;


public class PasoPorValor {
    public static void main(String[] args) { //lo primero cargamos nuestro main,creamos otro main despues de el metodo main
        var valorX = 20;//stack
        System.out.println("valorX = " + valorX);
        cambioValor(valorX); // Solo le enviamos una copia
        System.out.println("valorX = " + valorX);
        
        
    }
    public static void cambioValor(int arg1) { //con el modificador de acceso public para que funcione tambien debe ser tipo static
        System.out.println("arg1 = " + arg1); // parametro por valor
        
    }
            
    
}
