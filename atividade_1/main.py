import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    ra = Column("R.A", Integer, primary_key=True, autoincrement=True)
    nome = Column("Nome", String)
    idade = Column("Idade", Integer)
    email = Column("E-mail", String)
 
    def __init__(self, nome: str, idade: int, email: str) -> None:
        self.nome = nome
        self.idade = idade
        self.email = email

Base.metadata.create_all(bind=db)

os.system("cls || clear")

for i in range(2):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    email = input("Digite seu e-mail: ")

aluno = Aluno(nome= nome, idade= idade, email= email)
session.add(aluno)
session.commit()

lista_alunos = session.query(Aluno).all()

print("R.A || Nome || Idade || E-mail")

for aluno in lista_alunos:
    print(f"{aluno.ra} - {aluno.nome} - {aluno.idade} - {aluno.email}")