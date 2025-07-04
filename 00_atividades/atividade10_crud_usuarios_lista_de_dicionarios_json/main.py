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
tupla_chaves_de_usuario = (
    "Nome", 
    "Data de Nascimento",
    "CPF",
    "E-mail",
    "Telefone",
    "Filme Favorito"
    )


while True: 

    # print(f"{"="*15} MENU {"="*15}")
    print(f"{'-'*10} JSON {'-'*10}")
    print(f"Arquivo carregado: {nome_arquivo}{'' if not nome_arquivo else '.json'}")
    print(f"Diretorio do arquivo: {diretorio_arquivo}")
    print("1. Criar arquivo JSON.")
    print("2. Carregar arquivo JSON.")
    print(f"{'-'*10} CRUD {'-'*10}")
    print("3. Cadastrar usuario.")
    print("4. Listar usuários.")
    print("5. Pesquisar usuario especifico.")
    print("6. Alterar usuário.")
    print("7. Excluir usuário.")
    print("8. Sair do programa")
    print("\n")
    opcao_menu_principal = input("Opção desejada: ").strip()
    os.system('cls' if os.name == 'nt' else 'clear')

    match opcao_menu_principal:
        
        # CRIAR ARQUIVO JSON
        case "1":
            try:
                lista_vazia = []
                nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                diretorio_arquivo = input("Informe o diretorio do arquivo: ").strip()
                with open(f"{diretorio_arquivo}{nome_arquivo}.json", "w", encoding="utf-8") as t:
                    json.dump(lista_vazia, t, ensure_ascii=False, indent=4)
                os.system("cls" if os.name == "nt" else "clear")
                print("Arquivo criado com sucesso!")
            except Exception as e:
                print(f"Não foi possivel criar o arquivo json. Erro: {e}")
            continue
        
        # CARREGAR ARQUIVO JSON
        case "2":
            try:
                if not nome_arquivo:
                    nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                    diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()
                with open(f"{diretorio_arquivo}{nome_arquivo}.json", "r", encoding="utf-8") as t:
                    lista_arquivo_json = json.load(t)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Arquivo JSON carregado com sucesso!")
            except Exception as e:
                print(f"Não foi possivel carregar o arquivo json. Erro: {e}")
            continue
                
        # CADASTRAR USUARIO
        case "3":
            try:
                if not nome_arquivo:
                    nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                    diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()
                with open(f"{diretorio_arquivo}{nome_arquivo}.json", "r", encoding="utf-8") as t:
                    lista_arquivo_json = json.load(t)
                print("Informe os seguintes dados do usuario...")
                usuario = {
                    tupla_chaves_de_usuario[0]: input(f"{tupla_chaves_de_usuario[0]}: ").strip().title(), # nome
                    tupla_chaves_de_usuario[1]: input(f"{tupla_chaves_de_usuario[1]} (dd/mm/yyyy): ").strip(), # data de nascimento
                    tupla_chaves_de_usuario[2]: input(f"{tupla_chaves_de_usuario[2]} (000.000.000-00): ").strip(), # cpf
                    tupla_chaves_de_usuario[3]: input(f"{tupla_chaves_de_usuario[3]}: ").strip().lower(), # e-mail
                    tupla_chaves_de_usuario[4]: input(f"{tupla_chaves_de_usuario[4]} (DDD0000000000): ").strip(), # telefone
                    tupla_chaves_de_usuario[5]: input(f"{tupla_chaves_de_usuario[5]}: ").strip().title() # filme
                }
                lista_arquivo_json.append(usuario)
                if not nome_arquivo:
                    nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                    diretorio_arquivo = input("Informe o diretorio do arquivo: ").strip()
                with open(f"{diretorio_arquivo}{nome_arquivo}.json", "w", encoding="utf-8") as t:
                    json.dump(lista_arquivo_json, t, ensure_ascii=False, indent=4)
                os.system("cls" if os.name == "nt" else "clear")
                print("Usuario cadastrado e salvo com sucesso!\n")        
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
                    lista_arquivo_json = json.load(t)
                if not lista_arquivo_json:
                    print("Nenhum usuario cadastrado!")
                else:
                    print(f"{'-'*20} LISTA DE USUARIOS {'-'*20}")
                    for usuario in lista_arquivo_json:
                        print(f"Indice: {lista_arquivo_json.index(usuario)}")
                        for chave in usuario:
                            print(f"{chave.capitalize()}: {usuario.get(chave)}")
                        print('-'*40)
                    print("\n")
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
                    lista_arquivo_json = json.load(t) 
                while True:
                    print("Escolha uma opção...")
                    print("1. Pesquisar pelo 'Nome'.")
                    print("2. Pesquisar pelo 'CPF'.")
                    opcao_menu_pesquisar_usuario = input("Opção desejada: ").strip()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    match opcao_menu_pesquisar_usuario:
                        # PESQUISA PELO NOME
                        case "1":
                            nome_pesquisa = input("Informe o nome: ").strip().title()
                            os.system('cls' if os.name == 'nt' else 'clear')
                            lista_usuarios_nome_pesquisa = []                            
                            for indice, usuario in enumerate(lista_arquivo_json):
                                if usuario.get("Nome") == nome_pesquisa:
                                    lista_usuarios_nome_pesquisa.append((indice, usuario))
                            if not lista_usuarios_nome_pesquisa:
                                print(f"Não existe usuarios com este nome!")
                            else:
                                for indice, usuario in lista_usuarios_nome_pesquisa:
                                    print(f"Indice: {indice}")
                                    for chave in usuario:
                                        print(f"{chave.capitalize()}: {usuario.get(chave)}")
                                    print('-'*40)
                                print("\n")
                            break
                        # PESQUISA PELO CPF
                        case "2":
                            cpf_pesquisa = input("Informe o CPF (000.000.000-00): ").strip().title()
                            os.system('cls' if os.name == 'nt' else 'clear')
                            lista_usuarios_cpf_pesquisa = []                            
                            for indice, usuario in enumerate(lista_arquivo_json):
                                if usuario.get("CPF") == cpf_pesquisa:
                                    lista_usuarios_cpf_pesquisa.append((indice, usuario))
                            if not lista_usuarios_cpf_pesquisa:
                                print(f"Não existe usuarios com este CPF!")
                            else:
                                for indice, usuario in lista_usuarios_cpf_pesquisa:
                                    print(f"Indice: {indice}")
                                    for chave in usuario:
                                        print(f"{chave.capitalize()}: {usuario.get(chave)}")
                                    print('-'*40)
                                print("\n")
                            break
                        case _:
                            print("Opção invalida!")
                            continue
            except Exception as e:
                print(f"Não foi possivel listar os usuarios cadastrados. Erro: {e}")
            continue
        
        # ALTERAR USUARIO ESPECIFICO
        case "6":
            try:
                if not nome_arquivo:
                    nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                    diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()
                with open(f"{diretorio_arquivo}{nome_arquivo}.json", "r", encoding="utf-8") as t:
                    lista_arquivo_json = json.load(t) 
                
                indice_usuario_alterar = int(input("Informe o indice do usuario que deseja alterar: ").strip())
                os.system('cls' if os.name == 'nt' else 'clear')
                
                if indice_usuario_alterar >= 0 and indice_usuario_alterar < len(lista_arquivo_json):
                    # exibe os dados do usuario referente ao indice informado
                    print(f"Indice: {indice_usuario_alterar}")
                    for chave in lista_arquivo_json[indice_usuario_alterar]:
                        print(f"{chave}: {lista_arquivo_json[indice_usuario_alterar].get(chave)}")
                    print("\n")
                    
                    chave_usuario_alterar = input("Informe a chave que deseja alterar: ").strip()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if chave_usuario_alterar in lista_arquivo_json[indice_usuario_alterar]:
                        novo_valor_chave_usuario_alterar = input(f"Digite o novo valor para '{chave_usuario_alterar}': ").strip().title()
                        lista_arquivo_json[indice_usuario_alterar][chave_usuario_alterar] = novo_valor_chave_usuario_alterar
                        if not nome_arquivo:
                            nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                            diretorio_arquivo = input("Informe o diretorio do arquivo: ").strip()
                        with open(f"{diretorio_arquivo}{nome_arquivo}.json", "w", encoding="utf-8") as t:
                            json.dump(lista_arquivo_json, t, ensure_ascii=False, indent=4)
                        os.system("cls" if os.name == "nt" else "clear")
                        print("Alteração realizada com sucesso!\n") 
                    else:
                        print(f"A chave '{chave_usuario_alterar}' não existe no dicionário.\n")  
                else:
                    print(f"O indice '{indice_usuario_alterar}' não existe!\n")
 
            except Exception as e:
                print(f"Não foi possivel alterar o usuario. Erro: {e}")
            continue
        
        # EXCLUIR USUARIO ESPECIFICO
        case "7":
            try:
                if not nome_arquivo:
                    nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                    diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()
                with open(f"{diretorio_arquivo}{nome_arquivo}.json", "r", encoding="utf-8") as t:
                    lista_arquivo_json = json.load(t) 
                    
                indice_usuario_excluir = int(input("Informe o indice do usuario que deseja excluir: ").strip())
                os.system('cls' if os.name == 'nt' else 'clear')
                
                if indice_usuario_excluir >= 0 and indice_usuario_excluir < len(lista_arquivo_json):
                    # exibe os dados do usuario referente ao indice informado
                    print(f"Indice: {indice_usuario_excluir}")
                    for chave in lista_arquivo_json[indice_usuario_excluir]:
                        print(f"{chave}: {lista_arquivo_json[indice_usuario_excluir].get(chave)}")
                    print("\n")
                    
                    confirmacao_exclusao = input("Deseja realmente excluir? (s/n): ")
                    if confirmacao_exclusao == "s":
                        del(lista_arquivo_json[indice_usuario_excluir])
                        if not nome_arquivo:
                            nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
                            diretorio_arquivo = input("Informe o diretorio do arquivo: ").strip()
                        with open(f"{diretorio_arquivo}{nome_arquivo}.json", "w", encoding="utf-8") as t:
                            json.dump(lista_arquivo_json, t, ensure_ascii=False, indent=4)
                        print("Exclusao realizada com sucesso!\n")
                    else:
                        print("Exclusao não realizada!")
                else:
                    print(f"O indice '{indice_usuario_excluir}' não existe!\n")
            except Exception as e:
                print(f"Não foi possivel excluir o usuario. Erro: {e}")
            continue
        
        # SAIR
        case "8":
            print("Programa encerrado!")
            break
        case _:
            print("Opção invalida! Tente novamente.")
            continue

