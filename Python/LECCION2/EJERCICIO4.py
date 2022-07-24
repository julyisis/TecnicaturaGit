# EJERCICIO 4 ETAPAS DE LA VIDA
edad = int(input('Digite una edad de 0 a 41: '))
vida = None
if 0 <= edad < 10: # SINTAXIS SIMPLIFICADA
    vida = "la infancia es increible y bella"
elif 11 <= edad < 19:
    vida = "Tienes muchos cambios, mucho que estudiar"
elif 20 <= edad < 29:
    vida = "Amor y comienza el cambio"
elif 30 <= edad < 41:
    vida = "Madurez y equilibrio"
else:
    vida = "Te equivocaste no pertenece a una etapa de la vida aun"
print(f"La edad es: {edad} la vida es: {vida}")