# esta plantilla creada es para testear nuestro codigo con las plantillas ya creadas

from Cuadrado import Cuadrado
cuadrado1 = Cuadrado(5, 'Azul') # Creamos un Objeto
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