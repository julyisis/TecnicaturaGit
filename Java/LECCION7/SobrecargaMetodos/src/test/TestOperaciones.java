
package test;

import operaciones.Operaciones;


public class TestOperaciones {
    public static void main(String[] args) {
        var resultado = Operaciones.sumar(7, 9);
        System.out.println("resultado = " + resultado);
        var resultado2 = Operaciones.sumar(5.0, 7);//aqui para que llame al metodo double,uno de los dos argumentos deberia ser de tipo double
        System.out.println("resultado2 = " + resultado2);
        
        var resultado3 = Operaciones.sumar(8, 6L);
        System.out.println("resultado3 = " + resultado3);
    }
    
}
