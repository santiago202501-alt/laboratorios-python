class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def calcular_valor(self):
        return self._precio * self._cantidad

    # --- 3. Propiedades de consulta (getters) ---
    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        if nueva_cantidad < 0:
            return False

        self._cantidad = nueva_cantidad
        return True

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self._precio = nuevo_precio

producto = Producto("P001", "Teclado", 85000, 4)

print("Valor inicial:", producto.calcular_valor())

print("Código:", producto.codigo)
print("Nombre:", producto.nombre)
print("Cantidad inicial:", producto.cantidad)

print("\n--- Actualizando existencias ---")
print("Actualizar a 10 (válido):", producto.actualizar_existencias(10))
print("Cantidad actual:", producto.cantidad)

print("Actualizar a -5 (inválido):", producto.actualizar_existencias(-5))
print("Cantidad actual (debe seguir siendo 10):", producto.cantidad)

print("\n--- Modificando precio con setter ---")
producto.precio = 90000
print("Nuevo precio:", producto.precio)