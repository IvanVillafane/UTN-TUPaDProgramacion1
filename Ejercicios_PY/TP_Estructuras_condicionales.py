# PRÁCTICO 3: ESTRUCTURAS CONDICIONALES

# ========================================
# EJERCICIO 1: Verificar mayoría de edad
# ========================================

print("=== EJERCICIO 1 ===")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")

# ========================================
# EJERCICIO 2: Nota aprobado/desaprobado
# ========================================

print("\n=== EJERCICIO 2 ===")
nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# ========================================
# EJERCICIO 3: Números pares
# ========================================

print("\n=== EJERCICIO 3 ===")
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# ========================================
# EJERCICIO 4: Categorías por edad
# ========================================

print("\n=== EJERCICIO 4 ===")
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# ========================================
# EJERCICIO 5: Validar contraseña
# ========================================

print("\n=== EJERCICIO 5 ===")
contrasena = input("Ingrese una contraseña: ")

if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# ========================================
# EJERCICIO 6: Análisis estadístico de sesgo
# ========================================

print("\n=== EJERCICIO 6 ===")
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

# ========================================
# EJERCICIO 7: Agregar exclamación si termina en vocal
# ========================================

print("\n=== EJERCICIO 7 ===")
frase = input("Ingrese una frase o palabra: ")

vocales = "aeiouAEIOU"

if frase[-1] in vocales:
    resultado = frase + "!"
else:
    resultado = frase

print(resultado)

# ========================================
# EJERCICIO 8: Transformar nombre según opción
# ========================================

print("\n=== EJERCICIO 8 ===")
nombre = input("Ingrese su nombre: ")
print("Seleccione una opción:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con primera letra mayúscula")

opcion = int(input("Ingrese su opción (1, 2 o 3): "))

if opcion == 1:
    resultado = nombre.upper()
elif opcion == 2:
    resultado = nombre.lower()
elif opcion == 3:
    resultado = nombre.title()
else:
    resultado = "Opción inválida"

print(resultado)

# ========================================
# EJERCICIO 9: Clasificación terremoto escala Richter
# ========================================

print("\n=== EJERCICIO 9 ===")
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# ========================================
# EJERCICIO 10: Estaciones del año por hemisferio
# ========================================

print("\n=== EJERCICIO 10 ===")
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = int(input("¿Qué mes del año es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Convertir fecha a un número para facilitar comparación
fecha_numero = mes * 100 + dia

# Definir rangos de fechas
# Dic 21 - Mar 20: 1221-1231 y 101-320
# Mar 21 - Jun 20: 321-620
# Jun 21 - Sep 20: 621-920
# Sep 21 - Dic 20: 921-1220

if (fecha_numero >= 1221 and fecha_numero <= 1231) or (fecha_numero >= 101 and fecha_numero <= 320):
    periodo = 1  # Dic 21 - Mar 20
elif fecha_numero >= 321 and fecha_numero <= 620:
    periodo = 2  # Mar 21 - Jun 20
elif fecha_numero >= 621 and fecha_numero <= 920:
    periodo = 3  # Jun 21 - Sep 20
else:
    periodo = 4  # Sep 21 - Dic 20

if hemisferio == 'N':
    if periodo == 1:
        estacion = "Invierno"
    elif periodo == 2:
        estacion = "Primavera"
    elif periodo == 3:
        estacion = "Verano"
    else:
        estacion = "Otoño"
else:  # hemisferio == 'S'
    if periodo == 1:
        estacion = "Verano"
    elif periodo == 2:
        estacion = "Otoño"
    elif periodo == 3:
        estacion = "Invierno"
    else:
        estacion = "Primavera"

print(f"Usted se encuentra en {estacion}")