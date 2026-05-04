from vehiculo import Vehiculo

class Carros(Vehiculo):
    def __init__(self, marca, vel_max, tipo_gasolina):
        super().__init__(marca, vel_max)
        self.gasolina = tipo_gasolina

    # Aquí sobreescribimos el método: el carro sube de 30 en 30
    def acelerar(self):
        self.velocidad += 30
        print(f"El coche {self.marca} acelera rápido a {self.velocidad} km/h")

    def encender_radio(self):
        print(f"Radio del {self.marca} encendida.")
