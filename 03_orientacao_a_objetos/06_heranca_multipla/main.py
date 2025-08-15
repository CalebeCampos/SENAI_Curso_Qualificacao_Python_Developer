import Classe_ContaCorrente as cc
import os

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def main():

    conta = cc.ContaCorrente(
        nome="",
        cpf="",
        email="",
        profissao="",
        telefone="",
        endereco="",
        salario=0.0,
        agencia="0517",
        numero="0000255146-1",
        saldo=0.0)
    
    while True:

        print(f"{'-'*20} BANCO COBRA {'-'*20}")
        print("1 - Cadastrar Conta Corrente")
        print("2 - Exibir dados da conta")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Sair")
        opcao = input("Opcao desejada: ").strip()
        limpar_terminal()

        match opcao:

            case "1":
                try: 
                    conta.nome = input("Informe o nome do titular: ").strip().title()
                    conta.cpf = input("Informe o CPF do titular: ").strip()
                    conta.email = input("Informe o email do titular: ").strip()
                    conta.profissao = input("Informe a profissao do titular: ").strip().title()
                    conta.telefone = input("Informe o telefone do titular: ").strip()
                    conta.endereco = input("Informe o endereco do titular: ").strip().title()
                    conta.salario = float(input("Informe o salario atual do titular: ").strip().replace(',','.'))
                    limpar_terminal()
                    print("Conta cadastrada com sucesso!")
                except Exception as e:
                    print(f"Nao foi possivel cadastrar a conta. Erro: {e}")
                finally:
                    continue

            case "2":
                try: 
                    conta.exibir_dados()
                except Exception as e:
                    print(f"Nao foi possivel exibir os dados da conta. Erro: {e}")
                finally:
                    continue

            case "3":
                try: 
                    valor = float(input("Informe o valor a ser depositado: ").strip().replace(',','.'))
                    limpar_terminal()
                    if valor > 0:
                        print(f"Valor R$ {valor:.2f} depositado com sucesso! Novo saldo: {conta.fazer_deposito(valor)}")
                    else:
                        print("O valor deve ser maior que zero!")
                except Exception as e:
                    print(f"Nao foi possivel depositar o valor. Erro: {e}")
                finally:
                    continue

            case "4":
                try: 
                    valor = float(input("Informe o valor a ser sacado: ").strip().replace(',','.'))
                    limpar_terminal()
                    if valor > 0:
                        if valor <= conta.saldo:
                            print(f"Valor R$ {valor:.2f} sacado com sucesso! Novo saldo: {conta.fazer_saque(valor)}")
                        else:
                            print("Saldo insuficiente!")
                    else: 
                        print("O valor deve ser maior que zero.")
                except Exception as e:
                    print(f"Nao foi possivel sacar o valor. Erro: {e}")
                finally:
                    continue

            case "5":
                print("Saindo do programa...")
                break

            case _:
                print("Opcao invalida!")
                continue

if __name__ == "__main__":
    main()