#   ejercicio 1: llenar una lista
# LLENAR UNA LISTA CON LOS NUMEROS DEL 1 AL 50, LUEGO MOSTRA LA
# LISTA CON EL BUCLE FOR, LOS ELEMENTOS DEBEN MOSTRARSE
# DE LA SIGUIENTE FORMA:
# 1-2-3-4-5-..-50

#lista = []
#i = 1   # vamos a realizar un codigo mas eficiente de lo mismo pero en una sola linea
# while i <= 50:
#      lista.append(i)
#      i += 1
lista = list(range(1,51)) # algoritmo se reduce el codido para que sea mas eficiente
for i in lista:
    print(i,end='-')

