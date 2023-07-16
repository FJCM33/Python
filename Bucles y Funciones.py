'''
Javier Cerrudo
Prework Python Bucles y Funciones
'''

# 1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.
def fibonacci(n):
    numero_anterior = 0
    numero_actual = 1

    for _ in range(n):
        print(numero_actual)
        siguiente_numero = numero_anterior + numero_actual
        numero_anterior = numero_actual
        numero_actual = siguiente_numero

# llamar a la función
print('Ejercicio 1')
fibonacci(10)  

# 2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.
def obtener_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores
# llamar a la función
divisores = obtener_divisores(12)
print('Ejercicio 2')
print(divisores)

# 3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.
def obtener_elementos_unicos(lista):
    elementos_unicos = []
    for elemento in lista:
        if elemento not in elementos_unicos:
            elementos_unicos.append(elemento)
    return elementos_unicos
# llamar a la función
lista = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6]
elementos_unicos = obtener_elementos_unicos(lista)
print('Ejercicio 3')
print(elementos_unicos)

# 4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.
def sumar_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

resultado = sumar_digitos(12345)
print('Ejercicio 4')
print(resultado)

# 5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.
def contar_vocales(cadena):
    contador = 0
    vocales = "aeiouAEIOU"
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador
# llamar a la función
resultado = contar_vocales("Esto es una cadena de caracteres para contar")
print('Ejercicio 5')
print(resultado)

# 6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.

def obtener_primeros_n_elementos(lista, n):
    return lista[:n]
# llamar a la función
mi_lista = [1, 2, 3, 4, 5]
primeros_elementos = obtener_primeros_n_elementos(mi_lista, 3)
print('Ejercicio 6')
print(primeros_elementos)

# 7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
def contar_letras_mayusculas_minusculas(cadena):
    mayusculas = 0
    minusculas = 0

    for caracter in cadena:
        if caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1

    return mayusculas, minusculas
# llamar a la función
resultado = contar_letras_mayusculas_minusculas("Hola Mundo")
print('Ejercicio 7')
print("Mayúsculas:", resultado[0])
print("Minúsculas:", resultado[1])

