def mostrar_encabezado():
    print("==========================")
    print("     INVENTARIO PYTHON")
    print("==========================")

def mostrar_despedida():
    print("==========================")
    print("     ¡HASTA PRONTO!")
    print("==========================")


if __name__ == "__main__":
    mostrar_encabezado()
    print("Ejecutando proceso de registro...")
    
    print() 
    
    mostrar_encabezado()
    print("Ejecutando proceso de consulta...")
    
    print()
    
    mostrar_despedida()



def saludar(nombre):
    print(f"Hola, {nombre}")


saludar("Laura")
saludar("Andrés")




def mostrar_producto(nombre, cantidad):
    print(f"Producto: {nombre}")
    print(f"Existencias: {cantidad}")


mostrar_producto("Teclado", 4)
mostrar_producto("Mouse", 7)



def presentar(nombre, ciudad):
    print(f"{nombre} vive en {ciudad}")


presentar("Ana", "Bogotá")
presentar("Luis", "cali") #tenia el nombre en la parte da la ciudad y la ciudad en el nombre