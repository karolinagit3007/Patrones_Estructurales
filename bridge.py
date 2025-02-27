from abc import ABC, abstractmethod

class Dispositivo(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def set_volume(self, volume):
        pass

class Televisor(Dispositivo):
    def __init__(self):
        self.encendido = False
        self.volume = 0


    def encender(self):
        self.encendido = True
        print("Televisor encendido")

    def apagar(self):
        self.encendido = False
        print("Televisor apagado")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Volumen: {self.volume}")

class Radio(Dispositivo):
    def __init__(self):
        self.encendido = False
        self.volume = 5

    def encender(self):
        self.encendido = True
        print("Radio encendido")

    def apagar(self):
        self.encendido = False
        print("Radio apagado")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Volumen: {self.volume}")