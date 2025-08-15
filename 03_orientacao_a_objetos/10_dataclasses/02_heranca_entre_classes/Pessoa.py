from dataclasses import dataclass
from abc import ABC
from abc import abstractmethod

@dataclass # esta anotacao utiliza os mecanismos da biblioteca dataclasses para a confeccao da dataclasse
class Pessoa(ABC):
    email: str
    telefone: str
    endereco: str

    @abstractmethod # essa anotacao deixa a classe abstrata, ou seja, nao podera ser instanciada. necessario colocar essa anotacao em qualquer metodo para deixar a classe abastrata
    def __str__(self):
        return f"DADOS DA PESSOA\nNome: {self.email}\nCPF: {self.telefone}\nIdade: {self.endereco}"
