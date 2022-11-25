from Producto import Producto


class Orden:  # dentro de la plantilla orden estamos trabajando dentro de la variable de clase comenzamos con contador
    contandor_ordenes = 0  # y le asignamos el 0

    def __init__(self,
                 productos):  # inicializamos con dander init y va a necesitar un parametro mas que va hacer productos
        Orden.contandor_ordenes += 1  # comenzamos con la variable de clase Orden . contador_... y con el operador simplificado le pedimos que sume 1
        self.id_orden = Orden.contandor_ordenes
        self._productos = list(
            productos)  # aqui vamos a asignar la lista de productos como hacemos,vamos a tener que hacer una conversion con la palabra reservada de list y convertimos los productos a una lista

    def agregar_producto(self,
                         producto):  # aqui agregamos un metodo,este metodo es para agregar un producto de manera independiente y vamos a necesitar otro parametro que va hacer el producto
        self._productos.append(producto)  # esto es para agregar el nuevo producto

    # ahora vamos a definir otro metodo, este metodo va a ser para calcular el total, sumando todos los precios  que contenga la orden el identificador va ser calcular el total

    def calcular_total(
            self):  # no vamos a pedir ningun parametro mas y vamos a usar una variable temporal para almacenar el total temporal
        total = 0  # variable temporal para almacenar el total temporal/ aqui la inicializamos dandole el valor 0 y luego utilizmos un for para ir recorriendo la lista de productos y asi ir asignando cada uno de los precios
        # y va irlos sumando es por eso que es temporal ,porque va ir guardando los precios temporalmene pero al mismo tiempo los va a ir sumando 1 en 1 hasta que este metodo devuelva el total final de la lista de productos
        # que se ha armado ,vamos con un ciclo for
        for producto in self._productos:  # ese es el recorrido que vamos hacer recorremos los elementos de la lista,vamos a usar la variable temporal a esta le asignamos con el operador simplificado de suma, la suma se la lista
            total += producto.precio
        return total  # tenemos un retorno

    # POR ULTIMO AGREGAMOS EL METODO DANDER STR

    def __str__(self):
        # aqui vamos a tener que convertir todos los productos a una cadena tipo string, para convertir la lista vamos a tener que recorrer la lista,vamos a crear una variable,tbn temporal para lo que es la lista de
        # productos
        productos_str = ''
        for producto in self._productos:  # a traves del ciclo for vamos a ir recorriendo la lista por cada producto vamos a llamar al str de la clase producto
            productos_str += producto.__str__() + '|'  # aqui por cada producto lo vamos a ir concatenando ,sumando y llamando al str de la clase producto las comillas son para separar cada uno de los productos
            # aqui por cada producto vamos a ir almacenando de manera temporal los datos recibidos del metodo str de la clase producto
        return f'Orden: {self.id_orden}, \nProducto: {productos_str}'


if __name__ == '__main__':  # solo sera visible si la prueba se ejecuta desde aqui/ sin salirnos de la estructura if siguuiendo esta condicion
    producto1 = Producto('Camiseta', 100.00)
    producto2 = Producto('Pantalon', 150.00)
    productos1 = [producto1,producto2] # lista de productos
    orden1 = Orden(productos1)#primer objeto orden pasando la lista de productos
    print(orden1)
    orden2 = Orden(productos1)
    print(orden2)

#TAREA MODIFICAR: LA ORDEN 2 INGRESANDO NUEVOS PRODUCTOS CON SUS NOMBRES Y PRECIOS
# CREAR UNA NUEVA LISTA DE PRODUCTOS Y AGREGARLA A LA ORDEN2
    producto3 = Producto('Relojes', 250.00)
    producto3 = [producto3]
    orden2 = Orden(producto3)
    print(orden2)

