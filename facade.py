class Luces:
    def encender(self):
        print("Luces encendidas")
    
    def apagar(self):
        print("Luces apagadas")

class AireAcondicionado:
    def encender(self):
        print("Aire acondicionado encendido")
    
    def apagar(self):
        print("Aire acondicionado apagado")

class Televisor:
    def encender(self):
        print("Televisor encendido")
    
    def apagar(self):
        print("Televisor apagado")

class HogarInteligente:
    def __init__(self):  
        self.luces = Luces()
        self.aire = AireAcondicionado()
        self.tv = Televisor()

    def modo_noche(self):
        print("Activando modo noche...")
        self.luces.encender()
        self.aire.apagar()
        self.tv.encender()
    
    def modo_dia(self):
        print("Activando modo dia...")
        self.luces.apagar()
        self.aire.encender()
        self.tv.apagar()

casa = HogarInteligente()

casa.modo_dia()
casa.modo_noche()
