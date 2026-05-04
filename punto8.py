from pajaro import Pajaro
from avion import Avion

# Lista de cosas que vuelan
objetos_voladores = [Pajaro(), Avion()]

print("--- INTERFACES (PUNTO 8) ---")

for item in objetos_voladores:
    item.volar()
