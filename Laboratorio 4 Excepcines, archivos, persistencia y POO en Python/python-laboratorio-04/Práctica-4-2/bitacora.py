from pathlib import Path

def registrar_prueba():
    print("=== Registro de Bitácora de Pruebas ===")
    nombre = input("Nombre de la prueba: ").strip()
    resultado = input("Resultado (aprobada/fallida): ").strip()
    observacion = input("Observación breve: ").strip()
    linea_log = f"Prueba: {nombre} | Resultado: {resultado} | Observación: {observacion}\n"
    archivo_bitacora = Path("pruebas.txt")
    with open(archivo_bitacora, "a", encoding="utf-8") as archivo:
        archivo.write(linea_log)

    print("\n¡Entrada guardada correctamente en 'pruebas.txt'!")

if __name__ == "__main__":
    registrar_prueba()