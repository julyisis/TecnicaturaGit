# vamos a crear la clase vehiculo

class Vehiculo:
    '''
    Deinir una clase padre llanada vehiculo y dos clases hijas llamadas
    autos y bicicletas las cuales heredan de la clase padre vehiculo.
    la clase padre debe tener los siguientes atributos y metodos :
    vehiculo (clase padre )
    -Atributos (color,ruedas)
    -Metodos (__init__(color , ruedas) y __str__()) son los atributos de la clase padre

    Auto(clase hija de vehiculo)
    Atributos (velocidad( km/hr))
    -Metodos(__init__(color,ruedas,velocidad) y __str__())

    Bicicleta(clase hija de Vehiculo)
    -Atributos(tipo(urbana/ mostaña/ etc.)
    -Metodo (__init__(color, ruedas,tipo) y __str__()

    Crear un Objeto de cada clase
    '''

    def __init__(self, color, ruedas):  # metodo inicializador init de la clase Padre
        self.color = color
        self.ruedas = ruedas

    def __str__(self):  # cuando estamos creando el dander(str)devuelve tipo string en el caso ruedas no es tipo string es tipo entero,vamos a necesitar poner los parentesis en (self.ruedas)y anteponer str
        return 'color:' + self.color + ' , Ruedas:' + str(self.ruedas)  # y su metodo str

    '''
    seguimos con la creacion de la clase Auto, esta clase auo tiene que ser hija de la clase vehiculo para que sea hija los parentesis 
    '''
class Auto( Vehiculo):  # tenemos la clase auto heredando la clase Vehiculo, la clase Auto paso a ser hija en este momento vamos a crear el metodo dander init y str
        def __init__(self, color, ruedas, velocidad):
            super().__init__(color, ruedas)
            self.velocidad = velocidad

        def __str__(self):
            return super().__str__() + ', Velocidad(km/hr): ' + str(self.velocidad)


class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+', Tipo: '+self.tipo

    # VAMOS A CREAR EL PRIMER OBJETO DE LA CLASE PADRE VEHICULO

vehiculo = Vehiculo('Blanco', 4)
print(vehiculo)

# SEGUNDO OBJETO,PERO AHORA DE LA CLASE AUTO
auto = Auto('Amarillo',4, 120)
print(auto)

#TERCER OBJETO , EL ULTIMO DE LA CLASE BICICLETA
bici = Bicicleta('azul', 2,'Urbana ')
print(bici)


