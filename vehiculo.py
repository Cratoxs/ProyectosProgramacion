# vehiculo.py
class Vehiculo:
    def __init__(self, marca, vel_max):
        self.marca = marca
        self.velocidad = 0
        self.vel_max = vel_max

    def acelerar(self):
        self.velocidad += 15
        print(f"El {self.marca} aceleró a {self.velocidad} km/h")
