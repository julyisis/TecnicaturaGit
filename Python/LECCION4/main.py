# LAS LISTAS SON UN CONJUNTO DE ELEMENTOS, EJ UNA LISTA DE NOMBRES,NUMEROS
# LISTA = Ariel, Lilina,Natalia,Osvaldo (esto es una lista de string ) a cada uno de los
# elementos de una lista se le asigna un indice, ej el indice del primer elemento es el 0
# el cero correspode a Ariel
#COLECCIONES EN PYTHON

#nombres = ['Naty','Osvaldo','Lily','Ariel'] # aqui tenemos una lista,dentro de una lista pueden haber distintos tipos de datos
#print(nombres)# para definir los elementos de una lista se utilizan los corchetes
# PARA RECURRIR A LOS ELEMENTOS DE FORMA INDIVIDUAL
#print(nombres[0])
#print(nombres[1])
#print(nombres[3])
#print(nombres[-1])
#print(nombres[-2])
#COLECCIONES EN PYTHON,LAS LISTAS SON LAS QUE SE CONOCEN EN OTROS LENGUAJES COMO ARREGLOS O VECTORES


"""nombres = ['Nati','Osvaldo','Lily','Ariel']
print(nombres)

#RECUPERAR UN RANGO DE LA LISTA
print(nombres[0:2])#va a recorrer la posicion 0 y la posicion 1(Nati,Osvaldo)solo muestra el indice 0,1 pero no el 2

# IR DEL INICIO DE LA LISTA AL INDICE (SIN INCLUIRLO)
print(nombres[ :3])# INDICE A MOSTRAR 0,1,2

#DESDE EL INDICE INDICADO HASTA EL FINAL
print(nombres[1: ])

#MODIFICAR UN VALOR
nombres[2] ='LILIANA'
nombres[0] = 'NATALIA'
print(nombres)

# ITERAR NUESTRA LISTA
for nombre in nombres:  #nombre es singular ,la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

#PREGUNTAMOS CUANTOS ELEMENTOS TIENE UNA LISTA(la funcion len)len nos regresa la cantidad de elementos que tiene nuestra lista
print(len(nombres))#len es una funcion ,nos regresa la cantidad que tiene una lista,pero debemos pasarle un parametro(la lista tiene 4 elementos)

# AGREGAMOS UN ELEMENTO con la funcion append
nombres.append('Marcelo')# EN UNA LISTA PUEDE HABER DISTINTOS TIPOS DE DATOS,DENTRO DE UNA LISTA PUEDE HABER OTRA LISTA
nombres.append([1,2,3])
nombres.append(True)#PUEDE HABER UN BOOLEANO
nombres.append(10.45)#PUEDE HABER UN FLOTANTE
nombres.append([4,5])#ACA TENEMOS OTRA LISTA TENEMOS PARENTESIS Y CORCHETES
nombres.append(7)
print(nombres)

## INSERTAR UN ELEMENTO EN UN INDICE ESPECIFICO, NECESITAMOS COLOCAR UN NUMERO ENTERO,con la funcion INSERT(tenemos que poner primero el indice y luego el elemento a agregar)
nombres.insert(1,'Alberto')#ESTO ES MUY IMPORTANTE (SI NO PONEMOS EL INDICE Y EL ELEMENTO A AGREGAR DARA ERROR)(NECESITA LOS DOS ELEMENTOS)
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# PARA ELIMINAR ELEMENTOS(FUNCION REMOVE ,BORRA ELEMENTO DE LA LISTA)
nombres.remove('Alberto')
print(nombres)

# ELIMINAR EL ULTIMO ELEMENTO
nombres.pop()#ESTA FUNCION BORRA EL ULTIMO ELEMENTO QUE TENGAMOS EN NUESTRA LISTA
print(nombres)

# ELIMINAR UN INDICE ESPECIFICO
del nombres[2]# del significa (delete eliminar)
print(nombres)

#ELIMINAR BORRAR O LIMPIAR TODOS LOS ELEMENTOS DE LA LISTA
nombres.clear()
print(nombres)

# ELIMINAR LA LISTA
del nombres # AQUI NOS MOSTRARA UN ERROR PORQUE LA LISTA FUE ELIMINADA
print(nombres)

# verificamos como trabajar dia a dia en git


# SINTAXIS DE RANGE(INICIO <OPCIONAL>, FIN <REQUERIDO>,INCREMENTO <OPCIONAL>)

#EJERCICIO: 1 ITERAR UN RANGO DE 0 A 10 E IMPRIMIR NUMEROS DIVISIBLES ENTRE 3
# EJEMPLO DE EJECUCION: 0,3,6,9
print('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)

#EJERCICIO 2: CREAEAR UN RANGO DE NUMEROS DE  2 A 6 E IMPRIMIRLOS
# EJEMPLPLO DE EJECUCCCION:  2,3,4,5,6
print('Rango de valores de inicio = 2 y fin = 6')
rango = range(2, 7)
for i in rango:
    print(i)

# EJERCICIO 3: CREAR UN RANGO DE 3 A 10 PERO CON INCREMENTO DE 2 EN 2, EN LUGAR DE 1 EN 1
#EJEMBPLO DE EJECUCION: 3,5,7,9
print('Rango con vaslores de inicio = 3, fin = 10, incremento = 2')
for i in range(3, 11, 2):
    print(i)

#COLECCIONES  LAS TUPLAS
#EN LAS LISTAS SE RESPETA EL ORDEN DE LOS ELEMENTOS Y COMO SE VAN CAGANDO,LAS LISTAS SON MODIFICABLES O MUTABLES
# LAS TUPLAS SIGUE EL ORDEN DE LOS ELEMENTOS PERO ESTOS NO SE PUEDEN ELIMINAR,A ESTO SE LO LLAMA INMUTABLE O MODIFICABLE
# ESTA ES LA GRAN DIFERENCIA ENTRE LISTA Y TUPLAS

# DEFINIMOS UNA TUPLA solo se usan parantesis
cocina = ('cuchara','cuchillo','tenedor')# las funciones que usamos en una tupla son similiares a las que usamos en una lista
print(len(cocina))
# ACCEDER A UN ELEMENTO PARA ESTO UTILIZAMOS CORCHETES NO PARENTESIS
print(cocina[0])
# MOSTRAR LA MANERA INVERSA
print(cocina[-1])
# ACCEDER A UN RANGO
print(cocina[0:2])# UNA TUPLA SIEMPRE SE REPRECENTA ENTRE PARENTESIS COMILLAS Y NUNCA TIENE QUE FALTAR LA COMA
# a modo de ejemplo
verduras = ('papa') # esto es un TIPO STRIN CADENA, PORQUE LE FALTA LA COMA,AUNQUE SEA UN ELEMENTO NADA MAS
# RECORRMOS LOS ELEMENTOS DE UNA TUPLA
for cocinar in cocina:# Print esta usando \n para saltos de lineas, esto no tiene que ver con tuplas es solo la funcion print
    print(cocinar, end= ' ')# Usamos end= para eliminar los saltos de lineas
# la unica manera de cambier una tupla es haver una conversion, pero no es una buena ptactuica de programacion
# solo si es estrictamente necesario

cocinaLista = list(cocina)
cocinaLista[0]= 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)# en tuplas no se pueden utilizar las funciones append,insert y remove
# del cocina , esto es para eliminar una tupla

# LA LISTA MANTIENE  UN ORDEN QUE SE PUEDE MODIFICAR ES MUTABLE/ LA TUPLA MANTIENE UN ORDEN PERO NO SE PUEDE MODIFICAR ES INMUTABLE

# VEREMOS LA COLECCION DE (TIPO SET NO TIENE UN ORDEN ,NO PERMITE ALMACENAR ELEMENTOS DUPLICADOS O REPETIDOS, NO SE PUEDE MODIFICAR
# SI SE PUEDE AGREGAR O ELIMINAR )NO MANTIENE NINGUN INDICE EL ORDEN ES ALEATORIO
#ENTONCES UN ELEMENTO DE TIPO SET ES UNA COLECCION SIN ORDEN Y SIN INDICES

# TIPO SET UTILIZAMOS LAS LLAVES
planetas = {'Marte','Júpiter','Venus'}
print(len(planetas)) #funcion len,nos muestra el largo o la cantidad de elementos que estan dentro del set

# revisamos si un elemento existe dentro de nuestro conjunto set
print('Júpiter'in planetas)

# AGREGAR UN ELEMENTO
planetas.add('Tierra') # add es la funcion para agregar a un conjunto
print(planetas)# la funcion set nos sirve para evitar elementos duplicados en una lista de datos

# ELIMINAR ELEMENTOS, PUEDE ARROJAR UN ERROR SI EL ELEMENTO NO EXISTE
planetas.remove('Júpiter')#Esta funcion ante un mal ingreso u inexistencia del elemento da error
print(planetas)

planetas.discard('tierra')#Esta funcion no nos presenta ningin error
print(planetas)
# LIMPIAR SET

planetas.clear()
print(planetas)

# ELIMINAR SET o CONJUNTO
#del planetas
#print(planetas)# al eliminar nos muestra error

# DICCIONARIOS/UTILIZAMOS LLAVES
# 'Maradona':10 Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key, value)
diccionario = {
    'IDE':'Integrated develoment environment',
    'POO':'Programacion Orientadas a Objetos',
    'SABD': 'Sistema de Administaccion de Base de Datos'
    }
# VERIFICAR LA CANTIDAD DE ELEMENTOS DEL DICCIONARIO
print(len(diccionario))# un diccionario se parece a un tipo set porque no tenemos indices para acceder lo hacemos desde la llave
print(diccionario)

# ACCEDER A UN DICCIONARIO CON LA LLAVE (KEY)
print(diccionario['IDE'])# Los datos deben ser precisos
#OTRA FORMA DE RECURAR UN ELEMENTO
# SIN UTILIZAR CORCHETES ES CON .GET
print(diccionario.get('POO'))
print(diccionario.get('SABD'))
# MODIFICAMOS LOS ELEMENTOS /UTILIZAMOS LLAVE NOS VA A PERMITIR ACCEDER AL VALOR
diccionario['IDE'] = 'ENTORNO DE DESARROLLO INTEGRADO' # UN DICCIONARIO PUEDE MODIFICARSE
print(diccionario)
# COMO RECORRER LOS ELEMENTOS / UNA HERRAMIENTA A USAR ES EL CICLO FOR
for termino in diccionario:
    print(termino)# CON ESTA VARIABLE VAMOS A ACCEDER A LOS ELEMENTOS DE LAS LLAVES
 # no se puede acceder de manera directa al valor, solo se pudo acceder a las llaves

# Necesitamos una funcion para recorrer un diccionario (.items())
for termino, valor in diccionario.items():
    print(termino,valor)
# OTRAS MANERAS DE ACCEDER AL DICCIONARIO
for termino in diccionario.keys():# ESTAMOS USANDO UNA FUNCION
    print(termino)# MUESTRA SOLO LAS LLAVES
for valor in diccionario.values():# USAMOS UNA FUNCION PARA ACCEDER AL VALOR
    print(valor)
# COPROBAR LA EXISTENCIA DE ALGUN ELEMENTO
print('IDE' in  diccionario)# devuelve un booleano
# COMO AGREGAR UN ELEMENTO A NUESTRO DICCIONARIO
diccionario['PK'] = 'Primary Key'
print(diccionario)
# ELIMINAR UN ELEMENTO
diccionario.pop('SABD')
print(diccionario)
# VACIAR UN DICCIONARIO
diccionario.clear()
print(diccionario)
# ELIMINAR DICCIONARIO
del diccionario # el diccionario se borro
print(diccionario)"""

