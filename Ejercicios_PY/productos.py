
def crear_archivo_inicial():
    """Actividad 1: Crear archivo inicial con productos"""
    try:
        with open('productos.txt', 'w', encoding='utf-8') as archivo:
            archivo.write("Lapicera,120.5,30\n")
            archivo.write("Cuaderno,250.0,15\n")
            archivo.write("Mochila,3500.0,8\n")
        print("✓ Archivo productos.txt creado exitosamente\n")
    except Exception as e:
        print(f"Error al crear archivo: {e}")


def leer_y_mostrar_productos():
    """Actividad 2: Leer y mostrar productos"""
    print("=== PRODUCTOS DISPONIBLES ===")
    try:
        with open('productos.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()  
                if linea: 
                    datos = linea.split(",")
                    nombre = datos[0]
                    precio = datos[1]
                    cantidad = datos[2]
                    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
        print()
    except FileNotFoundError:
        print("El archivo productos.txt no existe. Creándolo...\n")
        crear_archivo_inicial()
        leer_y_mostrar_productos()
    except Exception as e:
        print(f"Error al leer archivo: {e}")


def agregar_producto():
    """Actividad 3: Agregar productos desde teclado"""
    print("=== AGREGAR NUEVO PRODUCTO ===")
    nombre = input("Ingrese el nombre del producto: ").strip()
    
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            if precio < 0:
                print("El precio no puede ser negativo. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número válido para el precio.")
    
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número entero válido para la cantidad.")
    
    try:
        with open('productos.txt', 'a', encoding='utf-8') as archivo:
            archivo.write(f"{nombre},{precio},{cantidad}\n")
        print(f"✓ Producto '{nombre}' agregado exitosamente\n")
    except Exception as e:
        print(f"Error al agregar producto: {e}")


def cargar_productos_en_lista():
    """Actividad 4: Cargar productos en una lista de diccionarios"""
    productos = []
    try:
        with open('productos.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    datos = linea.split(",")
                    producto = {
                        'nombre': datos[0],
                        'precio': float(datos[1]),
                        'cantidad': int(datos[2])
                    }
                    productos.append(producto)
        return productos
    except FileNotFoundError:
        print("El archivo no existe.")
        return []
    except Exception as e:
        print(f"Error al cargar productos: {e}")
        return []


def buscar_producto(productos):
    """Actividad 5: Buscar producto por nombre"""
    print("=== BUSCAR PRODUCTO ===")
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
    
    encontrado = False
    for producto in productos:
        if producto['nombre'].lower() == nombre_buscar.lower():
            print("\n✓ Producto encontrado:")
            print(f"  Nombre: {producto['nombre']}")
            print(f"  Precio: ${producto['precio']}")
            print(f"  Cantidad: {producto['cantidad']}\n")
            encontrado = True
            break
    
    if not encontrado:
        print(f"✗ Error: El producto '{nombre_buscar}' no existe en el inventario.\n")


def guardar_productos_actualizados(productos):
    """Actividad 6: Guardar los productos actualizados"""
    try:
        with open('productos.txt', 'w', encoding='utf-8') as archivo:
            for producto in productos:
                linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                archivo.write(linea)
        print("✓ Archivo actualizado correctamente\n")
    except Exception as e:
        print(f"Error al guardar productos: {e}")


def mostrar_productos_desde_lista(productos):
    """Mostrar productos desde la lista de diccionarios"""
    print("=== LISTA DE PRODUCTOS ===")
    if not productos:
        print("No hay productos en el inventario.\n")
        return
    
    for i, producto in enumerate(productos, 1):
        print(f"{i}. Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
    print()


def menu_principal():
    """Menú principal del programa"""
    print("="*50)
    print("  SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("="*50)
    
    try:
        with open('productos.txt', 'r', encoding='utf-8') as f:
            pass
    except FileNotFoundError:
        crear_archivo_inicial()
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Mostrar productos (lectura simple)")
        print("2. Agregar nuevo producto")
        print("3. Mostrar productos (desde lista)")
        print("4. Buscar producto por nombre")
        print("5. Guardar cambios")
        print("6. Ejecutar todas las actividades en secuencia")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            leer_y_mostrar_productos()
        
        elif opcion == "2":
            agregar_producto()
        
        elif opcion == "3":
            productos = cargar_productos_en_lista()
            mostrar_productos_desde_lista(productos)
        
        elif opcion == "4":
            productos = cargar_productos_en_lista()
            buscar_producto(productos)
        
        elif opcion == "5":
            productos = cargar_productos_en_lista()
            guardar_productos_actualizados(productos)
        
        elif opcion == "6":
            print("\n" + "="*50)
            print("EJECUTANDO TODAS LAS ACTIVIDADES")
            print("="*50 + "\n")
            
            # Act 1
            print(">>> Actividad 1: Crear archivo inicial")
            crear_archivo_inicial()
            
            # Act 2
            print(">>> Actividad 2: Leer y mostrar productos")
            leer_y_mostrar_productos()
            
            # Act 3
            print(">>> Actividad 3: Agregar producto desde teclado")
            agregar_producto()
            
            # Act 4
            print(">>> Actividad 4: Cargar productos en lista")
            productos = cargar_productos_en_lista()
            print(f"✓ Se cargaron {len(productos)} productos en memoria\n")
            
            # Act 5
            print(">>> Actividad 5: Buscar producto")
            buscar_producto(productos)
            
            # Act 6
            print(">>> Actividad 6: Guardar productos actualizados")
            productos = cargar_productos_en_lista()  
            guardar_productos_actualizados(productos)
            
            print("="*50)
            print("TODAS LAS ACTIVIDADES COMPLETADAS")
            print("="*50 + "\n")
        
        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        
        else:
            print("\n✗ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu_principal()