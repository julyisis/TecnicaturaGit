# Vamos a crear la clase aridmetica

class Aridmetica:
    """
    El nombre de esre tipo de comentario es: DocSring
    esto es documentacion de la clase en Python
    Vamos a hacer en esta clase algunas operaciones de:suma,resta,multiplicacion y mas
    """
    #vamos a crear el metodo init, es el metodo inicializador de los atributos / escribimos como si fuera una funcion def y los giones bajo esta predefinido el init(self):
    #que vamos a necesitar dentro de los parentesis (self,operandoA,operandoB):vamos a necesitar dos operadores

    def __init__(self,operandoA, operandoB):#dentro vamos a empezar apuntando a estas variables a crear los atributos para crearlos decimos self.operandoA
        self.operandoA = operandoA
        self.operandoB = operandoB # una vez echo esto salimoas del metodo inicializador
 # AHORA VAMOS A CONSTRUIR EL PRIMER METODO PARA SUMAR ,Resta,multiplicacion,division
    def sumar(self): # este metodo va a retornar atravez del self.operadorA + self.operadorB una suma/Ahora necesitamos un metodo para restar le ponemos de nombre resta
        return self.operandoA + self.operandoB

    def resta(self): # Aqui creamos el metodo de restar
        return self.operandoA - self.operandoB

    def multiplicacion(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

   # salimos de aqui y vamos a crear un objeto, creamos una instancia de la clase aridmetica
aridmetica1 = Aridmetica(7, 9)  #que necesitamos poner aqui en el constructor que se crea por defecto le pasamos dos numeros van a ser los necesarios para el operandoA y el B /Le pasamos los argumentos para los operad.
print(f'La Suma de los numeros es: aridmetica1.sumar())
print(f'La Resta de los numeros es: {aridmetica1.resta()}')
print(f'La Multiplicacion de los numeros es: {aridmetica1.multiplicacion()}')
print(f'La Division de los numeros es: {aridmetica1.dividir():.2f}') # E las divisiones nos va a dar un nmero flotante con los dos puntos(:)y un punto(.)/:.2f  le decimos que nos muestre despues del punto 2 numeros



