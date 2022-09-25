# EJERCICIO 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Nombre : Aragon
# clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase : Arquero
# Raza: Elfo Sindar

personajes = [] # Creamos una lista totalmente vacia
# Creamos un diccionarios
P = {'Nombre':'Aragon','Clase':'Guerrero','Raza':'Dunadan del norte'}
personajes.append(P) # Agregamos a la lista un personaje
P = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Istar','Nombre':'Frodo','Raza':'Hobbit','Clase':'Portador del anillo'}
personajes.append(P)
P = {'Nombre':'Gollum','clase':'Deagol','Raza':'Hobbit'}
personajes.append(P)
p ={'Nombre':'Legolas','clase':'Arquero','Raza':'Elfo Sindar'}
personajes.append(P)
P = {'Nombre':'Arwen','Clase':'sinderin ,doncella noble','Raza':'Peredhil,Noldar'}
personajes.append(P)
P = {'Nombre':'Gloin','Raza':'De los Enanos','Clase':'Miembro noble de la raza de los Enanos '}
personajes.append(P)
print(personajes)


