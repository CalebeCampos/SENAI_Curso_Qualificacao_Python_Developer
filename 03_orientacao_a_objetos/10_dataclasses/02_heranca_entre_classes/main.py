import os
import PessoaFisica as pf
import PessoaJuridica as pj

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = pf.PessoaFisica(
        email="",
        telefone="",
        endereco="",
        nome="",
        cpf="",
        idade=0
    )
    print("Informe os dados do usuario:\n")
    usuario.nome = input("Informe seu nome: ").strip().title()
    usuario.cpf = input("Informe seu CPF: ").strip()
    usuario.idade = int(input("Informe sua idade: ").strip())
    usuario.email = input("Informe seu email: ").strip().lower()
    usuario.telefone = input("Informe seu telefone: ").strip()
    usuario.endereco = input("Informe seu endereco: ").strip().upper()
    limpar_terminal()

    empresa = pj.PessoaJuridica(
        email="",
        telefone="",
        endereco="",
        nome_fantasia="",
        razao_social="",
        cnpj=""
    )
    print("Informe os dados da empresa:\n")
    empresa.razao_social = input("Informe a razao social: ").strip().title()
    empresa.nome_fantasia = input("Informe a nome fantasia: ").strip().title()
    empresa.cnpj = input("Informe o cnpj: ").strip()
    empresa.email = input("Informe o email da empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereco da empresa: ").strip().upper()
    limpar_terminal()

    print(usuario)
    print(empresa)

if __name__ == "__main__":
    main()
