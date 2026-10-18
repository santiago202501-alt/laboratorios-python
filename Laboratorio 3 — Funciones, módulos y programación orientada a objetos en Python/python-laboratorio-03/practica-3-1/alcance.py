def duplicar(numero):
    resultado = numero * 2
    return resultado 

doble = duplicar(8)
print(doble)


####

def calcular_unidades(productos):
    total = 0

    for producto in productos:
        total += producto["cantidad"]

    return total


inventario = [
    {"nombre": "Teclado", "cantidad": 4},
    {"nombre": "Mouse", "cantidad": 7}
]

print(calcular_unidades(inventario))



#####
def agregar(nombre, nombres):
    nombres.append(nombre)


productos = ["Teclado"]
agregar("Mouse", productos)

print(productos)



####
def agregar_en_copia(nombre, nombres):
    copia = nombres.copy()
    copia.append(nombre)
    return copia


original = ["Teclado"]
nueva = agregar_en_copia("Mouse", original)

print("Original:", original)
print("Nueva:", nueva)



#####


# Solución 1: Usando for y append()
def agotados_con_for(productos):
    lista_agotados = []
    for producto in productos:
        if producto['cantidad'] == 0:
            lista_agotados.append(producto['nombre'])
    return lista_agotados

# Solución 2: Usando comprensión de lista (más limpia y directa)
def agotados_por_comprension(productos):
    return [p['nombre'] for p in productos if p['cantidad'] == 0]


####