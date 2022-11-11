# si quisieramos poner que la clase Persona esta heredando de la clase object se abren los parentesis y se pone object
# de esa manera estaria heredando la clase Persona de la clase object, pro no hace falta poner dentro del parentesis
#esto se hace automaticamente

class Persona():# luego ponemos el metodo inicializador para nuestros atributos el metodo dander init/ Esta clase hereda de la clase object
    def __init__(self, nombre, edad): #aqui necesitamos pasar los parametros
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad
    def __str__(self): # Override = sobreescribir los atributos todo lo que recibe al ser miembro de la misma clase es que puede acceder a los metodos encapsulados,no los muestra con el valor real
        return  f'Persona:  [Nombre:{self._nombre}, Edad: {self._edad} ]'# este metodo nos va a mostrar de tipo cadena tipo string, este metodo tiene un return y usaremos la interpolacion pero desde afuera
#en la linea 25 nos muestra el overrrides method in object, la linea 25 y 26 sobrescribir quiere decir que un metodo definido en una clase Padre lo volvemos a definir en una clase hija ,esto es escribir
#o representar lo echo en la clase hija es la manera de describir el comportamiento y de definir n metodo de la clase padre ahora en la clase hija ,tambien es el metodo init el que se sobresribe en la clase hija
#lo hemos hechoe en la linea 34 para poder acceder al atributo de lo que es empleado ahora aqui de lo que es cliente hemos accedido a los atributos de lo que es la clase persona, pero no lo que es a la clase emplea
#do clase hija


class Empleado(Persona):    #aqui vamos hacer la herencia de la clase Persona, de esta forma decimos que la clase empleado es hija de la clase Persona
    def __init__(self,nombre,edad, sueldo): #El parametro que necesita es sueldo
        super().__init__(nombre , edad) # es el contructor de la clase Padre de todos object
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    #Aqui vamos a poner el metodo dander str

    def __str__(self):
        return f'Empleado: [ sueldo: {self._sueldo} ]{super().__str__()}'


# TAREA HACER CON LOS METODOS GETTER Y SETTER LOS ENCAPSULAMIENTOS
 #TAREA : ENCAPSULAR LOS ATRIBUTOS Y AGREGAR LOS METODOS GETTERS AND SETTERS
 #CREAR OTRO OBJETO PASAR LOS DATOS PARA NOMBRE EDAD Y SUELDO
#saliendo de las clases vamos a ver si podemos crear un objeto
# MOSTRAR ESTOS DATOS ,LUEGO MODIFICAR Y MOSTRAR NUEVAMENTE

empleado1 = Empleado('Ariel', 40, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

empleado2 = Empleado('Liliana', 38, 70000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)
empleado2.nombre = 'Natalia'
empleado2.edad = 35
empleado2.sueldo = 75000
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)



