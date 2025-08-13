"""
Atividade 13: Crie um programa de aplicativo de banco, onde:
- O usuário cria uma conta no banco com os seguintes dados:
-- Titular da conta
-- CPF do titular
-- Agência
-- Número da conta
-- Saldo
O usuário pode fazer no programa:
- Consultar dados
- Depositar valor
- Sacar valor
- Imprimir extrato (entende-se: gerar arquivo com os dados da conta)
- Sair do programa
# NOTE - o nome da classe é Conta
"""

import os
import classe as c

limpar_terminal = lambda: os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    # instanciando a classe Conta, sem dados iniciais
    conta_cadastrada = c.Conta(
        titular="",
        cpf="",
        agencia="",
        conta="",
        saldo=0.0
    )
    # definindo os dados da conta
    try:
        conta_cadastrada.titular = input("Digite o nome do titular da conta: ").strip().title()
        conta_cadastrada.cpf = input("Digite o CPF do titular: ").strip()
        conta_cadastrada.agencia = "0537"
        conta_cadastrada.conta = "10894-2"
        limpar_terminal()
        print("Conta criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar conta. Erro: {e}")
    
    while True:
        
        print(f"{'-'*20} BANCO COBRA {'-'*20}")
        print("1 - Consultar dados")
        print("2 - Depositar valor")
        print("3 - Sacar valor")
        print("4 - Imprimir extrato (arquivo JSON)")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")
        limpar_terminal()

        match opcao:

            case "1": # consultar dados
                conta_cadastrada.consultar_dados()
                continue

            case "2": # depositar valor
                try:
                    valor = float(input("Digite o valor a ser depositado: R$ ").strip().replace(',', '.'))
                    limpar_terminal()
                    if valor > 0:
                        conta_cadastrada.depositar(valor)
                        print(f"Depósito realizado com sucesso! Saldo: R$ {conta_cadastrada.mostrar_saldo():.2f}")
                    else: 
                        print("Valor inválido. O valor deve ser maior que zero.")
                except Exception as e:
                    print(f"Erro ao depositar valor. Erro: {e}")
                finally:
                    continue

            case "3": # sacar valor
                try:
                    valor = float(input("Digite o valor a ser sacado: R$ ").strip().replace(',', '.'))
                    limpar_terminal()
                    if valor > 0:
                        if valor <= conta_cadastrada.saldo:
                            conta_cadastrada.sacar(valor)
                            print(f"Saque realizado com sucesso! Saldo: R$ {conta_cadastrada.mostrar_saldo():.2f}")
                        else:
                            print("Saldo insuficiente.")
                    else:
                        print("Valor inválido. O valor deve ser maior que zero.")
                except Exception as e:
                    print(f"Erro ao sacar valor. Erro: {e}")
                finally:
                    continue

            case "4": # imprimir extrato
                try:
                    nome_arquivo = input("Digite o nome do arquivo para salvar o extrato: ").strip()
                    diretorio_arquivo = input("Digite o diretório para salvar o extrato: ").strip()
                    conta_cadastrada.imprimir_extrato(nome_arquivo, diretorio_arquivo)
                    print(f"Arquivo salvo com sucesso: {diretorio_arquivo}{nome_arquivo}.json")
                except Exception as e:
                    print(f"Erro ao imprimir extrato. Erro: {e}")
                finally:
                    continue

            case "5": # sair do programa
                limpar_terminal()
                print("Saindo do programa...")
                break
            
            case _:
                limpar_terminal()
                print("Opção inválida. Tente novamente.")
                continue