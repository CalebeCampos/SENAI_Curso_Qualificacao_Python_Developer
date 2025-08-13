import Classes as c
import os

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    
    proprietario = c.Pessoa(
        nome="",
        cpf="",
        email="",
        telefone="",
        endereco=""
    )

    print("DADOS DO PROPRIETARIO")
    proprietario.nome = input("Informe o nome: ").strip().title()
    proprietario.cpf = input("informe o CPF: ").strip()
    proprietario.email = input("Informe o email: ").strip().lower()
    proprietario.telefone =  input("Informe o telefone: ").strip()
    proprietario.endereco = input("Informe o endereco: ").strip().title()

    carro = c.Veiculo(
        fabricante="",
        modelo="",
        ano="",
        cor="",
        placa="",
        proprietario=""
    )

    print("DADOS DO VEICULO")
    carro.fabricante = input("Informe o fabricante: ").strip().title()
    carro.modelo = input("Informe o modelo: ").strip().title()
    carro.ano = input("Informe o ano: ").strip()
    carro.cor = input("Informe a cor: ").strip().title()
    carro.placa = input("Informe a placa: ").strip().upper()
    carro.proprietario = proprietario

    limpar_terminal()

    print("Dados do veiculo...")
    print(carro.exibir_dados_veiculo())
    print("Dados do proprietario do veiculo")
    print(carro.exibir_dados_proprietario())

if __name__ == "__main__":
    main()