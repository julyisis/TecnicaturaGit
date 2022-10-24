# Programacion orientada a objetos en este caso estamos hablando del encapsulamiento en Python  continuamos con los
# Metodos gett y sett, /El objetivo del encapsulamiento es que no se pueda acceder directamente a los atributos de la clase
# sabemos que es necesario que nosotros podamos acceder a ellos de alguna manera ,y para esto debemos saber sobre los métodos que se utilizan, que es el (Set que significa "Colocar
# Establecer,Modificar") y el (Get significa "obtener o recuperar") Los metodos getters nos permiten obntener los atributos de una clase ,los métodos Seters nos permiten modificar los atributos
# de una clase /Para cada uno de los atributos vamos a necesitar crear un metodo get y set ,pero lo vamos hacer creando aqui

# tenemos la clase vamos a crear el metodo init
class Persona2:
    def __init__(self, nombre, apellido, edad):  # necesitamos dentro de los parentesis poner los paramentros
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # de la linea 9 a la 12 tenemos definido el método init para inicializar los atributos /aqui no hay nada encapsulado vamos a poner tambien el metodo mostrar detalle
    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')  # Aqui tengo el metodo mostrar detalle ./para cada uno de los atributos necesitamos crear un metodo get y set

    # para crear el metodo get o set no vamos a  salir de la clase Perosna2 / Los atributos encontrados con guion bajo o doble guion bajo son encapsulados y por esto nunca deberiamos acceder si no a travez del get
    # o el set tambien/Entonces vamos a encapsular la linea 10,11 y 12 despues del punto(.) agregamos el guion bajo(_)ejemplo self.nombre = nombre queda self._nombre = nombre /esto va a estar encapsulado /Pero
    # tambien es super importante que adreguemos el guion bajo en la interpolacion el la fila 15 despues del punto(.)/Bien ahora esta todo encapsulado
    # El Primer Método que vamos a Crear es el Método Getters que se escribe de la siguiente manera

    @property  # Esto es un Decorador
    def nombre(self):  # creamos el getter lo vamos hacer para el nombre abrimos parentesis inmediatamente se agrega el self va a necesitar retornar el método getter
        print('Estamos usando el metodo get')
        return self._nombre  # terminando con esto asi se crea el metodo gett linea 20 a la 21/Pero vamos a necesitar para poder acceder al metodo como si fuera un atributo y de manera indirecta vamos a necesitar lo

    # que llamamos un decorador eso se pone arriba linea 21 /Asi se rea un método Getter desde la linea 22 hasta la 24
    # Ahora vamos a pasar a crear un método Setter
    @nombre.setter  # tambien para lo que es nombre punto(.) y buscamos a setter
    def nombre(self,nombre):  # en los parentesis siempre aparece self de manera automatica ,ya aparece por defecto /Bien ahora dentro de los parentesis vamos a pasar el parametro nombre dentro ponemos el self
        print('Estamos usando el método Set')
        self._nombre = nombre  # En la linea 28 tenemos creado el método Setter
    # Ahora la unica manera de acceder a los atributos es a travez de los métodos getter y setter /Salimos de la linea 29  a 31


# persona1 = Persona2('Ariel','Betancud','41') # Aqui hemos creado un objeto de persona1 de la clase Persona2
# print(persona1._nombre) # Ya no se puede acceder de esta forma esto ya es un error esto quiere decir que no tenemos idea de la sintaxis de Python, esto no se puede hacer /podriamos acceder si totalmente al nombre
# linea 35 lo podemos hacer mostrar el nombre pero esto esta mal no es la forma correcta
# que si se puede hacer /La forma correcta es:
# print(persona1.nombre) #aqui en los parentesis estariamos llamando al metodo que no necesita parametros, no necesita que le enviemos argumentos /Estariamos llamando al metodo getter de esta manera
# llamanos al metodo getter la linea 38 seria la sintaxis Pero ya de esta manera ya no utilizamos los parentesis no hace falta, nos permite acceder al metodo el property o decorador como si fuera un atributo
# y de manera indirecta aun sin los parentesis estariamos llamando ,sabemos que el atributo no se llama nombre solo, tiene su guion bajo(_) esta encapsulado /Entonces el compilador cuando ve esto directamente sabe
# que estamos hablando del metodo gett le va asignar directamente el metodo para mostrar
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self,edad):
        self._edad = edad
