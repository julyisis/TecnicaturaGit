/*
podemos ver el estado del objeto,tenemos varis datos, la mejor practica es encapsular varios atributos
ahota vamos autilizar un modificador de acceso llamdo private,este evita el acceso directo,para acceder a los datos 
solo sera por medio de otros metodos, esos metodosvan a ser el GETTER Y SETTER,elel estado del objeto es que va a estar encapsulado 
y la unica manera para acceder es atravez de lo externoque son los metodos de los objetos, inertface o metodos del objeto
son los get y los set y es la unica manera para poder llegar a los datos, el estado del objeto
como podemos observar la idea de encapsulamientode la programacion orientada a objetos es evitar el acceso y manipulacion directa de otras clases
a los datos de un objeto por datos nos referimos a cuaslquier atributo de la clase en cuestion,esto es el estado del objeto,para acceder a los
datos solo sera por medio de los metodos setter y getter
-Recuerden que Setter modifica el valor del atributo
-y los Getter obtienen informacion del atributo ,los getter y los setter van a ser los metodos de acceso y estos si deben ser publicos  para que logremos
acceder y los metodos setter y getter debemos crear uno por cada atributo 
*/
package dominio;


public class Persona { 
    /*ATRIBUTOS ESTA CLASE LA VAMOS ACREAR CON ATRIBUTOS DE TIPO PRIVATE
    que pasa si ponemos private con MAYUSCULA, no lo toma, es muy importante para Java lo que son MAYUSCULAS Y MINUSCULAS
    el tipo STRING comienza con Mayuscula porque String no esta dentro de lo que son los tipos primitivos 
    los tipos primitivos son double,boolean,int,long,todos estos son tipos primitivos, String no entra dentro de los grupos primitivos
    por eso debe comenzar con Mayusculas a diferencia de los otros
    los atributos se han marcado de color verde (nombre,sueldo y eliminado)las palabras reservadas el editor las muestra en azul
    */
    private String nombre;
    private double sueldo;
    private boolean eliminado;
    /*VAMOS A CREAR AL CONSTRUCTOR de la clase Persona que va hacer de tipo Publico
    recuerden que siempre el CONSTRUCTOR debe llevar el mismo nombre que la clase, pero ya si nuestros atributosa son de 
    tipo privateya no se pueden acceder a ellos, la unica manera de acceder a ellos es atravez de los metodos 
    en este caso EL METODO PRINCIPAL ES EL CONSTRUCTOR, entonces el CONSTRUCTOR debe ser de tipo PUBLICO si no o podriamos acceder a los atributos
    dentro de los parentesis necesitamos definir lo que serian los atributos,las variables que vamos a recibir para modificar estos atributos 
    */
  public Persona(String nombre, double sueldo, boolean eliminado){ //pasamos las variables que serian nombre,sueldo y elim...
      this.nombre = nombre; //vamos a usar this nombre se va aponer de verde mas oscuro este es el atributo el otro nombre es la variable
      this.sueldo = sueldo; // de la linea 34 a la 38 tenemos creado el contructor
      this.eliminado = eliminado;
    }
  //VAMOS A CREAR LOS METODOS QUE NECESITAMOS Y estos metodos van a ser el METODO SETTER Y GETTER 
  public String getNombre(){
      return nombre;
  }
  public void setNombre(String nombre){// es el que modifica 
      this.nombre =nombre;
      
  }
  public double getSueldo(){
      return sueldo;
  }
  public void setSueldo(double sueldo){ //los get no devuelven nada pero si necesitan recibir un parametro, que es el que va a modificar nuestro atributo
      this.sueldo =sueldo;
      
  }
  public boolean isEliminado(){ //"aca en get nombre vamos a USAR EL IS porque los booleanos hace una pregunta" solo cambia para el get en los boolean
      return eliminado;
  }
  public void setElimidado(boolean eliminado){
      this.eliminado = eliminado;
  }
    
}
