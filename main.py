from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///estoque_farmacia.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)



class Farmacia(Base):
    __tablename__ = "farmacia"

    id   = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    endereço  = Column(String(14), unique=True)

    # Acesso aos atendimentos deste paciente
    medicamentos = relationship("Medicamento", back_populates="farmacia", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Farmacia(id={self.id}, nome='{self.nome}')>"
    
class Medicamento(Base):
    __tablename__ = "medicamentos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    preço = Column(Integer, primary_key=True)
    estoque = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<Medicamento(nome='{self.nome}', estoque={self.estoque})>"


#Criar banco de dados

Base.metadata.create_all(engine)