"""# CONCATENAR LISTAS
lista1 = [1,2,3,1]
lista2 =[4,5,6,1]
lista3 = lista1+lista2 # CONCATENACION
print(lista3)
# OTRA FUNCION QUE SE LLAMA EXTEND ES PARA AGREGAR VARIOS ELEMENTOS DE UNA LISTA
lista3.extend([7,8,9,1])
print(lista3)
# ESTA FUNCION ES PARA SABER QUE INDICE ESTAN LOS ELEMENTOS
print(lista3.index(5))
#print(lista3.index(0)) ESTO DARIA ERROR POR NO SER EL ELEMENTO PARTE DE LA LISTA

# como saber cuantos valores repetdos hay dentro de una lista
print(lista3.count(1))# CUENTA CUANTOS VALORES IGUALES HAY DENTRO DE LA LISTA

# PARA PONER AL REVES UNA LISTA
lista3.reverse()
print(lista3)

# PARA QUE UNA LISTA SE MULTIPLIQUE REPITIENDO SUS ELEMENTOS
lista = [1,2,3] * 2
print(lista)
# METODOS DE ORDENAMIENTO / UNO DE LOS METODOS MAS EFICIENTES QUE EXISTEN, SIEMPRE VA A ORDENAR LOS ELEMENTOS DE MANERA ACCENDENTE
lista3.sort()
print(lista3) # ACCENDENTE
lista3.sort(reverse=True)
print(lista3)# DECENTENTEMENTE

# REPASO DE LO QUE SON LAS TUPLAS / VEREMOS QUE TIPOS DE DATOS PODEMOS INGREDAR A UNA TUPLA
tupla = (4,'Hola',6.78,[1,2,78],4,'Hola')# Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # ACCION BOOLEANA,SU RESPUESTA ES DE TIPO BOOLEANA
# LO QUE PODEMOS USAR DENTRO DE TUPLAS SON: INDEX,COUNT,LEN
# EN TUPLAS SE PUEDE CONVERTIR DE TUPLA A LISTA Y DE LISTA A TUPLA

# repaso de set o conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {}
conjunto2.add(7)
conjunto2 .add('Hola')
print(conjunto1)
conjunto1.add('hola')
print(conjunto1)
print((3 not in conjunto1))

# como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)

#OPERACIONES CON CONJUNTOS
conjunto3 = conjunto1 / conjunto2 # la linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2#que elementos tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2# asigna el valor que esta en el conjunto 1 y no en el conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 / conjunto2
print(conjunto2.issubset(conjunto3))#aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuprset(conjunto1))#preguntamos si los elementos del conjunto 1 estan dentro del 3
print(conjunto3.issuperset(conjunto2))# si es verdadero quiere decir que el conjunto 3 es un superconjunto
print((conjunto2.isdisjoint(conjunto3)))
#COMO SABER SI AMBOS CONJUNTO son DISCONEXOS, ESTO QUIERE DECIR QUE NO COMPARTEN ELEMENTOS EN COMUN
print(conjunto1.isdisjoint(conjunto2))# NO HAY COSAS EN COMUN ENTRE LOS DOS CONJUNTOS
#LOS CONJUNTOS NO SON NI TOTALMENTE MUTABLES Y TOTALMENTE INMUTABLES,SABEMOS QUE NO SE PUEDEN MODIFICAR,PODEMOS TRABAJAR CON UNA FUNCION QUE LOS CONJUMTOA SE VUELVAN INMUTABLES
#QUE NO SE PUEDAN MODIFICAR,AGREGAR

#convertir un diccionario totalmente en inmutable
conjunto1 = frozenset # ESO HACE QUE EL CONJUNTO SEA TOTALMENTE INMUTABLE
#NO SE PUEDE AGREGAR,MODIFICAR NI ELIMINAR ELEMENTOS DEL CONJUNTO"""

