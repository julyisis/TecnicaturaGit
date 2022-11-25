#    SOBRE CARGA DE OPERADORES PARTE1

a  = 3
b  = 5
print(a + b) # el mismo operador esta teniendo una sobrecarga en uno suma en el otro concatena, con las mismas variables

a = 'Hola'
b = 'Mundo'
print(a + b)
a = [3,4,5]
b = [6,7 ,8,9]
print(a + b)

# si tenemos dos objetos esto nos permita realizar la siguiente operacion
#miObjeto1 + miObjeto2 esto si fueran objetos no se pdrian hacer,porque el operador de por si de suma va a necesitar una sobrecarga  para poder realizar la operacion para la sobrecarga hay que sobreescribir
# el metodo heredado de la clase object, osea el metodo asociado al operador en este caso en el operador de suma


