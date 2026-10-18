print("=============================")
print("      COTIZADOR PYTHON")
print("=============================")

nombre_cliente = input("Nombre del cliente: ")
nombre_producto = input("Nombre del producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
descuento_ingresado = float(input("Descuento (%): "))
impuesto_ingresado = float(input("Impuesto (%): "))

costo_envio = float(input("Costo de envío: "))
nombre_vendedor = input("Nombre del vendedor: ")
codigo_cotizacion = input("Código de la cotización: ")

porcentaje_descuento = descuento_ingresado / 100
porcentaje_impuesto = impuesto_ingresado / 100

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * porcentaje_descuento
base = subtotal - valor_descuento
valor_impuesto = base * porcentaje_impuesto
total_con_impuesto = base + valor_impuesto
total_final = total_con_impuesto + costo_envio

print("-----------------------------")
print("RESUMEN DE COMPRA")
print("-----------------------------")
print(f"Código de cotización: {codigo_cotizacion}")
print(f"Vendedor: {nombre_vendedor}")
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {nombre_producto}")
print(f"Precio unitario: ${precio_unitario}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal}")
print(f"Descuento: ${valor_descuento}")
print(f"Base: ${base}")
print(f"Impuesto: ${valor_impuesto}")
print(f"Costo de envío: ${costo_envio}")
print(f"TOTAL FINAL: ${total_final}")
print("-----------------------------")