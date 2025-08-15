from dataclasses import dataclass
import Pessoa as p

@dataclass
class PessoaFisica(p.Pessoa):
    nome: str
    cpf: str
    idade: int

    def __str__(self):
        return f"\nDADOS DA PESSOA FISICA\nNome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}\nEmail: {self.email}\nTelefone: {self.telefone}\nEndereco: {self.endereco}\n"
    
#    def __str__(self):
#        return f"{super().__str__()}\nDADOS DA PESSOA FISICA\nNome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}"