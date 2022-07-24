# SENTENCIAS DE CONTROL IF / ELSE( solo puede arrojar un resultado True/ False
"""condicion = 10
if condicion == True:
    print("Condicion es VERDADERO") # CADA TABULACION ES UN NUEVO BLOQUE DE CODICO ES IMPORTANTE respetar la tabulacion
elif condicion == False:
    print("condicion es FALSA")

else:
    print("Condicion sin espesificar")
"""

# CONVERSION DE NUMERO A TEXTO
"""
num = int(input("Digite un numero en el rango del 1 al 3: "))
numTexto = ''
if num == 1:
    numTexto = "Numero uno"
elif num == 2:
    numTexto = "Numero dos"
elif num == 3:
    numTexto = "Numero tres"
else:
    numTexto = "Has ingresado un numero fuera de rango "
print(f"el numero ingresado es: {num} - {numTexto} ")
"""
# OPERADOR TERNARIO
condicion = True
if condicion:
    print('Condicion  VERDADERO')
else:
    print('Condiccion  es FALSO')
# AHORA VAMOS A VER LA SIMPLIFICACION CON EL OPERADOR TERNARIO ESTAMOS COMPARANDO EL EJERCICIO DE ARRIBA
# CON EL OPERADOR TERNARIO SOLO USAMOS UNA LINEA ES LA SINTAXIS SIMPLIFICADA
# SOLO SE RECOMIENDA SI EL CODIGO ES MUY PEQUEÑO
# SOLO PARA IF / ELSE
print('Condicion es VERDADERA') if condicion else print('Condicion es FALSO')






