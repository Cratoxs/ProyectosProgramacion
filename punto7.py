from perro import Perro
from gato import Gato

# Creamos la lista de animales
mis_mascotas = [Perro(), Gato()]

print("--- CLASES ABSTRACTAS (PUNTO 7) ---")

for animal in mis_mascotas:
    animal.hacerSonido()
