# Ejercicio 03: Funcion Recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
#puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5, dede imprimir:
#5
#4
#3
#2
#1
#En caso de ser el numero 3 debe imprimir:
#3
#2
#1
# si se imprimen numeros negativos no se imprime nada

# vamos a definir nuestra funcion y la vamos a llamar imprimir_numeros_recursivos,dentro del parentesis ponemos nuestro parametro

def imprimir_numeros_recursivos(numero): # vamos a utilizar una estructura if (numero)aca le llega el  parametro
    if  numero >= 1:    # dentro de esta estructura if vamos a poner que si el numero >=1
        print(numero) #y a continuacion vamos hacer recursivo que se llame a si mismo
        imprimir_numeros_recursivos(numero -1)  # fuera de la escructura if vamos a mandar a llamar a nuestra funcion/imprimir_numer.... caso Recursivo
    elif numero == 0:  # ponemos un return para que no halla error al ejecutar
        return

    elif numero <= 0:
        print('Valor ingresado es incorrecto..')

imprimir_numeros_recursivos(5) #(5) aca le estamos pasando el argumento

