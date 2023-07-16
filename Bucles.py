'''
Javier Cerrudo
Prework Python Bucles
for elemento in secuencia:
'''

# 1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for.
print('Ejercicio 1')
for numero in range(1, 11):
    print(numero)

# 2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while.
numero = 1
print('Ejercicio 2')
while numero <= 20:
    if numero % 2 == 0:
        print(numero)
    numero += 1

# 3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
suma = 0
numero = 1

while numero <= 100:
    suma += numero
    numero += 1
print('Ejercicio 3')
print("La suma es:", suma)
