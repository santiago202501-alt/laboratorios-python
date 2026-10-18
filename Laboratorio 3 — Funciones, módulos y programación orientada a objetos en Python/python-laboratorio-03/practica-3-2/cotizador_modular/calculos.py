def subtotal(precio, cantidad):
    return precio * cantidad

def descuento_valor(subtotal_val, porcentaje_desc):
    return subtotal_val * (porcentaje_desc / 100)

def impuesto_valor(monto_base, porcentaje_imp):
    return monto_base * (porcentaje_imp / 100)

def calcular_total_final(precio, cantidad, desc_pct, imp_pct):
    sub = subtotal(precio, cantidad)
    desc = descuento_valor(sub, desc_pct)
    base_imponible = sub - desc
    imp = impuesto_valor(base_imponible, imp_pct)
    return base_imponible + imp

if __name__ == "__main__":
    # Este bloque solo corre si ejecutas calculos.py directamente,
    # evitando que se ejecuten entradas al importarlo desde main.py.
    print("Módulo de cálculos cargado correctamente.")