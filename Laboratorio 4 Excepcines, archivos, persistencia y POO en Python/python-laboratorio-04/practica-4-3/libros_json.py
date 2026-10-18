import json
from pathlib import Path

def catalogo_libros():
    ruta = Path(__file__).parent / "libros.json"
    libros_iniciales = [
        {"codigo": "LIB001","titulo": "Cien años de soledad","autor": "Gabriel García Márquez","anio": 1967},

        {"codigo": "LIB002","titulo": "El alquimista","autor": "Paulo Coelho","anio": 1988},

        {"codigo": "LIB003","titulo": "Don Quijote de la Mancha","autor": "Miguel de Cervantes","anio": 1605}
    ]
    ruta.write_text(json.dumps(libros_iniciales, indent=4, ensure_ascii=False), encoding="utf-8")
    print("✓ Catálogo guardado en 'libros.json'.")
    def mostrar_libros():
        if ruta.exists():
            contenido = json.loads(ruta.read_text(encoding="utf-8"))
            print("\n=== Catálogo de Libros ===")
            for libro in contenido:
                print(f"[{libro['codigo']}] {libro['titulo']} - {libro['autor']} ({libro['anio']})")
        else:
            print("El archivo no existe.")
    mostrar_libros()

if __name__ == "__main__":
    catalogo_libros()


##

import json
from pathlib import Path

class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        if not codigo or not nombre or not categoria:
            raise ValueError("El código, el nombre y la categoría no pueden estar vacíos.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def a_diccionario(self):
        """Convierte el objeto a un diccionario compatible con JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Reconstruye un objeto Producto a partir de un diccionario."""
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["cantidad"]
        )

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} ({self.categoria}) - ${self.precio} | Stock: {self.cantidad}"


def probar_sistema():
    ruta = Path(__file__).parent / "productos.json"
    productos = [
        Producto("P001", "Teclado Mecánico", "Periféricos", 150000.0, 10),
        Producto("P002", "Mouse Gamer", "Periféricos", 80000.0, 15)
    ]
    datos_json = [p.a_diccionario() for p in productos]
    ruta.write_text(json.dumps(datos_json, indent=4, ensure_ascii=False), encoding="utf-8")
    print("✓ Productos guardados en formato JSON correctamente.\n")
    if ruta.exists():
        contenido_cargado = json.loads(ruta.read_text(encoding="utf-8"))
        productos_reconstruidos = [Producto.desde_diccionario(d) for d in contenido_cargado]

        print("=== Productos Reconstruidos desde el Archivo ===")
        for prod in productos_reconstruidos:
            print(type(prod), "->", prod)


if __name__ == "__main__":
    probar_sistema()