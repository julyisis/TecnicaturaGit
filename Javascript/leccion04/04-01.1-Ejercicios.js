//Estaciones del año
let mes = 4;
let estacion;//Undefined
if (mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Valor Incorrecto";
}
console.log("EL valor corresponde a la estacion de: "+estacion);

//Ejercicio 2 : Hora del dia
/*
de 6 a 11 saluda: good morning
de 12 a 16 saluda: good afternoon
de 17 a 19 saluda: good evening
de 20  a 23 saluda: goof night
se trabaja con 24 hs
*/

let horaDia = 6;
let mensje;
if(horaDia >= 6 && horaDia <= 11){
    mensje = "Good Morning";
}
else if(horaDia >= 12 && horaDia <= 16){
    mensje = "Good Afternoon";
}
else if(horaDia >= 17 && horaDia <= 19){
    mensje = "Good Evening";
}
else if(horaDia >= 20 && horaDia <= 23){
    mensje = "Good Night";
}
else{
    mensje = "Valor incorrecto";
}
console.log(mensje);

//Estructura Switch(La sintaxis es igual en JAVA)
switch(mes){//Ademas de numero, también se pueden utilizar cadenas
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "otono";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        estacion = "Valor incorrecto";

}
console.log("Bienvenido a la estacion de: "+estacion);

//Ampliando el uso de var let y const
/*
Con var puedes reasignar en cualquier momento este
forma parte del ambito global 
un error es que se sobreescriba 
*/

var nombre = 'Ariel';
nombre = 'Osvaldo';
console.log(nombre);

function saludar(){
    var nombre3 = 'Natalia';
    console.log(nombre3);
}
//console.log(nombre3); //Aqui no lee el dato en la funcion 


if(true){
    var edad = 34;
    console.log(edad);
}

/*
let:esta puede ser reasignada en cualquier momento la diferencia es que 
el ambito es de bloque,solo disponible dentro de un bloque de llaves o 
dentro de una funcion 
*/
function saludar2() {
    let nombre2 = 'Ariel'
    console.log(nombre2);
    
}

//console.log(nombre2);
if(true){
    let edad2 = 33;
    console.log(edad2);
}


//console.log(edad2);

/*
const se utiliza para calores constantes que no pueden
ser reasignadas
*/

const fechaNacimiento = 2006;
console.log(fechaNacimiento)
//fechaNacimiento = 2003;
//console.log(fechaNacimiento);//solo se ejecuta el console anterior

//Evitar repetir tu codigo
//Dry don't repeat yours yourself
//let days = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'];
let days = 5; //creamos una variable llamada days,donde le vamos a pner uno de los dias en codigo duro
switch (days) { //con switch que lea a traves de la variable creada que dato he ingresado
    case 1:
        console.log('hoy es Lunes');
        break;
    case 2:
        console.log('hoy es Martes');
        break;
    case 3:
        console.log('hoy es Miercoles');
        break;
    case 4:
        console.log('hoy es Jueves');
        break;
    case 5:
        console.log('hoy es Viernes');
        break;
    case 6:
        console.log('hoy es Sabado');
        break;
    case 7:
        console.log('hoy es Domingo'); 
        break;                      

    default:
        console.log('Error en el ingreso del dia de la semana');
        break;
}
//Asi logramos un codigo mucho mas eficiente
let days2 = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']//aqui creamos un arreglo
function getDay(n){
    if(n < 1|| n >7){
       throw new Error('out of range'); 
    }
    return days2[n-1];
}
console.log(getDay(3));//aqui tenemos 8 lineas de codigo

//Hacer un ejercicio similar al que esta hecho,pero con los meses del año,
//debes hacerlo con la estructura switch y luego con la funcion en
//la opcion mejorada 

let months = 1;
switch (months) {
    case 1:
        console.log('mes Enero');
        break;
    case 2:
        console.log('mes Febrero');
        break;
    case 3:
        console.log('mes Marzo');
        break;
    case 4:
        console.log('mes Abril');
        break;
    case 5:
        console.log('mes Mayo');
        break;
    case 6:
        console.log('mes Junio');
        break;
    case 7:
        console.log('mes Julio');
        break;
    case 8:
        console.log('mes Agosto');
        break;
    case 9:
        console.log('mes Septiembre');
        break;
    case 10:
        console.log('mes octubre');
        break;
    case 11:
        console.log('mes Noviembre');
        break;
    case 12:
        console.log('mes Diciembre');
        break;                

    default:
        console.log('Error No corresponde a ningun mes');
        break;
}

let months2 = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
function getMonths(n){
    if(n < 1 || n > 12){
        throw new Error('out of range');
    }
    return months2[n -1];
}
console.log(getMonths(5));
