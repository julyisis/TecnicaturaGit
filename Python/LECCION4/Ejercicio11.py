# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos.Crear un diccionario donde la clave sea el nombre del usuario y
# el valor sea el telefono, el programa tendra el siguiente menú de opciones:
#         1.Nuevo contacto
#         2.Borrar contacto
#         3.ver contactos existentes
#         4.Salir
agenda = {}
while True:
    print('\t.:Menu:.')
    print('1.Menu contacto')
    print('2.Borrar contacto')
    print('3.Ver contacto existente')
    print('4.Salir')
    opcion = int(input("Digite una opcion de Menu: ")) # LO QUE HACEMOS LE PEDIMNOS AL USUARIO QUE DIJITE UNA DE LAS OPCIONES DEL MENU
    if opcion == 1: # abrimos un if para hacer las comparativas de las distintas opciones
        nombre = input('Digite el nombre del contacto: ')# creamos una variable
        telefono = input('Digite el numero de telefono: ')# ahora creamos una estructura anidada para crear if lo que es nuestro diccionario
        if nombre not in agenda: # si el nombre no esta en la agenda
            agenda[nombre] = telefono # vamos a poner nuetro diccionario agenda ahi estamos creando nuestro diccionario
            print('Contacto agregado exitosamente! ') #SI EL CONTACTO YA HA SIDO UTILIZADO UTILIZAMOS UN ELSE
        else:
            print('Este nombre de contacto ya existe')
    elif opcion == 2:
        nombre = input('Cual es el nombre del contacto: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Se ha eliminado el contacto requerido ')
        else:
            print('Ese contaco No existe en la agenda')
    elif opcion == 3:
        print('Agenda de contactos ')
        for  clave, valor  in agenda.items():# PARA RECCORRER LAS COLECCIONES USAMOS UN CICLO FOR,vamos a utilizar dos variables y el valor1
             print(f"Nombre: {clave},Telefono: {valor}") # aqui se van a mostrar todos los numeros y nombres de la agenda
    elif opcion == 4:
        print("Gracias por utilizar su agenda de contactos ")
        break
    else:
        print("Se equivoco de opcion de menu")
    print()









