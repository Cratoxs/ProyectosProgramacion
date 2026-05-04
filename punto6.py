# punto6.py
from carros import Carros
from bicicleta import Bicicleta

# 1. Creamos una lista que mezcla diferentes tipos de objetos
mis_vehiculos = [
    Carros("Ferrari", 320, "Extra"),
    Bicicleta("GW", 40, True),
    Carros("Renault", 160, "Corriente"),
    Bicicleta("Shimano", 35, False)
]

print("--- POLIMORFISMO ---")

# 2. Recorremos la lista con un bucle 'for'
for v in mis_vehiculos:
    # Invocamos el mismo método en cada uno
    # El Carro acelerará de a 30 y la Bici de a 5 automáticamente
    v.acelerar()

print("-" * 45)
print(" Una sola orden hizo que cada uno actuara a su manera.")
