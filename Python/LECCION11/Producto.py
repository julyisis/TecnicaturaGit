class Producto:
    contador_productos = 0   #comenzamos con una variable de clase y la inicializamos en 0

    #ponemos el metodo inicializador dander init
    def __init__(self,nombre , precio): #como parametros le agregamos nombre y precio y vamos a llamar atraves de la clase Producto al contador productos para hacer el incremento
        Producto.contador_productos += 1 # aumento para la variable de clase
        self._id_producto = Producto.contador_productos # Asignacion desde la variable de clase
        self._nombre = nombre
        self._precio = precio
    # metodos setter y getter
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio


    @precio.setter
    def precio(self,precio):
        self._precio = precio

     #sobre escribimos el metodo str
    def __str__(self):
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio{self._precio}'
if __name__ == '__main__':  # solo sera visible se la prueba se ejecuta desde aqui
    producto1 = Producto('Camiseta', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon',  150.00)
    print(producto2)

