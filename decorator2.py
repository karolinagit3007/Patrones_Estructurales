from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

class NotificadorEmail(Notificador):
    def enviar(self, mensaje):
        print(f"📧 Enviando Email: {mensaje}")

class NotificadorDecorator(Notificador):
    def __init__(self, notificador):
        self.notificador = notificador

    def enviar(self, mensaje):
        self.notificador.enviar(mensaje)

class NotificadorSMS(NotificadorDecorator):
    def enviar(self, mensaje):
        super().enviar(mensaje)  
        print(f"📩 Enviando SMS: {mensaje}")

class NotificadorApp(NotificadorDecorator):
    def enviar(self, mensaje):
        super().enviar(mensaje)  
        print(f"📱 Enviando notificación en la App: {mensaje}")

notificador_basico = NotificadorEmail()

notificador_sms = NotificadorSMS(notificador_basico)

notificador_completo = NotificadorApp(notificador_sms)

print("🔔 Notificación enviada por una transacción bancaria:")
notificador_completo.enviar("⚠️ Se ha realizado un retiro de $500 de su cuenta.")
