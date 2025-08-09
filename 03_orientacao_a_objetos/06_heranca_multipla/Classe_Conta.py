import Interface_Conta

class Conta(Interface_Conta.IConta):
    def __init__(self, agencia, numero, saldo):
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo

    @property
    def agencia(self):
        return self.__agencia
    
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    
    # METODOS DA INTERFACE CONTA, CLASSE ICONTA
    def exibir_dados(self):
        print(f"Agencia: {self.agencia}")
        print(f"Numero: {self.numero}")
        print(f"Saldo: R$ {self.saldo:.2f}")
    
    def fazer_deposito(self, valor):
        self.saldo += valor
        return self.saldo
    
    def fazer_saque(self, valor):
        self.saldo -= valor
        return self.saldo