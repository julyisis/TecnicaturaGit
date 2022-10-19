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
    def __init__(self,nombre,apellido,dni,edad,*args,**kwargs):# aqui con def init inicializamos un objeto,init tiene una variable predefinida que es self,self es el parametro por default,
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de una manera sugerida
        self.edad = edad # no es comun asignar valores por default a los atributos, este ejercicio no es muy comun
        self.args = args
        self.kwargs = kwargs

    # por defecto se añade inmediatamente el self, es un operador que va a apuntar a un espacio de memoria y automaticamente se crease conoce como método de instancia es automatico
    def mostrar_detalle(self):#self es identica su sintasis a la palabra en java this/no es oblig que se llame self se le puede cambiar el nombre
        print(f'La clase Persona tiene los siguientes datos:{self.nombre} {self.apellido} {self._dni} {self.edad},la direccion es:{self.args},los datos importantes son: {self.kwargs}') #para acceder a los atributos usamos el objeto esto porque estamos fuera de cualquier metodo,/ahora cuando estamos dentro del
        #metodo para acceder a los atributos de otro metodo de esa misma clase, vamos a utilizar la palabrita self
        # La variable self solo se encuentra dentro de los metodos/ los metodos y las funciones son iguales, el metodo depende de que se llame atravez de
        #la clase,utilizamos lo mismo de una funcion para un metodo


#este parametro es una referencia al objeto que se va a crear el self, va ser la referencia al objeto,salimos de la clase
#los parentesis no pueden quedar vacios, necesitamos enviar argumentos
persona1 = Persona('Ariel','Betancud',32456987,40) # vamos a utilizar la asignacion de lo que es la clase Persona, abrimos parentesis este contructor que estamos poniendo
#este contructorPersona() apunta directamente al metodo def __int__(self):
#creacion de metodos por argumentos
#print(persona1.nombre)  # si aca ponemos un print y queremos ver de que se trata esta clase Persona NOS nuestra que es una clase
# nos muestra class -- main --Persona, ese main es el init
#print(persona1.apellido)
#print(persona1.edad)
print(f'El objeto1  de la clase persona: {persona1.nombre} {persona1 .apellido} su edad es: {persona1.edad}')
# creamos un segundo objeto
persona2 = Persona('Osvaldo','Giordanini',303214565,45)
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
# aqui usamos la variable persona1.mostr...utilizando esa variable a la cual ya le hemos dado el poder de acceder atravez del operador de punto(.) es un objeto atravez de la clase ,la hemos convertido a esta
#variable en un objetoa travez del operador de punto vamos a poder acceder a los metodos y tambien acceder a los atributos/ Atravez de los metodos vamos a empezar hacer acciones con estos objetos
#para la referencia de estos objetos ya al utilizarlo como corresponde ya aqui se pasa la referencia de manera automatica
persona1.mostrar_detalle() # la referencia en este caso se pasa de manera autoamatica
persona2.mostrar_detalle()

#la palabra reservada self y atreibutos de istancia, esta palabrita self es identica , su sintaxis su uso es identico a la palabra que conocemos en otro lenguaje como en Java, la conocemos como la palabra dess
# en este caso en Python se usa la palabrita self , no es obligatorio que se llame self se le puede cambiar el nombre por ej habria que cambiarlo donde va apuntando a cada uno de los atributos, la documentacion de
#python recomienda que usemos esta palabra, si la cambiamos tenemos que tener en cuenta siempre es que tiene el primer parametro,cuando la ponemos dentro de los parentesis siempre lleva el primer lugar dentro de
# los paramentros, siempre va self y luego y luego irian los otros nombres,siempre vamos aponer aqui en los parametros, el primer parametro que va es la palabrita self y luego los otros parametros que vallamos a
#utilizar apuntando mlo que es al atributo en si

# otra manera de llamar al metodo directamente es hacerlo con el tipo persona
#vamos usar directamente lo que es la clase persona y alli vamos aponer Persona.mostrar_detalle , pero cuando se hace de esta manera y no se esta mostrando un objeto persona1 o persona2 si no estamos utilizando
#los objetos y estamod utilizando directamente la clase para llamar un metodo en este caso si o si vamos a necesitar una referencia paarle una referencia si no la referencia en estos casos se pasa de manera
#automatica
# aca ya no podemos usar el self porque va dentro de los metodos
#debemos pasarle una referencia para el self o dara error
#esta linea de codigo ya no es comun, habra que solucionarlo
# una ventaja es que podemos agregar atributos al objeto, sin que esos atributos esten cargados aqui en el metodo init en el metodo de inicializacion
#Persona .mostrar_detalle(persona1) # aqui ya no se pasa de manera autoamtica,aqui lo que vamos a necesitar es uno de los objetos ej persona1, si lo quitamos a persona1 nos va a dar error,esta linea de codigo no es utilizado
#podemos usar el objeto de persona1. y vamos a crear un atributo pero este atributo es unatributo superficial,porque no se comparten con los demas objetos solo va ser para persona1 y NO persona2 no va a ser uso
#Si quisieramos acceder al atributo telefono pero ya desde el objeto2, debemos poner persona2. telefono
persona1.telefono = '45254531254'  #hemos creado un atributo de un objeto y si agregamos la interpolacion queda asi:
print(f'Este es el telefono de:{persona1.nombre} {persona1.telefono}')