# def apellido(self):
#     return self._apellido

# @apellido.setter
# def apellido(self,apellido):
#     self._apellido = apellido


    @property  #Properti tiene que ir en cualquier metodo
    def edad(self):
         return self._edad
    @edad.setter
    def edad(self,edad):
          self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}') # Aqui ponemos el atributo directamnte


# que diferencia hay entre el set y el get lo que hace el get es obtener lo que esta en el atributo en ese espacio de memoria y mostrarlo ,pero el metodo set lo que hace es modificarlo atravez del metodo set podemos
# modificar
if __name__ == '__main__':  # que va a suceder ahora, todo nuestro codigo simplemente lo vamos a poner dentro de la identacion de nuestra estructura if

# Vamos a llamar Persona1
    persona1 = Persona2('Ariel', 'Betancud', 41)
    print(persona1.nombre)  # llamamos al metodo getter
    persona1.nombre = 'Juan Pedro'  # llamamos el metodo setter
    print(persona1.nombre)  # otra vez con el metodo getter
    print(persona1.mostrar_detalles())  # llamams el metodo mostrar detalles
# persona1.edad = 40 #esta sintaxis no se puede hacer quedamos como ignorntes

# Atributos read -only solo lectura porque no tiene su metodo set
# se transformaria en un metodo read-only
# print(persona1.edad) # seria la edad porque no tiene el metodo set
# puede haber un atributo que no tenga suu metodo set , que tipo seria se le llamaria en lo que es programcion es lo que se llama un atributo read -only

# en el encapsulamiento el metodo mostrar detalle dentro de a misma clase puede acceder a los atributos sin ningun problema el encapsulamiento tiene por
# objetivo el que NO se pueda acceder a los atributos desde fuera de la clase
# en cada método get y set lo que hace es repetir el identificador se llaman igual,/Pero cual es la diferencia de un metodo get y un metodo set /1:La
# primer diferencia es que para el Getter es que estamos utilizando el @property ,/Despues el identificador es el mismo pero la diferencia es que el
# Setter ademas del self va a necesitar un parametro mas porque este viene a modificar el valor para el atributo / Aparte del @property del Getter
# el setter atravez del @ . setter asi lo convertimos en un setter /Lo que queria aclarar es que tienen el mismo identificador y en el metodo setter
# necesita que le pasemos un parametro


# TAREA CREAR TRES OBJETOS MAS, UTILIZANDO LOS MÉTODOS GETTER AND SETTER
# PARA MODIFICAR ,Y MOSTRAR LOS CAMBIOS

persona2 = Persona2('Flor', 'Romero', 23)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)
persona2.nombre = 'Florencia'
persona2.apellido = 'Romery'
persona2.edad = 22
print(persona2.mostrar_detalles())

persona3 = Persona2('Caro', 'felisa', 21)
print(persona3.nombre)
print(persona3.apellido)
print(persona3.edad)
persona3.nombre = 'Carolina'
persona3.apellido = 'Felix'
persona3.edad = 31
print(persona3.mostrar_detalles())

persona4 = Persona2('Naty', 'Lucer', 35)
print(persona4.nombre)
print(persona4.apellido)
print(persona4.edad)
persona4.nombre = 'Natalia'
persona4.apellido = 'Lucero'
persona4.edad = 33
print(persona4.mostrar_detalles())

# Aqui en Python existe una comprobacion de modulo princiapal en lo que es la ejecucion esta es una herramienta que
#tenemos si ponemos un print

print(__name__) #esta es una comprobacion que nos va a decir donde se esta ejecutando el codigo/ venimos a PruebaPersona2
# aqui con esto en la clase pruebaPersona2 se ejecuta Persona2, nos esta diciendo que esta ahi llega la clase Persona2
# y luego lo que continua es codigo de PruebaPersona2

