CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        if not codigo or not codigo.strip():
            raise ValueError("El código no puede estar vacío.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if categoria not in CATEGORIAS:
            raise ValueError(f"Categoría no válida. Debe ser una de: {CATEGORIAS}")
        if precio <= 0:
            raise ValueError("El precio unitario debe ser mayor que cero.")
        if cantidad < 0:
            raise ValueError("La cantidad disponible no puede ser negativa.")

        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._categoria = categoria
        self._precio = float(precio)
        self._cantidad = int(cantidad)

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        if nueva_cantidad < 0:
            return False
        self._cantidad = int(nueva_cantidad)
        return True

    def calcular_valor(self):
        return self._precio * self._cantidad