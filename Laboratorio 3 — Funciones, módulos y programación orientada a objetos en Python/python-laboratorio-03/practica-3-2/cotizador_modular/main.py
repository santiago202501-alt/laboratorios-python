import calculos
import validaciones

def main():
    print("--- Cotizador Modular ---")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))
    descuento = float(input("Porcentaje de descuento (%): "))
    impuesto = float(input("Porcentaje de impuesto (%): "))

    if (
        validaciones.precio_valido(precio)
        and validaciones.cantidad_valida(cantidad)
        and validaciones.porcentaje_valido(descuento)
        and validaciones.porcentaje_valido(impuesto)
    ):
        total = calculos.calcular_total_final(precio, cantidad, descuento, impuesto)
        print(f"El total final de la cotización es: {total}")
    else:
        print("Error: Revisa que los valores ingresados sean válidos.")

if __name__ == "__main__":
    main()