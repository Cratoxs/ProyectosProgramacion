# punto9.py
from motor import Motor

class Coche:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # Aquí guardamos el objeto Motor completo

    def describir_completo(self):
        # Usamos el método del motor dentro del coche
        detalles_motor = self.motor.obtener_detalles()
        print(f"Coche: {self.marca} {self.modelo}")
        print(f"Detalles: {detalles_motor}")

# PUNTO 9 ---
#  Creamos primero el motor
mi_motor = Motor(150, "Diesel")

# Se lo pasamos al coche al crearlo
mi_auto = Coche("Volkswagen", "Golf", mi_motor)

print("---  COMPOSICIÓN ---")
mi_auto.describir_completo()
