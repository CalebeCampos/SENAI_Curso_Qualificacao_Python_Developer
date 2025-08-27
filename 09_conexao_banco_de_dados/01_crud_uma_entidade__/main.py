from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

try:
    engine = create_engine("sqlite:///09_conexao_banco_de_dados/01_crud_uma_entidade/database/db_crud_uma_entidade.db")
    # engine = create_engine("mysql+mysqlconnector://informar_senha:informar_usuario@localhost:3306/informar_nome_da_base_de_dados")

    Base = declarative_base()

    class Pessoa(Base):
        __tablename__ = "pessoa"
        id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String, nullable=False)
        email = Column(String, nullable=False, unique=True)
        data_nascimento = Column(Date, nullable=False)

    Base.metadata.create_all(engine)


except Exception as e:
    print(f"Nao foi possivel conectar ao banco. Erro: {e}")