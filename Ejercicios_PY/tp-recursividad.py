# TP - RECURSIVIDAD

# 1) Factorial 
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def factoriales_hasta(n: int):
    print("\n--- FACTORIALES ---")
    for i in range(1, n + 1):
        print(f"{i}! = {factorial(i)}")


# 2) Serie de Fibonacci 
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def serie_fibonacci_hasta(n: int):
    print("\n--- SERIE DE FIBONACCI ---")
    for i in range(n):
        print(f"F({i}) = {fibonacci(i)}")


# 3) Potencia  
def potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


# 4) Conversión 
def decimal_a_binario(n: int) -> str:
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)


# 5) Palíndromo 
def es_palindromo(palabra: str) -> bool:
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


# 6) Suma 
def suma_digitos(n: int) -> int:
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)


# 7) Bloques 
def contar_bloques(n: int) -> int:
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)


# 8) Ocurrencias 
def contar_digito(numero: int, digito: int) -> int:
    if numero == 0:
        return 0
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


if __name__ == "__main__":
    print("===== RECURSIVIDAD =====")
    print("Seleccioná un ejercicio del 1 al 8:")
    print("""
1. Factorial de todos los números hasta N
2. Serie de Fibonacci hasta N
3. Potencia base^exponente
4. Convertir número decimal a binario
5. Verificar si una palabra es palíndromo
6. Sumar los dígitos de un número
7. Calcular bloques de una pirámide
8. Contar cuántas veces aparece un dígito en un número
""")

    opcion = int(input("Elegí una opción: "))

    if opcion == 1:
        n = int(input("Ingresá un número: "))
        factoriales_hasta(n)
    elif opcion == 2:
        n = int(input("Ingresá hasta qué posición querés la serie: "))
        serie_fibonacci_hasta(n)
    elif opcion == 3:
        base = int(input("Base: "))
        exp = int(input("Exponente: "))
        print(f"{base}^{exp} = {potencia(base, exp)}")
    elif opcion == 4:
        n = int(input("Ingresá un número decimal: "))
        print(f"Binario: {decimal_a_binario(n)}")
    elif opcion == 5:
        palabra = input("Ingresá una palabra (sin espacios ni tildes): ").lower()
        print("Es palíndromo" if es_palindromo(palabra) else "No es palíndromo")
    elif opcion == 6:
        n = int(input("Ingresá un número entero positivo: "))
        print(f"Suma de dígitos: {suma_digitos(n)}")
    elif opcion == 7:
        n = int(input("Bloques en el nivel más bajo: "))
        print(f"Total de bloques: {contar_bloques(n)}")
    elif opcion == 8:
        numero = int(input("Número: "))
        dig = int(input("Dígito a contar (0-9): "))
        print(f"El dígito {dig} aparece {contar_digito(numero, dig)} veces.")
    else:
        print("Opción inválida.")
