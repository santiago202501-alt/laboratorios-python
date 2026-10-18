import unidades

# Solicitar datos al usuario
print("--- CONVERSOR DE UNIDADES ---")
km_ingresados = float(input("Ingresa la cantidad en kilómetros: "))
celsius_ingresados = float(input("Ingresa la temperatura en grados Celsius: "))

# Realizar las conversiones llamando a las funciones del módulo
metros = unidades.kilometros_a_metros(km_ingresados)
fahrenheit = unidades.celsius_a_fahrenheit(celsius_ingresados)

# Mostrar los resultados
print("\n--- RESULTADOS ---")
print(f"{km_ingresados} kilómetros equivalen a {metros} metros.")
print(f"{celsius_ingresados} °C equivalen a {fahrenheit} °F.")