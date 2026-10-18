try:
    cantidad = int(input("Cantidad de productos: "))
    print("Cantidad registrada:", cantidad)
except ValueError:
    print("Debes escribir un número entero.")

print("Fin del programa.")




####

try:
    cantidad = int(input("Cantidad: "))
except ValueError:
    print("No es un número entero.")
else:
    if cantidad < 0:
        print("No se aceptan existencias negativas.")
    else:
        print("Cantidad aceptada:", cantidad)