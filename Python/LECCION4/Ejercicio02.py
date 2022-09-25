# EJERCICIO 2: MODIFICAR LOS ELEMENTOS DE UNA LISTA
# LLENAR UNA LISTA CON LOS NUMEROS DEL 1 AL 10,LUEGO  MODIFICAR LOS ELEMENTOS
# DE LA LISTA MULTIPLICANDOLOS POR UN VALOR INGRESADO POR EL USUARIO

lista = list(range(1,11)) # usamos la funcion range
print('lista Original')
for i in lista:
    print(i, end='-')
valor = int(input('\nDigite un valor a multiplicar:')) # AQUI LE PEDIMOS AL USUARIO QUE INGRESE UN VALOR PARA MULTIPLICAR
# MULTIPLICAMOS TODOA LOS ELEMENTOS DE LA LISTA    # vamos a usar una funcion para recorrer los indices, justamente porque el iterador no trabaja con los indices,es una sintaxis diferente,solo recorre los elementos,por eso usamos una funcion
 #que hace que indice  trabaje exclusivamente con los indices y se pueden modificar y multiplicar, si usaramos directamente el iterador,el iterador lo que hace es recorrerlos a los elementos,pero no tiene la habilidad de manipular
#de manipular esos elementos, solo los recorre, vamos usar esta funcion que es enumerate
for indice, i in enumerate(lista):# funcion para modificar los indices de la lista
    lista[indice] *= valor # el iterador solo recorre los indices, en esta linea se multiplica

print(f'lista final con los elementos multiplicados por {valor}')
for i in lista:
    print(i, end='-')



