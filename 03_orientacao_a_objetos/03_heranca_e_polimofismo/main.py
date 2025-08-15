import classes as c
import os

# criando uma funcao para limpar o terminal
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# criando uma funcao com toda a logica do programa, que será chamada no final do arquivo
def main():
    # instanciando uma pessoa fisica
    usuario = c.PessoaFisica(nome="",cpf="",telefone="",endereco="")

    # preenchendo os dados do usuario
    print("\nPreencha os dados do usuário:\n")
    usuario.nome = input("Nome: ").strip().title()
    usuario.cpf = input("CPF: ").strip()
    usuario.telefone = input("Telefone: ").strip()
    usuario.endereco = input("Endereço: ").strip().title()
    limpar_terminal()  # limpa o terminal para melhor visualização

    # instanciando uma pessoa juridica
    empresa = c.PessoaJuridica(nome_fantasia="",razao_social="",telefone="",endereco="",cnpj="")

    # preenchendo os dados da empresa
    print("\nPreencha os dados da empresa:\n")
    empresa.nome_fantasia = input("Nome Fantasia: ").strip().title()
    empresa.razao_social = input("Razão Social: ").strip().title()
    empresa.telefone = input("Telefone: ").strip()
    empresa.endereco = input("Endereço: ").strip().title()
    empresa.cnpj = input("CNPJ: ").strip()
    limpar_terminal()  # limpa o terminal para melhor visualização

    # saida de dados
    print("\nDados do Usuário:")
    usuario.exibir_dados()
    print("\nDados da Empresa:")
    empresa.exibir_dados()



# execucao do algoritmo
if __name__ == "__main__":
    main() # chama a funcao com a logica do programa