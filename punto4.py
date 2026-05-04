# punto4.py
from carros import Carros
from bicicleta import Bicicleta

mi_auto = Carros("Mazda", 200, "Extra")
mi_bici = Bicicleta("GW", 40, True)

print("--- HERENCIA ---")
mi_auto.acelerar()
mi_bici.acelerar()
mi_auto.encender_radio()
