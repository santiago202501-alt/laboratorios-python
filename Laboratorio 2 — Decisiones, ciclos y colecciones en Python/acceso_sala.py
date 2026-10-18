edad = int(input("Introduce tu edad: "))
autorizacion = input("¿Tienes autorización? (sí/no): ").strip().lower()

# Agregamos el 'if' y corregimos la indentación
if edad >= 18 or autorizacion == "sí" or autorizacion == "si":
    print("¡Acceso permitido! Puedes ingresar a la sala.")
else:
    print("Acceso denegado. No cumples con los requisitos.")