# Ejercicios de Estructuras Secuenciales en Python
# Tecnicatura Universitaria en Programación a Distancia

import math

def separador(titulo):
    """Función auxiliar para separar ejercicios visualmente"""
    print("\n" + "="*50)
    print(f"EJERCICIO {titulo}")
    print("="*50)

# Ejercicio 1: Hola Mundo
separador("1")
print("Hola Mundo!")

# Ejercicio 2: Saludo personalizado
separador("2")
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3: Información personal completa
separador("3")
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
lugar_residencia = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

# Ejercicio 4: Área y perímetro de un círculo
separador("4")
radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")

# Ejercicio 5: Conversión de segundos a horas
separador("5")
segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

# Ejercicio 6: Tabla de multiplicar
separador("6")
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Ejercicio 7: Operaciones matemáticas básicas
separador("7")
num1 = int(input("Ingresa el primer número entero (distinto de 0): "))
num2 = int(input("Ingresa el segundo número entero (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} x {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division:.2f}")

# Ejercicio 8: Índice de Masa Corporal (IMC)
separador("8")
altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

# Ejercicio 9: Conversión de Celsius a Fahrenheit
separador("9")
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# Ejercicio 10: Promedio de tres números
separador("10")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")

print("\n" + "="*50)
print("TODOS LOS EJERCICIOS COMPLETADOS")
print("="*50)