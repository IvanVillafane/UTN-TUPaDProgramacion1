
"""
Práctico 4: Estructuras Repetitivas
UTN
"""

import random


def actividad_1():
    """
    Actividad 1
    """
    print("=== ACTIVIDAD 1: Números del 0 al 100 ===")
    
    for i in range(101):  
        print(i)
    
    print("Fin de la actividad 1\n")


def actividad_2():
    """
    Actividad 2: 
    """
    print("=== ACTIVIDAD 2: Contar dígitos ===")
    
    try:
        numero = int(input("Ingrese un número entero: "))
        
        contador = 0
        numero_temporal = abs(numero) 
        
        if numero_temporal == 0:
            contador = 1
        else:
            while numero_temporal > 0:
                numero_temporal //= 10
                contador += 1
        
        print(f"El número {numero} tiene {contador} dígitos")
        
    except ValueError:
        print("Error: Debe ingresar un número entero válido")
    
    print("Fin de la actividad 2\n")


def actividad_3():
    """
    Actividad 3: 
    """
    print("=== ACTIVIDAD 3: Suma entre valores ===")
    
    try:
        valor1 = int(input("Ingrese el primer valor: "))
        valor2 = int(input("Ingrese el segundo valor: "))
        
        menor = min(valor1, valor2)
        mayor = max(valor1, valor2)
        
        suma = 0
        for i in range(menor + 1, mayor):
            suma += i
        
        if menor + 1 >= mayor:
            print(f"No hay números entre {menor} y {mayor} para sumar")
        else:
            print(f"La suma de los números entre {menor} y {mayor} (sin incluirlos) es: {suma}")
        
    except ValueError:
        print("Error: Debe ingresar números enteros válidos")
    
    print("Fin de la actividad 3\n")


def actividad_4():
    """
    Actividad 4: 
    """
    print("=== ACTIVIDAD 4: Suma secuencial ===")
    
    suma = 0
    print("Ingrese números enteros (0 para terminar):")
    
    while True:
        try:
            numero = int(input("Número: "))
            if numero == 0:
                break
            suma += numero
            print(f"Suma actual: {suma}")
        except ValueError:
            print("Error: Debe ingresar un número entero válido")
    
    print(f"Suma total acumulada: {suma}")
    print("Fin de la actividad 4\n")


def actividad_5():
    """
    Actividad 5: 
    """
    print("=== ACTIVIDAD 5: Juego de adivinanza ===")
    
    numero_secreto = random.randint(0, 9)
    intentos = 0
    
    print("¡Bienvenido al juego de adivinanza!")
    print("Adivina el número entre 0 y 9")
    
    while True:
        try:
            intentos += 1
            numero_usuario = int(input(f"Intento {intentos}: Ingrese su número: "))
            
            if numero_usuario < numero_secreto:
                print("El número es mayor")
            elif numero_usuario > numero_secreto:
                print("El número es menor")
            else:
                print("¡Felicitaciones! Adivinaste el número")
                break
                
        except ValueError:
            print("Error: Debe ingresar un número entero entre 0 y 9")
            intentos -= 1 
    
    print(f"Necesitaste {intentos} intentos para adivinar el número {numero_secreto}")
    print("Fin de la actividad 5\n")


def actividad_6():
    """
    Actividad 6: 
    """
    print("=== ACTIVIDAD 6: Números pares decreciente ===")
    
    print("Números pares del 100 al 0 (orden decreciente):")
    
    for i in range(100, -1, -2):  
        print(i)
    
    print("Fin de la actividad 6\n")


def actividad_7():
    """
    Actividad 7: 
    """
    print("=== ACTIVIDAD 7: Suma desde 0 hasta N ===")
    
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero > 0:
                break
            else:
                print("Error: Debe ingresar un número positivo")
        except ValueError:
            print("Error: Debe ingresar un número entero válido")
    
    suma = sum(range(numero + 1)) 
    
    print(f"La suma de los números desde 0 hasta {numero} es: {suma}")
    print("Fin de la actividad 7\n")


def actividad_8():
    """
    Actividad 8: 
    """
    print("=== ACTIVIDAD 8: Análisis de números ===")
    
    CANTIDAD = 10  
    
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    ceros = 0
    
    print(f"Ingrese {CANTIDAD} números enteros:")
    
    for i in range(1, CANTIDAD + 1):
        while True:
            try:
                numero = int(input(f"Número {i}: "))
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido")
        
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1
    
    print("\n--- RESULTADOS ---")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Números positivos: {positivos}")
    print(f"Números negativos: {negativos}")
    print(f"Números cero: {ceros}")
    print("Fin de la actividad 8\n")


def actividad_9():
    """
    Actividad 9: 
    """
    print("=== ACTIVIDAD 9: Calcular media ===")
    
    CANTIDAD = 10  
    
    suma = 0
    print(f"Ingrese {CANTIDAD} números enteros:")
    
    for i in range(1, CANTIDAD + 1):
        while True:
            try:
                numero = int(input(f"Número {i}: "))
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido")
        
        suma += numero
    
    media = suma / CANTIDAD
    
    print("\n--- RESULTADOS ---")
    print(f"Suma total: {suma}")
    print(f"Cantidad de números: {CANTIDAD}")
    print(f"Media: {media:.2f}")
    print("Fin de la actividad 9\n")


def actividad_10():
    """
    Actividad 10: 
    """
    print("=== ACTIVIDAD 10: Invertir dígitos ===")
    
    try:
        numero = int(input("Ingrese un número entero: "))
        numero_original = numero
        
        es_negativo = numero < 0
        if es_negativo:
            numero = abs(numero)  
        
        numero_invertido = 0
        
        if numero == 0:
            numero_invertido = 0
        else:
            while numero > 0:
                digito = numero % 10                    
                numero_invertido = numero_invertido * 10 + digito  
                numero //= 10                          
        
        if es_negativo:
            numero_invertido = -numero_invertido
        
        print(f"Número original: {numero_original}")
        print(f"Número invertido: {numero_invertido}")
        
    except ValueError:
        print("Error: Debe ingresar un número entero válido")
    
    print("Fin de la actividad 10\n")


def menu_principal():
    """
    Menú principal para ejecutar las actividades
    """
    actividades = {
        '1': actividad_1,
        '2': actividad_2,
        '3': actividad_3,
        '4': actividad_4,
        '5': actividad_5,
        '6': actividad_6,
        '7': actividad_7,
        '8': actividad_8,
        '9': actividad_9,
        '10': actividad_10
    }
    
    while True:
        print("=" * 50)
        print("PRÁCTICO 4: ESTRUCTURAS REPETITIVAS")
        print("=" * 50)
        print("1.  Números del 0 al 100")
        print("2.  Contar dígitos de un número")
        print("3.  Suma entre dos valores (excluyéndolos)")
        print("4.  Suma secuencial hasta encontrar 0")
        print("5.  Juego de adivinanza")
        print("6.  Números pares decreciente")
        print("7.  Suma desde 0 hasta N")
        print("8.  Análisis de números enteros")
        print("9.  Calcular media de números")
        print("10. Invertir orden de dígitos")
        print("0.  Salir")
        print("=" * 50)
        
        opcion = input("Seleccione una actividad (0-10): ").strip()
        
        if opcion == '0':
            print("¡Gracias por usar el programa =)!")
            break
        elif opcion in actividades:
            print()
            actividades[opcion]()
            input("Presione Enter para continuar...")
        else:
            print("Opción inválida. Por favor, seleccione un número del 0 al 10.")
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    """
    Punto de entrada principal del programa
    """
    menu_principal()
