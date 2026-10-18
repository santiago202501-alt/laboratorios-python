def leer_cantidad_valida():
    while True:
        entrada = input("Cantidad: ")
        try:
            cantidad = int(entrada)
        except ValueError:
            print("Debes escribir un entero.")
            continue
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            continue  
        print(f"Cantidad aceptada: {cantidad}")
        return cantidad
if __name__ == "__main__":
    leer_cantidad_valida()