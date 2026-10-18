celsius = float(input("Temperatura en °C: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius} °C equivalen a {fahrenheit} °F")






nombre_trabajador = input("Nombre del trabajador: ")
horas_trabajadas = float(input("Horas trabajadas: "))
valor_por_hora = float(input("Valor por hora: "))

pago_total = horas_trabajadas * valor_por_hora

print("-" * 25)
print("RESUMEN DE PAGO")
print("-" * 25)
print(f"Trabajador: {nombre_trabajador}")
print(f"Horas: {int(horas_trabajadas) if horas_trabajadas.is_integer() else horas_trabajadas}")
print(f"Valor por hora: ${valor_por_hora}")
print(f"Pago total: ${pago_total}")




producto = input("tipo de producto:")
precio = float(input("precio:"))
cantidad = float(input("catidad:"))

subtotal = precio * cantidad

print("Producto:", producto)
print("Subtotal: $", subtotal)