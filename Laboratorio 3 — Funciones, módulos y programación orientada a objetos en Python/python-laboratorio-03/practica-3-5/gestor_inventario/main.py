from producto import Producto, CATEGORIAS
from inventario import Inventario

def mostrar_menu():
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

def leer_precio():
    while True:
        try:
            precio = float(input("Precio unitario: "))
            if precio <= 0:
                print("El precio debe ser mayor que cero.")
                continue
            return precio
        except ValueError:
            print("Debes escribir un número válido.")

def leer_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad disponible: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            return cantidad
        except ValueError:
            print("Debes escribir un número entero.")

def main():
    inventario = Inventario()
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            print("\n--- Registro de Producto ---")
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            
            print(f"Categorías disponibles: {CATEGORIAS}")
            categoria = input("Categoría: ").strip()
            
            precio = leer_precio()
            cantidad = leer_cantidad()

            try:
                nuevo_prod = Producto(codigo, nombre, categoria, precio, cantidad)
                if inventario.registrar_producto(nuevo_prod):
                    print("Producto registrado con éxito.")
                else:
                    print("Error: Ya existe un producto con ese código.")
            except ValueError as e:
                print(f"Error de validación: {e}")

        elif opcion == "2":
            print("\n--- Lista de Productos ---")
            productos = inventario.listar_productos()
            if not productos:
                print("El inventario está vacío.")
            else:
                for p in productos:
                    print(f"{p.codigo} - {p.nombre} - {p.categoria} - ${p.precio} - {p.cantidad} unidades")

        elif opcion == "3":
            print("\n--- Buscar Producto ---")
            codigo = input("Ingrese el código a buscar: ").strip()
            p = inventario.buscar_por_codigo(codigo)
            if p:
                print(f"Encontrado: [{p.codigo}] {p.nombre} | Categoría: {p.categoria} | Precio: ${p.precio} | Stock: {p.cantidad}")
            else:
                print("El producto no existe en el inventario.")

        elif opcion == "4":
            print("\n--- Actualizar Existencias ---")
            codigo = input("Código del producto a actualizar: ").strip()
            p = inventario.buscar_por_codigo(codigo)
            if not p:
                print("El producto no existe.")
            else:
                nueva_cant = leer_cantidad()
                if inventario.actualizar_existencias(codigo, nueva_cant):
                    print("Existencias actualizadas correctamente.")
                else:
                    print("No se pudo actualizar la cantidad.")

        elif opcion == "5":
            print("\n--- Eliminar Producto ---")
            codigo = input("Código del producto a eliminar: ").strip()
            if inventario.eliminar_producto(codigo):
                print("Producto eliminado correctamente.")
            else:
                print("El código ingresado no existe en el inventario.")

        elif opcion == "6":
            print("\n--- Productos Sin Stock ---")
            agotados = inventario.productos_sin_stock()
            if not agotados:
                print("No hay productos agotados.")
            else:
                print("Sin existencias:")
                for nombre in agotados:
                    print(f"- {nombre}")

        elif opcion == "7":
            print("\n--- Resumen del Inventario ---")
            res = inventario.resumen()
            print(f"Productos registrados: {res['total_productos']}")
            print(f"Unidades disponibles: {res['unidades']}")
            print(f"Valor del inventario: ${res['valor_total']}")
            cats = ", ".join(res['categorias']) if res['categorias'] else "Ninguna"
            print(f"Categorías utilizadas: {cats}")

        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()