/*
Los diferentes significados de la palabra final dependiendo de la hubicacion en la que se encuentre
USO DE LA PALABRA FINAL
Esta palabra tiene diferentes significados dependiendo donde se aplique:
    variables:Evita cambiar el valor que almacana la variable 
    métodos:Evita que se modifique la definicion o el comportamiento de un metodo desde una subclase(hija)
    clases: Evita que se creen clases hijas
Otra caracteristica es que normalmente ,cuando trabajamos con variables se convina con el modificar de acceso estatico para 
convertir una variable en una cosntante, es decir que no se puede modificar su valor, el ejemplo de esto es la 
clase Math en la cual todos sus atributos son de tipo static y final, es por esto que la variable pi*se conoce como
una costante.

*/
package test;

import domain.Persona;


public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 39555278;
        System.out.println("miDni = " + miDni);
       // miDni = 20312321;No se puede modificar 
       //Persona.CONSTANTE_AQUI_= 9;// NO SE MODIFICA 
        System.out.println("Mi atributo consatante es: "+Persona.CONSTANTE_AQUI_);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona(); NO SE PUEDE SIGNAR UNA NUEVA REFERENCIA 
        persona1.setNombre("Ariel betancud");
        System.out.println("persona1 mombre: "+persona1.getNombre());
        /*
        NO SE PUEDE MODIFICAR LA REFERENCIA PERO SI EL CONTENIDO DEL OBJETO,EL OBJETO EN SI NO SE PUEDE HACER UNA NUEVA REFERENCIA PATA UN NUEVO OBJETO 
        PERO SI SE PUEDE MODIFICAR EL VALOR DEL ATRIBUTO, MODIFICAMOS Y MOSTRAMOS EL CAMBIO EN EL ATRIBUTO
        */
        persona1.setNombre("Liliana");
        System.out.println("persona1 mombre: "+persona1.getNombre());
    }
    
}
