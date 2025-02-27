class Luces:
    def encender(self):
        print("💡 Luces encendidas")
    
    def apagar(self):
        print("💡 Luces apagadas")

class AireAcondicionado:
    def encender(self):
        print("❄️ Aire acondicionado encendido")
    
    def apagar(self):
        print("❄️ Aire acondicionado apagado")

class Alarma:
    def activar(self):
        print("🚨 Alarma de emergencia activada")
    
    def desactivar(self):
        print("🚨 Alarma desactivada")

class HospitalInteligente:
    def __init__(self):
        self.luces = Luces()
        self.aire = AireAcondicionado()
        self.alarma = Alarma()

    def modo_emergencia(self):
        print("⚠️ Activando MODO EMERGENCIA...")
        self.luces.encender()
        self.aire.apagar()
        self.alarma.activar()

    def modo_normal(self):
        print("✅ Activando MODO NORMAL...")
        self.luces.apagar()
        self.aire.encender()
        self.alarma.desactivar()

# Simulación del sistema en un hospital
hospital = HospitalInteligente()

hospital.modo_normal()
hospital.modo_emergencia()
