import json

class Conta:

    # contrutor da classe Conta
    def __init__(self, titular, cpf, agencia, conta, saldo):
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    # metodos
    def consultar_dados(self):
        print(f"Titular: {self.titular}")
        print(f"CPF: {self.cpf}")
        print(f"Agência: {self.agencia}")
        print(f"Conta: {self.conta}")
        print(f"Saldo: R$ {self.saldo:.2f}")

    def mostrar_saldo(self):
        return self.saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor
    
    def imprimir_extrato(self, nome_arquivo, diretorio_arquivo):
        # para salvar os atributos da conta em um arquivo JSON, será necessario criar um dicionario
        # com os dados da conta, para serializar em JSON e so depois salvar em um arquivo JSON
        dados_conta = {
            "Titular": self.titular,
            "CPF": self.cpf,
            "Agência": self.agencia,
            "Conta": self.conta,
            "Saldo": f"R$ {self.saldo:.2f}"
        }
        # salva os dados da conta em um arquivo JSON
        with open(f"{diretorio_arquivo}{nome_arquivo}.json", "w", encoding="utf-8") as t:
            json.dump(dados_conta, t, ensure_ascii=False, indent=4)
        print("Arquivo JSON criado e salvo com sucesso!")
