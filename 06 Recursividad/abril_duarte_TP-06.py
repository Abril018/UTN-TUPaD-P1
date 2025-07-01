# 1 FACTORIAL DE UN NUMERO
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
numero = int(input("Ingrese un número: "))
for i in range(1, numero + 1):
    print(f"El factorial de {i} es {factorial(i)}")

# 2 VALOR SERIE FIBONACCI
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
posicion = int(input("Ingrese la posición de la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(posicion):
    print(fibonacci(i), end=" ")   

#3 CALCULAR POTENCIA DE UN NUMERO
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
base=int(input("Ingrese la base: "))
exponente=int(input("Ingrese el exponente: "))
resultado = potencia(base, exponente)
print(f"{base} elevado a {exponente} es {resultado}")

#4 ENTERO DECIMAL A BINARIO
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
numero=int(input("Ingrese un número entero positivo:"))
print(f"El número {numero} en binario es: {decimal_a_binario(numero)}")

#5 PALINDROMO
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")

#6 SUMA DIGITOS
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
numero=int(input("Ingrese un numero entero positivo "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es {resultado}") 

#7 PIRAMIDE DE BLOQUES
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
nivel = int(input("Ingrese el numero de bloques en el nivel mas bajo: "))
total=contar_bloques(nivel)
print(f"Se necesitan {total} bloques para construir la pirámide.")

#8 CONTAR DIGITOS
def contar_digitos(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digitos(numero // 10, digito)
        else:
            return contar_digitos(numero // 10, digito)

numero=int(input("Ingrese un numero entero positivo: "))
digito=int(input("Ingrese el digito a contar: "))
resultado = contar_digitos(numero, digito)
print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")   