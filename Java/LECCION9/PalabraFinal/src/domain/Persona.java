/*
Dentro de la clase Persona vamos a crear un atributo que va a ser public que es finalestatic, y lo que son las constantes 
se escriben con MAYUSCULA este formato se lo conoce como constante 
Una variable marcada como final generalmente se la convina con lo que es static esto para poder llamar a la variable 
solo utilizando el nombre de la clase sin necesidad de instanciar, esta no se piede modificar
se tecomienda que una CONSTANTE se defina el MAYUSCULAS 
*/
package domain;


public  class Persona { // Esta es una clase constante quiere decir que si creamos otra clase //vamos a crear un atributo
    public final static int CONSTANTE_AQUI_ =15;//esta es la sintaxis correcta para establecer una 
    private String nombre;//agregamos un atributo de tipo private va a ser String

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    public void imprimir(){
        System.out.println("Metodoas para imprimir");
        
    }
    
    
}
