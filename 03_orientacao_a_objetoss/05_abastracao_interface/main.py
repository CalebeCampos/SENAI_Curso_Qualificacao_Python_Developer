import classes as c
import os

def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def main():

    conta_corrente = c.ContaCorrente(
        titular="", 
        cpf="", 
        agencia="0517", 
        numero="000025145-6", 
        saldo=0.0
        )
    
    while True:
        
        print(f"{'-'*20} BANCO COBRA {'-'*20}\n")
        print("1 - Informar dados do titular")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Consultar dados da conta")
        print("5 - Sair do programa")
        opcao = input("Informe a opcao desejada: ").strip()
        limpar_terminal()

        match opcao:
            case "1": # informar dados do titular
                try:
                    nome_titular = input("Informe o nome do titular: ").strip().title()
                    cpf_titular = input("Informe o CPF do titular: ").strip()
                    conta_corrente.titular = nome_titular
                    conta_corrente.cpf = cpf_titular
                    limpar_terminal()
                    print("Dados do titular gravados com sucesso!")
                except Exception as e:
                    print(f"Nao foi possivel informar os dados do titular. Erro: {e}")
                finally:
                    continue
            case "2": # depositar
                try:
                    valor_depositar = float(input("Informe o valor a ser depositado: ").strip().replace(',','.'))
                    limpar_terminal()
                    if valor_depositar > 0:
                        print(f"Valor depositado com sucesso!")
                        print(f"Seu novo saldo é: R$ {conta_corrente.depositar(valor_depositar)}")
                    else:
                        print("Valor invalido! Informe um valor maior que zero.")
                except Exception as e:
                    print(f"Nao foi possivel depositar. Erro: {e}")
                finally:
                    continue
            case "3": # sacar
                try:
                    valor_sacar = float(input("Informe o valor a ser sacado: ").strip().replace(',','.'))
                    limpar_terminal()
                    if valor_sacar > 0:
                        if valor_sacar <= conta_corrente.saldo:
                            print(f"Valor sacado com sucesso!")
                            print(f"Seu novo saldo é: R$ {conta_corrente.sacar(valor_sacar)}")
                        else:
                            print("Saldo insuficiente!")
                    else:
                        print("Valor invalido! Informe um valor maior que zero.")
                except Exception as e:
                    print(f"Nao foi possivel sacar. Erro: {e}")
                finally:
                    continue
            case "4": # consultar dados da conta
                limpar_terminal()
                conta_corrente.consultar_dados()
                continue
            case "5":
                print("Saindo do programa...")
                break
            case _:
                print("Opcao invalida!")
                continue

if __name__ == "__main__":
    main()