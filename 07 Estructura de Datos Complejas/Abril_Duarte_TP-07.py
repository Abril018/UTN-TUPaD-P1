#1 PRECIOS FRUTAS
precios_frutas= {"banana":1200, "anana": 2500, "melon": 3000, "uva":1450}
precios_frutas["naranja"] = 1200
precios_frutas["manzana"] = 1500
precios_frutas["pera"] = 2300

print(precios_frutas)

#2 ACTUALIZAR PRECIOS
precios_frutas["banana"] = 1330
precios_frutas["manzana"] = 1700
precios_frutas["melon"] = 2800

print(precios_frutas)

#3 FRUTAS SIN PRECIOS
frutas_sin_precios = list(precios_frutas.keys())
print(frutas_sin_precios)

#4 NUMEROS TELEFONICOS
agenda={}
for i in range(5):
    nombre = input("Ingrese el nombre de la persona: ")
    telefono = input("Ingrese el número de teléfono: ")
    agenda[nombre] = telefono

consulta= input("Ingrese el nombre de la persona a consultar: ")
if consulta in agenda:
    print(f"El número de teléfono de {consulta} es: {agenda[consulta]}")
else:
    print(f"El contacto no se encuentra en la agenda.")

#5 PALABRAS UNICAS

frases= input("Ingrese una frase: ")
palabras = frases.split()
palabras_unicas = set(palabras)
print("Palabras únicas en la frase:")

frecuencia={}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print("Fracuencia de palabras:", frecuencia)

#6 NOTAS ALUMNOS
notas_alumnos ={}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno{i+1}: ")
    nota = input(f"Ingrese las nota de {nombre}: ")
    notas_tupla = tuple(int(nota) for nota in nota.split())
    notas_alumnos[nombre] = notas_tupla

for nombre, notas in notas_alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

#7 SETS DE APROBADOS
aprobados_parcial1 = {"Ana", "Luis", "Marcos", "Sofía", "Pedro"}
aprobados_parcial2 = {"Luis", "Marcos", "Lucía", "Pedro", "Valeria"}

ambos = aprobados_parcial1 & aprobados_parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = aprobados_parcial1 ^ aprobados_parcial2
print("Aprobaron solo uno de los dos parciales:", solo_uno)

al_menos_uno = aprobados_parcial1 | aprobados_parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

#8 STOCK DE PRODUCTOS
stock_productos = {"arroz": 20,"fideos": 15,"azúcar": 10,"aceite": 8}
producto = input("Ingrese el nombre del producto a consultar o agregar: ")

if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]}")
    agregar = input("¿Desea agregar unidades? (s/n): ")
    if agregar.lower() == "s":
        cantidad = int(input("¿Cuántas unidades desea agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
else:
    print(f"{producto} no existe en el stock.")
    agregar_nuevo = input("¿Desea agregar este producto al stock? (s/n): ")
    if agregar_nuevo.lower() == "s":
        cantidad = int(input("¿Cuántas unidades desea agregar?: "))
        stock_productos[producto] = cantidad
        print(f"{producto} agregado con {cantidad} unidades.")

print("Stock actual:", stock_productos)

#9 AGENDA DIA Y HORA
agenda_eventos = {}
for i in range(3):
    dia = input("Ingrese el día del evento: ")
    hora = input("Ingrese la hora del evento: ")
    evento = input("Ingrese el nombre del evento: ")
    agenda_eventos[(dia, hora)] = evento

print("Agenda de eventos:")
for clave, valor in agenda_eventos.items():
    print(f"Día: {clave[0]}, Hora: {clave[1]} -> Evento: {valor}")

#10 DICCIONARIO CAPITALES
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print("Diccionario invertido (capital: país):")
print(capitales_paises)