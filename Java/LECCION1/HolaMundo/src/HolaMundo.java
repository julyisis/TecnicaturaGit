
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
        /*var entrada = new Scanner(System.in);
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
        System.out.println("fraseChar = " + fraseChar);*/
 /*     int num1 = 5, num2 =4; //Para inicializar varias variables/En la inferencia de tipos no se puede inicializar varias variables al mismo tiempo
        var solucion = num1 + num2;//(var es una inferencia de tipo)
        System.out.println("solucion de la suma: "+ solucion);
        
        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);
        
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);
        solucion = num1 / num2;
        System.out.println("solucion de la division= " + solucion);
        
        var solucion2 = 3.4 / num2;//Inferencia de tipo
        System.out.println("solucion2 resultado de la division = " + solucion2);
        
        solucion = num1 % num2;//Guarda el residuo entero de la division
        System.out.println("solucion = " + solucion);// 5/4 
        
        if (num2 % 2 == 0)
            System.out.println("Es un numero Par");//en el if else cuando usamos una sola linea de codigo dentro del bloque no se necesitan las llaves
        else
            System.out.println("Es un numero Impar");*/
 /*     int varNum1 = 1, varNum2 = 4;
        var varNum3 = varNum1 + 6 - varNum2;//Una operacion
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 +=1; //varNum1 = varNum1 + 1;//operador de composicion esta asigando a la var Num1 sumado al valor que tiene dentro la variable
        System.out.println("varNum1 = " + varNum1);
//      -=    *=     /=      %=
        varNum2 -= 2;
        System.out.println("varNum2 = " + varNum2);
        
        varNum1 *= 5;
        System.out.println("varNum1 = " + varNum1);
        
        varNum3 /= 4;
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 %= 6;
        System.out.println("varNum1 = " + varNum1);*/
        //Para Java no es lo mismo cuando hablamos de flotante a float, el flotante real para Java es un tipo double ,Java automaticamente cuando nosotros
        //creamos con la inferencia de tipo un tipo flotante Java dice es double
        //OPERADORES UNARIOS:EMPEZAMOS CON EL PRIMER OPERADOR: CAMBIO DE SIGNO
        /*var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);    //En la variable B el resultado sera negativo

        //OPERADOR DE NEGACION
        var varC = true;
        var varD = !varC;
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);

        // OPERADORES UNARIOS DE INCREMENTO: PREINCREMENTO
        var varE = 9; //Se va a modificar su valor 
        var varF = ++varE;//Simbolo antes de la variable 
        //Primero se incrementa la variable y despues se usa su valor 
        System.out.println("varE = " + varE);//Se incrementa en la unidad
        System.out.println("varF = " + varF);//Va a sumar uno

        //Postincremento(el simbolo va despues de la variable)
        var varG = 3;
        var varH = varG++; //Primero vamos a ver el valor de la variable, y luego el incremento.
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);

        //OPERADORES UNARIOS DE DEREMENTO: PREDECREMENTO
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI); // La variable ya esta con decremento 
        System.out.println("varJ = " + varJ);
        //POSTDECREMNTO (SIMBOLO CA DESPUES DE LA VARIABLE
        var varK = 8;
        var varL = varK--; //Primero el valor de la variable,luego queda el decremento
        System.out.println("varK = " + varK);//Aui va a decrementar en la 1
        System.out.println("varL = " + varL);

        //OPERADORES DE IGUALDAD Y RELACIONALES
        var aNum = 5; //con la inferencia de tipo var sabemos que es tipo int
        var bNum = 4;
        var cNum = (aNum == bNum);//la compracion que estamos haciendo aqui es un true o false
        System.out.println("cNum = " + cNum);

        var dNum = aNum != bNum;//esta haciendo una comparacion tipo booleana 
        System.out.println("dNum = " + dNum);

        var cadenaA = "Hello"; // no esta haciendo una comprobacion de lo que tienen dentro,esta haciendo una comparacion de referencia  nos va a dar un valor booleano
        var cadenaB = "bye bye";//no esta comparando el contenido de la cadenaA y el contenido de la cadenaB
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);
        // si queremos comparar  el contenido de una cadena con otra tenemos que:utilizar el metodo equals(object)es de tipo booleano

        var fVar = cadenaA.equals(cadenaB);//en este caso si esta haciendo la comparacion interna, lo que tiene guardado dentro de las variables(si ponemos
        System.out.println("fVar = " + fVar); //dos cadenas hello nos devolvera un verdadero true)

        var gVar = aNum >= bNum; //En los operadores relacionales es opcional poner los parentesis 
        System.out.println("gVar = " + gVar); // > >= < <= == != (Estos son los operacores relacionales)

        if (aNum % 2 == 0) //en la estructura if para ver si es par o no 
        {
            System.out.println("El numero es Par: ");
        } else {
            System.out.println(" El numero es Impar: ");

        }
        var edad = 15;
        var adulto = 18;
        if (edad >= adulto) {
            System.out.println("Es Mayor e edad: ");
        }    
        else{
            System.out.println("Es Menor de edad: ");
        }*/
        // OPERADORES CONDICIONALES SON EL (AND Y OR) SINTAXIS EN JAVA
        //OPERADOR CONDICIONAL AND
        /*var valorA = -2;
        var valorMinimo = 0; //rango del 0 al  COMPARATIVA Y ESTAMOS AGREGANDO EL VALOR DE 0
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10; //REGLAS SI EN ESTE BLOQUE NOS DA VERDADERO

        if (respuesta) {
            System.out.println("Esta dentro del rango establecido ");
        } else {
            System.out.println("Esta fuera del rango establecido");
        }
          //CONDICIONAL OR 
        var vacaciones = false;
        var diaLibre = true;
        if(vacaciones||diaLibre)
            System.out.println("Papa SI puede asistir al juego de su hijo");
        else
            System.out.println("Papa No puede asistir al juego de su hijo");*/
        // OPERADOR TERNARIO
        //EL OPERADOR TIENE TRES PARTES 1° UNA CONDICION A EVALUAR 2° SEGUN AL EVALUAR LA PRIMER CONDICION NOS VA A DAR UN RESULTADO
        // NOS VA A REGRESAR UN VALOR Y PUDE SER UN VALOR Y LA 3°PUEDE REGRESAR OTRO VALOR DIFERENTE, SEGUN LA CONDICION VAMOS A TENER 2 RESULTADOS
        //UNO VERDADERO O UNO FALSO
        
        /*var resultadoT = (5 > 8 )? "verdadero":"falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 4;//el operador es solo para expresiones sencillas si se hace un codigo mas largo se usa el if ,else
        resultadoT = (numeroT % 2 == 0) ? "Es Par": "Es Impar";
        System.out.println("resultadoT = " + resultadoT);*/
        
        //PRIORIDAD DE LOS OPERADORES
        //RECORDEMOS LAS EXPRESIONES SE EVALUAN DE IZQUIERDA A DERECHA, NO DE LA ASIGNACION A UNA VARIABLE.RECUERDEN LA ASIGNACION A UNA VARIABLE
        //EVALUA EJ TIPO VAR DONDE LA VARIABLE X EVALUA PRIMERO LA PARTE DERECHA ENTONCES CON LA INFERENCIA DE TIPO, AUTOMATICAMENTE
        //JAVA EN ESTE CASO HACIA LA IZQUIERDA LE ASIGNA UN TIPO (INT,ENTERO)
        var x = 5;
        var y = 10;
        var z = ++x + y--;//recordar las expresiones ++x + y-- se evaluan de izquierda a derecha para poder usar la tabla de prioridad
        System.out.println("x = " + x); //6
        System.out.println("y = " + y ); //9
        System.out.println("z = " + z);  //16
        
        var solucionAritmetica = 4 + 5 * 6 / 3; // primero multiplica 5*6 depues sigue la division 30/3=10 y por ultimo la suma 10 + 4 =14
        System.out.println("solucionAritmetica = " + solucionAritmetica);//4+((5*6)/3)=30/3=10+4=14
        
        solucionAritmetica = (4 + 5) * 6/ 3;//4+5=9*6=54/3=18
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        

    }

}
