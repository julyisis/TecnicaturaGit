class MiClase:

    # agregamos un atributo de clase
    #VARIABLE DE CLASE ,ESTE ATRIBUTO DARA A CADA OBJETO EL MISMO VALOR

    Variable_clase = 'Esta es una variable de clase'

    # creamos el dander init
    def __init__(self, variable_instancia):# LA VARIABLE DE INSTANCIA ,DA DIFERENTES VALORES
        self.Variable_instancia = variable_instancia
print(MiClase.Variable_clase)

miClase1 = MiClase('Esta es una variable de instancia ') # estamos creando un objeto
print(miClase1.Variable_instancia)
print(miClase1.Variable_clase)

# los objetos tambien pueden acceder a la variable de clase
miClase2 = MiClase('Esta es otra prueba de variable de instancia ')
print(miClase2.Variable_clase)
print(miClase2.Variable_instancia)