class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalle(self):
        print("Código:", self.codigo)
        print("Producto:", self.nombre)
        print("Precio:", self.precio)
        print("Cantidad:", self.cantidad)

    def calcular_valor(self):
        return self.precio * self.cantidad

teclado = Producto("P001", "Teclado", 85000, 4)

print("--- Atributos individuales ---")
print(teclado.codigo)
print(teclado.nombre)
print(teclado.precio)
print(teclado.cantidad)

print("\n--- Detalle y cálculo de valor ---")
teclado.mostrar_detalle()
print("Valor:", teclado.calcular_valor()) 

print("\n--- Creando un segundo objeto (Mouse) ---")
mouse = Producto("P002", "Mouse", 45000, 7)

print("Valor del teclado:", teclado.calcular_valor())
print("Valor del mouse:", mouse.calcular_valor())

print("\n--- Modificando el stock del mouse ---")
print("Cantidad de teclado antes de modificar el mouse:", teclado.cantidad)
mouse.cantidad = 2 
print("Cantidad de mouse modificada:", mouse.cantidad)
print("Cantidad de teclado después de modificar el mouse (debe seguir intacta):", teclado.cantidad)