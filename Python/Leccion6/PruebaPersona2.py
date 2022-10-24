# Aqui lo que vamo hacer ed importar una clese,para importar una clase, archivo o modulo es lo mismo
#Lo que vamos usar para importar usamos from Persona...  import
# podriamos importar mas de una clase / El modulo Persona2 entonces que es lo que se haria si
#si quisieramos importar todas solo debemos agregar un asterisco(*) y esto incluye a las funciones
# que tambien esten alli con el asteristico estariamos importando todas las clases


from Persona2 import Persona2
print('Creacion  de objetos'.center(50,'-'))
if __name__ =='__main__':
    persona5 = Persona2('Lionel','Messi',35) # En los parentesis les vamos a pasar los argumentos
    persona5.mostrar_detalles()

# Cuando nosotros estamos importando el compilador va a leer todo lo que este en la clase Persona
#en este caso es en pruebaPersona2/ no vamos a usar persona1 en la linea 10 simplemente vamos hacer unos cambios
#porque ya teniamoa a persona1 en lo que era en la clase Persona2 y hemos llegado a persona4 vamos a crear una persona5
# en la linea 10 en vez de persona1 va a hacer persona5

# Aqui en Python existe una comprobacion de MODULO PRINCIPAL en lo que es la ejecuccion esta es una herramienta que tenemos si ponemos un print
print(__name__) #ejecutamos y vemos que hasta ahi llega la clase Persona2 pero estamos ejecutando este otro codigo dentro de lo que es el main
#la clase donde estamos ejecutando el main para que sirve esto mas alla de decirnos donde estamos, nos venimos a Persona2 y ejecutamos hasta aqui
# nos va a decir que lo que tenemos aqui es del main /Estasmos en la clase Persona2 ejecutando el codigo / Que hay que hacer para que todo este codigo
# que hemos estado trabajando dentro de programacion orientada a objetos no se vea cuando estamos en PruebaPersona2 simplemente que trabaje con las
#comprobaciones que estamos haciendo dentro de la prueba entonces vamos a poner una extructura if


#Ahora vamos a ir con lo que se llama destructor de objetos /vamos a poner un print
print('Eliminacion de objetos'.center(50,'-'))
del persona5