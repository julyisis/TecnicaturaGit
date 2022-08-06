
import java.util.Scanner;

public class HolaMundo {
    public static void main(String[] args) {
       /* System.out.println("Hola Mundo desde Java");
        
        int miVariable = 10; //tipo primitivo que es el INT(entero)
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        // TIPO STRING( no es un tipo primitivo es una tipo de clase)
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en Programacion";
        System.out.println(miVariableCadena);*/
        // VAR- INFERENCIA DE TIPOS EN JAVA
       /* var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " +miVariableEntera2);
        System.out.println("miVariableCadena2 = "+ miVariableCadena2);//CONCATENACION DE CADENAS*/
       
        //REGLAS PARA DEFINIR UNA VARIABLE EN JAVA
        // 1 SE RECOMIENDA EMPEZAR CON MINUSCULA ESCRITURA CAMELCASE
        //2 NO SE PUEDE COMENZAR CON UN NUMERO PARA EMPEZAR UNA VARIABLE
        // 3 NINGUN CARACTER ESPECIAL
        // 4 SI PUEDE TENER GUION BAJO PARA INICIAR LA VARIABLE PERO NO ES COMUN
        // 5 SI SE PUEDE INICIAR CLA VARIABLE CON EL SIGNO DE DOLAR
        // 6 SE PUEDE PONER ACENTOS,PERO NO ES RECOMENDADO
        // 7 EL NUMERAL ES UN CARACTER ILEGAL PARA COMENZAR UNA VARIABLE
        
        /*var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " +usuario;
        System.out.println("union = " +union);
        
        var a = 8; //no es recomendable que las variables sean cortas, y no podemos utilizar como 
        var b = 4; // identificar una variable con palabras reservadas de java
        System.out.println(usuario + (a + b));//los parantesis hacen la prioridad */
        
        //EJERCICIO: CARACTERES ESPECIALES CON JAVA
       /* var nombre = "Natalia"; //ESTO ES CODIGO DURO CUANDO LE ESTAMOS ASIGNANDO LOS VALORES A LAS VARIABLES
        System.out.println("\nNueva linea: \n "+ nombre);//NOS DA UN SALTO DE LINEA CON DIAGONAL INVERSA MAS n
        System.out.println("Tabulador: \t"+ nombre);//tabulador diagonal mas t nos hace un espacio para centrar
        System.out.println("\t\t.:MENU:.");//hacemos que se desplace, esto se puede hacer al omienzo de una cadena que se quiere mostrar
        System.out.println("Retroceso: \b"+nombre);//CARACTER DE RETROCESO
        System.out.println("COMILLAS SIMPLES: \'"+nombre+"\'");//COMILLAS SIMPLES
        System.out.println("COMILLAS DOBLES: \""+nombre+"\"");//COMILLAS DOBLES*/
        
        //CLASE SCANNER
        /*Scanner entrada = new Scanner(System.in);//DE ESTA FORMA SE INICIALIZA LA CLASE SCANNER(HEMOS CREADO UN OBJETO)LLAMADO ENTRADA
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();//entrada ES UN OBJETO LA HEMOS INICIALIZADO CON LA CLASE SCANNER,PERO POR AHORA USAREMOS COMO VARIABLE
        System.out.println("usuario2 = " + usuario2);//soutv + tab 
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);*/
        
        //EJERCICIO EL LIBRO
        
       
                    
                
        
        
        // TIPOS PRIMITIVOS EN JAVA (TIPOS ENTEROS,SON BYTE,SHORT,INT Y LONG)
        // BYTE ESTE ES EL MAS PEQUEÑO DE LOS TIPOS PRIMITIVOS ENTEROS,EL MAS UTILIZADO ES EL INT
       /* byte numEnteroByte = (byte)127;//el compilador nos avisa que hemos superado el rango,ya no hay mas num positivos, esto es perdida de presicion
        System.out.println("numEnteroByte = "+ numEnteroByte);
        System.out.println("valor minimo del Byte: "+Byte.MIN_VALUE);//el tipo de dato Byte lo ponemos con mayuscula porque son clases(clase Byte)
        System.out.println("valormaximo del Byte: "+Byte.MAX_VALUE);//hemos mandado a imprimir el rango ninimo y maximo
        
        //TIPOS NUMERICOS ENTEROS(TIPO SHORT QUE ALMACENA HASTA 16 BITS)
        short numEnteroShort = (short)32767;
        System.out.println("numEnteroShort = "+numEnteroShort);
        System.out.println("valor minimo del Short: "+Short.MIN_VALUE);//mayuscula Short.MiN es porque samos la clase Short
        System.out.println("Valor maximo del Short: "+ Short.MAX_VALUE);//las clases siempre empiezan con mayusculas
        //debido a las limitaciones del short y byte se recomienda pasar al int
        //EN JAVA POR DEFAULT VA A TRABAJAR CON EL TIPO ENTERO INT DE 32 BITS
        
        int numEnteroInt = 2147483647;// debemos poner al final una L mayuscula la literal pasa a ser long + de 32 bits esta literal es entera por default
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("valor minimo del Int: "+Integer.MIN_VALUE);// con esta clase Integer podemos hacer la evaluacion de maximo y minimo
        System.out.println("Valor maximo del Int: "+Integer.MAX_VALUE);
        
        //TIPO LONG
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del Long: "+Long.MIN_VALUE);
        System.out.println("Valor maximo del Long: "+Long.MAX_VALUE);*/
        
        //TIPOS PRIMITIVOS TIPOS FLOTANTES
        //LOS FLOTANTES SON CON PUNTO DECIMAL ,EL FLOAT DE 32 BITS Y EL DOBLE DE 64 BITS
        //LAS LITERALES EN JAVA POR DEFAULT SON DE TIPO DOUBLE(UN DOUBLE ES DE 64 BITS)
        /*float numFloat = 3.4028235E38F;//este dato el compilador lo va a leer como tipo flotante(F)
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo de Float: "+Float.MIN_VALUE);
        System.out.println("El valor maximo de Float: "+Float.MAX_VALUE);
        //tipo double
        double numDouble = 1.7976931348623157E308;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor minimo de Double es: "+Double.MIN_VALUE);
        System.out.println("El valor maximo de Double es: "+Double.MAX_VALUE);*/
        // INFERENCIA DE TIPO VAR Y TIPOS PRIMITIVOS
        /*var numEntero = 20; // las literales sin punto automaticamente son de tipo Int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; //automaticamente con el punto se transforma en tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
        
        //TIPOS PRIMITIVOS CHAR(caracteristica puede almacenar solo un caracter
        //tenemos tres formas de ingresar el codigo unicode
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        //tipo unicode caracteres especiales
        
        char varCaracter = '\u0024';//IDICAMOS A JAVA LA ASIGNACION CON EL CODIGO UNICODE
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; //valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$';// un caracter especial podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        //inferencia de tipo VAR
       
       var varCaracter1 = '\u0024';//IDICAMOS A JAVA LA ASIGNACION CON EL CODIGO UNICODE
        System.out.println("varCaracter1 = " + varCaracter1);
       var varCaracterDecimal1 = (char)36; //valor Entero le asigna un tipo Intcon char tuvimos que hacer la conversion asi da $
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
       var varCaracterSimbolo1 = '$';// un caracter especial podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar);*/
        //TIPOS PRIMITIVOS tipos BOOLEN
        /*var varBool = false;//en java es distinto que la sintaxis de python true en java comienza con minuscula
        System.out.println("varBool = " + varBool);
        
        if(varBool){
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("La bandera es roja");
        }
        // Algoritmo: ¿Es mayor de edad?
        var edad = 18;// Literal tener presente la inferencia de tipos
        //var adulto = edad >= 18; //Esta es una expresion Booleana
        if(edad >= 18){
            System.out.println("Eres Mayor de edad");
        }
        else{
            System.out.println("Eres Menor de edad");
        }*/
        //conversion de tipo primitivos
//        var edad = Integer.parseInt("20");
//        System.out.println("edad = " + (edad + 1));
//        var valorPI = Double.parseDouble("3.1416");
//        System.out.println("valorPI = " + valorPI);
//        
//         //pedir un Valor al usuario
        var entrada = new Scanner(System.in);
//        System.out.println("Digite su edad");
//        edad = Integer.parseInt(entrada.nextLine());
//        System.out.println("edad = " + edad);
       // CONVERSION DE TIPOS PRIOMITIVOS EN JAVA PARTE 2
       var edadTexto = String.valueOf(10);//String no es un dato primitivo es un tipo object
        System.out.println("edadTexto = " + edadTexto);
        
       var fraseChar = "programadores".charAt(3);
       System.out.println("fraseChar = " + fraseChar);
       
        System.out.println("Digite un caracter");
        fraseChar = entrada.nextLine().charAt(0);//el charAt es solo para los tipos string tienen este metodo
        System.out.println("fraseChar = " + fraseChar);
        
        
        
        
    }
    
}
