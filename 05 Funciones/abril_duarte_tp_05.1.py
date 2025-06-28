#1 "HOLA MUNDO"
def imprimir_hola_mundo():
    print("HOLA MUNDO!")

imprimir_hola_mundo

#2 SALUDAR A UN NOMBRE
def saludar_usuario(nombre):
    return f"Hola, {nombre}!"

nombre=input("Ingresa tu nombre: ")
saludo=saludar_usuario(nombre)
print(saludo)

#3 INFORMACION PERSONAL
def informacion_personal(nombre, apellido, edad, residencia):
    print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#4 AREA Y PERIMETRO DEL CIRCULO
def calcular_area_circulo(radio):
    pi = 3.14159
    area = pi * (radio ** 2)
    return area

radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
print(f"El área del círculo es: {area}")

def calcular_perimetro_circulo(radio):
    pi = 3.14159
    perimetro = 2 * pi * radio
    return perimetro
perimetro = calcular_perimetro_circulo(radio)
print(f"El perímetro del círculo es: {perimetro}")

print("Ingrese el radio del círculo:")
calcular_area_circulo
calcular_perimetro_circulo

#5 DE SEGUNDOS A HORAS
def segundos_a_horas(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return horas, minutos, segundos_restantes

segundos= int(input("Ingrese la cantidad de segundos: "))
horas, minutos, segundos_restantes = segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")

#6 TABLA DE MULTIPLICAR
def tabla_multiplicar(numero):
    for i in range (1, 11):
        resultado =numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#7 OPERACION BASICA
def operaciones_basicas (a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    
    return suma, resta, multiplicacion, division
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

#8 CALCULAR IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print (f"su IMC es: {imc:.2f}")

#9 CELSIUS A FAHRENHEIT
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")

#10 CALCULAR PROMEDIO
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio 
a= float(input("Ingrese el primer número: "))
b= float(input("Ingrese el segundo número: "))  
c= float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")   

