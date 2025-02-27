from abc import ABC, abstractmethod

# Interfaz base de notificación
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

# Implementación base: Notificación por Email
class NotificadorEmail(Notificador):
    def enviar(self, mensaje):
        print(f"📧 Enviando Email: {mensaje}")

# Decorador base
class NotificadorDecorator(Notificador):
    def __init__(self, notificador):
        self.notificador = notificador

    def enviar(self, mensaje):
        self.notificador.enviar(mensaje)

# Decorador adicional: Notificación por SMS
class NotificadorSMS(NotificadorDecorator):
    def enviar(self, mensaje):
        super().enviar(mensaje)  # Llama al método enviar del decorado (Email)
        print(f"📩 Enviando SMS: {mensaje}")

# Decorador adicional: Notificación en App
class NotificadorApp(NotificadorDecorator):
    def enviar(self, mensaje):
        super().enviar(mensaje)  # Llama al método enviar del decorado (Email o SMS)
        print(f"📱 Enviando notificación en la App: {mensaje}")

# Notificador básico solo con Email
notificador_basico = NotificadorEmail()

# Notificador con Email y SMS
notificador_sms = NotificadorSMS(notificador_basico)

# Notificador con Email, SMS y Notificación en la App
notificador_completo = NotificadorApp(notificador_sms)

# Simulación de notificación por una transacción bancaria
print("🔔 Notificación enviada por una transacción bancaria:")
notificador_completo.enviar("⚠️ Se ha realizado un retiro de $500 de su cuenta.")
