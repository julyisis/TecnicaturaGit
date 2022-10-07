# UNA FUNCION EN PYTHON ES UN BLOQUE DE CODIGO QUE VAMOS A PODER LLAMAR "N" CANTIDAD DE VECES,PERO PARA QUE SE PUEDA EJECUTAR
# DEBE SER LLAMADA ESTA FUNCION, PODEMOS CREAR UNA FUNCION Y SI NUNCA LLAMAMOS NUNCA SE VA A EJECUTAR VA A ESAR CARGADO EL COGIGO
# EL COGIGO VA A SER COMO UN COGIGO MUERTO, ES POR ESO QUE UNA FUNCION NECESITA SER LLAMADA, PARA QUE SE EJECUTE EL COGIGO QUE
# ESTA DENTRO DE ESE BLOQUE DE FUNCION
# PARA DEFINIR UNA FUNCION, VAMOS A UTILIZAR UNA PALABRA RESERVADA

# COMENZAMOS CON FUNCIONES
# DEFINIMOS UNA FUNCION,(CON LA PALABRA def DEFINIMOS UNA FUNCION,# El nombre o el identificador de la funcion se esta utilizando un guion bajo,la
# la nomenclatura que se utiliza es la snake case , la otra nomenclatura es de camel case
# USAMOS EN ESTE JERCICIO SNAKE CASE Y LOS PARENRTESIS ESTO ES PARA IDENTIFICAR LO QUE ES UNA FUNCION SI OS SI NECESITA LOS PARENTESIS DE MANERA OPCIONAL
# PODEMOS ENVIAR INFORMACION A LA FUNCION A ESTO SE LO LLAMA(PARAMETROS)
# DESPUES DE LOS DOS PUNTOS DANDO ENTER SE GENERA UNA TABULACION, ESTA TAMBIEN SE SUELE GENERAR DENTRO DE UNA ESTRUCTURA IF, DENTRO DE  LOS CICLOS
#NO SOLO SE LLAMA TABULACION SI NO TAMBIEN AQUI EN PYTHON SE LLAMA (IDENTACION) Y EL BLOQUE SERA NUESTRA FUNCION, Y EL BLOQUE QUE RESPETE ESTA IDENTACION
# VA A SER NUESTRA FUNCION, EN EL MOMENTO QUE QUITEMOS ESTA IDENTACION ,QUE DEJEMOS DE RESPETAR LA TABULACION, LO QUE QUEDE SIN TABULACION  ESTA FUERA DE
# NUESTRA FUNCION
#mi_funcion() NO SE PUEDE LLAMAR ANTES DE DEFINIR A UNA FUNCION
def mi_funcion(): # PARA IDENTIFICAR A LA FUNCION UTILIZAMOS PARENTESIS
     print('SALUDOS A TODOS LOS ESTUDIANTES DE LA TECNICATURA')
#    print()
#    print()# lo que hay desde el primer print y todos los print que pongamos respetando la identacion esta dentro del bloque de la funcion
#print()   #este print esta fuera de la identacion , entonces esta fuera de la funcion
# FUERA DE LA FUNCION LO QUE VAMOS HACER ES LLAMAR A LA FUNCION PARA QUE ESTA SE PUEDA EJECUTAR
#    LLAMAMOS A LA FUNCION
mi_funcion() # ESTAMOS LLAMANDO A LA FUNCION , y la podemos llamar N veces, no se puede llamar si no esta definida la uncion,y la definimos con
mi_funcion() # (def mi_funcion)
mi_funcion()
# SI UNA FUNCION SE DEFINE EN OTRO MODULO, PODEMOS TENER UNA FUNCION EN OTRO LUGAR OTRO MODULO, SI QUEREMOS UTILIZAR ESA FUNCION EN ESTE MODULO
# ENTONCES LO QUE SE HACE ES IMPORTAR A ESE MODULO, PARA LOGRAR LLAMAR ESA FUNCION 

# DESEMPAQUETADO DE LISTAS UNPACKING
# VAMOS CREAR UNA FUNCION LA VAMOS A LLAMAR SHOW
def show(name,lastName): #dentro de los parentesis necesitamos dos parametros
     print(name+'  '+lastName)            #vamos a crear una lista llamada person dentro de la lista pondremos nombre
