"""
Atividade 07 - Crie um programa que faça as seguintes operações:
1. Cadastre novo nome na lista.
2. Liste todos os nomes da lista.
3. Pesquise um nome na lista.
4. Altere um nome na lista.
5. Exclua um nome da lista.
6. Sair do programa.
Obs: A lista deve começar vazia.
"""

import os

nomes = []

while True:

    print(f"{'='*10} MENU {'='*10}\n")
    print("1. Cadastrar novo nome")
    print("2. Listar todos os nomes")
    print("3. Pesquisar um nome")
    print("4. Alterar um nome")
    print("5. Excluir um nome")
    print("6. Sair do programa")
    print("\n")
    opcao =  input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            try:
                nome_cadastrar = input("Informe o nome a ser cadastrado: ").title().strip()
                nomes.append(nome_cadastrar)
                print("Nome cadastrado com sucesso!\n")
            except Exception as e:
                print(f"Ocorreu um erro ao cadastrar o nome. Erro: {e}\n")
            finally:
                continue
        case "2":
            if not nomes:
                print("Nenhum nome cadastrado.\n")
            else:
                print("Lista de nomes cadastrados:")
                for i in range(len(nomes)):
                    print(f"Indice {i}: {nomes[i]}")
                print("\n")
            continue                
        case "3":
            nome_pesquisar = input("Informe o nome a ser pesquisado: ").title().strip()
            if nome_pesquisar not in nomes:
                print(f"O nome '{nome_pesquisar}' não está na lista.\n")
            else:
                quantidade = nomes.count(nome_pesquisar)
                print(f"O nome '{nome_pesquisar}' aparece {quantidade} vezes na lista.")
                indice_nome_pesquisado = nomes.index(nome_pesquisar)
                print(f"A primeira ocorrência do nome '{nome_pesquisar}' está no índice {indice_nome_pesquisado}.\n")
            continue
        case "4":
            try:
                indice_alterar = int(input("Informe o índice do nome a ser alterado: "))
                if indice_alterar < 0 or indice_alterar >= len(nomes):
                    print("Índice inválido.\n")
                else:
                    nome_alterar = input("Informe o nome a ser alterado: ").title().strip()
                    nomes[indice_alterar] = nome_alterar
                    print("Nome alterado com sucesso!\n")
            except Exception as e:
                print(f"Ocorreu um erro ao alterar o nome. Erro: {e}\n")
            finally:
                continue
        case "5":
            try:
                indice_excluir = int(input("Informe o índice do nome a ser excluído: "))
                if indice_excluir < 0 or indice_excluir >= len(nomes):
                    print("Índice inválido.\n")
                else:
                    del(nomes[indice_excluir])
                    print("Nome excluído com sucesso!\n")
            except Exception as e:
                print(f"Ocorreu um erro ao excluir o nome. Erro: {e}\n")
            finally:
                continue
        case "6":
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Tente novamente.\n")
            continue
