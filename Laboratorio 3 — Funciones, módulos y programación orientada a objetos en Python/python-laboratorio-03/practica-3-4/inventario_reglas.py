class Producto:
    def __init__(self, codigo, nombre):
        self._codigo = codigo
        self._nombre = nombre

    @property
    def codigo(self):
        return self._codigo

class Inventario:
    def __init__(self):
        self._productos = []

    def buscar_por_codigo(self, codigo):
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def agregar(self, producto):
        if self.buscar_por_codigo(producto.codigo):
            return False 
        self._productos.append(producto)
        return True

    def eliminar(self, codigo):
        producto = self.buscar_por_codigo(codigo)
        if producto:
            self._productos.remove(producto)
            return True
        return False  
inv = Inventario()
p1 = Producto("P001", "Teclado")
p2 = Producto("P002", "Mouse")

print(inv.agregar(p1))
print(inv.agregar(p2))  
print(inv.agregar(Producto("P001", "Otro"))) 

print(inv.eliminar("P002"))  
print(inv.eliminar("P999"))  