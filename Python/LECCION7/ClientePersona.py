#Sobrescrituras del metodo danther str
# vamos a importar ,seguiremos con la clase Persona y su clase hija Empleado usamos la palabra reservada from
# y ponemos la palabra reservada import, al poner el asterisco importamos las dos clases la clase Persona y la clase hija
# empleado o las clases ,wu tengamos para importar todo lo del modulo de la clase Persona se va a importar ahora a la
#clase clientePersona

from Persona import * # ahora vamos a crear un objeto lo vamos a llamar persona1
persona1 = Persona('Osvaldo',40) # la clase pesona cuantos atributos tiene ,tiene 2 atributos/asi creamos un objeto de la clase persona
print(persona1)

empleado3 = Empleado ('Pablo', 23,57000)
print(empleado3)