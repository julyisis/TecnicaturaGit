# Ejercicio 04: SUMAR NUMEROS PARES DENTRO SE UN RANGO
# HACER UN PROGRAMA PARA SUMAR NUMEROS PARES DENTRO
# DE UN RANGO,POR EJEMPLO
#                       SUMA DE NUMEROS PARES DEL 2 AL 30
#                       SUMA = 240

a = int(input('Didite de donde va a comenzar la suma: '))
b = int(input('Digite hasta donde quiere llegar a sumar: '))
suma = 0  #Aqui en la funcion range le decimos donde comienza y donde termina
for i in range(a, b+1): # CON EL CICLO FOR VAMOS A UTILIZAR LA FUNCION RANGE, AQUI PONEMOS MAS 1 PORQUE EL NUMERO ESPECIFICADO EN LA  EN LA VARIABLE, LE VA A LLEGAR UNA POSICION MENOS
     if i % 2 == 0: #por eso usamos el mas 1para que llegue a una posicion mas,DENTRO NUESTRO CICLO FOR VAMOS A NECESITAR,UNA ESTRUCTURA IF,PARA PONER LA PERACION DE LOS NUMEROS PARES
         suma +=  i   # Usamos el operador de suma simplificado
print(f'\nLa suma de numeros pares dentro de rango es : {suma}')
# PARA LLEGAR A ESTO HEMOS TENIDO QUE LLEGAR A 30
#DENTRO DE LA FUNCION RANGE PODEMOS USAR VARIABLE Y EL DATO SE SUMARLE 1 A LA VARIABLE B,PARA QUE LLEGUE JUSTAMENTE AL NUMERO DESEADO



