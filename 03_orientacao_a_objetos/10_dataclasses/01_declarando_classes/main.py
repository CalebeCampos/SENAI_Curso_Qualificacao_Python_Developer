import Pessoa as p
import os

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    # instanciando a classe Pessoa
    usuario = p.Pessoa(
        nome="",
        email="",
        cpf="",
        idade=0,
        altura=0.0
    )
    # atribuindo valores aos atributos do objeto usuario da classe Pessoa
    usuario.nome = input("Informe seu nome: ").strip().title()
    usuario.email = input("Informe seu email: ").strip().lower()
    usuario.cpf = input("Informe seu CPF: ").strip()
    usuario.idade = int(input("Informe seu idade: ").strip().replace(',','.'))
    usuario.altura = float(input("Informe seu altura: ").strip().replace(',','.'))
    limpar_terminal()
    # exibindo os valores dos atributos do objeto usuario da classe Pessoa, invocando o metodo especial __str__
    print(usuario)

if __name__ == "__main__":
    main()
