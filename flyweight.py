class TipoEnemigo:
    def __init__(self, nombre, textura, sonido):
        self.nombre = nombre
        self.textura = textura
        self.sonido = sonido

    def mostrar(self, x, y):
        print(f"Mostrando {self.nombre} en ({x}, {y}) con la textura {self.textura} y el sonido {self.sonido}")


class FabricaEnemigos:
    _tipos = {}

    @staticmethod
    def obtener_tipo_enemigo(nombre, textura, sonido):
        if nombre not in FabricaEnemigos._tipos:
            print(f"Creando nuevo tipo de enemigo: {nombre}")
            FabricaEnemigos._tipos[nombre] = TipoEnemigo(nombre, textura, sonido)
        return FabricaEnemigos._tipos[nombre]
    

class Enemigo:
    def __init__(self, tipo, x, y):
        self.x = x
        self.y = y
        self.tipo = tipo

    def dibujar(self):
        self.tipo.mostrar(self.x, self.y)


tipo_orco = FabricaEnemigos.obtener_tipo_enemigo("Orco", "orco.png", "sonido_orco.mp3")
tipo_elfo = FabricaEnemigos.obtener_tipo_enemigo("Elfo", "elfo.png", "sonido_elfo.mp3")

enemigos = [
    Enemigo(tipo_orco, 10, 20),
    Enemigo(tipo_orco, 50, 20),
    Enemigo(tipo_elfo, -10, 20),
    Enemigo(tipo_elfo, 0, 0),
]

for enemigo in enemigos:
    enemigo.dibujar()
