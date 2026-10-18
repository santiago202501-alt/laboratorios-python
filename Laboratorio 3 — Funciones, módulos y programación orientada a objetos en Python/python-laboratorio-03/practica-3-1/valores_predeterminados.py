def calcular_total(precio, cantidad, descuento=0):
    subtotal = precio * cantidad
    return subtotal - subtotal * descuento / 100


print(calcular_total(50000, 2))
print(calcular_total(50000, 2, 10))
print(calcular_total(precio=50000, cantidad=2, descuento=20))


def calcular_cobro(valor_compra, envio=10000):
    return valor_compra + envio

compra_1 = 50000
total_predeterminado = calcular_cobro(compra_1)

compra_2 = 50000
total_gratis = calcular_cobro(compra_2, envio=0)

print(f"Compra de ${compra_1} con envío predeterminado: ${total_predeterminado}")
print(f"Compra de ${compra_2} con envío gratuito: ${total_gratis}")