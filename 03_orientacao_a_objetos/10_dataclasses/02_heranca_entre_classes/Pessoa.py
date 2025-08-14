from dataclasses import dataclass

@dataclass # esta anotacao utiliza os mecanismos da biblioteca dataclasses para a confeccao da dataclasse
class Pessoa:
    email: str
    telefone: str
    endereco: str

#    def __str__(self):
#        return f"DADOS DA PESSOA\nNome: {self.email}\nCPF: {self.telefone}\nIdade: {self.endereco}"