#RePaso de diccionarios
diccionarioNuevo = {'Azul':'Blue','Rojo':'Red','Verde':'Green','Amarillo':'Yellow'}
print(diccionarioNuevo)
#COMO ELIMINAR
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)
#LOS DICCIONARIOS ACEPTAN DIFERENTES  TIPOS DE DATOS,VAMOS AGREGAR LO QUE SON CADENAS,TEXTOS,VALORES ENTEROS, REALES Y OTRAS COLECCIONES
# EN ESTE CASO LISTAS,TUPLAS Y PODEMOS PONER OTROS DICCIONARIOS DENTRO
diccionario2 = {'Ariel': {'edad': 40,'Altura':1.83},'Osvaldo':[45,1.85],'Natalia':[35,1.67 ]}#RECORDAR LAS LISTAS VAN CON CORCHETES
print(diccionario2)

seleccionArgentina = {
    10:{'Nombre': 'Lionel Messi', 'Edad': 35,'Altura': 1.70,'Precio':'50 Millones','Posicion':'Extremo Derecho'},
    11:{'Nombre': 'Angel Di Maria','Edad':34,'Altura':1.80,'Precio': '12 Millones','Posicion': 'Extremo Derecho'},
    24:{'Nombre': 'Paulo Dybala','Edad':28,'Altura': 1.77,'Precio':'35 Millones','Posicion':'Media Punta'},
    19:{'Nombre': 'Nicolas Otamendi','Edad':34,'Altura':1.83,'Precio':'3.5 Millones','Posicion':'defensa central'},
    1:{'Nombre':'Franco Armani','Edad':35,'Altura':1.89,'Precio':'3.5  Millones','Posicion':'Portero'},
    22:{'Nombre': 'Julian Alvarez','Edad':22,'Altura': 1.70,'Precio':'23 Millones','pocsicion': 'Delantero'},
    4:{'Nombre': 'Gonzalo Montiel','Edad':25,'Altura':1.76,'Precio':'14 Millones','Posicion':'Laeral Derecho'},
    6:{'Nombre': 'German Pezzela','Edad':31,'Altura':1.87,'Precio':'5 Millones','Posicion':'Defensor Central'},
    13:{'Nombre': 'Cristian Romero','Edad':24,'Altura':1.85,'Precio':'48 Millones','Posicion':'Defensor Central'},
    14:{'Nombre': 'Exequiel Palacios','Edad': 23,'Altura':1.77,'Precio':'15 Millones','Posicion':'Volante Central'}
}
print(seleccionArgentina.values())# PODEMOS USAR UNA FUNCION PARA VER LOS VALORES,EN ESTA FUNCION VALUES NO SE LE INGRESA NINGUN DATO DENTRO DE LOS PARENTESIS
#SIMPLEMENTE EN UN DICCIONARIO PONEMOS ESTA FUNCION Y VA MOSTRAR LOS VALORES DENTRO DEL DICCIONARIO

