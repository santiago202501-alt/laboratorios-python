class Inventario:
    def __init__(self):
        self._productos = []

    def buscar_por_codigo(self, codigo):
        for prod in self._productos:
            if prod.codigo == codigo:
                return prod
        return None

    def registrar_producto(self, producto):
        if self.buscar_por_codigo(producto.codigo) is not None:
            return False  # Código duplicado
        self._productos.append(producto)
        return True

    def listar_productos(self):
        # Devuelve una copia para no exponer la lista interna directamente
        return list(self._productos)

    def actualizar_existencias(self, codigo, nueva_cantidad):
        prod = self.buscar_por_codigo(codigo)
        if prod is None:
            return False
        return prod.actualizar_existencias(nueva_cantidad)

    def eliminar_producto(self, codigo):
        prod = self.buscar_por_codigo(codigo)
        if prod is not None:
            self._productos.remove(prod)
            return True
        return False

    def productos_sin_stock(self):
        return [
            producto.nombre
            for producto in self._productos
            if producto.cantidad == 0
        ]

    def resumen(self):
        total_productos = len(self._productos)
        unidades = sum(producto.cantidad for producto in self._productos)
        valor_total = sum(producto.calcular_valor() for producto in self._productos)
        categorias = {producto.categoria for producto in self._productos}
        
        return {
            "total_productos": total_productos,
            "unidades": unidades,
            "valor_total": valor_total,
            "categorias": categorias
        }