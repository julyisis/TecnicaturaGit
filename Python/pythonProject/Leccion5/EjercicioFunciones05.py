# Ejercicio 05: Convertidor de temperatura
# Realizaer dos funciones para convertie de grados celsius
# a fahrenheit y viseversa
# Investigar las formulas

#funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius): # aqui como parametros vamos a necesitar recibir los celcius, entramos en la funcion
    return celsius * 9 / 5 + 32 # la presedencia de operacion lo 1ero es la multiplicacion , luego la diision y por ultimo suma
# Funcion que convierte de fahrenheit a celsius
def fahrenheit_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9  # importante recordar la presedencia para que el calculo salga bien y no de error/ se hace como arriba pero invertidos los numeros es comodar vuelta la formula ,aqui lo
#primero que va hacer es la multiplicacion,luego la division y luego la resta de esta forma no sale el calculo exacto necesitamos algo que es cambiar esta presendencia porque es primero que la multiplicacion y la
#division y son los parentesis primero va a suceder la resta,luego la miltiplicacion y luego la division
# la unica forma de respetar la presenencia es utilizar parentesis

celsius = float(input('Digite el valor de celsius: ')) # ahora creamos una variable que se llame resultado y llamar a nuestra funcion y tenemos que pasarle el valor que ha digitado el usuario
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}') # si es un numero flotante no se genere un numero tan gigante,simplemente queremos que muestre nada mas despues del punto 2 posiciones nada masponemos(:. y 2f)

# ahora vamos a crear la variable fahrenheit que nos va el usuario a ingresar el valor
fahrenheit = float(input('Digite el valor de fahrenheit: '))
resultado = fahrenheit_celcius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado:.2f}')

















