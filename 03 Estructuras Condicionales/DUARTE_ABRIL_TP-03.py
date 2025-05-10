#EJERCICIO N°1 "MAYOR EDAD"
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#EJERCICIO N°2 "APROBADO O DESPROBADO"
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#EJERCICIO N°3 "NUMERO PAR O IMPAR"
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#EJERCICIO N°4 "EDADES"
edad= int(input("Ingrese su edad: "))
if edad >=0 and edad <=12:
    print("Es un niño")
elif edad >= 13 and edad <= 17:
    print("Es un adolescente")
elif edad >= 18 and edad <= 30:
    print("Es un adulto/joven")
else :
    print("Es un adulto")

#EJERCICIO N°5 "CONTRASEÑA"
Contraseña= input("Ingrese su contraseña: ")
if len(Contraseña) >= 8 and len(Contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña entre 8 y 14 caracteres")

#EJERCICIO N°6 "STATISTICS"
import random
from statistics import mean, median, mode
numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print("Lista de números aleatorios:", numeros_aleatorios)
print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)
if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "No hay sesgo o datos no siguen la tendencia esperada"
print("Sesgo:", sesgo)

#EJERCICIO N°7 "VOCAL"
palabra= input("Ingrese una palabra: ")
if palabra[-1].lower() in "aeiou":
    print(palabra +"!")
else:
    print(palabra)

#EJERCICIO N°8 "NOMBRE EN 1,2,3"
nombre= input("Ingrese su nombre: ")
print("Seleccione una opcion:")
print("1. Mostrar nombre en mayúsculas")
print("2. Mostrar nombre en minúsculas")
print("3. Mostrar nombre con la primera letra en mayúscula")
opcion= int(input("Ingrese su opción: "))
if opcion ==1:
    print(nombre.upper())
elif opcion ==2:
    print(nombre.lower())
elif opcion ==3:
    print(nombre.title())
else:
    print("Opción no válida. Por favor, ingrse 1, 2 o 3.")

#EJERCICIO N° 9 "TERREMOTO"
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3.0:
    print("Muy leve")
elif 3.0 <= magnitud < 4.0:
    print("Leve")
elif 4.0 <= magnitud < 5.0:
    print("Moderado")
elif 5.0 <= magnitud < 6.0:
    print("Fuerte")
elif 6.0 <= magnitud < 7.0:
    print("Muy fuerte")
elif 7.0 <= magnitud < 8.0:
    print("Extremo")

#EJERCICIO N°10 "ESTACIONES DEL AÑO"
mes = int(input("Ingrese el número del mes (1-12): "))
hemisferio= input("Ingrese el hemisferio (N/S): ").upper()
if hemisferio == "S":
    #estaciones en el hemisferio sur
    if mes == 12 or mes == 1 or mes == 2:
        print("Verano")
    elif mes == 3 or mes == 4 or mes == 5:
        print("Otoño")
    elif mes == 6 or mes == 7 or mes == 8:
        print("Invierno")
    elif mes == 9 or mes == 10 or mes == 11:
        print("Primavera")
if hemisferio == "N":
    #estaciones en el hemisferio norte
    if mes == 12 or mes == 1 or mes == 2:
        print("Invierno")
    elif mes == 3 or mes == 4 or mes == 5:
        print("Primavera")
    elif mes == 6 or mes == 7 or mes == 8:
        print("Verano")
    elif mes == 9 or mes == 10 or mes == 11:
        print("Otoño")

