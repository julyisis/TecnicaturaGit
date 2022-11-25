from Orden import Orden
from Producto import Producto

"""  DISEÑO DE CLASES
Vamos a crear mas productos a estos los vamos a agregar de manera independiente despues de haber creado una orden 
vamos a crear lo que es nuevos productos una nueva lista una nueva orden ,vamos a utilizar los metodos que son para calcular el 
total de las ordenes de los productos el total de los productos y tbn vamos a utilizar el metodo para agregar productos 
AQUI HEMOS AGREGADO EL CONCEPTO DE DISEÑO DE CLASES, YA ESTAMOS CREANDO MAS DE UNA CLASE Y TAMBIEN APLICAMOS EL CONCEPTO 
RELACION DE AGREGACION, AGREGANDO HACIA OTRA CLASE UN NUEVO PRODUCTO  
"""

producto1 = Producto('Camiseta', 100.00) # Aqui hemos creado varios productos,pero no todos estan dentro de la lista
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('medias', 45.00)
producto4 = Producto('campera', 250.00)
producto5 = Producto('sweter', 95.00)
producto6 = Producto('Blusa', 75.00)

productos1 = [producto1, producto2]  # lista de productos
orden1 = Orden(productos1)  # primer objeto orden pasando la lista de productos
#han quedado afuera el producto 4,5,6 ahora hay que agregarlos ponemos orden1
orden1.agregar_producto(producto5)
orden1.agregar_producto(producto3)
print(orden1) # Aqui despues del print 1 vamos a ver la lista de los productos 1 ponemos otro print para usar un metodo vamos hacer la interpolacion
print(f'Total de la orden1: {orden1.calcular_total()}')
productos2 = [producto3,producto4] #Aqui vamos a crear una lista de productos 2
orden2 = Orden(productos2)
orden2.agregar_producto(producto6)
orden2.agregar_producto(producto2)
print(orden2)
print(f'Total de la orden2: {orden2.calcular_total()}')