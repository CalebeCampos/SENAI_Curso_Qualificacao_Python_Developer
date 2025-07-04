# diretorio: 02_projetos_manipulacao_arquivos/02_manipulando_json/parte07_criando_novo_arquivo_json/

import os
import json

usuarios = []
nome_arquivo = ""

while True:
    usuario = {}
    try:
        print(f"{'='*20} MENU {'='*20}")
        print("1 - Cadastrar novo usuario")
        print("2 - Salvar aquivo JSON")
        print("3 - Fazer leitura do JSON")
        print("4 - Sair do programa")
        opcao = input("Informe a opção desejada: ")
        os.system("cls" if os.name == "nt" else "clear")
        match opcao:
            case "1":
                usuario['nome'] = input("Informe o nome: ").strip().title()
                usuario['idade'] = int(input("Informe a idade: ").strip())
                usuario['email'] = input("Informe o e-mail: ").strip().lower()
                usuarios.append(usuario)
                os.system("cls" if os.name == "nt" else "clear")
                print("Usuario cadastrado com sucesso!")
                continue
            case "2":
                if not nome_arquivo:
                    nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                    diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()
                with open(f"{diretorio_arquivo}{nome_arquivo}.json", "w", encoding="utf-8") as t:
                    json.dump(usuarios, t, ensure_ascii=False, indent=4)
                os.system("cls" if os.name == "nt" else "clear")
                print("Arquivo criado e salvo com sucesso!")
                continue
            case "3":
                nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()
                with open(f"{diretorio_arquivo}{nome_arquivo}.json", "r", encoding="utf-8") as t:
                    lista_usuarios_json = json.load(t) # cria a lista de dicionarios em python
                # exibindo os usuarios cadastrados
                print(f"{'-'*20} LISTA DE USUARIOS {'-'*20}")
                for usuario in usuarios:
                    for chave in usuario:
                        print(f"{chave.capitalize()}: {usuario.get(chave)}")
                    print('-'*40)
                continue
            case "4":
                print("Programa encerrado.")
                break 
            case _:
                print("Opção invalida!")
                continue
    except Exception as e:
        print(f"Não foi possivel salvar o nome arquivo. Erro: {e}")
        continue