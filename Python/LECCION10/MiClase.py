class MiClase:

    # agregamos un atributo de clase
    #VARIABLE DE CLASE ,ESTE ATRIBUTO DARA A CADA OBJETO EL MISMO VALOR

    Variable_clase = 'Esta es una variable de clase' # esta es una variable de clase la podemos crear aqui o en la linea 22

    # creamos el dander init
    def __init__(self, variable_instancia):# LA VARIABLE DE INSTANCIA ,DA DIFERENTES VALORES
        self.Variable_instancia = variable_instancia

    """
       Ahora vamos a continuar con "METODOS ESTATICOS",como tenemos "VARIABLES DE CLASE", tambien tenemos "METODOS DE CLASE"LA VARIABLE DE CLASE 
       esta en la linea 6 vimos que la podemos crear como un atributo o la podemos crear a abajo en la linea 27 fuera de lo que es el cuerpo de la clase 
       Hay dos tipos de metodos, bien vamos hablar de los metodos de clase tenes dos que se pueden asociar a una clase
       1: SON LOS METODOS ESTATICOS 
       2:LOS METODOS DE CLASE 
       LOS METODOS ESTATICOS:Se asocian a la clase para utilizarlo o ejecutarlo sera atravez de la clase, luego llamamos al metodo ESTATICO
       el ej lo vimos con una variable de clase linea 39
       Para indicar a un metodo ESTATICO se utiliza un "DECORADOR" en la linea 38 lo vamos a hubicar un "METODO ESTATICO" que DECORADOR 
       vamos a utilizar , el @staticmethod
    """
    """
    que puede acceder al dinamico porque estamos viendo en este caso cuando trabajamos con variables de clase con metodos de clase 
    sabemos que estamos hablando del contexto estatico que es la creacion de metodos o variables que se asocian directamente a la clase NO AL OBJETO"
    lo que "SI SE ASOCIA AL OBJETO LAS COSAS QUE SON DE CONTEXTO DINAMICO"ES la accion apartir de la creaccion de una isntancia y con ellas 
    trabaja
    "EL CONTECTO DINAMICO: POR EJ ES UN DANDER _INIT_ esta dentro del CONTEXTO DINAMICO, el dander init esta creado justamente para la instancia de objetos
    "UNA VARIABLE DE CLASE: esta dentro del CONTEXTO ESTATICO que esta asociada a la ( clase en si linea 1) este metodo estatico no necesita la 
    palabrita reservada self porque esa palabrita reservada es un operador que nos ayuda para la instancia de los objetos ,para reasignar tbn a los atributos
    los valores que recibe por parametro en la creacion de cada instancia 
    """
    """
    La clase que se llama MiClase se carga en memoria la primera vez que se crea un objeto, la clase no se crea en memoria hasta que no se crea un objeto en si 
    se carga la clase memoria a partir de la primera instancia 
    """
        #METODO ESTATICO SE ASOCIA A LA CLASE
    @staticmethod # un decorador como este que hace modifica el metodo para asociarlo a la clase y NO AL OBJETO , creamos el objeto pero en los parentesis se desaparece el self:
    def metodo_estatico(): #el metodo estatico no recibe el self LA PALABRA "SELF REFERENCIA AL OBJETO"El estatico no puede acceder al dinamico ni a los atributos,que hacemos dentro del metodo statico
        print(MiClase.Variable_clase)

    """
    METODOS DE CLASE: UN METODO ESTATICO NO RECIBE NINGUNA INFORMACION DE LA CLASE EN SI MISMA POR ESTO SE DICE QUE UN METODO ESTATICO NO TIENE INFORMACION
    DIRECTAMENTE RELACIONADA CON  LA CLASE  PODRIAMOS SUSTITUIR ESTE TIPO DE METODO CON CUALQUIER OTRO CREADO DENTRO DE ESTE ARCHIVO, COMO UNA FUNCION MAS
    DENTRO DEL MODULO 
    EL METODO ESTATICO SIRVE PARA ASOCIAR DE MANERA LOGICA ALGUN OTRO METODO QUE NO TENGA NADA QUE VER CON LOS ATRIBUTOS DE NUESTRA CLASE SI NO QUE 
    SIRVA POR UNA CUESTION LOGICA ASOCIAR EL TIPO DE METODO QUE NO TENGA QUE TRABAJAR CON LAS VARIABLES DE CLASE PARA DEFINIR UN METODO DE CLASE UTILIZAMOS 
    UN DECORADOR 
    """
    """
    en este segundo decorador en vez de recibir un self ,estamos recibiendo un cls,en un metodo de clase, que diferencia hay entre el self y el cls
    con respecto al decorador a diferencia de un metodo estatico, un metodo de clase si recibe un contexto de clase 
    el cls es una referencia a la clase en si misma se puede utilizar otra palabra no solamente el cls,otra palabra como parte, pero este parametro
    puede ser cambiado se recomienda por sintaxis usar el cls
    """
    @classmethod # decorador necesario para un metodo de clase
    def metodo_clase(cls):
        print(cls.Variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.Variable_clase)
        print(self.Variable_instancia)





