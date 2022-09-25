# Ejercicio1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuacion #elimine los elementos repetidos,por ultimo
#mostrar la lista

#CREAMOS UNA LISTA
lista = [1,2,3,"Ariel",7,7,3,"Alberto",1,"Ariel",2,"Alberto"] # Una lista se comienza con corchetes
#los tipos set o conjuntos no pueden tener elementos repetidos, entonces pasamos nuestra lista a un conjunto
conjunto = set(lista)#Convertimos la lista a un conjunto de tipo set
lista = list(conjunto)# Convertimos el conjunto a una lista
lista = list(set(lista))# de esta forma redujimos el codigo simplificamos el mismo ejercicio, con una sola linea de codigo (eficiente)
print(lista)



