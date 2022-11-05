  
package Operaciones;


public class PruebaAritmetica {
    public static void main(String[] args) {
        /*lo que es aritmetica con parentesis estamos llamando a la clase en si en este caso estamos llamando al contructor esto reserva espacio de memoria
        este objeto que hemos creado va a trabajar directamente sobre el espacio de menoria que tiene aqui el constructor de la clase aritmetica ahora a esteobjeto le vamos
        agregar valores pero esos valores le vamos agregar van hacer para los tributos, vamos a modificar el valor de los atributos por medio del objeto aritmetica1
        */
        //VARIABLE LOCAL EN ESTE CASO PODEMOS USAR VAR O LA PODEMOS DEJAR DE TIPO ENTERA 
        var a = 10; //los atributos no es lo mismo que la variable tienen un alcance superior a una variable local es por eso que atravez del new el alcance de los contructores
        int b = 7;//el alcance del atributo es superior totalmente a una variables estas son variables locales //memoria STACK
        miMetodo();//Llamamos el metodo nuevo
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        
        aritmetica1.sumarNumeros();// que hizo le hemos asignado el valor al atributo a, le asignamos valor al atributo b luego estamos atravez del objeto llamando al metodo 
        //que el metodo lo que hace es sumar 
        //PARA ALMACENAR UN OBJETO O LOS ATRIBUTOS SE UTILIZA LA MEMORIA HEAP
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
      resultado = aritmetica1.sumarConArgumentos(12,26);
        System.out.println("Resultado usando argumentos = "+resultado);
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        
        
        //aritmetica1 = null; nunca se debe utilizar 
        //System.gc();metodo para limpiar residuos, es pesado, no utilizar 
        Persona persona = new Persona("Ariel","Betancud");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona nombre: "+persona.apellido);
        
    }
    
    /*
    DE LA LINEA 6 HASTA LA LINEA 31 TENEMOS EL METODO MAIN INCLUYENDO LA LLAVE DESPUES DE LA LLAVE DANDO ENTER PODEMOS CREAR OTRO METODO, CREAMOS EL MODIFICADOR DE ACCESO
    para que esto funcione tiene quie ser static void y el identificador va hacer miMetodo, aqui tenemos un metodo mas
    EL ALCANCE DE VARIABLE ES DENTRO DE UN METODO
    */
    //MODULARIDAD CREAMOS UN NUEVO METODO
    public static void miMetodo(){ //esta variable no puede trasender del metodo main al metodo miMetodo()no tieneese alcanse
       // a = 10;//una variable esta limitada, si no la inicializamos con el int surge un error 
        System.out.println("Aqui hay otro metodo");
    }
}

/*
AQUI VAMOS A CREAR UNA CLASE DENTRO DE OTRA CLASE: SI QUEREMOS CREAR UNA CLASE,FUERA DE LO QUE ES LA CLASE QUE YA TENEMOS,SOLO PUEDE SER UNA CLASE PUBLICA
LAS DEMAS NO, COMO YA TENEMOS, LA CLASE PUBLIC PruebaAritmatica,solo puede ser una clase publica, las demas no,como ya tenemos la clase Prueba Aritmetica de tipo publica
la proxima clase que creemos aqui abajo,fuera de esta clase,ya no puede ser de tipo publica,no puede tener este modifiacador de acceso
el modificador de acceso que va a tener por default se lo conoce tambien como packcage y nunca se va a mostrar, no es necesarioescribirlo
tampoco,pero al omitir cualquier modificador es asi como se le va a conocer
para crear una clase lo hacemos en minuscula y empezamos con la palabrita class y no olvidar las llaves 
dentro de la clase le vamos asignar atributos, a esta clase solo se puede acceder dentro del mismo paquete ,vamos a crear dos atributos dentro del misma clase
y vamos a crear un metodo este tambien es un costructor va a hacer del tipo persona de la clase que estamos haciendo
pero tampoco a este metodo se le va a asignar un modificador de acceso,tambien va a recibir un modificador por default
*/

class Persona {
    String nombre;
    String apellido;
    
    Persona(String nombre , String apellido){ //para diferenciar esto vamos a necesitar el operador this //CONSTRUCTOR
        //super();//Llamada al constructor de la clase Padre object
        //Imprimir imprimir = new Imprimir();//asi es como construiamos un objeto, lo estamos constr, en la clase persona,pero estamos constr, un obj instanciandolo de la clase
        //Imprimir que esta en la linea 103 y podemos acceder sin restricionesya que todo esta dentro del cuerpo de lo que estan todas las clases serian miembros de un 
        //mismo lugar ahora vamos hacerlo de la sigiente manera usando directamente new
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}    
    /*
    En la linea 62 a la 64 hemos definido la clase Personade la 66 a la 69 hemos creado un metodo constructor para esta clase
    SI NOSOTROS AQUI EN LA LINEA 75 QUEREMOS MOSTRAR UN OBJETO COMO ES QUE PODEMOS IMPRIMIR EL OBJETO ACTUALPODEMOS HACER DIRECTAMENTE DESDE EL THIS
    es la forma que tenenmos pára trabajar de una clase o dentro de los metodos, en este caso en el metodo constructor de la clase persona 
    utilizamos el this dentro de lo que es el main,utilizamos los objetos y dentro de lo que es una clase vamos a utilizar el this
    para acceder esa es la manera 
    esto que va hacer va a mostrar el mismo espacio de memoria que estamos trabajando
    -dentro de este contructor vamos a encontrar una llamada que no vemos del contructor de la clase padre y es un contructor vacio
    que tiene la clase padre, no lo vemos. Al haber otra clase de por medio es esa la manera en que esta trabajando, ese 
    contructor vacio no necesita pasar argumentos, este constructor de la clase object es el encargado de reservar el espacio de memoria 
    si lo ponemos debe estar en la primera linea,tambien es el encargado de regresar esa referencia, cual seria entoncees el metodo 
    constructor de la clase Padreseria en la linea 73 super()antes de lo que son los atributos y las variables y los atributos para apuntar a 
    los espacios de memoria de estos atributos "super" seria el constructor vacio que no necesita qque le pasemos argumentos es el encargado de 
    regresar esa referencia 
    Gracias a esto es que el operador this puede utilizarce para acceder al espscio de memoria como lo hicimos aqui en la linea 76 
    ahora vemos que el operador this apunta mas alla de lo que es esta clase persona 
    todas las clases son herencia de una clase object, detras de cada clase hay otras clase a las cuales hay llamados que se estan haciendo 
    de los cuales desconocemos.Es por eso que atravez del operador this se habilita para regresar esta referencia y utilizar el espacio de memoria que se 
    le ha asignado
    VAMOS A CREAR OTRA CLASE QUE SE VA A LLAMAR IMPRIMIR
    */

class Imprimir{
    public Imprimir(){ //Dentro de esta clase vamos a poner el metodo constructor Imprimir
        super();    //Dentro de este metodo constructor vamos a poner el //constructor de la clase Padre para reservar memoria 
    } 

    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresion del objeto actual (this): "+this);
    }

}
