# EJERCICIO 9: MOSTRAR UNA FRASE SIN ESPACIOS Y CONTAR SU LONGITUD
# HACER UN PROGRAMA DONDE EL USUARIO INGRESE UNA FRASE SE LE
# DEVOLVERA LA MISMA FRASE PERO EN BLANCO,Y
# ADEMAS UN CONTADOR DE CUANTOS CARACTERES TIENE LA FRASE
# ( SIN CONTAR LOS ESPACIOS EN BLANCO
# EJEMPLO:      FRASE = VIVIR POR SIMPRE EN PAZ
#               FRASE FINAL = VIVIRPORSIMPREENPAZ
#               N DE CARACTER = 21

frase1 = input("Digite una frase: ") # Creamos la variable frase y le asignamos como va hacer de tipo string no hace falta hacer ninguna trasformacion le decimos al usuario que digite una frase
frase2 = " " # a la frase 2 le vamos a asigar un espacio un vacio
for i in frase1:  # recorremos la frase con ciclo for, poner los dos puntos :
    if i  != " ":        # esta es la sintaxis , le vamos a decir que si el iterador es diferentea un espacio
        frase2 += i      # Aqui dentro vamos hacer la frase2, vamos a utilizar un operador simplificado para asignarle el iterador
        # saliendo ya del ciclo if y del ciclo for
frase1 = frase2 # en la frase 1 se ingreso toda la cadena con sus espacios luego en el ciclo con el condicional se quitan todos los espacios,en el momento se quitaron todos los espacios se guardo esto en frase2
print(f"\nFRASE FINAL: {frase1}")
print(f'N° de caracteres: {len(frase1)}')  # Aqui usamos la funcion len para cadenas


