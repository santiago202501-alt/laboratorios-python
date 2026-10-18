from pathlib import Path
import csv


BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "reportes" / "inventario.csv"


def exportar_csv(inventario):
    """
    Exporta el inventario a un archivo CSV.

    Devuelve la ruta del archivo generado.
    """

    # Crear la carpeta reportes si no existe.
    RUTA_CSV.parent.mkdir(parents=True, exist_ok=True)

    campos = [
        "codigo",
        "nombre",
        "categoria",
        "precio",
        "cantidad",
        "valor_inventario"
    ]

    # Obtener datos mediante la interfaz pública.
    productos = inventario.listar_productos()

    with RUTA_CSV.open(
        "w",
        encoding="utf-8",
        newline=""
    ) as archivo:

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos
        )

        escritor.writeheader()

        for producto in productos:
            escritor.writerow({
                "codigo": producto.codigo,
                "nombre": producto.nombre,
                "categoria": producto.categoria,
                "precio": producto.precio,
                "cantidad": producto.cantidad,
                "valor_inventario": producto.calcular_valor()
            })

    return RUTA_CSV