person = ['Ariel','Betancud']# llamamos a nuestra funcion show  le vamos a decir person y podemos ir pasando uno por uno los datos directamente a nuestra funcion y esos datos son los que se guardaron en nuestra variable
#person
show(person[0], person[1]) #abrimos corchetes y podemos pasar uno por uno los datos a nuestra funcion, estos datos son los que se guardaron en nuestra variable person o nuestra lista.# tambien hay una forma de ir pasando
#los datos a nuestra funcion para que los muestre que es el trabajo que va a hacer nuestra funcion por eso se llama show,y tambien podemos hacer que muestre todos los datos que le hemos ido ingresando en codigo duro
# a la lista persona, en esta lista que se van agregando los valores a los parametros, le estamos enviando los parametros recorriendo la lista esto lo podemos hacer tambien de la sgte manera
# de esta manera resumimos la forma de desempaquetar una lista a traves de una misma funcion que necesita que le pasemos los argumentos y en la  funcion recibe los parametros para luego mostrarlos, tambien esto NO solo se
#utiliza con listas si no tambien se utiliza con TUPLAS .
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto que lo anterior usamos *person para simplificar
#RECUERDEN QUE LAS TUPLAS SE CREAN CON LOS PARANTESIS
persona2 = ('Osvaldo ','Giordanini') # aqui tenemos una TUPLA ,desempaquetqamos a travez de una TUPLA
show(*persona2) #pomnemos nuesta funcion (*person2)Aqui lo hacemos con una tupla
          #VEAMOS CON UN DICCIONARIO( PARA CREAR UN DICCIONARIO USAMOS LLAVES)
# como desempaquetamos este diccionario mas o menos siguiendo la misma sintaxis,lo hacemos de la sgte manera,mandamos a llamar a nuestra funcion show y simplemente cuando poniamos 1 era porque iba recorriendo un
#elemento dentro de lo que era lista o tuplas en este caso necesitamos lo que es:(CLAVE Y VALOR( **)
persona3 = {'lastName':'Lucero','name':'Natalia'}
show(**persona3)
      #VAMOS HACER UN REPASO DE LO QUE ES EL CICLO FOR ,ELSE
# VAMOS ACREAR UNA VARIABLE SE VA A LLAMAR NAMBERS Y ESTO VA A SER UNA LISTA DE NUMEROS
# si nuestra lista estuviera vacia[] igual se ejecutaria nuestro else diciendo 'Esto se termino'de que manera hacemos para que no se muestre este mensaje es utilizando antes un ciclo if antes del else y un break
# SERIA LA UNICA MANERA PARA QUE NO SE MOSTRARA EL ELSE
numbers =[1, 2, 3, 4, 5] #creamos una lista de numeros, y vamos a poner un ciclo for, AUN CON LA LISTA VACIA SE EJECUTA EL ELSE
for n  in numbers:  # vamos a utilizar una variable n
     print(n) # luego de esto vamos a poner aun else
     if n == 5 :
          break
else:  # con el else ha terminado de recorrer la lista
     print('Esto se termino ')

     # LIST COMPREHENCION, LISTA DE COMPRENCION
   # LA FORMA PARA TOMAR O NECESARIO DE UNA LISTA Y NADA MAS Y NO HACER NINGUN TPO DE MODIFICACIONES EN ESA LISTA ,SIMPLEMENTE TOMAMOS ESA LISTA SACAMOS LO QUE NECESITAMOS Y LISTO, LA LISTA NO SE TOCA NO SE
   #MODIFICA ABSOLUTAMENTE NADA
