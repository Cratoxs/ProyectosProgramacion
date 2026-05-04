#importamos clase carro 
from coche import Carro

mi_carro = Carro("Mi auto", "Toyota", "Fortuner", 2026)

carro1 = Carro("Auto 1", "Chevrolet", "Onix", 2023)
carro2 = Carro("Auto 2", "Audi", "A4", 2020)
carro3 = Carro("Auto 3", "Willys", "Jeep", 1954)

# Mostrarlos
mi_carro.info_carro()
carro1.info_carro()
carro2.info_carro()
carro3.info_carro()
