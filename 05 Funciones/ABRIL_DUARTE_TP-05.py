#1 LISTA DEL 1 AL 100
multiplos_de_4 = [num for num in range(1, 101) if num % 4 == 0]
print(multiplos_de_4)== list(range(1, 101))
print(multiplos_de_4)

#2 MOSTRAR PENULTIMO LISTA
lista=("maggie", "perro", "froddo", "pollo", "pelota")
posicion_lista=lista[3]
print(posicion_lista)

#3 LISTA VACIA
lista=[]
lista.append("maggie")
lista.append("perro")
print(lista)

#4 REEMPLAZAR VALOR
animales= ["perro", "gato", "conejo", "pez"]
animales[1]= "loro"
animales[3]= "oso"
print(animales)

#5 REMOVE NUMEROS
numeros= [8, 15, 3, 22,7]
numeros.remove(max(numeros))
print(numeros)

#el codigo elimina el numero mas grande de la lista.

#6 LISTA DEL 1 AL 30
numeros= list(range(10, 31, 5))
print(numeros[:2])

#7 REEMPLAZAR VALOR AUTOS
autos= ["sedan", "polo", "suran", "gol"]
autos[1]= "volkswagen"
autos[2]= "toyota"
print(autos)

#8 LISTA VACIA DOBLE
dobles= []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#9 AGREGAR A LISTA
compras= [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a)
compras[2].append("jugo")
#b)
indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"
#c)
compras[0].remove("pan")
print(compras)

#LISTA ANIDADA
lista_anidada= [[15,True], [25.5, 57.9, 30.6][False]]
print(lista_anidada)

