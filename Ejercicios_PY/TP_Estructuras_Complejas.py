# TP 6: Estructuras de datos complejas

print("=" * 60)
print("EJERCICIO 1: Añadir frutas al diccionario")
print("=" * 60)

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(f"Diccionario inicial: {precios_frutas}")

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(f"Diccionario actualizado: {precios_frutas}")

print("\n" + "=" * 60)
print("EJERCICIO 2: Actualizar precios")
print("=" * 60)

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(f"Diccionario con precios actualizados: {precios_frutas}")

print("\n" + "=" * 60)
print("EJERCICIO 3: Lista de frutas sin precios")
print("=" * 60)

lista_frutas = list(precios_frutas.keys())
print(f"Lista de frutas: {lista_frutas}")

print("\n" + "=" * 60)
print("EJERCICIO 4: Agenda telefónica")
print("=" * 60)

agenda = {}

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    telefono = input(f"Ingrese el número de teléfono de {nombre}: ")
    agenda[nombre] = telefono

buscar = input("\nIngrese un nombre para buscar su número: ")
if buscar in agenda:
    print(f"El número de {buscar} es: {agenda[buscar]}")
else:
    print(f"El contacto {buscar} no existe en la agenda.")

print("\n" + "=" * 60)
print("EJERCICIO 5: Palabras únicas y conteo")
print("=" * 60)

frase = input("Ingrese una frase: ")
palabras = frase.split()

palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")

conteo_palabras = {}
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print(f"Conteo de palabras: {conteo_palabras}")

print("\n" + "=" * 60)
print("EJERCICIO 6: Promedio de notas de alumnos")
print("=" * 60)

alumnos_notas = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota1 = float(input(f"Ingrese la nota 1 de {nombre}: "))
    nota2 = float(input(f"Ingrese la nota 2 de {nombre}: "))
    nota3 = float(input(f"Ingrese la nota 3 de {nombre}: "))
    alumnos_notas[nombre] = (nota1, nota2, nota3)

print("\nPromedios de cada alumno:")
for alumno, notas in alumnos_notas.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {promedio:.2f}")

print("\n" + "=" * 60)
print("EJERCICIO 7: Sets de estudiantes - Parciales")
print("=" * 60)

parcial1 = {101, 102, 103, 104, 105}
parcial2 = {103, 104, 105, 106, 107}

print(f"Aprobaron Parcial 1: {parcial1}")
print(f"Aprobaron Parcial 2: {parcial2}")

ambos = parcial1 & parcial2
print(f"\nAprobaron ambos parciales: {ambos}")

solo_uno = parcial1 ^ parcial2
print(f"Aprobaron solo uno de los dos: {solo_uno}")

al_menos_uno = parcial1 | parcial2
print(f"Aprobaron al menos un parcial: {al_menos_uno}")

print("\n" + "=" * 60)
print("EJERCICIO 8: Gestión de stock de productos")
print("=" * 60)

stock_productos = {}

while True:
    print("\n--- Menú de Stock ---")
    print("1. Consultar stock")
    print("2. Agregar/Actualizar producto")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print(f"El producto {producto} no existe en el inventario.")
    
    elif opcion == '2':
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        
        if producto in stock_productos:
            stock_productos[producto] += cantidad
            print(f"Se agregaron {cantidad} unidades. Nuevo stock: {stock_productos[producto]}")
        else:
            stock_productos[producto] = cantidad
            print(f"Producto {producto} agregado con {cantidad} unidades.")
    
    elif opcion == '3':
        print("Saliendo del sistema de stock...")
        break
    
    else:
        print("Opción no válida.")

print("\n" + "=" * 60)
print("EJERCICIO 9: Agenda de eventos")
print("=" * 60)

agenda_eventos = {
    ('Lunes', '09:00'): 'Reunión de equipo',
    ('Martes', '14:00'): 'Presentación del proyecto',
    ('Miércoles', '10:00'): 'Revisión de código'
}

print("Agenda actual:")
for clave, evento in agenda_eventos.items():
    print(f"{clave}: {evento}")

dia = input("\nIngrese el día: ")
hora = input("Ingrese la hora (formato HH:MM): ")

if (dia, hora) in agenda_eventos:
    print(f"Evento: {agenda_eventos[(dia, hora)]}")
else:
    print("No hay ningún evento programado para ese día y hora.")

print("\n" + "=" * 60)
print("EJERCICIO 10: Invertir diccionario países-capitales")
print("=" * 60)

paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo',
    'Paraguay': 'Asunción'
}

print(f"Diccionario original (países → capitales):")
print(paises_capitales)

capitales_paises = {}
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print(f"\nDiccionario invertido (capitales → países):")
print(capitales_paises)

print("\n" + "=" * 60)
print("FIN DEL PRÁCTICO")
print("=" * 60)