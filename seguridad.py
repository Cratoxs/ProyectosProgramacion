# seguridad.py

# Creamos nuestra propia excepción personalizada
class ExcesoVelocidadException(Exception):
    """Excepción lanzada cuando el coche supera el límite permitido."""
    pass

class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.velocidad = 0

    def incrementarVelocidad(self, incremento):
        nueva_velocidad = self.velocidad + incremento
        
        # Si supera los 200, lanzamos la alarma (excepción)
        if nueva_velocidad > 200:
            raise ExcesoVelocidadException(f"¡PELIGRO! {nueva_velocidad} km/h supera el límite de 200.")
        
        self.velocidad = nueva_velocidad
        print(f"Velocidad actual de {self.marca}: {self.velocidad} km/h")