#print(persona2.telefono) # ejecutamos dentro del print, nos da error,de tipo atributo persona el objeto no tiene el atributo telefono/Todo esto no se usa normalmente la creacion del atributo atravez del objeto
# se pueden crear desde el mismo objeto el atributo, pero hoy en dia seria muy obsoleto, si nos muestra esto es para reparar en algun momento
persona3 = Persona('Rogelio','Romero',35789456,22,'Telefono','2614445557','calle Lopez',823,'Manzana',77,'Casa',18, Altura = 1.83,Peso=105,CFavorito='Azul',Auto='Citroen',Modelo=2021)
persona3.mostrar_detalle() # para acceder al DNI vamos hacerlo desde el metodo mostrar_detalle/ y muestra a Rogelio Romero 35789456 , 45
# Esto no se debe utilizaren Python esta encapsulado  print(persona3._dni)
#print(persona3._dni)# aqui el compilador de Python interpretando que esto no deberia suceder ,igual lo permite/cuando vemos esto que esta siendo mal utilizado porque dni esta encapsulado, pero python dicen
#podes utilizarlo igual,cuando vemos esto es porque el programador no sabe mucho del lenguaje de python esto no se debe utilizar de esta manera


#VAMOS A VER LO QUE SON LOS ENCAPSULAMIENTOS EN PYTHON ESTOS SON: TODOS LOS ATRIBUTOS QUE VEMOS EN DEF__INIT__(SELF)
#                                                                                                   SELF.NOMBRE = NOMBRE
#                                                                                                   SELF.APELLIDO = APELLIDO /TODO ESTO LO ESTAMOS MANEJANDO DE MANERA PUBLICA/EL ENCAPSULAMIENTO ES TOTALMENTE
#PUBLICO,/NO VAMOS A ENCONTRAR EN PYTHON PORQUE PYTHON NO FUNCIONA COMO OTROS LENGUAJES DONDE TIENEN LOS MODIFICADORES DE ACCESO QUE HEMOS VISTO EN JAVA, QUE EN JAVA TENEMOS LOS MODIFICADORES DE LA CLASE PUBLIC
#PRIVATE,/EN PYTHON NO ES ASI, EN PYTHON CUANDO VEMOS ESTE TIPO DE SINTAXIS SABEMOS QUE ESTOS ATRIBUTOS SON DE TIPO PUBLICO,ACA NO HAY NADA PRIVADO, NO HAY ENCAPSULAMIENTO, SU MODIFICADOR DE ACCESO SERIA PUBLICO
#DE MANERA PUBLICA ES QUE HEMOS PODIDO ACCEDER AQUI FUERA DE LA CLASE, CUANDO SALIMOS DE LA IDENTACION DE LA CLASE, YA ESTAMOS FUERA DE LA CLASE,FUERA DE LA CLASE HEMOS TRABAJADO CREANDO CON SUS INSTANCIAS LA
#CLASE Y DE ESTA MANERA ACCEDEMOS A LOS ATRIBUTOS DESDE LA INSTANCIA, PARA ACCEDER A ESOS ATRIBUTOS, ESTO ES PORQUE NUESTROS ATRIBUTOS SON COMPLETAMENTE PUBLICOS, NO HAY RESTRICCIONES DE ACCESO, ENTONCES A AUN FUERA
#DE LA CLASE SE PUEDEN ACCEDER A LOS ATRIBUTOS DESDE SUS INSTANCIAS Y OBJETOS ES LO MISMO
# VAMOS A VER COMO ES PARA MODIFICAR LO QUE EN EL ENCAPSULAMIENTO NUESTROS ATRIBUTOS NO PUEDAN SER USADOS LIBREMENTE PUBLICAMENTE FUERA DE NUESTRA CLASE, SI NO QUE ESTEN LIMITADOS, UNA VEZ QUE LOS ATRIBUTOS NO SEAN
# DE ACCESO PUBLICO DEBEMOS APRENDER UNA FORMA PARA LOGRAR ACCEDER A NUESTROS ATRIBUTOS
# EL ENCAPSULAMIENTO LO VAMOS HACER POR EJEMPLO CON self.apellido = apellido y va a cambiar a esto self._apellido = apellido y tambien tenemos que cambiarlo en el metodo aqui en metodo no habria problema que
#utilicemos el atributo, porque cuando lo encapsulamos no habria problema que se utilice por los mismos mienbros de la clase/en este caso metodo usar_detalle es un miembro dentro de la clase Persona/Pero ya todo lo
#que esta afuera las cosas deberian cambiar para lo que es el apellido, para que no hallan grandes cambios vamos a crear otro atributo que realmente quede encapsulado y ese atributo va a ser self.DNI

# Lo otro que se conoce pero no es tan utilizado seria el doble guion bajo(__)en el atributo esta es otra anotacion en Python para evitar que sea modificado esto si evita pero no se usa tanto ,si podemos acceder
# desde el metodo ,ahora si ponemos persona3.__nombre ya no nos aparece y nos da atributo de error en la clase persona el objeto no esta el atributo

#persona3.__nombre # Esta totalmente encapsulada/ De esta forma es la forma de encapsularlo estrictamente con el doble guion bajo
#Ahora si se podria acceder totalmente desde lo que es mostrar detalle,porque desde alli se puede hacer al trabajar con un metodo de la misma clase,cuando un metodo esta encapsulado tambien de esta manera,tampoco va
#aceptar ningun tipo de cambio como se hizo en el objeto persona donde cambiamoe el nombre,apellido y la edad, tampoco se va a poder cambiar ni modificar ninguno de los valores dentro de los atributos








