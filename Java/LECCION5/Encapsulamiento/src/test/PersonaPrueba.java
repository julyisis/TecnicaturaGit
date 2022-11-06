/*

*/
package test;

import dominio.Persona;
public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new   Persona("Osvaldo",57.000,false);
        //MODIFICAR A TRAVEZ DE LOS METODOS
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        persona1.setNombre("Juan Ignacio");
       //persona1.nombre = "juan Ignacio";//Ya no se puede utilizar
       // System.out.println("Nombre es: "+persona1.nombre);ERROR
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        //Tarea: crear otro objeto de tipo Persona,asignar valores de manera inicial 
        // y Imprimir, luego modificar sus valores y volver a imprimir TEREA PARA HECER 
        System.out.println("persona1 = " + persona1);//De esta forma ya cuando ponemos que estamos concatenando clase persona1, va a llamr solito al TOSTRING
    }
    
}