for valor in seleccionArgentina.values():
    print(valor)
for llave,valor in seleccionArgentina.items():
    print(llave,valor)
# COMO TAREA AGREGAR POR LO MENOR 4 JUGADORES MAS AL DICCIONARIO :SELECCION ARGENTINA
print('Tenemos cargados en el diccionario la cantidad de jugadores es:',end=' ')
print(len(seleccionArgentina))

#PILAS USANDO LISTAS, aca siempre se trabaja con los ultimos elementos,ya  sea para  quitar o agregar
pila =[1, 2, 3]
#Vamos a ver como agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
pila.append(6)
print(pila)
#VEMOS COMO ES SACAR ELEMENTOS POR EL FINAL
pila.pop()#El metodo pop con esta funcion SACA Y RETORNA,El metodo pop va a eliminar el ultimo elemento de nuestra lista
print(pila)
elementoBorrado = pila.pop()#Quita el ultimo elemento y lo guarda
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')

# Colas con listas, Estas son una estructura de datos de tipo Fifo,Fifo significa(first input / first output)primero en entrar y primero en salir
#la represenacion es como hacer una cola en el banco, el primero que llega es el primero que van a atender, y si sucesivamente
#la forma es el primero que llega lo atienden y se va, atiendeal al segundo que esta en la fila, y se va , pasa el tercero y se va asi sucesivamente
# Esto es una lista
cola = ['Ariel','Osvaldo','Liliana','Pilar']

#AGREAMOS ELEMENTOS AL FINAL DE LA COLA
cola.append('Natalia')
cola.append('Jose')
print(cola)

#SACAMOS ELEMENTOS DE LA COLA

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)







