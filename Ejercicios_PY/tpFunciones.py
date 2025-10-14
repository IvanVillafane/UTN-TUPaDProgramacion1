import math

def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def segundos_a_horas(segundos):
    return segundos / 3600

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# PROGRAMA 
def main():
    # Ej 1
    print("=== EJERCICIO 1 ===")
    imprimir_hola_mundo()
    print()
    
    # Ej 2
    print("=== EJERCICIO 2 ===")
    nombre = input("Ingresa tu nombre: ")
    print(saludar_usuario(nombre))
    print()
    
    # Ej 3
    print("=== EJERCICIO 3 ===")
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    residencia = input("Ingresa tu residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    print()
    
    # Ej 4
    print("=== EJERCICIO 4 ===")
    radio = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")
    print()
    
    # Ej 5
    print("=== EJERCICIO 5 ===")
    segundos = float(input("Ingresa la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")
    print()
    
    # Ej 6
    print("=== EJERCICIO 6 ===")
    numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)
    print()
    
    # Ej 7
    print("=== EJERCICIO 7 ===")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    suma, resta, multiplicacion, division = operaciones_basicas(a, b)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")
    print()
    
    # Ej 8
    print("=== EJERCICIO 8 ===")
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")
    print()
    
    # Ej 9
    print("=== EJERCICIO 9 ===")
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
    print()
    
    # Ej 10
    print("=== EJERCICIO 10 ===")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    c = float(input("Ingresa el tercer número: "))
    promedio = calcular_promedio(a, b, c)
    print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")

if __name__ == "__main__":
    main()