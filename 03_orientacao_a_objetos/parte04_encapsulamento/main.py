import classes as c
import os

limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():

    usuario = c.PessoFisica(telefone="", endereco="", nome="", cpf="")
    empresa = c.PessoaJuridica(telefone="", endereco="", nome_fantasia="", cnpj="")

    # setando os valores dos atributos do objeto usuario, com encapsulamento
    print("Informe os dados do usuario:\n")
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o cpf: ").strip()
    usuario.telefone = input("Informe o telefone: ").strip()
    usuario.endereco = input("Informe o endereco: ").strip().title()
    limpar_terminal()

    # setando os valores dos atributos do objeto empresa, com encapsulamento
    print("Informe os dados da empresa:\n")
    empresa.nome_fantasia = input("Informe o nome fantasia: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.telefone = input("Informe o telefone: ").strip()
    empresa.endereco = input("Informe o endereco: ").strip().title()
    limpar_terminal()

    # usando os metodos getter do objeto usuario
    print(f"\nDados do usuario:\n")
    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"Telefone: {usuario.telefone}")
    print(f"Endereco: {usuario.endereco}")

    # usando os metodos getter do objeto empresa
    print(f"\nDados da empresa:\n")
    print(f"Nome Fantasia: {empresa.nome_fantasia}")
    print(f"CNPJ: {empresa.cnpj}")
    print(f"Telefone: {empresa.telefone}")
    print(f"Endereco: {empresa.endereco}")

if __name__ == "__main__":
    main()