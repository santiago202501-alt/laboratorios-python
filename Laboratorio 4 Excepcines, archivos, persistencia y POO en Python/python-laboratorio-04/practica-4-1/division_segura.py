def division_segura():
    num1_str = input("Introduce el numerador: ")
    num2_str = input("Introduce el divisor: ")

    try:
        numerador = float(num1_str)
        divisor = float(num2_str)
        
        resultado = numerador / divisor
    except ValueError:
        print("Error: Una o ambas entradas no se pueden convertir a número.")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
    else:

        if resultado.is_integer():
            print(f"Resultado de la división: {int(resultado)}")
        else:
            print(f"Resultado de la división: {resultado}")


if __name__ == "__main__":
    division_segura()