
# superclasse
class Pessoa:
    def __init__(self, telefone, endereco):
        #self.__telefone = telefone # atributo privado, usar dois underscores (private)
        #self._endereco = endereco # atributo protegido, usar um underscore (protected)
        self.__telefone = telefone
        self.__endereco = endereco

    # metodos de acesso getter (obs: os metodos getter devem ser daclarados antes dos metodos setter)

    @property # essa anotacao transforma o metodo em um metodo de acesso getter
    def telefone(self):
        return self.__telefone

    @property # essa anotacao transforma o metodo em um metodo de acesso getter
    def endereco(self):
        return self.__endereco
    
    # metodos de acesso setter

    @telefone.setter # essa anotacao transforma o metodo em um metodo de acesso setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @endereco.setter # essa anotacao transforma o metodo em um metodo de acesso setter
    def endereco(self, endereco):
        self.__endereco = endereco




# subclasses
class PessoFisica(Pessoa):
    def __init__(self, telefone, endereco, nome, cpf):
        super().__init__(telefone, endereco)
        self.__nome = nome
        self.__cpf = cpf

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

class PessoaJuridica(Pessoa):
    def __init__(self, telefone, endereco, nome_fantasia, cnpj):
        super().__init__(telefone, endereco)
        self.__nome_fantasia = nome_fantasia
        self.__cnpj = cnpj

    @property
    def nome_fantasia(self):
        return self.__nome_fantasia
    
    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        self.__nome_fantasia = nome_fantasia

    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj