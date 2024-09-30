class Dipendente:
    
    def __init__(self, nome:str, stipendio:int):
        self.nome = nome
        self.stipendio = stipendio
    
    def get_nome(self):
        return self.nome

    def get_stipendio(self):
        return self.stipendio

class Manager(Dipendente):
    
    def __init__(self, nome:str, stipendio:int, numero_di_team:int):
        super().__init__(nome, stipendio)
        self.numero_di_team = numero_di_team
    
    def get_numero_di_team(self):
        return self.numero_di_team

class Sviluppatore(Dipendente):

    def __init__(self,nome:str, stipendio:int,linguaggio_di_programmazione:str):
        super().__init__(nome, stipendio)
        self.linguaggio_di_programmazione = linguaggio_di_programmazione

    def get_linguaggio_di_programmazione(self):
        return self.linguaggio_di_programmazione

manager = Manager("Quinto", 70000, 5)
print(manager.get_nome())  
print(manager.get_stipendio())  
print(manager.get_numero_di_team())  

sviluppatore = Sviluppatore("Simona", 50000, "Python")
print(sviluppatore.get_nome())  
print(sviluppatore.get_stipendio())  
print(sviluppatore.get_linguaggio_di_programmazione())  