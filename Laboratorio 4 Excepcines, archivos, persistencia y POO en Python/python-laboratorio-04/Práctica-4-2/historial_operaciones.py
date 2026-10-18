from pathlib import Path

def historial():
    ruta = Path(__file__).parent / "operaciones.txt"

    while True:
        opc = input("\n1. Registrar | 2. Mostrar | 0. Salir: ").strip()

        if opc == "1":
            concepto = input("Concepto: ").strip()
            try:
                valor = float(input("Valor: "))
                with open(ruta, "a", encoding="utf-8") as f:
                    f.write(f"{concepto}: {valor}\n")
                print("Registrado.")
            except ValueError:
                print("Valor no válido.")

        elif opc == "2":
            if ruta.exists():
                print("\n--- Historial ---")
                print(ruta.read_text(encoding="utf-8") or "Vacío.")
            else:
                print("Sin operaciones registradas.")

        elif opc == "0":
            break

if __name__ == "__main__":
    historial()