names = ['Paolo','Rodrigo','Lupe','Pepe']# es una lita de nombres, es una string
# Que estamos haciendo aqui para utilizar la p, que hace esta p esto es para cada elemento,pero en singular para utilizamos la p entonces p for,p in names esto es para recorrer todos los nombres de la lista y con
#el if p[0] == 'p' aqui tenemos una condicion,la CONDICION ES SI LOS elementos desde 0 en adelante alguno es igual a la letra p entonces eso lo que va a regeresar es una nueva lista ,donde se va a guardar en alongP
# Esto regresa una nueva lista # ahora hacemos la compresion, tomar lo necesario de esta lista, creamos una lista nueva
# donde estan las comillas y la P en mayusculas si cambiamos por la R nos va a imprimir Rodrigo
# vemos que en la nueva lista almaceno solo los nombres que estan escritos con la letra P mayusculaes eso lo que empezo a buscar y a recorrido sin utilizar un ciclo for SIMPLEMENTE HEMOS UTILIZADO UNA CONDICCION
#recorriendo en lo que es la lista names sin modificar la lista names y singular aqui estamos recorriendo pieza por pieza, elemento por elemento , y logramos obtener un resultado, esto no solo se puede hacer con lo
# que es las listas, tambien con diccionarios en fin cuando estamos tratando con array y tambien respetando lo que son inmutables o mutables, justamente qie tiene que ver esto con mutables e inmutables es que no
# modifican nunca la lista, la tupla o lo que este recorriendo ,asi sea un diccionario nunca lo modifica, nunca lo afecta en nada, simplemente extrae de ellos lo necesario nada mas
alongP = [p for p in names if p[0] == 'P' ] # aqui vamos a mostrar una nueva lista pusimos la p y la P mayuscula porque son nombres
print(alongP)

   # VAMOS A VER ESTO CON UN DICCIONARIO
 # AQUI TENEMOS UN DICCIONARIO CON BOTELLAS DE CERVEZA, TENEMOS NOMBRE QUILMES Y EL PAIS DE ORIGEN DE ESTA CERVEZA ARGENTINA, DESPUES CORONA MEXIXO ETC
 # AHORA VAMOS A CREEAR EL DICCIONARIO PARA GUARDAR LO QUE NOSOTROS NECESITAMOS DE ESTE DICCIONARIO A PARTE
bottleC = [{'name':'Quilmes','country':'Arg'},
           {'name':'Corona','country': 'Mx'},
           {'name':'Stella Artois','country':'Belgium'},
           ]
# Estamos haciendo lo que hicimos arriba recorremos elemento por elemento en lo que es en nuestro diccionario bottleC y luego aqui  tenemos la condicion "if b['country]"diciendole que si aqui el elemento
# b['country] == 'Arg'que estamos recorriendo singularmente dentro de lo que es country es igual al valor de Arg en tipo string entonces Aqui se va a crear el diccionario Arg
# vamos a mostrar los dos diccionarios el bottleC y el Arg
Arg = [b for b in bottleC if b['country'] == "Arg" ]
print(Arg) # solo toma lo que necesitamos
print(bottleC)#el diccionario completo aqui no se ha modificado en nada

#CONTINUAMOS CON FUNCIONES EN LO QUE SON EN 'PASO DE ARGUMENTOS (FUNCIONES) vamos a definir una funcion,creamos una funcion lamada mi_funcion2,en los parentesis ponemos los parametros
#Dentro de nuestra funcion ya le pasamos lo que son los parametros y ponemos para imprimir
def mi_funcion2(name, lastName): # Aqui tenemos los Paramentros,El parametro va a trabajar con una variable dentro de lo que es la funcion
     print('Saludos a todos los que nos ven a traves del canal de you tobe')# ponemos otro print mas ,este segundo print lo hacemos con la interpolacion
     print(f'Nombre: {name}, Apellido: {lastName}')# hemos creado esta fucnion es que la mandemos a llamar
 # LA DIFERENCIA ES QUE LOS PARAMETROS SON LAS VARIABLES QUE DECLAREMOS EN LA FUNCION Y EL ARGUMENTO ES EL VALOR QUE ENVIAMOS A LA FUNCION
mi_funcion2('Jorge','Lucero')# Aqui necesita que le pasemos lo que son los argumentos, SI aui llamamos a la funcion sin poner los argumentos, tendriamos un error, estos argumentos son el valor'Jorge Lucero'
# que va a recibir el parametro, en este caso mi funcion 2 pero con DIFERENTES ARGUMENTOS
mi_funcion2('Ariel','Betencud')
mi_funcion2('Analia','Pedrosa')# aca estamos pasando distintos Argumentos y es por eso que va a mostrar distintos valores
 #    LA PALABRA RETURN EN FUNCIONES
 #  VAMOS A CREEAR UNA FUNCUION PARA SUMAR
 # CUANDO CREAMOS UNA FUNCION TENEMOS DOS OPCIONES 1: ES ASIGNAR A UNA VARIABLE EL RESULTADO DE LA OPERACION Y DESPUES ESA VARIABLES ES LA QE VAMOS A RETORNAR  Y SI NO
                                        # OPCION 2: REGRESAR EL RESULTADO DIRECTAMENTE CON RETURN HACIENDO LA OPERACION DENTRO DE RETURN
  # VAMOS HACER LA OPCION 2:
