#EJERCICIO 3 CALCULAR LA ESTACION DEL AÑO
mes = int(input('digite un numero del 1 al 12: '))
estacion = None # esto indica que la variable no tiene asignado un valor
if 1 == 3 or mes == 2 or mes ==3:
    estacion = "verano"
elif mes == 4 or mes == 5 or mes == 6:
    estacion = "otoño"
elif mes == 7 or mes == 8 or mes == 9:
    estacion = "invierno"
elif mes == 10 or mes == 11 or mes ==12:
    estacion = "primavera"
else:
    estacion= "Se equivoco no pertenece a ninguna estacion"
print(f"Para el mes: {mes} la estacion es:{estacion}")

