from dataclasses import dataclass
import Pessoa as p

@dataclass
class PessoaJuridica(p.Pessoa):
    nome_fantasia: str
    razao_social: str
    cnpj: str

    def __str__(self):
        return f"\nDADOS DA PESSOA JURIDICA\nNome Fantasia: {self.nome_fantasia}\nRazao Social: {self.razao_social}\nCNPJ: {self.cnpj}\nEmail: {self.email}\nTelefone: {self.telefone}\nEndereco: {self.endereco}\n"
    
#    def __str__(self):
#        return f"{super().__str__()}\nDADOS DA PESSOA JURIDICA\nNome Fantasia: {self.nome_fantasia}\nRazao Social: {self.razao_social}\nCNPJ: {self.cnpj}\nEmail: {self.email}\nTelefone: {self.telefone}\nEndereco: {self.endereco}\n"
