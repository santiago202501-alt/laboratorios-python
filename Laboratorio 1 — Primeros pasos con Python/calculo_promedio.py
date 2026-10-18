# Declaración de las tres notas (puedes cambiar estos valores para probar otros)
nota_1 = 4.2
nota_2 = 3.8
nota_3 = 4.5

# Cálculo del promedio sumando las notas y dividiendo entre la cantidad total
promedio = (nota_1 + nota_2 + nota_3) / 3

# Muestra de resultados utilizando f-strings
print("-------------------------------")
print("     CÁLCULO DE PROMEDIO       ")
print("-------------------------------")
print(f"Nota 1:    {nota_1}")
print(f"Nota 2:    {nota_2}")
print(f"Nota 3:    {nota_3}")
print("--------------------------")
print(f"Promedio:  {promedio:.2f}")
print("--------------------------")