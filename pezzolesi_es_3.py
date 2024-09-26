class Veicolo:
    numero_dei_veicoli = 0

    def __init__(self,tipo:str ,marca: str) -> None:
        self.tipo = tipo
        self.marca = marca
        Veicolo.numero_dei_veicoli += 1 

    @classmethod
    def get_numero_dei_veicoli(cls)-> int:
        return cls.numero_dei_veicoli

print(Veicolo.get_numero_dei_veicoli())  
auto_1 = Veicolo("Auto", "Toyota")
auto_2 = Veicolo("Moto", "Honda")
print(Veicolo.get_numero_dei_veicoli())