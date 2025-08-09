import Classe_Pessoa as p
import Classe_Conta as c

class ContaCorrente(p.Pessoa, c.Conta):
    def __init__(self, nome, cpf, email, profissao, telefone, endereco, salario, agencia, numero, saldo):
        p.Pessoa.__init__(self, nome, cpf, email, profissao, telefone, endereco, salario)
        c.Conta.__init__(self, agencia, numero, saldo)

    # polimorfismo, continuando o metodo exibir_dados
    def exibir_dados(self):
        print(f"{'-'*20} DADOS DA CONTA {'-'*20}")
        p.Pessoa.exibir_dados(self)
        c.Conta.exibir_dados(self)
