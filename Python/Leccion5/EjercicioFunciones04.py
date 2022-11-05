# Ejercicio 4: Calculadora de Impuestos
# Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado.(IVA)
# Formula: Pago-total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
#Prporcione el monto del impuesto: 21%
# Pago con impuesto: xxxx

#Creamos la funcion que calcula el total del pago incliyendo el impuesto
def calcular_total_pago(pago_sin_impuestos,impuesto): # creamos la funcion con el nombre de la variable calcular_total_pago y en los parentesis agregamos dos parametros
 #ahora vamos a usar la variable de pago_total y aqui vamos a poner la formula que les habia mostrado en la linea 4
    pago_total =  pago_sin_impuestos + pago_sin_impuestos * (impuesto/100)
    return pago_total # a return le pedimos que nos devuelva pago_total/ cuando presinamos enter sale del return y de la identacion sabe que es el final de la funcion
# Vamos a ejecutar lo que es la funcion atravez de pedir los datos al usuario esto va a ser de tipo flotante
pago_sin_impuesto = float(input('Digite el pago sin impuesto: ')) # estamos usando variables descriptivas
impuesto = float(input('Digite el monto del impuesto a aplicar:  '))
# ahora si vamos a llamar a nuestra funcion antes vamos a crear otra variable que se va a llamar pago con impuesto
#a esta variable le vamos a asignar el llamado que le hagamos a la funcion calcular_tot...tiene que recibir esta funcion dos parametros donde aqui ahora van a ser argumentos, en estos argumentos necesitamos pasarles
# el pago_sin_impuestos y impuestos
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'El pago con impuesto es: {pago_con_impuesto}')

