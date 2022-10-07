# Ejercicio 01: Crear una funcion para sumar los valores recibidos de tipo
#numericos ,utilizando argumentos variables *args como parametro de la
# funcion y agregar como resultado la suma de  todos los valores pasados
# como argumentos

#Empezamos definiendo lo que es una funcion ,usamos la palabra reservada def para crear la funcion y le vamos a poner de nombre "sumar_valor"
def sumar_valor(*args):# hemos creado nuestra funcion,ahora todo esto sumar _valor con los parentesis y el parametro dentro ,esto es lo que se llama firma de nuestro metodo o firma de nuestera funcion ,aca recibimos una
#cantidad de parametros indefinidos
    resultado = 0 # vamos a iterar cada elemento con un ciclo for
    for valor in args:
        resultado += valor  # y ahora simplemente lo que es fuera del ciclo for hacemos un return
    return resultado # Vamos a reetornar lo que es la variable resultado, esto seria todo para ir sumando valores o parametros indefinidos, una cantidad indefinida


   # pass # esta palabrita se usa para no dejar vacia la funcion y que tengamos un error ,pones esta palabra salis de la funcion seguir programando y despues venis y llenas la funcion
#vamos a llamar a la funcion atravez de un print, lo que hacemos es pasar los argumentos, agregamos los elementos(3,5,9)
print(sumar_valor(3, 5, 9, 2 , 1))