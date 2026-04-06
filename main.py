from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///estoque_farmacia.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Farmacia(Base):
    __tablename__ = "farmacia"

    id   = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    endereco  = Column(String(140), unique=True)

    # Acesso aos atendimentos deste paciente
    medicamentos = relationship("Medicamento", back_populates="farmacia")

    def __repr__(self):
        return f"<Farmacia(id={self.id}, nome='{self.nome}')>"
    
class Medicamento(Base):
    __tablename__ = "medicamentos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Integer)
    estoque = Column(Integer)

    farmacia_id = Column(Integer, ForeignKey("farmacia.id"), nullable=False)
    farmacia = relationship("Farmacia", back_populates="medicamentos")


    def __repr__(self):
        return f"<Medicamento(nome='{self.nome}', estoque={self.estoque})>"


#Criar banco de dados

Base.metadata.create_all(engine)

#FUNÇÕES

def cadastrar_farmacia():
    with Session() as session:
        try:
            nome_farmacia = input("Digite o nome da farmacia: ").capitalize()
            endereco_input = input("Digite o endereço da farmacia:")
            farmacia = Farmacia(nome=nome_farmacia, endereco=endereco_input)
            
            session.add(farmacia)
            session.commit()
            print(f"Farmacia cadastrada com sucesso!")
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro: {erro}")

cadastrar_farmacia()


def cadastrar_medicamentos():
    with Session() as session:
        try:
            nome_medicamento = input("Digite o nome do medicamento: ").capitalize()
            medicamento = session.query(Medicamento).filter_by(nome=nome_medicamento).first()
            session.add(medicamento)
            session.commit()
            print(f"Medicamento cadastrado com sucesso!")

        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro {erro} ")
cadastrar_medicamentos()
           






