class Rectangulo:
    """
    Crear una clase llamada Rectangulo, Debe tener dos atributos: altura y base
    el nombre del metodo sera calcular_area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por el usuario y los objetos deben ser tres
    """
    def __init__(self,altura,base): # Vamos a llamar al metodo que inicaliza los atributos con el init__self debe tener dos atributos que son altura y base
        self.altura = altura
        self.base = base
    def calcular_area(self):
        return self.base * self.altura

base = int(input('Digite el numero para la base del rectanngulo: '))
altura = int(input('Digite el numero para la altura del rectangulo: '))
rectangulo1 = Rectangulo(base ,altura) # aqui vamos a instanciar un objeto de la clase  Rectangulo
print(f'El area del Rectangulo es: {rectangulo1.calcular_area()}')



