'''
# TODO: atividade 06 - crie um programa em que o usuario informa um ano e o programa exibe todo o calendario daquele ano.
# NOTE: o usuario podera informar qualquer ano a partir de 1900.
# NOTE: use a biblioteca calendar para exibir o calendario.
'''

import calendar

try:

    while True:

        ano = int(input("Informe um ano (a partir de 1900): "))

        if ano < 1900:
            print("Ano inválido! O ano deve ser a partir de 1900.")
            continue
        else:
            print(calendar.TextCalendar().formatyear(ano))

        continuar = input("Deseja informar outro ano? (s/n): ").strip().lower()

        match continuar:
            case "s":
                continue
            case "n":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida!\n")
                continue

except Exception as e:
    print(f"Nao foi possivel executar o programa. Erro: {e}")