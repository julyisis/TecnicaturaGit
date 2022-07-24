# CICLO WHILE ( MIENTRAS O DURANTE)
"""
contador = 0
while contador < 9:
    print('Ejecutamos nuestro ciclo while ',contador)
    contador +=1
else:
    print('FIN del ciclo while')
"""
"""
maximo = 5
contador = 0
while contador <= 5:
    print("ejecutamos el contador",contador)
    contador +=1
else:
    print("fin del ciclo")
"""
"""
minimo = 1
contador =5
while contador >= 1:
    print('contador',contador)
    contador -= 1
"""
# CICLO FOR (CICLO PARA) NOS PERMITE ITERAR UNA LISTA DE DATOS
# LA DIFERENCIA CON EL CICLO WHILE ES QUE TIENE UN NUMERO INDETERMINADO DE ITERACIONES
# ITERAR ES RECORRER CADA ELEMENTO DE UN CONJUNTO DE DATOS
# VAMOS A ITERAR UNA CADENA ,UNA CADENA ES UN ARREGLO DE CARACTERES
"""
cadena = 'Hello'
for letra in cadena:
    print(letra)
else:
    print('FIN del ciclo FOR')
"""
"""
# PALABRAS RESERVADAS BREAK
for letra in 'Alemania':
    if letra == "a":
        print(f"letra encontrada: {letra} ")
        break # romper cualquier tipo de estructura al encontrar el primer elemento
else:
        print("FIN del ciclo for" )
"""
# PALABRA RESERVADA CONTINUE
for i in range(6):
    if i % 2 == 0:
        print(f'valor: {i}') # ejercicio de abajo cambiamos la logica para utilizar continue y ver los mismos resultados

for i in range(6):
    if i % 2 != 0:
        continue
    print(f"valor: {i}")