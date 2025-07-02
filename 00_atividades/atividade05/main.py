"""
# TODO - atividade: Crie um programa que recebe do usuário o nome e a idade, e em seguida, mostre um menu de filmes com suas respectivas classificações indicativas e salas de exibição. Exemplo:
- Sala 1: A Roda Quadrada - Livre
- Sala 2: A Volta dos Que Não Foram - 12 anos
- Sala 3: Poeira em Alto Mar - 14 anos
- Sala 4: As Tranças do Rei Careca - 16 anos
- Sala 5: A Vingança do Peixe Frito - 18 anos
O usuário deve escolher a sala que está passando o filme que deseja assistir. - Se o usuário tiver a idade mínima ou mais para ver o filme, 
o programa imprime o ingresso com o nome do usuário, a sala, o nome do filme, a data e a hora da compra do ingresso, e deseje bom filme, e em seguida, encerra o programa.
- Se o usuário não tiver a idade mínima para ver o filme, o programa bloqueia a sua entrada, e re-exibe o menu de filmes para que ele escolha outro filme.
"""

import datetime as dt
import os

try:

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    while True:

        print(f"{'-'*20}LISTA DE FILMES{'-'*20}\n")
        print("Escolha um filme para assistir...")
        print("Sala 1: A Roda Quadrada - Livre")
        print("Sala 2: A Volta dos Que Não Foram - 12 anos")
        print("Sala 3: Poeira em Alto Mar - 14 anos")
        print("Sala 4: As Tranças do Rei Careca - 16 anos")
        print("Sala 5: A Vingança do Peixe Frito - 18 anos")

        sala = int(input("\nInforme o filme desejado: "))

        os.system('cls' if os.name == 'nt' else 'clear')

        match sala:
            case 1:
                idade_minima = 0
            case 2:
                idade_minima = 12
            case 3:
                idade_minima = 14
            case 4:
                idade_minima = 16
            case 5:
                idade_minima = 18
            case _:
                idade_minima = idade+1
                print("Opção inválida! Escolha um filme válido.\n")
                continue
        
        if idade >= idade_minima:
            print(f"\nIngresso comprado com sucesso!\n")
            print(f"{'-'*5} Dados de identificação {'-'*5}")
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"{'-'*5} Dados da seção {'-'*5}")
            print(f"Seção: {sala}")
            print(f"Idade minima: {idade_minima}")
            print(f"{'-'*5} Dados da compra {'-'*5}")
            data_compra = dt.today().strftime('%d/%m/%Y')
            hora_compra = dt.datetime.now().strftime('%H:%M:%S')
            print(f"Data: {data_compra}")
            print(f"Hora: {hora_compra}")
            print("Boa seção!\n")
            break
        else:
            print(f"{nome} você não pode assistir este filme.")
            print(f"A idade mínima para este filme é: {idade_minima}")
            print("Escolha outro filme!\n")
            
            continuar = input("Deseja escolher outro filme? (s/n): ").lower()

            match continuar:
                case "s":
                    continue
                case "n":
                    break
                case _:
                    print("Opção inválida!\n")
                    continue

except Exception as e:
    print(f"Nao foi possivel executar o programa. Erro: {e}")

# finally:
#     print("Programa encerrado.")




