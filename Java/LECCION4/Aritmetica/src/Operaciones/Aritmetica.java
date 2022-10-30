/*
EN ESTE PROYECTO VAMOS A COMENZAR CON LOS ATRIBUTOS, LOS ATRIBUTOS Y METODOS COMIENZAN CON MINUSCULA,ESTO PARA SABER DIFERENCIAR ENTRE ESTOS Y UNA CLASE
LA NOMENCLATURA QUE USAMOS PARA LAS CLASES ES LA TIPO PASCALCASE, NO ASI PARA LOS METODOS Y ATRIBUTOS PARA ESTOS SIEMPRE EMPIEZAN CON MINUSCULA, LA CLASE SIEMPRE TIENE QUE 
SOBRESALIR Y COMIENZA CON MAYUSCULA, SIMPRE QUE ENCONTRAMOS UN CODIGO UNA PALABRA QUE EMPIEZA CON MAYUSCULA SABEMOS QUE ESTA APUNTANDO A UNA CLASE
*/
package Operaciones; //necesitamos que se muestre el paquete,la carpeta que se llama Operaciones,que se muestre el origen donde se esta guardando nuestra clase que es Aritmetica


public class Aritmetica {
    //ATRIBUTOS DE LA CLASE/VAMOS A PONER LOS ATRIBUTOS DE TIPO ENTERO,PERO NO LO VAMOS APONER DE UNA MANERA DESCRIPTIVA VAMOS A USAR VOCALES O LETRAS
    //esto en los tipos primitivos su valor por defoult es 0/un tipo entero que comienza sin asignarle nada el valor que le asigna java x default es 0
    int a; //estas variables no estan vacias tienen el valor de 0 asignado por default por java/ Algo muy importante los programadores deben buscar soluciones y repara errores
    int b;
    /*AQUI VAMOS A CREAR UN METODO 
    LOS METODOS COMIENZAN CON EL MODIFICADOR DE ACCESO,HAY QUE ESPECIFICAR EL METODO DE ACCESO, ENTE CASO ES DE TIPO PUBLICO(PUBLIC)Y VOID (SIGNIFICA QUE NO VA A DEVOLVER NADA 
    PONEMOS EL NOMBRE DE SUMA PARENTESIS Y ABRIMOS LLAVE,suma esta escrito en MINUSCULA SI TUVIERA QUE SEGUIR DE UNA PALABRA IRIA EN MAYUSCULA,SERIA NOMENCLATURA DE CAMELCASE
    EJ:public void sumaNumeros(){ numeros va a comenzar con MAYUSCULA,la escritura CAMELCASE es lo que se utiliza para los METODOS Y ATRIBUTOS,pero para "LA CLASE ES PASCALCASE"
    EXISTEN VARIOS MODIFICADORES DE ACCESO/ EL MODIFICADOR ES EL PUBLIC Y ESTO ES PARA QUE OTROS METODOS TENGAN ACCESO A ESTE OTRO Y OTRAS CLASES TUVIERAN ACCESO CUANDO USAMOS  
    EL DE TIPO PUBLICO / PARA EL METODO PONEMOS EL IDENTIFICADOR DE ESTE METODO QUE SERIA EL NOMBREDE ESTE METODO SERIA sumarNumero ese es el identificador
    ponemos public luego ponemos void el nombre de nuestro metodo,con el tipode escritura camelcase y luego los parentesis/que dentro de los parentesis podemos necesitar
    poner atributos por ejemplo de tipo enteros num1,num2
    todo lo que esta dentro del metodo se lo conoce como cuerpo de la clase y las variables que se definen dentro se definen como variables locales,estas variables se crean
    y se destuyen al terminar de ejecutar aqui tambien se pueden llamar a otros metodos
    
    vamos a crear una variable de tipo local que se va a llamar resultado 
    
    */
    public void sumarNumeros(){ //este no tiene nada,no retorna nada simplemente devuelve un mensaje 
        int resultado = a + b ;//le vamos a asignar la suma de los dos atributos 
        System.out.println("resultado = " + resultado);//mandar informacion a la consola no es lo mismo que regresar un valor /uuna cosa es definir el netodo y otra es utilizarlo
        
        //en este caso lo hemos definido pero no lo hemos utilizado 
        /*
        vamos a ir a la clase y vamos a crear otro metodo en la clase este metodo se va a llamar,primero va hacer public si ponemos void, no nos devuelve ningun valor es vacio
        en este caso lo vamos hacer de tipo entero
        */
    }
    public int sumarConRetorno(){ //este consta de un tipo entero retorna ya aldo l que es este metodo, este retorna el valor de una expresion 
     //int resultado = a+ b; //le ponemos una variable que va hacer resultado = a+b
       return a + b;
    } 
    /*
    Para recordar cuando ponemos public(es el modificador de acceso)luego pasamos al tipo de retorno va a ser int,void
    lo siguiente es el identificador o nombre del metodo ,en esta ocacion es sumar con argumentos ,dentro de los parentesis vamos a pasarle
    argumentos de tipo entero 
    se puede ver que el editor hace una diferencia entre la variable y el atributo cambia el color aqui lo marca al atributo en color verde
    */
    /*
    Ahora vamos a continuar con lo que es el uso del operador this/this es una palabra reservada de lo que es Java 
    y es una variable que se crea de manera automatica, en el momento que se esta ejecutando un objeto es cuando se crea
    automaticamente esta variable u operador tambien se le llama,Esta es una variable que apunto al objeto en ejecucion apunta al 
    objeto pero al espacio de memoria donde esta cargado el objeto bien 
    ponemos this y usamos el operador de punto se nos abre un monton de opciones, porque justamente es un operador que tiene el poder de señalar lo que es el atributo
    hacia lo que es otros metodos
    *//*
    this no lo habiamos puesto y por defecto ya se habia creado, al mismo tiempo que se creo para utilizar o apuntar hacia lo que es el atributo al mismo tiempo una vez que 
    se hizo la suma, se llamo al metodo de sumar con retorno, una vez finalizado eso y sale de la clase, este objeto this esta variable se elimina 
    Este this es solo dentro de la clase 
    */
    public int sumarConArgumentos(int a, int b){ //con las llaves ya creamos el metodo los argumentos es la informacion que va a recibir el metodo
        this.a = a;//El argumento a se asigna al atributo this.a/arg1 es la variable para el argumento y this es el atributo
        this.b = b;
        //return a + b;
        return sumarConRetorno();//dentro de un metodo lo que se esta pidiendo que se retorne otro metodo 
        //cuando ponemos el this los programadores es para que el codigo sea mas legible, el operador this hace que se diferencien los atributos de los argumentos aunque tengan 
        //los mismos nombres 
    }
}
