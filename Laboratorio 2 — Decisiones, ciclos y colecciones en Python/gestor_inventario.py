# Lista de diccionarios para productos
# Tupla de categorías válidas
# Ciclo del menú
#   Registrar
#   Listar
#   Buscar
#   Actualizar
#   Eliminar
#   Filtrar sin stock
#   Mostrar resumen

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

productos = []
opcion = ""

while opcion != "0":
    print()
    print("================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("0. Salir")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        codigo = input("Código: ").strip()
        if not codigo:
            print("Error: El código no puede estar vacío.")
            continue
        
        repetido = False
        for p in productos:
            if p["codigo"] == codigo:
                repetido = True
                break
        if repetido:
            print("Error: Ya existe un producto registrado con ese código.")
            continue

        nombre = input("Nombre: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            continue

        print(f"Categorías permitidas: {CATEGORIAS}")
        categoria = input("Categoría: ").strip()
        if categoria not in CATEGORIAS:
            print("Error: Categoría no válida.")
            continue

        precio = float(input("Precio: "))
        if precio <= 0:
            print("Error: El precio debe ser mayor que cero.")
            continue

        cantidad = int(input("Cantidad: "))
        if cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
            continue

        nuevo_producto = {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "cantidad": cantidad
        }
        productos.append(nuevo_producto)
        print("Producto registrado.")

    elif opcion == "2":
        if not productos:
            print("No hay registros en el inventario.")
        else:
            for p in productos:
                print(f"{p['codigo']} - {p['nombre']} - {p['categoria']} - ${p['precio']} - {p['cantidad']} unidades")

    elif opcion == "3":
        codigo_buscado = input("Código a buscar: ").strip()
        encontrado = None
        for p in productos:
            if p["codigo"] == codigo_buscado:
                encontrado = p
                break
        if encontrado is not None:
            print(f"Código: {encontrado['codigo']}")
            print(f"Nombre: {encontrado['nombre']}")
            print(f"Categoría: {encontrado['categoria']}")
            print(f"Precio: ${encontrado['precio']}")
            print(f"Cantidad: {encontrado['cantidad']}")
        else:
            print("El producto no existe.")

    elif opcion == "4":
        codigo_buscado = input("Código del producto a actualizar: ").strip()
        encontrado = None
        for p in productos:
            if p["codigo"] == codigo_buscado:
                encontrado = p
                break
        if encontrado is not None:
            nueva_cantidad = int(input("Nueva cantidad disponible: "))
            if nueva_cantidad < 0:
                print("Error: La cantidad no puede ser negativa. Se conserva la cantidad anterior.")
            else:
                encontrado["cantidad"] = nueva_cantidad
                print("Existencias actualizadas.")
        else:
            print("El producto no existe.")

    elif opcion == "5":
        codigo_buscado = input("Código del producto a eliminar: ").strip()
        encontrado = None
        for p in productos:
            if p["codigo"] == codigo_buscado:
                encontrado = p
                break
        if encontrado is not None:
            productos.remove(encontrado)
            print("Producto eliminado.")
        else:
            print("El producto no existe.")

    elif opcion == "6":
        agotados = [
            producto["nombre"]
            for producto in productos
            if producto["cantidad"] == 0
        ]
        if agotados:
            print("Sin existencias:")
            for nombre in agotados:
                print(f"- {nombre}")
        else:
            print("No hay productos sin stock.")

    elif opcion == "7":
        if not productos:
            print("El inventario está vacío.")
        else:
            total_productos = len(productos)
            unidades_totales = sum(p["cantidad"] for p in productos)
            valor_inventario = sum(p["precio"] * p["cantidad"] for p in productos)
            categorias_utilizadas = {
                p["categoria"]
                for p in productos
            }
            print(f"Productos: {total_productos}")
            print(f"Unidades: {unidades_totales}")
            print(f"Valor del inventario: ${valor_inventario}")
            print(f"Categorías utilizadas: {', '.join(categorias_utilizadas)}")

    elif opcion == "0":
        print("Programa finalizado.")
    else:
        print("Opción no válida.")