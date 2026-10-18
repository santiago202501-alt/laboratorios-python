def leer_edad():
    entrada = input("Por favor, introduce tu edad: ")

    try:
        edad = int(entrada)
    except ValueError:
        print("Error: El valor introducido no es un número entero válido.")
        return
    if edad < 0:
        print("Error: La edad no puede ser un número negativo.")
    elif edad > 120:
        print("Error: La edad no puede ser superior a 120 años.")
    else:
        print(f"¡Edad válida! Has introducido: {edad} años.")
if __name__ == "__main__":
    leer_edad()