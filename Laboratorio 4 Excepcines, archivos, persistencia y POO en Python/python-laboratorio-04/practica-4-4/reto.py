class Notificacion:
    def enviar(self, mensaje):
        raise NotImplementedError

class NotificacionCorreo(Notificacion):
    def enviar(self, mensaje):
        print(f"[CORREO] Enviando email: '{mensaje}'")

class NotificacionConsola(Notificacion):
    def enviar(self, mensaje):
        print(f"[CONSOLA] Mostrando en pantalla: '{mensaje}'")

# Colección y recorrido polimórfico
notificaciones = [NotificacionCorreo(), NotificacionConsola()]
mensaje_prueba = "Alerta: Stock mínimo alcanzado."

for n in notificaciones:
    n.enviar(mensaje_prueba)