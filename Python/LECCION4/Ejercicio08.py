# EJERCICIO 8: MENU INTERACTIVO -CAJERO AUTOMATICO
# HACER UN PROGRAMA QUE SIMULE UN CAJERO AUTOMATICO CON UN SALDO
# INICIAL DE 1000$ Y TENDRA EL SIGUIENTE MENU DE OPCIONES:
#         1.INGRESAR DINERO EN LA CUENTA
#         2. RETIRAR DINERO DE LA CUENTA
#         3. MOSTRAR DINERO DISPONIBLE
#         4. SALIR

saldo = 1000
while True:  # en nuestro ciclo while le vamos a decir mientras sea True
    print("\t.:MENU:.")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible ")
    print("4. Salir")
    opcion = int(input("Digite una opcion de menu: "))# Creamos nuestra variable opcion para la opcion que va a ir digitanddo el usuario
    print() # el print con los parentesis vacios representa un salto de linea
    if opcion == 1:  # comenzamos con la estructura if ,le vamos a decir que: si opcion es igual a 1, si el usuario ingresa 1 vamos a crear una variable que se llame extra
        extra = float(input("Cuanto dinero desea ingresar ->"))  # Esta variable va a ser de tipo float, porque manejamos dinero,convertimos el input a un numero flotante ,aqui se guarda la cantidad de dinero
        saldo += extra #  Operador  Simplificado de += esto representa que deberia estar repetida la variable saldo con extra
        print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 2: # el elif va a decir que si la opcion es igual a 2, entonces va a pasar que lo que pedia en el menu 2 es retirar el dinero de la cuenta, creamos la variable retirar
        retirar = float(input("Cuanto dinero desea retirar: ->"))# una vez hecho esto debemos poner una estructura if anidada, donde le ponga un limite al usuario en que no retiere mas dinero del que tiene en la cuenta
        if retirar > saldo: # vamos a utilizar la estructura if,le vamos a decir que si retirar es Mayor al saldo le diremos que no tiene esa cantidad de dinero
            print("No tiene esa cantidad de dinero")# ahora tenemos que poner un else, si esto no es asi, si es lo que ha ingresado y se ha guardado en la variable retirar ese monto resulta que ese monto no es mayor que saldo
         # eso quiere decir que le tenemos que habilitar el proceso de sacar o retirar el dinero y al mismo tiempo le temenos que decir cuanto dinero le quedo
        else:
            saldo -= retirar# operador de sigancion en este caso para restar con la variable retirar
            print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 3: # vamos a necesitar otro elif para la opcion 3
        print(f"Dinero en la cuenta el momento: ${saldo}") # eso es todo lo que necesita hacer en la opcion tres
    elif opcion == 4:
        print("Gracias por usar su cajero automatico, hasta pronto")# la f de format la interpolacion no la vamos a utilizar porque no hay variables que mostrar pero si necesitamos romper tanto el bucle como los condicionales
        break
    else:  # con este else lo que vamos hacer es que si el usuario digita otro numero de opcion diferente a 1,2,3,4
        print("ERROR, se equivoco en opcion de menu")
        print()








