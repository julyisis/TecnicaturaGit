
package Operaciones;


public class PruebaAritmetica {
    public static void main(String[] args) {
        /*lo que es aritmetica con parentesis estamos llamando a la clase en si en este caso estamos llamando al contructor esto reserva espacio de memoria
        este objeto que hemos creado va a trabajar directamente sobre el espacio de menoria que tiene aqui el constructor de la clase aritmetica ahora a esteobjeto le vamos
        agregar valores pero esos valores le vamos agregar van hacer para los tributos, vamos a modificar el valor de los atributos por medio del objeto aritmetica1
        */
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();// que hizo le hemos asignado el valor al atributo a, le asignamos valor al atributo b luego estamos atravez del objeto llamando al metodo 
        //que el metodo lo que hace es sumar 
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
      resultado = aritmetica1.sumarConArgumentos(12,26);
        System.out.println("Resultado usando argumentos = "+resultado);
    }
    
    
}
