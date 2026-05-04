 # clase carro 
class Carro:
    def __init__(self, nombre, marca, modelo, año):
      
        self.__nombre = nombre
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def set_marca(self, nueva_marca):
        self.__marca = nueva_marca

    def set_modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo

    def info_carro(self):
       
        print(f"{self.__nombre}: {self.__marca} {self.__modelo} año {self.__año}")
