class ReporteTexto:
    def generar(self, datos):
        return f"Reporte detallado - Contenido: {datos}"

class ReporteResumen:
    def generar(self, datos):
        return f"Reporte resumen - Cantidad de registros: {len(datos)}"
reportes = [ReporteTexto(), ReporteResumen()]
datos_ejemplo = ["Venta 1", "Venta 2", "Venta 3", "Venta 4"]
for r in reportes:
    print(r.generar(datos_ejemplo))



class Persona:
        def __init__(self, nombre):
            self.nombre = nombre


class Aprendiz(Persona):
    def __init__(self, nombre, ficha):
        self.ficha = ficha


aprendiz = Aprendiz("Carlos", "123456")
print(aprendiz.nombre)