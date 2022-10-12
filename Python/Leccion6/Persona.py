# vamos a empezar a crear una clase se va a llamar persona,dentro de esta clase
#HEMOS CREADO UNA CARPETA para comenzar a trabajar con una  CLASE, UNA CLASE ES LA PLANTILLA,despues vamos a tener atributos
#que son las caracteristicas y los objetos que son las acciones

# Ahora vamos a pasar a los atributos para agregar caracteristicas o atributos a una clase necesitamos utilizar un metodo,este metodo se lo conoce
#como init, este metodo inicializado se lo conoce como un costructor ,en Python el costructor esta oculto y se llama directamente por el lenguaje asi es que
# el metodo init es llamado por lenguaje Python. Para poder inizializar los objetos va a depender de este metodo init

#class Persona: # Creamos una clase, dentro vamos a poner un pass
 #   pass # No se procesa nada mas (No tiene contenido)siempre que usemos pass se va a salir de la identacion
 #estamos viendo atributos que tienen que ver con objetos,mas adelante vamos a ver atributos con clases, ya que estos no son atributos con clases
 #porque estamos dentro de un metodo, si quisieramos poner un atributo debe ir arriba de este metodo, estamos usando atributos dentro de un metodo

class Persona:
    #se lo metodo se lo llama init Dunder
    #como va a diferenciar nuestro metodo cual es el atributo y cual es la variable, en este caso lo hace atravez del self.nombre ya sabe self.nombre es
    #el atributo y nombre va a ser la variable, nos marca error necesitamos dejar el self que va por defaultponemos, (apellido,nombre y edad estas son las
    #variables que van a venir por parametro
    #self.nombre son atributos de metodo , no de clase porque en la clase no hemos puesto ningun atributo
    def __init__(self,nombre,apellido,edad):# aqui con def init inicializamos un objeto,init tiene una variable predefinida que es self,self es el parametro por default,
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad # no es comun asignar valores por default a los atributos, este ejercicio no es muy comun

    # por defecto se añade inmediatamente el self, es un operador que va a apuntar a un espacio de memoria y automaticamente se crease conoce como método de instancia es automatico
    def mostrar_detalle(self):
        print(f'Persona:{self.nombre} {self.apellido} {self.edad}') #para acceder a los atributos usamos el objeto esto porque estamos fuera de cualquier metodo,/ahora cuando estamos dentro del
        #metodo para acceder a los atributos de otro metodo de esa misma clase, vamos a utilizar la palabrita self
        # La variable self solo se encuentra dentro de los metodos/ los metodos y las funciones son iguales, el metodo depende de que se llame atravez de
        #la clase,utilizamos lo mismo de una funcion para un metodo


#este parametro es una referencia al objeto que se va a crear el self, va ser la referencia al objeto,salimos de la clase
#los parentesis no pueden quedar vacios, necesitamos enviar argumentos
persona1 = Persona('Ariel','Betancud','40') # vamos a utilizar la asignacion de lo que es la clase Persona, abrimos parentesis este contructor que estamos poniendo
#este contructorPersona() apunta directamente al metodo def __int__(self):
#creacion de metodos por argumentos
#print(persona1.nombre)  # si aca ponemos un print y queremos ver de que se trata esta clase Persona NOS nuestra que es una clase
# nos muestra class -- main --Persona, ese main es el init
#print(persona1.apellido)
#print(persona1.edad)
print(f'El objeto1  de la clase persona: {persona1.nombre} {persona1 .apellido} su edad es: {persona1.edad}')
# creamos un segundo objeto
persona2 = Persona('Osvaldo','Giordanini',45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2 .apellido} su edad es: {persona2.edad}')
# se deben respetar las reglas de solo acceder a atributos existentes, si ponemos alguno que no esta nos va a dar error, si pongo el atributo mascota
#no esta, no esta el aributo mascota, esta el atributo apellido ,nombre y edad
# se utilizan tipos dinamicos ,puede variar de que tipo sea
# los objetos no comparten los valores, solo comparten los atributos y asi podemos asignar diferentes  valores a cada atributo
#hasta aqui hemos creado atributos de instancia de objetos, estos se asgnan a nuestros objetos de esta manera es que no comparten informacion

# referencias de memoria de los objetos

#¿ SE PUEDEN MODIFICAR LOS ATRIBUTOS DE UN OBJETO?, BUENO TOTALMENTE SE PUEDEN MODIFICAR

persona1.nombre = 'Liliana '  # persona1 lo vamos a modificar con .(punto) acceder a nombre y le asignamos un nuevo nombre
persona1.apellido ='Buccella'
persona1.edad = '40' # hemos modificado todos los datos
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1 .apellido} su edad es: {persona1.edad}')
# Se pueden modificar sin problema estos objetos


#LOS METODOS DE INSTANCIAS
#Los atributos son: caracteristicas
#Los metodos son: el comportamiento que van a tener los objetos(acciones)
# un método es igual que una funcion, ahora cual es la diferencia que al método se lo llama ,porque se asocia con una clase, esa es la diferencia entre
#el método y la funcion, que el método esta asociado a una clase y la función no es propia de si misma.

#Vamos a definir un metodo de lo que es la clase,respetando lo que es la tabulacion y la identacion tiene que haber una tabulacion para ingresar datos en
#lo que es la clase

persona1.mostrar_detalle()
persona2.mostrar_detalle()

