from sqlalchemy import create_engine
from sqlalchemy import Column, Integer
from sqlalchemy import String, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

#limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def criar_tb_pessoa(engine, Base):
    try:
        class Pessoa(Base):
            __tablename__ = "pessoa"
            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
            nome = Column(String, nullable=False)
            email = Column(String, nullable=False, unique=True)
            data_nascimento = Column(Date, nullable=False)
        Base.metadata.create_all(engine)
        # cria classe Pessoa e retorna a proprio classe Pessoa
        return Pessoa
    except Exception as e:
        print(f"Nao foi possivel conectar ao banco. Erro: {e}")

def cadastrar_pessoa(session, Pessoa):
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

def listar_pessoas(session, Pessoa):
    pessoas = session.query(Pessoa).all()
    print("\nPESSOAS CADASTRADAS\n")
    print(f"{'-'*40}")
    for pessoa in pessoas:
        print(f"ID: {pessoa.id_pessoa}")
        print(f"Nome: {pessoa.nome}")
        print(f"Email: {pessoa.email}")
        print(f"Data de nascimento: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
        print(f"{'-'*40}")

def main():
    # cria a base de dados
    # engine = create_engine("mysql+mysqlconnector://informar_senha:informar_usuario@localhost:3306/informar_nome_da_base_de_dados")
    engine = create_engine("sqlite:///09_conexao_banco_de_dados/01_crud_uma_entidade/database/db_crud_uma_entidade.db")
    Base = declarative_base()
    # cria a tabela pessoa
    Pessoa = criar_tb_pessoa(engine=engine, Base=Base)
    # inicia sessao para conexao com o banco de dados
    Session = sessionmaker(bind=engine)
    session = Session()

    limpar_terminal()
    while True:
        print(f"{'-'*20}SISTEMA CRUD{'-'*20}")
        print("1 - Cadastrar nova pessoa.")
        print("2 - Listar pessoas cadastradas.")
        print("3 - Alterar cadastro de uma pessoa.")
        print("4 - Excluir cadastro de uma pessoa.")
        print("5 - Sair do programa.")
        opcao = input("Informe a opcao desejada: ").strip()
        limpar_terminal()
        match opcao:
            case "1":
                # chama a funcao cadastrar pessoa e passa os parametros de sessao e classe Pessoa
                cadastrar_pessoa(session=session, Pessoa=Pessoa)
                continue
            case "2":
                listar_pessoas(session=session, Pessoa=Pessoa)
                continue
            case "3":
                ...
            case "4":
                ...
            case "5":
                print("Programa finalizado!")
                break
            case _:
                print("Opcao invalida! Tente novamente.")
                continue

    # encerra a sessao com o banco de dados
    session.close()

if __name__ == "__main__":
    main()