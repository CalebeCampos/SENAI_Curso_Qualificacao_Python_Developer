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

import json
import contas as c
import menus as m
import os

if __name__ == "__main__":
    
    try:
        
        def limpar_console():
            os.system('cls' if os.name == 'nt' else 'clear')

        while True:
            m.menu_principal()
            opcao = input("Opcao desejada: ")

            match opcao:
                
                # CADASTRAR CONTA
                case "1": 
                    limpar_console()
                    nome = input("Informe o nome do titular da conta: ").title()
                    cpf = input("Informe o CPF do titular da conta: ")
                    c.cadastrar_conta(nome, cpf)
                    continue
                
                # LISTAR CONTAS CADASTRADAS
                case "2": 
                    limpar_console()
                    c.listar_contas()
                    continue 
                
                # ALTERAR TITULAR DA CONTA
                case "3": 
                    limpar_console()
                    indice_conta_alterar = int(input("Informe a posicao da conta que deseja alterar: "))
                    if c.validar_conta(indice_conta_alterar):
                        c.imprimir_conta(indice_conta_alterar)
                        while True:
                            m.menu_alteracao_titular()
                            opcao_titular_escolhida = input("Opção desejada: ")
                            match opcao_titular_escolhida:                            
                                    case "1":                                     
                                        novo_titular_nome = input("Informe o nome do novo titular: ")
                                        c.alterar_nome_titular(indice_conta_alterar, novo_titular_nome)
                                        continue                                
                                    case "2":
                                        novo_titular_cpf = input("Informe o CPF do novo titular: ")
                                        c.alterar_cpf_titular(indice_conta_alterar, novo_titular_cpf)
                                        continue                                
                                    case "0":
                                        break
                                    case _:
                                        print("Opcao invalida!")
                                        print("\n")
                                        continue
                    else:
                        print("Conta nao encontrada!")
                    continue
                
                # EXCLUIR CONTA
                case "4": 
                    limpar_console()
                    indice_conta_deletar = int(input("Informe a posicao da conta que deseja deletar: "))
                    if c.validar_conta(indice_conta_deletar) == True:
                        c.imprimir_conta(indice_conta_deletar)
                        c.excluir_conta(indice_conta_deletar)
                    else:
                        print("Conta nao encontrada!")
                    continue
                
                # SACAR
                case "5": 
                    limpar_console()
                    indice_conta_sacar = int(input("Informe a posicao da conta que deseja sacar: "))
                    if c.validar_conta(indice_conta_sacar) == True:
                        c.imprimir_conta(indice_conta_sacar)                    
                        while True:
                            m.menu_saque()
                            opcao_saque_escolhido = input("Opção desejada: ")                  
                            match opcao_saque_escolhido:                                
                                case "1":  
                                    valor_saque = float(input("Valor a ser sacado: ").replace(",","."))
                                    c.sacar(indice_conta_sacar, valor_saque)
                                    continue                            
                                case "0":
                                    break                            
                                case _:
                                    print("Opcao invalida!")
                                    print("\n")
                                    continue
                    else:
                        print("Conta nao encontrada!")
                    continue

                case "6": # DEPOSITAR
                    limpar_console()
                    indice_conta_depositar = int(input("Informe a posicao da conta que deseja depositar: "))
                    if c.validar_conta(indice_conta_depositar) == True:
                        c.imprimir_conta(indice_conta_depositar) 

                        while True:
                            m.menu_deposito()
                            opcao_deposito_escolhida = input("Opção desejada: ")
                            match opcao_deposito_escolhida:
                                case "1":
                                    valor_deposito = float(input("Informe o valor a ser depositado: ").replace(",","."))
                                    c.depositar(indice_conta_depositar, valor_deposito)
                                    continue
                                case "0":
                                    break
                                case _:
                                    print("Opcao invalida!\n")
                                    continue
                    else:
                        print("Conta nao encontrada!")                        
                    continue                           

                case "7": # CONSULTAR SALDO
                    limpar_console()
                    indice_conta_consultar_saldo = int(input("Informe a posicao da conta que deseja consultar o saldo: "))
                    if c.validar_conta(indice_conta_consultar_saldo) == True:
                        c.imprimir_conta(indice_conta_consultar_saldo)
                        c.consultar_saldo(indice_conta_consultar_saldo)
                    else:
                        print("Conta nao encontrada!")
                    continue

                case "8": # IMPRIMIR DADOS DA CONTA (SALVAR EM ARQUIVO)
                    limpar_console()
                    indice_conta_consultar_saldo = int(input("Informe a posicao da conta que deseja consultar o saldo: "))
                    if c.validar_conta(indice_conta_consultar_saldo) == True:
                        nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                        diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()
                        # dados_da_conta = c.contas_cadastradas[indice_conta_consultar_saldo]
                        dados_da_conta = c.imprimir_conta(indice_conta_consultar_saldo)
                        with open(f"{diretorio_arquivo}{nome_arquivo}.json", "w", encoding="utf-8") as t:
                            json.dump(dados_da_conta, t, ensure_ascii=False, indent=4)
                        print("Arquivo JSON criado e salvo com sucesso!")
                    else:
                        print("Conta nao encontrada!")
                    continue

                # SAIR
                case "0": 
                    limpar_console()
                    print("Programa finalizado!")
                    break

                case _:
                    limpar_console()
                    print("Opção invalida!")
                    print("\n")
                    continue

    except Exception as e:
        print(f"Nao foi possivel cadastrar a conta bancaria. Erro: {e}")