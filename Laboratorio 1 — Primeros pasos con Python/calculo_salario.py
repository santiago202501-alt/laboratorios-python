# Declaración de variables y constante
unidades = 4
precio = 25000.0
descuento = 0.20

# Operaciones matemáticas
subtotal = unidades * precio
valor_descuento = subtotal * descuento
total = subtotal - valor_descuento

# Presentación detallada en consola
print("-" * 30)
print("     CÁLCULO CON DESCUENTO")
print("-" * 30)
print(f"Unidades: {unidades}")
print(f"Precio por unidad: ${precio:,.1f}")
print(f"Subtotal: ${subtotal:,.1f}")
print(f"Descuento aplicable (20%): ${valor_descuento:,.1f}")
print(f"Total a pagar: ${total:,.1f}")