# EJERCICIO 1 "RANGO O A 100"
for numero in range(101):
    print(numero)

#EJERCICIO 2 "CANTIDAD DIGITOS"
numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print(f"El número ingresado tiene {cantidad_digitos} dígitos.")

#EJERCICIO 3 "SUMA ENTRE DOS VALORES"
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
inicio = min(valor1, valor2) + 1
fin = max(valor1, valor2)
suma = sum(range(inicio, fin))
print(f"La suma de los números entre {valor1} y {valor2}, excluyéndolos, es: {suma}")

#EJERCICIO 4 "SUMA ACUMULADA"
total=0
while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    total += numero

print(f"El total acumulado es: {total}")

# EJERCICIO 5 "ADIVINAR UN NUMERO"
import random

numero_aleatorio = random.randint(0, 9)
intentos = 0

print("¡Adivina el número entre 0 y 9!")

while True:
    intento = int(input("Ingresa tu número: "))
    intentos += 1
    if intento == numero_aleatorio:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    elif intento < numero_aleatorio:
        print("El número es mayor. Intenta nuevamente.")
    else:
        print("El número es menor. Intenta nuevamente.")

# EJERCICIO 7 "SUMA ENTRE 0 Y UN NUMERO POSITIVO"
numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("El número ingresado no es positivo.")
else:
    suma = sum(range(numero + 1))
    print(f"La suma de todos los números entre 0 y {numero} es: {suma}")

# EJERCICIO 8 "ANALISIS DE 100 NUMEROS"
cantidad_pares = 0
cantidad_impares = 0
cantidad_positivos = 0
cantidad_negativos = 0
for _ in range(100):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1
    if numero > 0:
        cantidad_positivos += 1
    elif numero < 0:
        cantidad_negativos += 1

print(f"Cantidad de números pares: {cantidad_pares}")
print(f"Cantidad de números impares: {cantidad_impares}")
print(f"Cantidad de números positivos: {cantidad_positivos}")
print(f"Cantidad de números negativos: {cantidad_negativos}")

# EJERCICIO 9 "MEDIA DE 100 NUMEROS"
numeros = []
for _ in range(100):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

media = sum(numeros) / len(numeros)
print(f"La media de los números ingresados es: {media}")

# EJERCICIO 10 "INVERTIR DIGITOS DE UN NUMERO"
numero = int(input("Ingrese un número entero: "))
numero_invertido = int(str(abs(numero))[::-1])  # Invierte los dígitos
if numero < 0:
    numero_invertido = -numero_invertido  # Mantiene el signo negativo si aplica
print(f"El número invertido es: {numero_invertido}")
