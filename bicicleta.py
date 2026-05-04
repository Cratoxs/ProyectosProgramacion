from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, vel_max, todo_terreno):
        super().__init__(marca, vel_max)
        self.todo_terreno = todo_terreno

    # Aquí sobreescribimos: la bici sube de 5 en 5 (a pedal)
    def acelerar(self):
        self.velocidad += 5
        print(f"La bicicleta {self.marca} avanza pedaleando a {self.velocidad} km/h")

    def tocar_campana(self):
        print("bueno")
