num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2


if num2 != 0:
    division = num1 / num2
    division_entera = num1 // num2
    residuo = num1 % num2
else:
    division = "No se puede dividir entre cero"
    division_entera = "No aplica"
    residuo = "No aplica"


print("-----------------------------------")
print("       OPERACIONES ARITMÉTICAS     ")
print("-----------------------------------")
print(f"Número 1: {num1}")
print(f"Número 2: {num2}")
print("----------------------------------")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"División entera: {division_entera}")
print(f"Residuo (Módulo): {residuo}")