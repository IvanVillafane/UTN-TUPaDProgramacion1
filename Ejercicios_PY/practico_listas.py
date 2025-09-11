import random

# 1) 
notas = [8.5, 7.2, 9.1, 6.8, 8.9, 7.5, 9.3, 6.2, 8.7, 7.8]

print("1) Notas de estudiantes:")
for i, nota in enumerate(notas):
    print(f"Estudiante {i+1}: {nota}")

promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Nota más alta: {max(notas)}")
print(f"Nota más baja: {min(notas)}")
print()

# 2) 
productos = []
print("2) Ingrese 5 productos:")
for i in range(5):
    producto = input(f"Producto {i+1}: ")
    productos.append(producto)

productos_ordenados = sorted(productos)
print("Lista ordenada:")
for producto in productos_ordenados:
    print(f"- {producto}")

eliminar = input("¿Qué producto desea eliminar? ")
if eliminar in productos:
    productos.remove(eliminar)
    print("Lista actualizada:")
    for producto in productos:
        print(f"- {producto}")
else:
    print("Producto no encontrado")
print()

# 3)
numeros = [random.randint(1, 100) for _ in range(15)]
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("3) Números generados:")
for num in numeros:
    print(num, end=" ")
print(f"\nPares ({len(pares)}):")
for par in pares:
    print(par, end=" ")
print(f"\nImpares ({len(impares)}):")
for impar in impares:
    print(impar, end=" ")
print("\n")

# 4)
lista_repetidos = [1, 2, 2, 3, 4, 4, 5, 1, 6, 3]
sin_repetidos = []

for elemento in lista_repetidos:
    if elemento not in sin_repetidos:
        sin_repetidos.append(elemento)

print("4) Lista original con repetidos:")
for elem in lista_repetidos:
    print(elem, end=" ")
print("\nLista sin repetidos:")
for elem in sin_repetidos:
    print(elem, end=" ")
print("\n")

# 5) 
estudiantes = ["Ana", "Luis", "María", "Carlos", "Laura", "Pedro", "Sofia", "Diego"]

print("5) Estudiantes actuales:")
for i, estudiante in enumerate(estudiantes):
    print(f"{i+1}. {estudiante}")

opcion = input("¿Desea (a)gregar o (e)liminar un estudiante? ").lower()
if opcion == 'a':
    nuevo = input("Nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif opcion == 'e':
    eliminar = input("Nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)

print("Lista final:")
for i, estudiante in enumerate(estudiantes):
    print(f"{i+1}. {estudiante}")
print()

# 6) 
numeros_rotar = [10, 20, 30, 40, 50, 60, 70]
print("6) Lista original:")
for num in numeros_rotar:
    print(num, end=" ")

ultimo = numeros_rotar[-1]
numeros_rotar = [ultimo] + numeros_rotar[:-1]

print("\nLista rotada:")
for num in numeros_rotar:
    print(num, end=" ")
print("\n")

# 7) 
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = [
    [15, 25], [12, 28], [18, 30], [14, 26], [16, 29], [20, 32], [17, 27]
]

suma_min = 0
suma_max = 0
mayor_amplitud = 0
dia_mayor_amplitud = ""

print("7) Temperaturas de la semana:")
for i, dia in enumerate(dias):
    min_temp, max_temp = temperaturas[i]
    amplitud = max_temp - min_temp
    suma_min += min_temp
    suma_max += max_temp
    
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dia
    
    print(f"{dia}: {min_temp}°C - {max_temp}°C")

promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print(f"Promedio mínimas: {promedio_min:.2f}°C")
print(f"Promedio máximas: {promedio_max:.2f}°C")
print(f"Mayor amplitud térmica: {dia_mayor_amplitud} ({mayor_amplitud}°C)")
print()

# 8) 
estudiantes_notas = [
    [8.5, 7.2, 9.1],
    [6.8, 8.9, 7.5],
    [9.3, 6.2, 8.7],
    [7.8, 8.1, 7.4],
    [8.2, 9.0, 8.5]
]
materias = ["Matemáticas", "Historia", "Ciencias"]

print("8) Promedios por estudiante:")
for i, notas_est in enumerate(estudiantes_notas):
    promedio_est = sum(notas_est) / len(notas_est)
    print(f"Estudiante {i+1}: {promedio_est:.2f}")

print("Promedios por materia:")
for j, materia in enumerate(materias):
    suma_materia = sum(estudiante[j] for estudiante in estudiantes_notas)
    promedio_materia = suma_materia / len(estudiantes_notas)
    print(f"{materia}: {promedio_materia:.2f}")
print()

# 9) 
tablero = [["-", "-", "-"] for _ in range(3)]
jugador_actual = "X"

def mostrar_tablero():
    for fila in tablero:
        for celda in fila:
            print(celda, end=" ")
        print()

print("9) Ta-Te-Ti - Estado inicial:")
mostrar_tablero()


jugadas = [(0,0,"X"), (1,1,"O"), (0,1,"X"), (2,0,"O"), (0,2,"X")]
for fila, col, simbolo in jugadas:
    tablero[fila][col] = simbolo
    print(f"Jugador {simbolo} en posición ({fila},{col}):")
    mostrar_tablero()
    print()

# 10) 
productos_ventas = ["Producto A", "Producto B", "Producto C", "Producto D"]
ventas_matriz = [
    [120, 150, 180, 90, 200, 160, 140],
    [80, 110, 95, 130, 170, 120, 100],
    [200, 180, 220, 190, 210, 240, 180],
    [150, 140, 160, 170, 180, 155, 165]
]

print("10) Análisis de ventas:")
total_por_producto = []
for i, producto in enumerate(productos_ventas):
    total = sum(ventas_matriz[i])
    total_por_producto.append(total)
    print(f"{producto}: {total} unidades")

ventas_por_dia = []
for dia in range(7):
    total_dia = sum(ventas_matriz[producto][dia] for producto in range(4))
    ventas_por_dia.append(total_dia)

dia_mayor_venta = ventas_por_dia.index(max(ventas_por_dia))
print(f"Día con mayores ventas: Día {dia_mayor_venta + 1} ({max(ventas_por_dia)} unidades)")

producto_mas_vendido = total_por_producto.index(max(total_por_producto))
print(f"Producto más vendido: {productos_ventas[producto_mas_vendido]} ({max(total_por_producto)} unidades)")
