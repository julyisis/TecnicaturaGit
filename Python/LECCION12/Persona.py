class Persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other): # este parametro de other puede recibir otro nombre other significa otro
        return f'{self.nombre}  {other.nombre} '

    def __sub__(self, otro): # sub significa  = subtraction (resta)
        return self.edad - otro.edad # aqui hacemos que retorne lo que es la resta

persona1 = Persona('Ariel',40) # aqui creamos un objeto
persona2 = Persona('betancud', 5)

# al llamar al metodo add la sintaxis seria la siguiente
persona1.__add__(persona2)# pero esta sintaxis NO es como se acostumbra a escribir, pero como seria que esta sintaxis se genere en lo real en los hechos
# No hace falta llamar al metodo dander add simplemente si pusieramos un print
print(persona1 + persona2) # dentro de esta sintaxis estaria sucediendo lo de arriba linea 14 el primer objeto llama al dander add y dentro es que necesita que pase
# el otro objeto por eso other = otro lo que hizo es que lo unio sumo una cadena con la otra solo estamos trabajando con lo que es el nombre, no estamos trabajando con la edad
# esta es la sintaxis
print(persona1 - persona2)
