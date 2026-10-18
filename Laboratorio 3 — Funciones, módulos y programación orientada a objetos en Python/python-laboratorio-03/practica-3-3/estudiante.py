class Estudiante:
    def __init__(self, nombre, ficha, promedio):
        self.nombre = nombre
        self.ficha = ficha
        self.promedio = promedio

    def mostrar_perfil(self):
        print(f"Estudiante: {self.nombre} | Ficha: {self.ficha} | Promedio: {self.promedio}")

    def aprobo(self):
        return self.promedio >= 3.0

# --- Comprobación ---
estudiante1 = Estudiante("Carlos Pérez", "2894120", 2.8)
estudiante2 = Estudiante("Ana Gómez", "2894120", 4.1)

estudiante1.mostrar_perfil()
print(f"¿Aprobó? {estudiante1.aprobo()}")

print("-" * 30)

estudiante2.mostrar_perfil()
print(f"¿Aprobó? {estudiante2.aprobo()}")