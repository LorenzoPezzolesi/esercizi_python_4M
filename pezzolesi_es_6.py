class Pagamento:
    
    def processa_pagamento(self):
        raise NotImplementedError("Questo metodo deve essere implementato nelle classi derivate")


class CartaDiCredito(Pagamento):
    
    def __init__(self, nome_intestatario:str, numero_carta:str, scadenza:str, cvv:str):
        self.nome_intestatario = nome_intestatario
        self.numero_carta = numero_carta
        self.scadenza = scadenza
        self.cvv = cvv

    def processa_pagamento(self):
        print(f"Elaborazione pagamento con Carta di Credito per {self.nome_intestatario}")


class PayPal(Pagamento):
    
    def __init__(self, email:str, password:str):
        self.email = email
        self.password = password

    def processa_pagamento(self):
        print(f"Elaborazione pagamento con PayPal per {self.email}")

def effettua_pagamento(metodo_di_pagamento: Pagamento):
    metodo_di_pagamento.processa_pagamento()

pagamento_carta = CartaDiCredito("Simona Piselli", "2324 5456 5465 2344", "03/26", "386")
pagamento_paypal = PayPal("simona.piselli@gmail.com", "124tro12")

effettua_pagamento(pagamento_carta)  
effettua_pagamento(pagamento_paypal)