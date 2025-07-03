import os
import json

usuarios = []

while True:
    usuario = {}
    try:
        print(f"{'='*20} MENU {'='*20}")
        print("1 - Cadastrar novo usuario")
        print("2 - Salvar aquivo JSON")
        print("3 - Fazer leitura do JSON")
        print("4 - Sair do programa")
        opcao = input("Informe a opção desejada: ")

        match opcao:
            case "1":
                ...
            case "2":
                ...
            case "3":
                ...
            case "4":
                print("Programa encerrado.")
                break                
            case _:
                print("Opção invalida!")
                continue




    except Exception as e:
        print(f"Não foi possivel salvar o nome arquivo. Erro: {e}")
        continue