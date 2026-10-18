class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre


class Instructor(Empleado):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre)
        self.especialidad = especialidad


instructor = Instructor("Ana", "Python")

print(instructor.nombre)
print(instructor.especialidad)


###

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje

    def __str__(self):
        return f"Moto -> Marca: {self.marca} | Modelo: {self.modelo} | Cilindraje: {self.cilindraje}cc"

moto1 = Motocicleta("Yamaha", "R15", 155)
moto2 = Motocicleta("Kawasaki", "Ninja 400", 399)
print(moto1)
print(moto2)