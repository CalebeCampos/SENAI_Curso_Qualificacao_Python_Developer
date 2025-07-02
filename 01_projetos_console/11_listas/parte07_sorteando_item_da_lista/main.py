import os
import random

nomes = []

while True:
    print(f"{'='*10} MENU {'='*10}\n")
    print("1. Inserir nome")
    print("2. Listar nomes")
    print("3. Sortear nome")
    print("4. Sair do programa")
    print("\n")
    opcao =  input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            try:
                nome_inserir = input("Informe o nome a ser inserido: ").title().strip()
                nomes.append(nome_inserir)
                print("Nome cadastrado com sucesso!\n")
            except Exception as e:
                print(f"Ocorreu um erro ao inserir o nome: {e}\n")
            finally:   
                continue
        case "2":
            if not nomes:
                    print("Nenhum nome cadastrado.\n")
            else:
                nomes.sort() # ordenando a lista de nomes
                print("Lista de nomes cadastrados:")
                for nome in nomes:
                    print(f"- {nome}")
                print("\n")
            continue
        case "3":
            if not nomes:
                print("Nenhum nome cadastrado para sortear.\n")
            else: 
                # sorteio de um nome aleatório usando random.choice que escolhe um elemento aleatório da lista
                # nome_sorteado = random.choice(nomes)

                # sorteio de um nome aleatório usando random.randint pelo indice dos elementos na lista
                indice_sorteado = random.randint(0, len(nomes) - 1)
                nome_sorteado = nomes[indice_sorteado]
                print(f"O nome sorteado é: {nome_sorteado}\n")
            continue
        case "4":
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Tente novamente.\n")
            continue