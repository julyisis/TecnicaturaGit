/*
la clase cliente va a ser hija de la clase Persona en la linea 7 a continuacion de 
cliente ponemos cliente extends Persona {
*/
package domain;

import java.util.Date;

/*
sabemos que la clase cliente esta heredando de la clase Persona,cliente entonces es clase hija 
de la clase Padre Persona 
vamos a poner los atributos que sabemos ya que la clase cliente no va a tener hijas, asi que 
podemos encapsularlo nuestros atributos de manera privada, en privateya no es protected porque no va a heredar
a nadie de lo que es la clase cliente 
*/
public class Cliente extends Persona{
    //ATRIBUTOS
    private int idCliente;
    private Date fechaRegistro;//Importar la clase Date 
    private boolean vip; //Very important person
    private static int contadorCliente; //Tip estatico
    
    //Constructor
    public Cliente(Date fechaRegistro,boolean Vip, String nombre,
            char genero, int edad,String direccion){
        super(nombre, genero,edad,direccion); //va en primer lugar de la clase hija  contructor de la clase Padre object desde alli viene atravez de el podemos acceder a los datos de la clase PadrePersona
        this.idCliente = ++Cliente.contadorCliente;//estamos llamando a los argumentos de la clase Padre para utilizarlos 
        this.fechaRegistro = fechaRegistro;
        this.vip = vip;
                
    }

    public int getIdCliente() {
        return this.idCliente;
    }


    public Date getFechaRegistro() {
        return this.fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public boolean isVip() {
        return this.vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente{idCliente=").append(idCliente);
        sb.append(", fechaRegistro=").append(fechaRegistro);
        sb.append(", vip=").append(vip);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
    
    
    
    
}