# 8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
def es_numero_perfecto(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma == n
# llamar a la función
resultado = es_numero_perfecto(6)
print('Ejercicio 8')
print(resultado)

# 9. Ejercicio: Define una función que reciba un número y retorne su representación en binario.
def a_binario(n):
    return bin(n)[2:]
# llamar a la función
print('Ejercicio 9')
print(a_binario(10)) 

# 10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
def interseccion(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    return list(conjunto1 & conjunto2)
# llamar a la función
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
print('Ejercicio 10')
print(interseccion(lista1, lista2))  # Output: [3, 4]

# 11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
def es_palindromo(cadena):
    cadena = cadena.lower()  # convertir a minúsculas
    cadena = cadena.replace(" ", "")  # eliminar espacios
    return cadena == cadena[::-1]
# llamar a la función
print('Ejercicio 11')
print(es_palindromo("Anita lava la tina"))  # Output: True

# 12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.
print('Ejercicio 12')
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.

def ordenar_lista(lista):
    return sorted(lista)
# llamar a la función
lista_desordenada = [14, 13, 10, 11, 12]
lista_ordenada = ordenar_lista(lista_desordenada)
print('Ejercicio 13')
print(lista_ordenada)  # Output: [10, 11, 12, 13, 14]

# 14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
def palabras_mas_largas(lista, n):
    resultado = [palabra for palabra in lista if len(palabra) > n]
    return resultado
# llamar a la función
lista = ["perro", "cazadores", "despertador"]
print('Ejercicio 14')
print(palabras_mas_largas(lista, 6))  # Output: ["cazadores", "despertador"]

# 15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib
# llamar a la función
print('Ejercicio 15/1')
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# Codigo que nos facilitaron en la clase en directo pera esto, utilizando iteracion

maximo = 10

def fibonacci(resultado):
    if(resultado <=1):
        return resultado
    else:
        return fibonacci(resultado -1) + fibonacci(resultado -2)

def fibonacci(n):
    a, b, = 0, 1
    for i in range(n):
        print(a, end='\n') # '\t'
        a, b = b, a + b

print('Ejercicio 15/2')
# llamar a la función
for iterador in range(maximo):
    print(fibonacci(iterador))

print('segunda forma')
print('Ejercicio 15/3')
fibonacci(10)
# duda, ¿porque la segunda funcion devuelve un numero mas que la primera?

# 16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.
print('Ejercicio 16')
def maximo(lista):
    return max(lista)
# llamar a la función
lista = [5, 3, 1, 4, 2]
max_num = maximo(lista)
print('Ejercicio 16')
print(max_num)  # Output: 5

# 17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
def suma_cubos_digitos(n):
    suma = 0
    while n:
        n, digito = divmod(n, 10)
        suma += digito ** 3
    return suma
# llamar a la función
print('Ejercicio 17')
print(suma_cubos_digitos(123))

# 18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
def segundo_maximo(lista):
    if len(lista) < 2:
        return None
    lista_ordenada = sorted(set(lista), reverse=True)
    if len(lista_ordenada) < 2:
        return None
    return lista_ordenada[1]

# llamar a la función
lista = [5, 3, 1, 4, 2]
segundo_max = segundo_maximo(lista)
print('Ejercicio 18')
print(segundo_max)  # Output: 4

# 19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
def tienen_comun(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    interseccion = conjunto1 & conjunto2
    return len(interseccion) > 0
# llamar a la función
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
lista3 = [5, 6, 7, 8]
print('Ejercicio 19')
print(tienen_comun(lista1, lista2))  # Output: True
print(tienen_comun(lista1, lista3))  # Output: False

# 20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
def invertir_lista(lista):
    return lista[::-1] # [::-1] crea una nueva lista en orden inverso a la original
# llamar a la función
lista = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista(lista)
print('Ejercicio 20')
print(lista_invertida)

# 21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
def contar_digitos_letras(cadena):
    num_digitos = sum(caracter.isdigit() for caracter in cadena) #cuenta los digitos
    num_letras = sum(caracter.isalpha() for caracter in cadena) #cuenta las letras
    return num_digitos, num_letras
# llamar a la función
cadena = "123aertybc4sdfsdf56d458ef"
num_digitos, num_letras = contar_digitos_letras(cadena)
print('Ejercicio 21')
print("Número de dígitos:", num_digitos)
print("Número de letras:", num_letras)

# 22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números
def suma_acumulada(lista):
    return sum(lista)
# llamar a la función
lista = [1, 2, 3, 4, 5]
suma = suma_acumulada(lista)
print('Ejercicio 22')
print(suma)  # Output: 15

# 23. Ejercicio: Define una función que encuentre el elemento más común en una lista.
from collections import Counter

def elemento_mas_comun(lista):
    conteo = Counter(lista)
    return conteo.most_common(1)[0][0]
# llamar a la función
lista = [1, 2, 3, 1, 2, 1, 3, 3, 3, 3, 10, 12, 13 ,15, 28]
mas_comun = elemento_mas_comun(lista)
print('Ejercicio 23')
print(mas_comun)

# 24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
def tabla_multiplicar(n):
    return {i: n * i for i in range(1, 11)}
# llamar a la función
tabla = tabla_multiplicar(5)
print('Ejercicio 24')
print(tabla)

# 25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
from collections import Counter

def contar_caracteres(cadena):
    return Counter(cadena)

# llamar a la función
cadena = "Hola, mundo!"
conteo = contar_caracteres(cadena)
print('Ejercicio 25')
print(conteo)  
# Output: Counter({'o': 2, ' ': 1, 'H': 1, 'l': 1, 'a': 1, ',': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1, '!': 1})

# 26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
def elementos_no_comunes(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    no_comunes = list(conjunto1.symmetric_difference(conjunto2))
    return no_comunes
# llamar a la función
lista1 = [1, 2, 3, 4, 5, 23, 50]
lista2 = [4, 5, 6, 7, 8, 13, 15]
no_comunes = elementos_no_comunes(lista1, lista2)
print('Ejercicio 26')
print(no_comunes)

# 27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.
def eliminar_duplicados(lista):
    return list(set(lista)) # return list(dict.fromkeys(lista)) para conservar el orden de los elementos de la lista original
# llamar a la función
lista = [1, 2, 2, 3, 4, 4, 5, 5]
sin_duplicados = eliminar_duplicados(lista)
print('Ejercicio 27')
print(sin_duplicados)  # Output: [1, 2, 3, 4, 5]

# 28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.
def suma_cuadrados_pares(n):
    return sum(i**2 for i in range(0, n+1, 2))
# llamar a la función
n = 10
suma = suma_cuadrados_pares(n)
print('Ejercicio 28')
print(suma)  # Output: 220

# 29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
def promedio(lista):
    return sum(lista) / len(lista)
# llamar a la función
lista = [1, 2, 3, 4, 5]
prom = promedio(lista)
print('Ejercicio 29')
print(prom)  # Output: 3.0

# 30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
def cadena_mas_larga(lista):
    return max(lista, key=len)
# llamar a la función
lista = ["coche", "moto", "ordenador"]
mas_larga = cadena_mas_larga(lista)
print('Ejercicio 30')
print(mas_larga)

# 31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeros_n_primos(n):
    primos = []
    i = 2
    while len(primos) < n:
        if es_primo(i):
            primos.append(i)
        i += 1
    return primos
# llamar a la función
print('Ejercicio 31')
n = 10
primos = primeros_n_primos(n)
print(primos)

# 32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
def invertir_palabras(cadena):
    palabras = cadena.split()
    palabras.reverse()
    cadena_invertida = ' '.join(palabras)
    return cadena_invertida
# llamar a la función
print('Ejercicio 32')
cadena = "Hola mundo"
cadena_invertida = invertir_palabras(cadena)
print(cadena_invertida)  # Output: "mundo Hola"

# 33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
def ordenar_por_ultimo_elemento(lista):
    return sorted(lista, key=lambda x: x[-1])
# llamar a la función
print('Ejercicio 33')
lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lista_ordenada = ordenar_por_ultimo_elemento(lista)
print(lista_ordenada)

# 34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = 'aeiou'
    contador = 0
    for char in cadena:
        if char in vocales:
            contador += 1
    return contador
# llamar a la función
print('Ejercicio 34')
cadena = "Hola Mundo"
cantidad_vocales = contar_vocales(cadena)
print(cantidad_vocales)

# 35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
# llamar a la función
print('Ejercicio 35')
num = 13
if es_primo(num):
    print(f"{num} ES un número primo.")
else:
    print(f"{num} NO es un número primo.")
