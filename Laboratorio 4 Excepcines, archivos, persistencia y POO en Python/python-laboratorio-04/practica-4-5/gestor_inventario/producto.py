import math


CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        if not codigo or not codigo.strip():
            raise ValueError("El código no puede estar vacío.")

        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if categoria not in CATEGORIAS:
            raise ValueError(
                f"Categoría no válida. Debe ser una de: {CATEGORIAS}"
            )

        if not isinstance(precio, (int, float)):
            raise ValueError("El precio debe ser un número.")

        if not math.isfinite(precio):
            raise ValueError("El precio debe ser un número finito.")

        if precio <= 0:
            raise ValueError(
                "El precio unitario debe ser mayor que cero."
            )

        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise ValueError(
                "La cantidad debe ser un número entero."
            )

        if cantidad < 0:
            raise ValueError(
                "La cantidad disponible no puede ser negativa."
            )

        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._categoria = categoria
        self._precio = float(precio)
        self._cantidad = cantidad

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
        if not isinstance(nueva_cantidad, int) or isinstance(
            nueva_cantidad, bool
        ):
            return False

        if nueva_cantidad < 0:
            return False

        self._cantidad = nueva_cantidad
        return True

    def calcular_valor(self):
        return self._precio * self._cantidad

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    @classmethod
    def desde_diccionario(cls, datos):
        if not isinstance(datos, dict):
            raise ValueError(
                "Cada producto debe ser un objeto/diccionario."
            )

        campos = (
            "codigo",
            "nombre",
            "categoria",
            "precio",
            "cantidad"
        )

        for campo in campos:
            if campo not in datos:
                raise ValueError(
                    f"Falta el campo obligatorio: '{campo}'."
                )

        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["cantidad"]
        )