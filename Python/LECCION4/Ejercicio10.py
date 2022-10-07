# EJERCICIO 10: NO REPETIR CARACTERES
# HACER UN PROGRAMA QUE PIDA UNA CADENA POR TECLADO ,LUEGO
# METER LOS CARACTERES EN UNA LISTA SIN REPETIR CARACTERES
cadena = input(('Digite una cadena: '))
lista = [] # tenemos una lista vacia, esta lista ahora necesita llenarse, vamos a usar un ciclo for recorriendo la cadena ingresada por el usuario con el iterador para ir asignando esto
for i in cadena: # dentro de este ciclo for vamos a poner una estructura if en la condicion aun no esta en la lista
    if i not in lista: # if iterador si no esta en la lista: #si el caracter aun no esta en la lista
        lista.append(i) # lo agregamos a la lista
print(f'\nLista de caracteres sin repetir ninguno: \n{lista}')