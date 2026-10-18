from pathlib import Path

def generar_reporte():
    base_dir = Path(__file__).parent
    carpeta_reportes = base_dir / "reportes"
    carpeta_reportes.mkdir(exist_ok=True)
    archivo_resumen = carpeta_reportes / "resumen.txt"
    contenido = (
        "Reporte de Ejecución de Sistema\n"
        "Estado: Operación completada con éxito.\n"
        "Total de módulos procesados: 5\n"
    )
    archivo_resumen.write_text(contenido, encoding="utf-8")
    texto_leido = archivo_resumen.read_text(encoding="utf-8")
    print("=== Contenido del archivo ===")
    print(texto_leido)
    print("=== Ubicación del archivo ===")
    print(f"Ruta completa: {archivo_resumen.resolve()}")

if __name__ == "__main__":
    generar_reporte()



###

from pathlib import Path

ruta = Path("historial.txt")
ruta.write_text("Registro 1\n", encoding="utf-8")
ruta.write_text("Registro 2\n", encoding="utf-8")

print(ruta.read_text(encoding="utf-8"))