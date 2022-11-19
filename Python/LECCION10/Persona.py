class Persona:
    contador_personas = 0    # VARIABLE DE CLASE
    #vamos a agregar lo que es un metodo de clase agregamos un decorador
"""
En la linea 7 a la 10 lo que se puede hacer atraves de este metodo de clases es: Podemos incrementar valores sin crear un objeto 
"""

    @classmethod  # de la linea 8 a la 16 es contexto estetico
    def generar_siguiente_valor(cls):
        cls.contador_persona += 1
        return cls.contador_persona

    def __init__(self,nombre ,edad):   # contexto dinamico
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad



persona1 = Persona('Ariel',40)
print(persona1)
persona2 = Persona('Osvaldo',45)
print(persona2)
persona3 = Persona('Liliana',35)
print(persona3)
Persona.generar_siguiente_valor()# Para acceder aun metodo de clase,como a una variable de clase  vamos a necesitar hacerlo desde la misma clase
persona4 = Persona('Natalia',35)        #vamos a crear otro objeto
print(persona4)

print(f'Valor contador Persona: {Persona.contador_personas}')