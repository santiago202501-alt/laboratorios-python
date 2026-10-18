def registro_compras():
    contador_compras = 0
    suma_acumulada = 0.0

    print("=== Registro de Compras ===")
    print("Introduce los importes de tus compras uno a uno.")
    print("Escribe '0' para finalizar el registro.\n")

    while True:
        entrada = input("Introduce el importe de la compra (0 para salir): ").strip()

        try:
            importe = float(entrada)
            if importe == 0:
                break
            if importe < 0:
                print("  [Error] El importe no puede ser negativo. Inténtalo de nuevo.\n")
                continue
            suma_acumulada += importe
            contador_compras += 1
            print(f"  -> Compra de {importe:.2f} € registrada correctamente.\n")

        except ValueError:
            print("  [Error] Entrada no válida. Debes introducir un número numérico.\n")
    print("\n=== Resumen de Compras ===")
    print(f"Total de compras aceptadas: {contador_compras}")
    print(f"Suma acumulada total: {suma_acumulada:.2f} €")


if __name__ == "__main__":
    registro_compras()