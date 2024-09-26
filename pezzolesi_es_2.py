class Contobancario:

    def __init__(self, numero_conto, intestatario, saldo) -> None:
        self.numero_conto = numero_conto
        self.intestatario = intestatario
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def deposita(self, soldi):
        self.__saldo = self.__saldo + soldi

    def preleva(self, soldi):
        self.__saldo = self.__saldo - soldi

conto = Contobancario("573923869", "Simona Piselli", 100000.0)
print(conto.get_saldo())

conto.deposita(50000.0)
print(conto.get_saldo())

conto.preleva(20000.0)
print(conto.get_saldo)