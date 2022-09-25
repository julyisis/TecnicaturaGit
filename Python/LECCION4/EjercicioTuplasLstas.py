import math #Importamos la clase math para hacer uso de la funcion sqrt(raiz cuadrada)

# DADAS LAS SIGUIENTE TUPLA
tupla = (13, 1, 8, 3, 2,5 ,8)# DEFINIMOS LA TUPLA
# CREAR UNA LISTA QUE SOLO INCLUYA LOS NUMEROS MENORES A 5 E IMPRIMA POR CONSOLA [1,3,2]

lista = [] # DEFINIMOS FILA LISTA
# FILTRAMOS LOS ELEMENTOS MENORES  5 DE LA TUPLA
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

# EJERCICIO DE MATEMATICAS
# PARA SACAR LA RAIZ CUADRADA DE UN NUMERO POSITIVO
# PODEMOS LLAMAR A LA CLASE MATH POR QUE ESTA IMPORTADA  EN LA PARTE SUPERIOR LA HEMOS LLAMADO CON EL OPERADOR DE PUNTO PUNTO LLAMAMOS A LA FUNCION PARA LA RAIZ CUADRADA
numero = int(input('Digite un numero positivo:  '))
while numero < 0:
    print('Error ->Deberia ser un numero positivo')
    numero = int((input('Digite un numero positivo')))
print(f'\nSu raiz cuadrado es: {math.sqrt(numero):.2f}')   # lo que esta dentro de las llaves de esta forma el numero que nos de con coma no es tan largo 0,25
#

