# punto5.py
from carros import Carros
from bicicleta import Bicicleta

# Creamos los objetos para demostrar la sobreescritura
mi_carro = Carros("Mazda", 220, "Extra")
mi_bici = Bicicleta("GW", 45, True)

print("---  SOBREESCRITURA (Punto 5) ---")

# Aunque usamos el mismo método .acelerar(), cada uno responde diferente
mi_carro.acelerar() # El carro subirá de a 30
mi_bici.acelerar()  # La bici subirá de a 5

print("-" * 40)
print("Nota: El carro y la bici aceleran con valores distintos")
