# Definición de datos iniciales
nombre_producto = "Teclado mecánico"
precio_unitario = 100000.0
cantidad = 2
porcentaje_descuento = 0.10

# Reto adicional: Impuesto
PORCENTAJE_IMPUESTO = 0.19

# Cálculos de subtotal y descuento
subtotal = precio_unitario * cantidad
valor_descuento = subtotal * porcentaje_descuento
total_con_descuento = subtotal - valor_descuento

# Cálculos del reto adicional (Impuesto sobre la base con descuento)
base_despues_descuento = total_con_descuento
valor_impuesto = base_despues_descuento * PORCENTAJE_IMPUESTO
total_final = base_despues_descuento + valor_impuesto

# Presentación en consola
print("-" * 35)
print("           FACTURA SIMPLE")
print("-" * 35)
print(f"Producto: {nombre_producto}")
print(f"Precio unitario: ${precio_unitario:,.1f}")
print(f"Cantidad: {cantidad}")
print("-" * 35)
print(f"Subtotal: ${subtotal:,.1f}")
print(f"Descuento: ${valor_descuento:,.1f}")
print(f"Total después del descuento: ${total_con_descuento:,.1f}")
print("-" * 35)
print(f"Base después del descuento: ${base_despues_descuento:,.1f}")
print(f"Valor del impuesto: ${valor_impuesto:,.1f}")
print(f"Total final: ${total_final:,.1f}")