"""
Atividade 10 - faça um CRUD (create, read, update, delete) em um JSON.

Opções de menu:
- Criar novo arquivo JSON (informar o diretorio que deseja salvar).
- Abrir arquivo JSON.
- Cadastrar novo usuario.
- Listar usuarios cadastrados.
- Pesquisar por um usuario (pelo valor de uma chave) de arquivo JSON.
- Alterar dados de um usuario especifico em um arquivo JSON.
- Deletar um usuario especifico de um arquivo JSON.
- Sair do programa.
- OBS: mostar nome do arquivo JSON e diretorio que foi salvo ou lido

Dados do usuario:
- Nome
- Data de Nascimento
- CPF
- Email
- Telefone
- Filme favorito
"""


import os
import json

nome_arquivo = ""
diretorio_arquivo = ""
lista_de_usuarios = []
tupla_chaves_de_usuario = (
    "Nome", 
    "Data de Nascimento",
    "CPF",
    "E-mail",
    "Telefone",
    "Filme Favorito"
    )


while True: 

    print(f"{"="*30} MENU {"="*30}")
    print("1. Criar/Salvar arquivo JSON.")
    print("2. Ler/Abrir arquivo JSON.")
    print("3. Cadastrar usuario.")
    print("4. Listar usuários.")
    print("5. Pesquisar usuario especifico.")
    print("6. Alterar usuário.")
    print("7. Excluir usuário.")
    print("8. Sair do programa")
    print(f"Arquivo aberto: {nome_arquivo}{'.json' if not nome_arquivo else ''}")
    print(f"Diretorio do arquivo: {diretorio_arquivo if not diretorio_arquivo else ''}")
    opcao_menu_principal = input("Informe a opção desejada: ").strip()
    os.system('cls' if os.name == 'nt' else 'clear')

    match opcao_menu_principal:
        # CRIAR OU SALVAR ARQUIVO JSON
        case "1":
            try:
                nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                diretorio_arquivo = input("Informe o diretorio do arquivo: ").strip()
                with open(f"{diretorio_arquivo}{nome_arquivo}.json", "w", encoding="utf-8") as t:
                    json.dump(lista_de_usuarios, t, ensure_ascii=False, indent=4)
                os.system("cls" if os.name == "nt" else "clear")
                print("Arquivo criado ou salvo com sucesso!")
            except Exception as e:
                print(f"Não foi possivel criar ou salvar o arquivo json. Erro: {e}")
            continue
        # LER OU ABRIR O ARQUIVO JSON
        case "2":
            try:
                if not nome_arquivo:
                    nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                    diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()
                with open(f"{diretorio_arquivo}{nome_arquivo}.json", "r", encoding="utf-8") as t:
                    lista_usuarios_json = json.load(t)
                # exibindo os usuarios salvos no arquivo json
                print(f"{'-'*20} LISTA DE USUARIOS {'-'*20}")
                for usuario in lista_usuarios_json:
                    for chave in usuario:
                        print(f"{chave.capitalize()}: {usuario.get(chave)}")
                    print('-'*40)
            except Exception as e:
                print(f"Não foi possivel abrir ou ler o arquivo json. Erro: {e}")
            continue
        # CADASTRAR USUARIO
        case "3":
            try:
                print("Informe os seguintes dados do usuario...")
                usuario = {
                    tupla_chaves_de_usuario[0]: input(f"{tupla_chaves_de_usuario[0]}: ").strip().title(), # nome
                    tupla_chaves_de_usuario[1]: input(f"{tupla_chaves_de_usuario[1]} (dd/mm/yyyy): ").strip(), # data de nascimento
                    tupla_chaves_de_usuario[2]: input(f"{tupla_chaves_de_usuario[2]} (000.000.000-00): ").strip(), # cpf
                    tupla_chaves_de_usuario[3]: input(f"{tupla_chaves_de_usuario[3]}: ").strip().lower(), # e-mail
                    tupla_chaves_de_usuario[4]: input(f"{tupla_chaves_de_usuario[4]} (DDD0000000000): ").strip(), # telefone
                    tupla_chaves_de_usuario[5]: input(f"{tupla_chaves_de_usuario[5]}: ").strip().title() # filme
                }
                lista_de_usuarios.append(usuario)
                os.system("cls" if os.name == "nt" else "clear")
                print("Usuario cadastrado com sucesso!")
            except Exception as e:
                print("Não foi possivel cadastrar usuario. Erro: {e}")
            continue
        # LISTAR USUARIOS
        case "4":
            try:
                if not nome_arquivo:
                    nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                    diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()
                with open(f"{diretorio_arquivo}{nome_arquivo}.json", "r", encoding="utf-8") as t:
                    lista_usuarios_json = json.load(t)
                # exibindo os usuarios salvos no arquivo json
                print(f"{'-'*20} LISTA DE USUARIOS {'-'*20}")
                for usuario in lista_usuarios_json:
                    for chave in usuario:
                        print(f"{chave.capitalize()}: {usuario.get(chave)}")
                    print('-'*40)
            except Exception as e:
                print(f"Não foi possivel listar os usuarios cadastrados. Erro: {e}")
            continue
        # PESQUISAR USUARIO ESPECIFICO
        case "5":
            try:
                if not nome_arquivo:
                    nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                    diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()
                with open(f"{diretorio_arquivo}{nome_arquivo}.json", "r", encoding="utf-8") as t:
                    lista_usuarios_json = json.load(t)
                # exibindo os usuarios salvos no arquivo json

                while True:
                    print("Escolha uma opção...")
                    print("1. Pesquisar usuario pelo 'Nome'.")
                    print("2. Pesquisar usuario pelo 'CPF'.")
                    opcao_menu_pesquisa = input("Informe a opção desejada: ").strip()
                    match opcao_menu_pesquisa:
                        case "1":
                            ...
                            break
                        case "2":
                            ...
                            break
                        case _:
                            print("Opção invalida! Tente novamente.")
                            continue

            except Exception as e:
                print(f"Não foi possivel listar os usuarios cadastrados. Erro: {e}")
            continue
        case "6":
            ...
        case "7":
            ...
        case "8":
            print("Programa encerrado!")
            break
        case _:
            print("Opção invalida! Tente novamente.")
            continue

