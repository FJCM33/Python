'''
Javier Cerrudo
Prework Python Condicionales
'''

# 1. Ejercicio: Dado un número, imprime si es positivo o negativo.
numero = float(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# 2. Ejercicio: Dado un número, imprime si es par o impar.
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# 3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3
print("El número mayor es:", mayor)


# Diccionarios
persona = {"nombre": "Javier", "edad": 60}
persona['edad'] = 30
print(persona['edad'])


