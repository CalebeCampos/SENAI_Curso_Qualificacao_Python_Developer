from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import entidades as ent
import funcoes as fun

def main():
    # cria a base de dados
    # engine = create_engine("mysql+mysqlconnector://informar_senha:informar_usuario@localhost:3306/informar_nome_da_base_de_dados")
    engine = create_engine("sqlite:///09_conexao_banco_de_dados/01_crud_uma_entidade/database/db_crud_uma_entidade.db")
    Base = declarative_base()
    # cria a tabela pessoa
    Pessoa = ent.criar_tb_pessoa(engine=engine, Base=Base)
    # inicia sessao para conexao com o banco de dados
    Session = sessionmaker(bind=engine)
    session = Session()

    fun.limpar_terminal()
    while True:
        print(f"{'-'*20}SISTEMA CRUD{'-'*20}")
        print("1 - Cadastrar nova pessoa.")
        print("2 - Listar pessoas cadastradas.")
        print("3 - Pesquisar pessoas.")
        print("4 - Alterar cadastro de uma pessoa.")
        print("5 - Excluir cadastro de uma pessoa.")
        print("6 - Exportar dados para CSV.")
        print("7 - Exportar dados para EXCEL.")
        print("8 - Sair do programa.")
        opcao = input("Informe a opcao desejada: ").strip()
        fun.limpar_terminal()
        match opcao:
            case "1":
                # chama a funcao cadastrar pessoa e passa os parametros de sessao e classe Pessoa
                fun.cadastrar_pessoa(session=session, Pessoa=Pessoa)
                continue
            case "2":
                fun.listar_pessoas(session=session, Pessoa=Pessoa)
                continue
            case "3":
                fun.pesquisar_pessoas(session=session, Pessoa=Pessoa)
                continue
            case "4":
                fun.alterar_dados(session=session, Pessoa=Pessoa)
                continue
            case "5":
                fun.excluir_pessoa(session=session, Pessoa=Pessoa)
                continue
            case "6":
                fun.exportar_dados_pessoas_csv(engine=engine)
                continue
            case "7":
                fun.exportar_dados_pessoas_excel(engine=engine, Pessoa=Pessoa)
                continue            
            case "8":
                print("Programa finalizado!")
                break
            case _:
                print("Opcao invalida! Tente novamente.")
                continue

    # encerra a sessao com o banco de dados
    session.close()

if __name__ == "__main__":
    main()