print(MiClase.Variable_clase)
miClase1 = MiClase('Esta es una variable de instancia ') # estamos creando un objeto
print(miClase1.Variable_instancia)
print(miClase1.Variable_clase)
# los objetos tambien pueden acceder a la variable de clase
miClase2 = MiClase('Esta es otra prueba de variable de instancia ')
print(miClase2.Variable_clase)
print(miClase2.Variable_instancia)

MiClase.Variable_clase2 = 'Valor de variable de clase 2' #Al crear en esta parte el codigo si o si tenemos que asignarle un valor,no le puede faltar que le asignemos un valor la hemos creado llamando a la clase con el operador de punto
print(MiClase.Variable_clase2)
print(miClase1.Variable_clase2)
print(miClase2.Variable_clase2)

#AQUI AL FINAL VAMOS A LLAMAR AL METODO ESTATICO Y SE LLAMA A TRAVES DE LA CLASE MIClase.metodo_estatico
#para acceder a un metodo de clase utilizando la clase misma aqui abajo, tbn podemos acceder desde un objeto como lo vimo en la linea 76 y 77
MiClase.metodo_estatico()
MiClase.metodo_clase()# vamos a llamar al metodo de clase necesitamos a MiClase

"""
EN EL COMPILADOR NOS DICE "ESTA ES UNA VARIABLE DE CLASE" cuando llega aqui lo que hace es llamar al "METODO ESTATICO" A TRAVES DE L CLASE VA A LLAMAR 
A LA VARIABLE DE CLASE  la primera creada que esta creada arriba linea 6 y muestra el resuldado y vuelve a la linea 40 y muestra todos los resultados 
en este ejercio vemos lo que es la creacion de la variable de clase dentro del cuerpo de la clase 
y la creacion de variable de clase fuera del cuerpo de la clase y LA CREACION DE UN METODO ESTATICO LINEA 38,las variables de clases son tambien dentro 
del contexto estatico, el metodo estatico esta dentro del contexto estatico y hemos hecho un entrelazado con objetos que ya estarian dentro del contexto 
dinamico

EL CONTEXTO ESTATICO: TRABAJA DESDE LA CLASE 
EL CONTEXTO DINAMICO: NO PUEDE ACCEDER AL CONTECTO ESTATICO HASTA QUE NO SE HALLA INSTANCIADO , UNA VEZ QUE SE INSTANCIO A PARTIR DE ALLI ES 
QUE RECIEN PUEDE ACCEDER A TRAVES DEL OBJETO A UN ELEMENTO DE CONTEXTO ESTATICO, MIENTRAS NO ESTE EL OBJETO CREADO, MIENTRAS NO HALLA NINGUN TIPO 
 DE INSTANCIA SEPUEDE SEGUIR TRABAJANDO CON LO QUE ES EL CONTEXTO ESTATICO, PERO EL DINAMICO NO PUEDE HACEDER AL ESTATICO HASTA QUE NO HALLA SUCEDIDO
 LA CREACION DE UNA INSTANCIA SERIA LA LOGICA Y LA SINTAXIS DE LO QUE ES EL CONTEXTO ESTATICO Y DINAMICO 
 """

#creamos otro objeto al crear el objeto se ha creado el contexto dinamico ,vamos acrear un metodo de intancia, linea 60
miObjeto1 = MiClase('Variable de instancia')
miObjeto1.metodo_clase() # accedemos al objeto

miObjeto1.metodo_instancia()#ponemos mi objeto ,vamos a llamar con el operacor de punto vamos a acceder al metodo instancia

