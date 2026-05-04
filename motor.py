# motor.py
class Motor:
    def __init__(self, potencia, tipo):
        self.potencia = potencia
        self.tipo = tipo

    def obtener_detalles(self):
        return f"Motor {self.tipo} de {self.potencia} CV"
