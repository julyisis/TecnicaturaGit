from abc import ABC,abstractmethod
#ABC SIGNIFICA: Abstract Base Class,convierte una clase en abstracta
#falta agregar algo a la importacion en la linea 6 agregamos parentesis


class FiguraGeometrica(ABC):  # clase Padre // AHORA LA CLASE FIGURAGEOMETRICA VA A SER HIJA DE LA CLASE ABC
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho):  # sintaxis simplificada para preguntar un rango
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo para el ancho: {ancho}')
        if self._validar_valores(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo para el alto: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho): # Metodo encapsulado
           self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto):
           self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')

    @abstractmethod # para que este metodo se lo considere abstracto debe tener el decorador
    def calcular_area(self):
        pass    # NO TIENE QUE IMPLEMENTARSE esto es de manera abstracta el metodo calcular_area, hace que sea obligatorio para las clases hijas cuadrado, rectangulo que tengan el metodo calcular_area

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]'

       # METODO ENCAPSULADO
    def _validar_valores(self, valor): # este metodo no se debe utilizar fuera de esta clase, si no de manera interna en  la clase Padre dentro le vamos a poner un retorno antes del retorno neces un parametro
        return True if 0 < valor < 10 else False    # sintaxis simplificada de if else va a trabajar de manera encapsulada

