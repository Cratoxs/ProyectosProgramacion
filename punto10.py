# punto10.py
from seguridad import Coche, ExcesoVelocidadException

mi_carro = Coche("Ferrari")

print("---  EXCEPCIONES ---")

try:
    #  1: Velocidad normal
    mi_carro.incrementarVelocidad(120)
    
    #  2: Aquí se va a disparar la excepción
    print("Intentando acelerar a fondo...")
    mi_carro.incrementarVelocidad(100) 

except ExcesoVelocidadException as e:
    # Si ocurre el error, lo atrapamos aquí y mostramos el mensaje
    print(f"Error detectado: {e}")

print("\nEl programa continuó normal gracias al manejo de excepciones.")
