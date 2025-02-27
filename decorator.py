from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass


class NotificadorEmail(Notificador):
    def enviar(self, mensaje):
        print(f"Enviando email: {mensaje}")

class NotificadorDecorator(Notificador):
    def __init__(self, notificador):
        self.notificador = notificador

    def enviar(self, mensaje):
        self.notificador.enviar(mensaje)


class NotificadorSMS(NotificadorDecorator):
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")


notificador_basico = NotificadorEmail()

notificador_sms = NotificadorSMS(notificador_basico)
print("Enviado con email y SMS: ")
notificador_sms.enviar("Hola, tiene un mensaje")      