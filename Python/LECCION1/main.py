'''
miVariable = 3
print(miVariable)
miVariable = "Hello a todos los students de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# LAS LITERALES SE ESCRIBEN X 280 CADA VEZ QUE EJECUTAMOS CAMBIA EL VALOR DE LA VARIABLE X 768
# la literal (x) 744 ,(y) 488 y la (z) 808 al ejecutar cambia la referencia de memoria
print(id(y))
print(id(z))

# LOS TIPOS INT, FLOAT, STRING, BOOL
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "hola alumnos"
print(x)
print(type(x))
x = True
print(type(x))
print(x)
x = False
print(type(x))
print(x)

# MANEJO DE CADENAS (STRING)
miGrupoFavorito = "Dymash"
print("Mi grupo favorito es: "+miGrupoFavorito)

#numero1 = "7"
#numero2 = "8"
#print(int(numero1) + int(numero2))

# TIPOS BOOLEANOS (BOOL)
miBooleano = 3 > 2
print(miBooleano)
if miBooleano:
    print("el resultado es verdadero ")
else:
    print("el resultado es falso")

# PROCESAR LA ENTRADA EL USUARIO
# FUNCION INPUT
#resultado = input("Digite un numero: ") # INPUT NOS REGRESA UN DATO TIPO STRING
#print(resultado)
# CONVERSION DE LA ENTRADA DE DATOS
#numero1 = int(input("Escribe el primer numero: "))
#numero2 = int(input("Escribe el segundo numero: "))
#resultado = numero1 + numero2
#print("el resultado de la suma es: ", resultado)

# COMO ESTUVO MI DIA
#dia = int(input(" como estuvo tu dia del 1 al 10: "))
#print(dia)
titulo = "El Principito"
autor = "Antoine de Saint Exupery"
print("El titulo del libro es: ", titulo)
print("El autor es: ",autor)
'''
'''
# LOS OPERADORES DE ASIGNACION EN PYTHON
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("El resultado de la suma: ",suma)
print(f"El resultado de la suma es: {suma}") # INCLUIR LA VARIABLE DENTRO DE LAS LLAVES ES INPERPOLACION NO HACE FALTA CONCATENAR, NO OLVIDAR LA F
#OPERADOR DE RESTA
resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")
# OPERADOR DE LA MULTIPLICACION
multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")
# OPERADOR DE LA DIVISION
division = operandoA / operandoB
print(f"El resultado de la division es: {division} ")
division =operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")
# OPERADOR MODULO O RESIDUO
modulo = operandoA % operandoB
print(f"El resultado de la division o residuo (modulo) es: {modulo}") # el resultado que vamos a resivir es la division
# OPERADOR DE EXPONENTE
exponente = operandoA ** operandoB
print(f"el resultado del exponente es: {exponente}")
'''
"""
# CALCULAR EL AREA Y EL PERIMETRO DE UN RECTANGULO
alto = int(input("Escribe un numero : "))
ancho = int(input("Escribe un numero: "))
resultado = alto * ancho
print(f"el resultado del area es: {resultado} ")
perimetro = (alto + ancho)* 2
print(f"el resultado del perimetro es: {perimetro}")
"""
"""
miVariable3 = 10
print(miVariable3)
# VAMOS A AMPLIAR Y VEREMOS LO QUE SON
# OPERADORES DE REASIGNACION
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1 # SINTAXIS DE FORMA RESUMIDA EN LO QUE ESTA EN LA LINEA 106
print(miVariable3)
# miVariable3 = miVariable3 - 2
miVariable3 -= 2   # EN LA RESTA
print(miVariable3)
# miVariable3 = miVariable * 3
miVariable3 *= 3
print(miVariable3)
# miVariable3 = miVariable3 / 2
miVariable3 = miVariable3 / 2
print(miVariable3)
# OPERADORES DE COMPARACION ,NOS PERMITEN SABER SI DOS VALORES SON IGUALES  O DISTINTOOS
d = 4
b = 2
resultado = d == b  # COMPROBAMOS SI SON IGUALES
print(resultado)
# OPERADORES DIFERENTES
resultado = d != b
print(resultado)
# OPERADOR MAYOR QUE
resultado = d > b
print(resultado)
# OPERADOR MENOR QUE
resultado = d < b
print(resultado)
# OPERADO MENOR O IGUAL
resultado = d >= b
print(resultado)
resultado = d <= b
print(resultado)
"""
"""
# EJERCICIO : NUMERO PAR O IMPAR
a = int(input("digite un numero"))
print(f"El residuo de la division es: { a % 2} ")
if  a % 2 == 0:
    print(f"El valor de a es: {a} es un numero PAR") # EL RESIDUO DE LA DIVISION
else:
    print(f"El valor de a es: {a} es un numero IMPAR ")
"""
"""
# EJERCICIO DETERMINAR SI ES MAYOR DE EDAD
adulto = 18
edadPersona = int(input("digite un numero: "))
if edadPersona >= adulto:
    print(f"Eres Mayor de edad")
else:
    print(f"Eres Menor de edad")
"""
"""
# OPERADORES LOGICOS
# CON AND
a = False
b = True
resultado = a and b  # ESTO EN CODIGO DURO
print(resultado)
# CON OR
resultado = a or b
print(resultado)
# OPERADOR NOT
resultado = not a
print(resultado)
"""
"""
# EJERCICIO VALOR DENTRO DE UN RANGO
valor = int(input("Digite un valor: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = valor >=valorMinimo and valor <=valorMaximo
if dentroRango:
    print(f"El valor {valor} esta DENTRO del Rango")
else:
    print(f"El valor {valor} esta FUERA del Rango")
"""
"""
# EJERCICIO OPERADOR OR , OPERADOR NOT
# UN PADRE PUEDE ASISTIR AL JUEGO DE SU HIJO?
vacaciones = False
diaDescanso = False
if not (vacaciones or diaDescanso):
    print("Tene trabajo que hacer ")
else:
    print("Puede asistir al juego")
"""
"""
# EJERCICIO RANGO ENTRE LAS EDADES 20 Y 30 AÑOS
edad = int(input("Digite su edad: "))
#veinte = edad >=20 and edad<= 30
#print((veinte))
#treinta = edad >= 30 and edad < 40
#print(treinta)

# if veinte or treinta:
if (edad >= 20 and edad < 30) or (edad >=30 and edad < 40):
    print("Estas dentro del  Rango de los (20'0) a (30'0) años")
#    if veinte:
#        print('Esta Dentro del Rango de los (20\'0) años ')# EN ESTE CASO COMO SON COMILLAS SIMPLES NECESITAMOS LAS BARRAS BASLASH
#    elif treinta:
#       print('Estas dentro del rango de los 30\'0) años')
#    else:
#        print('No estas dentro del rango')

else:
    print("No estas dentro del  Rango de los (20'0) a (30'0) años") # no nos da error tiene las comillas dobles
"""
"""
# EJERCICIO EL MAYOR DE DOS NUMEROS
numero1 = int(input('digite el valor para el numero1: '))
numero2 = int(input('Digite el valor para el numero2: '))
if numero1 > numero2:
    print('el numero 1 es Mayor')
else:
    print('El numero 2 es Menor')
"""
"""
# EJERCICIO TIENDA DE LIBRO
print("DIGITE LOS SIGUIENTES DATOS DEL LIBRO")
titulo = input("Titulo del libro: ")
id = int(input("id del libro: "))
precio = float(input("Precio del libro: "))
envioGratuito = input("Indicar si el envio del libro es gratuito (True/False): ")
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = "el valor es incorrecto, debe escribir True/ False"
print(f'''  
        Titulo: {titulo}
        Id:    {id}
        Precio: {precio}
        ENVIO Gratuito?: {envioGratuito}
''')
"""










