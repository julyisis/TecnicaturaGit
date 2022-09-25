# Ejercicio 3: Insertar elementos y ordenarlos
# pedir numeros y meterlos en una lista,cuando el usuario
# introduzca un numero 0, nuestro programa dejaria de isertar
# por ultimo, mostrar los numeros ordenados de menor a mayor
lista = []
salir = False
while not salir: # mientras salir sea, si es falso, cuando le ponemos el operador not le estamos diciendo verdadero, mientras salir sea verdadero va a seguir funcionando se va a seguir ejecutando
    numero = int(input('Digite un numero: ')) # Pedimos los datos al usuario
    if numero == 0: # usamos un condicional
        salir = True
    else:
        lista.append(numero)
lista.sort() # La lista esta ordenada con esta funcion
print(f'\nLista ordenada : \n{lista}')


