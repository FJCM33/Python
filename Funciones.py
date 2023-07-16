'''
Javier Cerrudo
Prework Python Funciones
'''

# 1. Ejercicio: Define una función que tome dos números y retorne su suma.
def sumar_numeros(num1, num2):
    suma = num1 + num2
    return suma

resultado = sumar_numeros(5, 3)
print(resultado)

# 2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
def calcular_factorial(numero):
    factorial = 1

    # Verificar si el número es negativo
    if numero < 0:
        return "El factorial no está definido para números negativos."
    
    # Calcular el factorial
    for i in range(1, numero + 1):
        factorial *= i
    
    return factorial

resultado = calcular_factorial(5)
print(resultado)

# 3. Ejercicio: Define una función que tome un número y determine si es primo.
def es_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    
    return True

numero = float(input("Ingrese un número: "))
if es_primo(numero):
    print(numero, "es primo.")
else:
    print(numero, "no es primo.")

# 4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
def sumar_numeros(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        suma += numero
    return suma

numeros = [2, 4, 6, 8, 10]
resultado = sumar_numeros(numeros)
print(resultado)

# 5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
def invertir_cadena(cadena):
    cadena_invertida = cadena[::-1]
    return cadena_invertida

texto = "Hola, mundo"
texto_invertido = invertir_cadena(texto)
print(texto_invertido)
