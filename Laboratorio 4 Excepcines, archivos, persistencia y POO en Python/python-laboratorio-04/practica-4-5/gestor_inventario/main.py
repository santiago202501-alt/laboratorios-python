from producto import Producto, CATEGORIAS
from inventario import Inventario
from almacenamiento import cargar_inventario, guardar_inventario
from reportes import exportar_csv


def mostrar_menu():
    print()
    print("================================")
    print("      GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("8. Guardar inventario")
    print("9. Exportar reporte CSV")
    print("0. Salir")
    print("================================")


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


def registrar_producto(inventario):
    print("\n--- Registro de Producto ---")

    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()

    print(f"Categorías disponibles: {CATEGORIAS}")
    categoria = input("Categoría: ").strip()

    precio = leer_precio()
    cantidad = leer_cantidad()

    try:
        nuevo_prod = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            cantidad
        )

        if inventario.registrar_producto(nuevo_prod):
            print("Producto registrado con éxito.")
            return True

        print("Error: Ya existe un producto con ese código.")
        return False

    except ValueError as error:
        print(f"Error de validación: {error}")
        return False


def listar_productos(inventario):
    print("\n--- Lista de Productos ---")

    productos = inventario.listar_productos()

    if not productos:
        print("El inventario está vacío.")
        return

    for producto in productos:
        print(
            f"{producto.codigo} - "
            f"{producto.nombre} - "
            f"{producto.categoria} - "
            f"${producto.precio} - "
            f"{producto.cantidad} unidades"
        )


def buscar_producto(inventario):
    print("\n--- Buscar Producto ---")

    codigo = input("Ingrese el código a buscar: ").strip()

    producto = inventario.buscar_por_codigo(codigo)

    if producto:
        print(
            f"Encontrado: [{producto.codigo}] "
            f"{producto.nombre} | "
            f"Categoría: {producto.categoria} | "
            f"Precio: ${producto.precio} | "
            f"Stock: {producto.cantidad}"
        )
    else:
        print("El producto no existe en el inventario.")


def actualizar_existencias(inventario):
    print("\n--- Actualizar Existencias ---")

    codigo = input(
        "Código del producto a actualizar: "
    ).strip()

    producto = inventario.buscar_por_codigo(codigo)

    if not producto:
        print("El producto no existe.")
        return False

    nueva_cantidad = leer_cantidad()

    if inventario.actualizar_existencias(
        codigo,
        nueva_cantidad
    ):
        print("Existencias actualizadas correctamente.")
        return True

    print("No se pudo actualizar la cantidad.")
    return False


def eliminar_producto(inventario):
    print("\n--- Eliminar Producto ---")

    codigo = input(
        "Código del producto a eliminar: "
    ).strip()

    if inventario.eliminar_producto(codigo):
        print("Producto eliminado correctamente.")
        return True

    print(
        "El código ingresado no existe en el inventario."
    )
    return False


def consultar_sin_stock(inventario):
    print("\n--- Productos Sin Stock ---")

    agotados = inventario.productos_sin_stock()

    if not agotados:
        print("No hay productos agotados.")
        return

    print("Sin existencias:")

    for nombre in agotados:
        print(f"- {nombre}")


def mostrar_resumen(inventario):
    print("\n--- Resumen del Inventario ---")

    resumen = inventario.resumen()

    print(
        f"Productos registrados: "
        f"{resumen['total_productos']}"
    )

    print(
        f"Unidades disponibles: "
        f"{resumen['unidades']}"
    )

    print(
        f"Valor del inventario: "
        f"${resumen['valor_total']}"
    )

    categorias = resumen["categorias"]

    if categorias:
        categorias_texto = ", ".join(
            sorted(categorias)
        )
    else:
        categorias_texto = "Ninguna"

    print(
        f"Categorías utilizadas: "
        f"{categorias_texto}"
    )


def guardar(inventario):
    """
    Intenta guardar el inventario.

    Solo muestra el mensaje de éxito si la escritura
    terminó correctamente.
    """

    try:
        guardar_inventario(inventario)
        print("Inventario guardado correctamente.")
        return True

    except OSError as error:
        print(f"Error de escritura: {error}")
        print(
            "Los cambios podrían existir solamente en memoria."
        )
        return False


def exportar_reporte(inventario):
    try:
        ruta = exportar_csv(inventario)
        print(f"Reporte exportado: {ruta}")
        return True

    except OSError as error:
        print(f"Error al exportar el reporte: {error}")
        return False


def main():
    archivo_danado = False

    # Cargar automáticamente al iniciar.
    try:
        inventario = cargar_inventario()

        if inventario.listar_productos():
            print(
                "Inventario cargado correctamente."
            )
        else:
            print(
                "No hay productos guardados. "
                "Inventario vacío."
            )

    except ValueError as error:
        print("\nERROR AL CARGAR EL INVENTARIO")
        print(error)
        print(
            "El archivo existente no será sobrescrito "
            "automáticamente."
        )
        print(
            "Las operaciones de modificación están "
            "bloqueadas hasta resolver el problema."
        )

        inventario = Inventario()
        archivo_danado = True

    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        # ============================================
        # 1. Registrar
        # ============================================
        if opcion == "1":

            if archivo_danado:
                print(
                    "No se puede modificar el inventario "
                    "porque productos.json tiene errores."
                )
                continue

            if registrar_producto(inventario):
                guardar(inventario)

        # ============================================
        # 2. Listar
        # ============================================
        elif opcion == "2":
            listar_productos(inventario)

        # ============================================
        # 3. Buscar
        # ============================================
        elif opcion == "3":
            buscar_producto(inventario)

        # ============================================
        # 4. Actualizar
        # ============================================
        elif opcion == "4":

            if archivo_danado:
                print(
                    "No se puede modificar el inventario "
                    "porque productos.json tiene errores."
                )
                continue

            if actualizar_existencias(inventario):
                guardar(inventario)

        # ============================================
        # 5. Eliminar
        # ============================================
        elif opcion == "5":

            if archivo_danado:
                print(
                    "No se puede modificar el inventario "
                    "porque productos.json tiene errores."
                )
                continue

            if eliminar_producto(inventario):
                guardar(inventario)

        # ============================================
        # 6. Sin stock
        # ============================================
        elif opcion == "6":
            consultar_sin_stock(inventario)

        # ============================================
        # 7. Resumen
        # ============================================
        elif opcion == "7":
            mostrar_resumen(inventario)

        # ============================================
        # 8. Guardar
        # ============================================
        elif opcion == "8":

            if archivo_danado:
                print(
                    "No se puede guardar porque el archivo "
                    "productos.json tiene errores."
                )
                continue

            guardar(inventario)

        # ============================================
        # 9. Exportar CSV
        # ============================================
        elif opcion == "9":
            exportar_reporte(inventario)

        # ============================================
        # 0. Salir
        # ============================================
        elif opcion == "0":

            if archivo_danado:
                print(
                    "El programa finalizará sin sobrescribir "
                    "el archivo dañado."
                )
            else:
                # Guardado final para conservar los cambios.
                print("Guardando inventario antes de salir...")

                if guardar(inventario):
                    print("Programa finalizado.")
                else:
                    print(
                        "Programa finalizado. "
                        "El último guardado no pudo confirmarse."
                    )

            break

        else:
            print(
                "Opción no válida. Intente de nuevo."
            )


if __name__ == "__main__":
    main()
