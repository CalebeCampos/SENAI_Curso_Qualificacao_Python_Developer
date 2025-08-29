from datetime import datetime
import os

#limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def cadastrar_pessoa(session, Pessoa):
    try:
        nome = input("Informe o nome: ").strip().title()
        email = input("Informe o email: ").strip().lower()
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