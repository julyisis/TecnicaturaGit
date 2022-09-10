package cicloWhile;

public class EjercicioWhile01 {

    public static void main(String[] args) {
        var conteo = 0; //INFERENCIA DE TIPO
        while (conteo < 3) { //Primero esta la condicion si no se cumple jamas se accede al codigo dentro del ciclo
            System.out.println("conteo = " + conteo);//el ciclo while y do while maneja un ciclo INDETERMINADO DE ITERACIONES
            conteo++; //VAMOS AUMENTANDO EN UNO LA VARIABLE 
        }
        var contador = 0;
        do {//ejecuta primero el codigo de su interior y luego hace la comprobacion de la condicion,sabemos que una vez se ejecuta su codigo si la condicion es 
            System.out.println("contador = " + contador);   //verdadera vuelve a repetir hasta que sea falsa y sale del ciclo
            contador++;
        } while (contador <= 7);//en do while es necesatio poner el punto y coma, es necesaria para el buen funcionamiento del programa 

        for (var contando = 0; contando < 7; contando++) { //Maneja un numero DETERMINADO DE ITERACIONES a diferencia de los ciclos while y do while,tiene una condicion
            if (contando % 2 == 0) {  // si es verdadera se ejecuta el codigo dentro del ciclo,si es falsa no ejecuta nada dentro del ciclo 
                System.out.println("contando = " + contando);
                break;  //La palabra break nos permite romper un ciclo
            }
        }
        inicio:
        for (var contando = 0; contando < 7; contando++) {
            if (contando % 2 != 0) { //(para los numeros impares(!=))
                continue inicio;//VAMOS A LA SGTE ITERACION
            }
            System.out.println("contando = " + contando);

        }

        //USOS DE ETIQUETAS LABELS,UNA ETIQUETA NOS VA A PERMITIR INDICAR A LAS PALABRAS CONTINUE Y BREAK IR AL LUGAR ESPECIFICO DE NUESTRO PROGRAMA
        //LAS ETIQUETAS SE COMBINAN CON LAS DOS PALABRAS(BREAK O CONTINUE)NO ES RECOMENDABLE DE APLICAR,PUEDE ROMPER CON LA LOGICA DEL PROGRAMA ,ES NECESARIO CONOCER ESTA SINTAXIS 
        //SI NO,NO VAMOS A SABER QUE HACER
    }
}

 

