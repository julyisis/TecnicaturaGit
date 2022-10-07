# EJERCICIO 7: JUEGO ADIVINA EL NUMERO
# REALIZAR UN JUEGO PARA ADIVINAR UN NUMERO. PARA ELLO SE DEBE GENERAR UN NUMERO ALEATORIO ENTRE 1-100
# Y LUEGO IR PIDIENDO NUMERO INDICADO "ES MAYOR" O "ES MENOR, SEGUN SEA MAYOR O MENOR
# CON RESPECTO A "N" EL PROCESO TERMINA CUANDO EL USUARIO ACIERTA Y ALLI SE DEBE MOSTRAR EL NUMERO INTENTOS

# PARA HACER ESTE EJERCICIO NECESITAMOS HACER UNA IMPORTACION DE LO QUE ES (RANDOM QUE ES PARA LOS NUMEROS ALEATORIOS
#import random
import random
print("\t.:Juego Adivina el numero:.") # DE ESTA FORMA PONEMOS UN TITULO CENTRADO

aleatorio = random.randint(0, 100) # aqui vamos a ponerle esta variable el numero aleatorio que este eligiendo aqui nuestra funcion random aqui toma de (0 a 100 literal)
contador = 0
while True: # necesitamos un bucle while y True es con "Mayuscula"( ESTE WHILE MIENTRAS SEA VERDADERO SEGUIRA ANDANDO)
    numero = int(input('Digite un numero: ')) # LE PEDIMOS AL USUARIO QUE DIGITE UN NUMERO DE TIPO ENTERO, ESTAMOS DENTRO DEL CICLO
    contador += 1  # utilizamos el contador para ir aumentando con el operador simplificado para que valla aumentando en 1
    if numero > aleatorio: # VAMOS A UTILIZAR UNA ESTRUCTURA IF ,ELIF PARA IR HACIENDO ESTAS COMPROBACIONES
        print("\tNo es el numero,digite un numero MENOR") # esto sirve para para centrar el mensaje
    elif numero < aleatorio: # vamos a utilizar una estructura elif
        print("\tNo es el numero,digite un numero MAYOR")
    else:
        print(f"FELICIDADES acabas de adivinar el numero {aleatorio}")
        break # ROMPE CON EL CICLO Y EL BUCLE
# AQUI LO QUE PODEMOS HACER ES UNA PRESENTACION LA PONDRIA ANTES DE GENERAR EL NUMERO ALEATORIO
print(f"\nNumero de intentos: {contador}")



