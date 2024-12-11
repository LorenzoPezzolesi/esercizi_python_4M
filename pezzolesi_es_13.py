class Stanza:
    def __init__(self,nome:str,superficie:float):
        self.nome = nome
        self.superficie = superficie

class Casa:
    def __init__(self,indirizzo: str,proprietario:str):
        self.indirizzo = indirizzo
        self.proprietario = proprietario
        self.stanze = list[Stanza]()

    def aggiungi_stanza(self,stanza:Stanza):
        self.stanze.append(stanza)



# Creazione dell'istanza di Casa
casa = Casa("Via delle Rose 15", "Maria Rossi")

# Creazione delle istanze di Stanza
soggiorno = Stanza("Soggiorno", 30)
cucina = Stanza("Cucina", 15)
camera = Stanza("Camera da Letto", 20)

# Aggiunta delle stanze alla casa
casa.aggiungi_stanza(soggiorno)
casa.aggiungi_stanza(cucina)
casa.aggiungi_stanza(camera)

# Verifica dell'associazione
print(f"Casa di {casa.proprietario} situata in {casa.indirizzo} contiene le seguenti stanze:")
for stanza in casa.stanze:
    print(f"- {stanza.nome} ({stanza.superficie} mq)")