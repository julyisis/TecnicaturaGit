# esta plantilla creada es para testear nuestro codigo con las plantillas ya creadas

from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print('Creacion de objeto clase Cuadrado'.center(50, '_'))
cuadrado1 = Cuadrado(8, 'Azul') # Creamos un Objeto
cuadrado1.alto = 7
cuadrado1.ancho = 7
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Calculo del area del cuadrado: {cuadrado1.calcular_area()}')

"""
METODO RESOLUCTION OCTHOR (MRO) CUANDO TRABAJAMOS CON LA HERENCIA MULTIPLE ES IMPORTANTE SABER EL ORDEN WN QUE SE VAN LLAMANDO LAS 
CLASES PADRES PARA ESTO HAY UN METODO CONOCIDO COMO (MRO)ESTE NOS PERMITE CONOCER LA JERARQUIA DE LO QUE SON LAS CLASES FRENTE A LA 
CLASE ACTUAL EN LA QUE ESTAMOS LLAMANDO A UN METODO EJ SI QUEREMOS SABER EL ORDEN EN QUE SE LLAMAN O DEVUELVEN LOS METODOS 
"""
# MRO = METHOD RESOLUCTION ORDER
print(Cuadrado.mro()) # nos da la informacion del orden conque los metodos segun la jerarquia de clase que ya hemos definido


print(cuadrado1) # al poner esto asi estamos llamando al metodo dander mtr
print('Creacion de objeto clase Rectangulo'.center(50, '_'))
rectangulo1 = Rectangulo(3, 9, 'verde')
rectangulo1.ancho = 8
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)


#figura1 = FiguraGeometrica() NO se puede instanciar, es abstracta
print(Cuadrado.mro()) # nos va amostrar la clase cuadrado muestra la gerarquia de clases

"""
Cuando queremos que un atributo se pueda modificar despues de haber inicializado un objeto, hacemos que sean de solo lectura,ej: linea 9 y 10 no queremos 
aceptar que se hagan estas modificaciones, simplementes queremos instanciar o inicializar un objeto aqui con los valores linea 8 
ej: si queremos modificar en el cuadrado 9 y 10 tenemos que modificar los dos lados lo que es el alto y el ancho , pero si de 
repente uno de ellos no se modifica se modifica uno solo deja de ser un cuadrado se altera todo ej el ancho tiene 7 y el alto 8
deja de ser un cuadrado pasa a ser un rectangulo y ya no esta repetando las reglas del de lo que es un cuadrado sus lados tienen que ser 
todos iguales , CUANDO NO QUEREMOS QUE SE ALTERE en lo que es la clase FiguraGeometrica si modificamos se va ver afectado todas las 
clases hijas, lo que se hace en la clase padre FiguraGeometrica es quitar el setter de lo que es el alto y el ancho y quedan como atributos 
de solo lectura es asi que no se van a poder seguir modificando 

"""