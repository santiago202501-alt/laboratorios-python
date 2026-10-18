inventario = [
    {"codigo": "A01", "nombre": "Laptop", "precio": 2500000, "cantidad": 3},
    {"codigo": "A02", "nombre": "Mouse", "precio": 60000, "cantidad": 0},
    {"codigo": "A03", "nombre": "Teclado", "precio": 120000, "cantidad": 5}
]


def mostrar_productos(productos):
    for p in productos:
        print(f"Código: {p['codigo']} | Nombre: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")


def buscar_producto(productos, codigo):
    for p in productos:
        if p['codigo'] == codigo:
            return p
    return None


def valor_inventario(productos):
    total = 0
    for p in productos:
        total += p['precio'] * p['cantidad']
    return total

def productos_sin_stock(productos):
    return [p['nombre'] for p in productos if p['cantidad'] == 0]

if __name__ == "__main__":
    print("=== 1. MOSTRAR PRODUCTOS ===")
    mostrar_productos(inventario)
    
    print("\n=== 2. BUSCAR PRODUCTO (A02) ===")
    resultado_busqueda = buscar_producto(inventario, "A02")
    print(resultado_busqueda)
    
    print("\n=== 3. VALOR TOTAL DEL INVENTARIO ===")
    total_valor = valor_inventario(inventario)
    print(f"Valor total: ${total_valor}")
    
    print("\n=== 4. PRODUCTOS SIN STOCK ===")
    sin_stock = productos_sin_stock(inventario)
    print(sin_stock)