unidades_disponibles = 12
unidades_solicitadas = 8

suficientes = unidades_disponibles >= unidades_solicitadas
iguales = unidades_disponibles == unidades_solicitadas
mas_solicitadas = unidades_solicitadas > unidades_disponibles

print(f"--- Caso 1 (Solicitadas: {unidades_solicitadas}) ---")
print(f"¿Hay suficientes unidades?: {suficientes}")
print(f"¿Las cantidades son iguales?: {iguales}")
print(f"¿Se solicitaron más unidades de las disponibles?: {mas_solicitadas}\n")