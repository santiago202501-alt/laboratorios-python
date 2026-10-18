import json
from pathlib import Path

def lectura_protegida():
    ruta = Path(__file__).parent / "productos.json"
    productos = []

    print("=== Intentando cargar 'productos.json' ===")

    try:
        if not ruta.exists():
            print("[Aviso] El archivo no existe. Iniciando con una lista vacía.")
            return productos
        contenido_texto = ruta.read_text(encoding="utf-8")
        productos = json.loads(contenido_texto)
        print(f"✓ Archivo cargado correctamente. Se encontraron {len(productos)} elemento(s).")

    except json.JSONDecodeError:
        print("\n[Error de Formato] El archivo 'productos.json' está dañado o mal estructurado.")
        print("[Protección] No se sobrescribirá el archivo para evitar pérdida de datos.")
        
        print("\n--- Contenido actual del archivo (para revisión) ---")
        print(contenido_texto if 'contenido_texto' in locals() else "No se pudo leer el contenido.")
        print("-----------------------------------------------------")

    except Exception as e:
        print(f"[Error Inesperado]: {e}")

    return productos

if __name__ == "__main__":
    lectura_protegida()