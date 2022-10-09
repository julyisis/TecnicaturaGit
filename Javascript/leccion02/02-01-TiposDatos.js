//tipos de datos en JavaScript
/*
La sintaxis en lo que es comentarios es muy similar a la de Java 
realmente diriamos que es identica
*/
//vamos a comenzar con un dato de tipo string,podemos utilizar doble comilla o simples
var nombre = "Ariel";
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);
//vamos a crear un tipo numerico
var numero = 3000; //Tipo Numerico
console.log(numero);
//Tipo Objeto // se abren llaves, para los objetos se mayormente de esta manera,para 
var objeto = {  //asignarle a lo que son los obj ya dentro de la asignacion a un obj no se 
    nombre:"Ariel",//usa el igual se usan los dos puntos(:)ete obj queremos que tenga un nombre
    apellido:"Betancud",
    telefono: "2614563546"//en la ultima caract no hace falta agregar coma(,)
}
console.log(typeof objeto);
//Las variables en JavaScript SON DINAMICAS, SE PUEDEN MODIFICAR EL TIPO DE DATO,
//REUTILIZANDO la misma variable 

//Tipo de dato boolean
var bandera = true;
console.lo(bandera);

//Tipo de dato funcion 
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato Symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

//VAMOS A VER LAS CLASES //TIPO DE DATOS CLASES
//LAS CLASES SON TAMBIEN SON FUNCIONES 
class Persona{   // esto es parecido a definir un objeto a esta clase persona le podemos agregar lo que llamamos atributos,especificandolos con un contructor,el contructor nos va a permitir crear un objeto de la clase
    constructor(nombre,apellido){  // asi definimos lo que es una clase, que tambien es una funcion
        this.nombre = nombre;
        this.apellido = apellido;
    }

}

console.log(Persona);

