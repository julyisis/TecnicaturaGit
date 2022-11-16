from FiguraGeometrica import FiguraGeometrica      #clase Hija
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
       # super.__init__(lado)

#el constuructor super para llamar a la clase Padre aqui en la clase hija poniamos el super.se abre el init y pasabamos en este caso el lado
#el problema con este metodo a que padre va a acudir a la clase FiguraGeometrica, a Color , a cual acudiria si usaramos la linea 8
#por eso en la herencia multiple no vamos a usar el 'super' podriamos generar una cierta confuncion aqui,tanto para el programador
#como para el programador como para el compilador

         FiguraGeometrica.__init__(self, lado, lado) # Aqui estamos inicializando la clase FiguraGeometrica
         Color.__init__(self, color)# en este estamos inicializando la clase color , el atributo color

    def calcular_area(self):
        return self.alto * self.ancho




    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'


