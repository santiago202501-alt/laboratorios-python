def calcular_subtotal(precio, cantidad):
    # Completa el cálculo.
    return precio * cantidad

def calcular_descuento(subtotal, porcentaje):
    # El porcentaje 10 representa 10 %.
    return subtotal * (porcentaje / 100)

def calcular_impuesto(base, porcentaje):
    # Calcula el impuesto sobre la base recibida.
    return base * (porcentaje / 100)

# --- Datos de entrada ---
precio = 100000
cantidad = 2
porcentaje_descuento = 10
porcentaje_impuesto = 19

# --- Guardar cada resultado en una variable antes de imprimir ---
subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal, porcentaje_descuento)
base_despues_descuento = subtotal - descuento
impuesto = calcular_impuesto(base_despues_descuento, porcentaje_impuesto)
total = base_despues_descuento + impuesto

# --- Resultados ---
print(f"Subtotal: {subtotal}")
print(f"Descuento: {descuento}")
print(f"Base después del descuento: {base_despues_descuento}")
print(f"Impuesto: {impuesto}")
print(f"Total: {total}")