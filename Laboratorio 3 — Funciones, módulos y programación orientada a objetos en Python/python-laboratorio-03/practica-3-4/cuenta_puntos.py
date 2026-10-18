class CuentaPuntos:
    def __init__(self, titular):
        self._titular = titular
        self._puntos = 0  
    @property
    def titular(self):
        return self._titular

    @property
    def puntos(self):
        return self._puntos
    def sumar(self, cantidad):
        if cantidad <= 0:
            return False
        
        self._puntos += cantidad
        return True


    def canjear(self, cantidad):
        if cantidad <= 0:
            return False
        
        if cantidad > self._puntos:
            return False
        
        self._puntos -= cantidad
        return True

cuenta = CuentaPuntos("Carlos Gómez")

print(f"Titular: {cuenta.titular}")
print(f"Puntos iniciales: {cuenta.puntos}")
resultado_suma = cuenta.sumar(80)
print(f"Sumar: 80 -> {'aceptado' if resultado_suma else 'rechazado'}")
resultado_canje1 = cuenta.canjear(30)
print(f"Canjear: 30 -> {'aceptado' if resultado_canje1 else 'rechazado'}")
resultado_canje2 = cuenta.canjear(100)
print(f"Canjear: 100 -> {'aceptado' if resultado_canje2 else 'rechazado'}")
print(f"Total de puntos actuales: {cuenta.puntos}")