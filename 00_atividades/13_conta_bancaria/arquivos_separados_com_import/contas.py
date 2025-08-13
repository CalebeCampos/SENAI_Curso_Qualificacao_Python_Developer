import random
import os

contas_cadastradas = []

def gerar_numero_conta():
    return str(random.randint(10**9, 10**10 - 1))

def cadastrar_conta(nome, cpf):
    conta = {
        "Nome": nome,
        "CPF": cpf,
        "Agencia": "1010",
        "Numero": gerar_numero_conta(),
        "Saldo": 0.0
    }
    contas_cadastradas.append(conta)
    print(f"Conta cadastrada com sucesso!")
    print("\n")

def validar_conta(indice_da_conta):
    if indice_da_conta < 0 or indice_da_conta > len(contas_cadastradas):
        return False
    else:
        return True

def imprimir_conta(indice_da_conta):
    for chave in contas_cadastradas[indice_da_conta]:
        print(f"{chave}: {contas_cadastradas[indice_da_conta].get(chave)}")
    print("\n")

def listar_contas():
    if not contas_cadastradas:
        return print("Nenhuma conta cadastrada!\n")
    else:
        os.system('cls')
        for conta in range(len(contas_cadastradas)):
            print(f"Posicao {conta}:")
            imprimir_conta(conta)
            print("\n")
            
def alterar_nome_titular(indice_da_conta, novo_nome):
    if indice_da_conta < 0 or indice_da_conta > len(contas_cadastradas):
        return print("Conta nao encontrada!\n")
    else:
        contas_cadastradas[indice_da_conta]["Nome"] = novo_nome
        print("Alteração realizada com sucesso!\n")

def alterar_cpf_titular(indice_da_conta, novo_cpf):
    if indice_da_conta < 0 or indice_da_conta > len(contas_cadastradas):
        return print("Conta nao encontrada!\n")
    else:
        contas_cadastradas[indice_da_conta]["CPF"] = novo_cpf
        print("Alteração realizada com sucesso!\n")
        
def excluir_conta(indice_da_conta):
    if indice_da_conta < 0 or indice_da_conta > len(contas_cadastradas):
        return print("Conta nao encontrada!\n")
    else:
        contas_cadastradas.pop(indice_da_conta)
        print("Conta excluida com sucesso!\n")

def consultar_saldo(indice_da_conta):
    if indice_da_conta < 0 or indice_da_conta > len(contas_cadastradas):
        return print("Conta nao encontrada!\n")
    else:
        os.system('cls')
        print("Registro encontrado!\n")
        print(f"Nome: {contas_cadastradas[indice_da_conta].get("Nome")}")
        print(f"Numero: {contas_cadastradas[indice_da_conta].get("Numero")}")
        print(f"SALDO: {contas_cadastradas[indice_da_conta].get("Saldo"):,.2f}\n")

def sacar(indice_da_conta, valor):
    if valor < 0:
        return print("Valor invalido!\n")
    elif valor == 0:
        print("Informe um valor maior que zero!\n")
    elif valor > contas_cadastradas[indice_da_conta].get("Saldo"):
        print("Saldo insuficiente!\n")
    elif valor > 0 and valor <= contas_cadastradas[indice_da_conta].get("Saldo"):
        contas_cadastradas[indice_da_conta]["Saldo"] -= valor
        novo_saldo = contas_cadastradas[indice_da_conta].get("Saldo")
        print(f"Valor R$ {valor} sacado com sucesso!")
        print(f"Seu novo saldo é R$ {novo_saldo}")
        print("Retire as cedulas da maquina...\n")
    else:
        print("Valor invalido!\n")

def depositar(indice_da_conta, valor):
    if valor < 0:
        return print("Informe um valor maior que zero!\n")
    else:
        contas_cadastradas[indice_da_conta]["Saldo"] += valor
        novo_saldo = contas_cadastradas[indice_da_conta]["Saldo"] + valor
        print(f"Valor R$ {valor} depositado com sucesso!\n")
        print(f"Seu novo saldo é R$ {novo_saldo}\n")