from sqlalchemy import Column, Integer
from sqlalchemy import String, Date

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