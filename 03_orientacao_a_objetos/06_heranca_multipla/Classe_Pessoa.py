class Pessoa:
    def __init__(self, nome, cpf, email, profissao, telefone, endereco, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__profissao = profissao
        self.__telefone = telefone
        self.__endereco = endereco
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def profissao(self):
        return self.__profissao
    
    @profissao.setter
    def profissao(self, profissao):
        self.__profissao = profissao
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Email: {self.email}")
        print(f"Profissao: {self.profissao}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereco: {self.telefone}")
        print(f"Salario: {self.salario:.2f}")