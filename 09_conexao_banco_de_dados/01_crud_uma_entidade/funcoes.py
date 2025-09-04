from datetime import datetime
import pandas as pd
import os

#limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def cadastrar_pessoa(session, Pessoa):
    try:
        nome = input("Informe o nome: ").strip().title()
        email = input("Informe o email: ").strip().lower()
        pessoas = session.query(Pessoa).filter(Pessoa.email == email).all()
        if email in [pessoa.email for pessoa in pessoas]:
            print("Email já cadastrado! Favor informar outro.")
        else:
            data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
            data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            # cria objeto pessoa
            nova_pessoa = Pessoa(
                nome=nome,
                email=email,
                data_nascimento=data_nascimento)
            # realiza a insercao do objeto pessoa na tabela pessoa do banco de dados
            session.add(nova_pessoa)
            session.commit()
            print(f"Pessoa cadastrada com sucesso! Nome: {nome}")
    except Exception as e:
        print(f"Nao foi possivel cadastrar pessoa. Erro: {e}")

def listar_pessoas(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()
        print("\nPESSOAS CADASTRADAS\n")
        print(f"{'-'*40}")
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"Email: {pessoa.email}")
            print(f"Data de nascimento: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
            print(f"{'-'*40}")
    except Exception as e:
        print(f"Nao foi possivel listar pessoas. Erro: {e}")

def pesquisar_pessoas(session, Pessoa):
    print(f"{'-'*10}PESQUISAR PESSOAS{'-'*10}\n")
    print("1 - ID")
    print("2 - Nome")
    print("3 - Email")
    print("4 - Data de Nascimento")
    print("5 - Voltar ao menu principal")
    campo =  input("Informe o campo a ser pesquisado: ").strip()
    limpar_terminal()
    match campo:
        case "1":
            valor = input("Digite o ID para pesquisa: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.id_pessoa == valor).all()
        case "2":
            valor = input("Digite o NOME para pesquisa: ").strip().title()
            pessoas = session.query(Pessoa).filter(Pessoa.nome.like(f"%{valor}%")).all()
        case "3":
            valor = input("Digite o EMAIL para pesquisa: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.email.like(f"%{valor}%")).all()
        case "4":
            try:
                valor = input("Digite a DATA DE NASCIMENTO para pesquisa (dd/mm/aaaa): ").strip()
                valor = datetime.strptime(valor, "%d/%m/%Y").date()
                pessoas = session.query(Pessoa).filter(Pessoa.data_nascimento == valor).all()
            except Exception as e:
                print(f"Não foi possivel pesquisar pela data informada. Erro: {e}")
        case "5":
            pass
        case _:
            print("Opção invalida! Tente novamente.")
    limpar_terminal()
    print("\nRESULTADO DA PESQUISA\n")
    if pessoas:
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"Email: {pessoa.email}")
            print(f"Data de Nascimento: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
            print(f"{'-'*40}")
    else:
        print("Nenhum registro foi encontrado!")

def alterar_dados(session, Pessoa):
    id_pesquisar = ""
    email_pesquisar = ""
    novo_nome = ""
    novo_email = ""
    nova_data = ""
    try:
        print(f"{'-'*10}DESEJA PESQUISAR POR QUAL CAMPO{'-'*10}")
        print(f"1 - ID")
        print(f"2 - Email")
        print(f"3 - Voltar")
        opcao_pesquisa = input("Informe a opção: ").strip()
        limpar_terminal()
        match opcao_pesquisa:
            case "1":
                id_pesquisar = input("Informe o ID: ").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pesquisar).first()
                # o first funciona como o limit 1 ou top 1 que retorna o primeiro registro
            case "2":
                email_pesquisar = input("Informe o email: ").strip()
                pessoa = session.query(Pessoa).filter_by(email=email_pesquisar).first()
            case "3":
                print("Pesquisa cancelada!")
            case _:
                print("Opcao invalida!")
        if pessoa: 
            while True:
                print(f"{'-'*10}DADOS DA PESSOA - ESCOLHA A COLUNA QUE DESEJA ALTERAR{'-'*10}")
                print(f"ID: {pessoa.id_pessoa}")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"2 - Email: {pessoa.email}")
                print(f"3 - Data de Nascimento: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
                print(f"4 - Voltar/Alterar")
                opcao_alterar = input("Informe a coluna que deseja alterar: ").strip()
                limpar_terminal()
                match opcao_alterar:
                    case "1":
                        novo_nome = input("Informe o novo nome: ").strip().title()
                        print(f"Novo nome a ser gravado: {novo_nome}")
                        continue
                    case "2":
                        novo_email = input("Informe o novo email: ").strip().lower()
                        pessoas = session.query(Pessoa).filter(Pessoa.email == novo_email).all()
                        if novo_email in [pessoa.email for pessoa in pessoas]:
                            print("Email já cadastrado! Favor informar outro.")
                        else:
                            print(f"Novo email a ser gravado: {novo_email}")
                        continue
                    case "3":
                        nova_data = input("Informe a nova data de nascimento (dd/mm/aaaa): ").strip()
                        print(f"Nova data a ser gravada: {nova_data}")
                        continue
                    case "4":
                        novo_nome = novo_nome if novo_nome != "" else pessoa.nome
                        novo_email = novo_email if novo_email != "" else pessoa.email
                        nova_data = datetime.strptime(nova_data, "%d/%m/%Y").date() if nova_data != "" else pessoa.data_nascimento
                        break
                    case _:
                        print("Opcao invalida!")
                        continue    
            pessoa.nome = novo_nome 
            pessoa.email = novo_email 
            pessoa.data_nascimento = nova_data
            session.commit()
            limpar_terminal()
            print("Pessoa alterada com sucesso!")
        else:
            print("Pessoa nao encontrada!")
    except Exception as e:
        print(f"Nao foi possivel alterar pessoa. Erro: {e}")


def excluir_pessoa(session, Pessoa):
    id_pesquisar = ""
    email_pesquisar = ""
    try:
        print(f"{'-'*10}DESEJA PESQUISAR POR QUAL CAMPO{'-'*10}")
        print(f"1 - ID")
        print(f"2 - Email")
        print(f"3 - Voltar")
        opcao_pesquisa = input("Informe a opção: ").strip()
        limpar_terminal()
        match opcao_pesquisa:
            case "1":
                id_pesquisar = input("Informe o ID: ").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pesquisar).first()
            case "2":
                email_pesquisar = input("Informe o email: ").strip()
                pessoa = session.query(Pessoa).filter_by(email=email_pesquisar).first()
            case "0":
                print("Pesquisa cancelada!")
            case _:
                print("Opcao invalida!")
        if pessoa:
            print(f"{'-'*10}DADOS DA PESSOA PESQUISADA{'-'*10}")
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"Email: {pessoa.email}")
            print(f"Data de Nascimento: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
            print("\n")
            opcao_excluir = input("Deseja excluir? 1 (sim) ou 2 (nao): ").strip()
            limpar_terminal()
            match opcao_excluir:
                case "1":
                    session.delete(pessoa)
                    session.commit()
                    print("Pessoa excluida com sucesso!")
                case "2":
                    print("Exclusao cancelada!")
                case _:
                    print("Opcao invalida!")
        else:
            print("Pessoa nao encontrada!")
    except Exception as e:
        print(f"Nao foi possivel excluir a pessoa. Erro: {e}")

def exportar_dados_pessoas_csv(engine):
    try:
        diretorio = input("Informe o diretorio que deseja salvar o arquivo: ").strip()
        nome_Arquivo = input("Informe o nome do arquivo sem extensao: ").strip()
        sql_query = "SELECT * FROM pessoa ORDER BY id_pessoa"
        data_frame = pd.read_sql_query(sql_query, engine)
        data_frame.to_csv(f"{diretorio}{nome_Arquivo}.csv", index=False)
        print("Dados exportados com sucesso!")
    except Exception as e:
        print(f"Nao foi exportar os dados. Erro: {e}")

def exportar_dados_pessoas_excel(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()
        # Cria uma lista de dicionários com os dados das pessoas
        dados = [
            {
                "ID": pessoa.id_pessoa,
                "Nome": pessoa.nome,
                "E-mail": pessoa.email,
                "Data de nascimento": pessoa.data_nascimento.strftime("%d/%m/%Y")
            }
            for pessoa in pessoas
        ]
        df = pd.DataFrame(dados)
        df.to_excel("09_conexao_banco_de_dados/01_crud_uma_entidade/pessoas.xlsx", index=False)
        print("Dados exportados para pessoas.xlsx com sucesso.")
    except Exception as e:
        print(f"Erro ao exportar dados: {e}")