def sumar(a , b): # fuera de lo que es la funcion vamos a crear una variable se va a llamar resultado
    return a + b
#resultado = sumar(78, 22, )# aqui nnuestra funcion necesita que le pasemos los argumentos que le vamos a pasar son 78,...
#print(f'El resultado de la suma es: {resultado}')
print(f'El resuldado de la suma es: {sumar(55,45)}')

#  VOLORES POR DEFAULT EN LOS PARAMENTROS DE UNA FUNCION
# VAMOS A CREAR OTRA FUNCION  LLAMADA SUMAR2
def sumar2(a = 0, b = 0 ):# el valor por default va hacer este (a = 0, b = 0)
    return a + b  # ESTA ES TODA NUESTRA FUNCION , SICREAMOS LA VARIABLE  PONEMOS UN RESULTADO, Y SI LLAMAMOS A LA FUNCION SUMAR2 Y NO LE PASAMOS ABSOLUTAMENTE NADA
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")# nos va a dar error, estan faltando los argumentos,para que esto no suceda, hay que darle un valor por default a lo que son nuestros paramentros
print(f"Resultado de la suma: '{sumar2(22, 66)}") # en sumar2 ponemos un valor, ya le habiamos dado un valor por default que es 0 no va a pasar nada en la primera vez va a dar el resultado de 0 porque el valor de
#default es valor 0 a cada uno de los parametros pero aqui le estamos pasando un valor, y este valor por default se ve alterado cuando nosotros le pasamos un argumento valido entonces vamos a ejecutar y ven que el resultado
# primero es 0 ,pero el segundo es 88 es porque le hemos pasado valores el 22 + 66 =88 esta es la manera de trabajar con funciones para evitar errores se puede trabajar dandoles valores a las variables numericas
# un valor por default

# ARGUMENTOS (estos argumentos son variables en funciones)
# Normalmente se utiliza: *args
def listaNombres(*nombres):  # vamos a definir  una funcion def y le vamos a poner listaNombres()con los parentesis desconocemos el N°de argumentos que va a recibir nuestra funcion, no sabemos cuantos nombres,sabemos que va a recibir nombres
    #pero no sabemos cuanto van hacer, entonces normalmente se utiliza de la sgte manera def lista((*nombres):esta es la forma para que varien los argumentos,vamos a utilizar un ciclo for dentro de nuestra funcion
    for nombre in nombres: # vamos a utilizar la variable nombre y hacemos un print
        print(nombre)# saliendo ya lo que es la funcion listaNombres y saliendo tambien del cuerpo del ciclo for del bloque for, entonces es que aqui vamos a pasar directamente los argumentos y vamos a poner la funcion
listaNombres('Lucas','Jose','Claudia','Rosa','Maria')  # Aqui ingresamos varios nombres # con def listaNombres(*nombres): hemos capturado cada uno de la lista de los nombres si utilizaramos la misma variable
listaNombres('Marcos','Daniel','Romina','Pepe','Marcela','Carlos')#y agregamos mas nombres nos los añade a todos esta es una manera muy practica pero de trabajar para con una funcion que no tenemos idea ,de los
#argumentos que va a recibir, lo puede recibir cantidad de argumentos que van a variar es lo que sucedio aqui, cada vez que llamo a la funcion pues recibe mas argumentos y esto se va añadiendo a la funcion y los va
# mostrando, tambien recorriendolos a cada uno de ellos , en la sintaxis de *nombre generalmente se utiliza: *args es lo que van a encontrar en la sintaxis, se va a convertir dentro de nuestra funcion en que se
#va a convertir la (variable nombre en que se conbierte el parametro for nombre in nombres:)se va a convertir en una tupla, son tuplas las que esta recibiendo son tuplas, lo que ya no pueden ser modificadas y se van
#agregando los elementos como argumentos










