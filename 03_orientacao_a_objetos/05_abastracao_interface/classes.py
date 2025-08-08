# para tornar uma classe abstrata é necessario fazer os seguintes importes da biblioteca abc
from abc import ABC
from abc import abstractmethod

# para tornar a classe conta abstrata basta:
# ela ser uma subclasse da classe ABC, class Conta(ABC)
# e adicionar a anotacao @abstractmethod acima do metodo contrutor para impedir a classe de ser instanciada
class Conta(ABC):

    @abstractmethod
    def __init__(self, saldo):
        # encapsulando o atributo saldo
        self.__saldo = saldo

    # metodo getter do atributo saldo
    @property
    def saldo(self):
        return self.__saldo
    
    # metodo setter do atributo saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    # a anotacao @abstractmethod funciona como uma interface, obriga as subclasses a desenvolverem os metodos da superclasse com essa anotacao

    # metodos que as subclasses necessariamente deverão ter, colocar a anotacao @abstractmethod, funciona como interface, ou seja, obriga as subclasses a desenvolverem esses metodos
    @abstractmethod
    def consultar_dados(self):
        pass # o comando pass é o mesmo que reticencias

    # metodos que as subclasses necessariamente deverão ter, colocar a anotacao @abstractmethod, funciona como interface, ou seja, obriga as subclasses a desenvolverem esses metodos
    @abstractmethod
    def depositar(self, valor):
        pass # o comando pass é o mesmo que reticencias

    # metodos que as subclasses necessariamente deverão ter, colocar a anotacao @abstractmethod, funciona como interface, ou seja, obriga as subclasses a desenvolverem esses metodos
    @abstractmethod
    def sacar(self, valor):
        pass # o comando pass é o mesmo que reticencias



# subclasse ContaCorrente herdando da classe Conta
class ContaCorrente(Conta):
    def __init__(self, titular, cpf, agencia, numero, saldo):
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = agencia
        self.__numero = numero
        super().__init__(saldo)

    # metodos get e set...

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

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


    # metodos obrigatorios da interface...

    def consultar_dados(self):
        print(f"{'-'*20} DADOS DA CONTA {'-'*20}\n")
        print(f"Titular: {self.__titular}")
        print(f"CPF: {self.__cpf}")
        print(f"Agencia: {self.__agencia}")
        print(f"Numero: {self.__numero}")
        #print(f"Saldo: R$ {self.__saldo:.2f}")
        #print(f"Saldo: R$ {super().__saldo:.2f}")
        print(f"Saldo: R$ {self.saldo:.2f}")
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo