from pathlib import Path
import json

from producto import Producto
from inventario import Inventario


BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "datos" / "productos.json"


def guardar_inventario(inventario):
    """
    Guarda el inventario completo en productos.json.

    La función no informa éxito mediante print().
    Si la escritura falla, lanza la excepción correspondiente.
    """

    datos = inventario.exportar_datos()

    # Crear la carpeta datos si no existe.
    RUTA_JSON.parent.mkdir(parents=True, exist_ok=True)

    # Escribir el JSON usando UTF-8 e indentación.
    with RUTA_JSON.open("w", encoding="utf-8") as archivo:
        json.dump(
            datos,
            archivo,
            ensure_ascii=False,
            indent=4
        )


def cargar_inventario():
    """
    Carga el inventario desde productos.json.

    Si el archivo no existe:
        devuelve un Inventario vacío.

    Si existe:
        valida todo el contenido antes de devolverlo.

    Si hay algún error:
        lanza ValueError sin modificar el archivo original.
    """

    # Primera ejecución: no existe todavía el JSON.
    if not RUTA_JSON.exists():
        return Inventario()

    try:
        with RUTA_JSON.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

    except json.JSONDecodeError as error:
        raise ValueError(
            "El archivo productos.json tiene un formato JSON "
            f"incorrecto: {error}"
        ) from error

    except OSError as error:
        raise ValueError(
            f"No se pudo leer productos.json: {error}"
        ) from error

    # El archivo debe contener una lista.
    if not isinstance(datos, list):
        raise ValueError(
            "La estructura del JSON no es válida. "
            "Debe contener una lista de productos."
        )

    # Inventario temporal.
    # No se devuelve hasta validar TODOS los productos.
    inventario_temporal = Inventario()

    for numero, registro in enumerate(datos, start=1):
        try:
            producto = Producto.desde_diccionario(registro)

        except (ValueError, TypeError, KeyError) as error:
            raise ValueError(
                f"El producto número {numero} es inválido: {error}"
            ) from error

        # registrar_producto controla códigos duplicados.
        if not inventario_temporal.registrar_producto(producto):
            raise ValueError(
                f"El código '{producto.codigo}' está repetido "
                "en el archivo JSON."
            )

    return inventario_temporal
