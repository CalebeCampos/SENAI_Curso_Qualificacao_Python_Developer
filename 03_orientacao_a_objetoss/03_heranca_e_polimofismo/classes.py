# superclasse ou classe pai
class Pessoa:
    # construtor
    def __init__(self, telefone, endereco):
        self.telefone = telefone
        self.endereco = endereco

    def exibir_dados(self):
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")



# subclasse ou classe filha PessoaFisica
class PessoaFisica(Pessoa):
    # construtor
    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        # chama o construtor da classe pai
        super().__init__(telefone, endereco)

    # aplicando o polimorfismo, sobrescrevendo o metodo exibir_dados
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        # executa a mesma acao do metodo da classe pai
        super().exibir_dados()



# subclasse ou classe filha PessoaJuridica
class PessoaJuridica(Pessoa):
    # construtor
    def __init__(self, nome_fantasia, razao_social, telefone, endereco, cnpj):
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        # chama o construtor da classe pai
        super().__init__(telefone, endereco)
        self.cnpj = cnpj

    # aplicando o polimorfismo, sobrescrevendo o metodo exibir_dados
    def exibir_dados(self):
        print(f"Nome Fantasia: {self.nome_fantasia}")
        print(f"Razão Social: {self.razao_social}")
        print(f"CNPJ: {self.cnpj}")
        # executa a mesma acao do metodo da classe pai
        super().exibir_dados()
