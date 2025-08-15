# importando a biblioteca dataclass
from dataclasses import dataclass

# declarando a classe Pessoa
@dataclass
class Pessoa:
    # declarando os atributos
    nome: str
    email: str
    cpf: str
    idade: int
    altura: float

    # metodo especial para retornar os valores dos atributos
    def __str__(self):
        return f"DADOS DA PESSOA\nNome: {self.nome}\nEmail: {self.email}\nCPF: {self.cpf}\nIdade: {self.idade}\nAltura: {self.altura}"
    