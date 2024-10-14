import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
import time

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("Id", Integer, primary_key=True, autoincrement=True)
    nome = Column("Nome", String)
    idade = Column("Idade", Integer)
    email = Column("E-mail", String)
 
    def __init__(self, nome: str, idade: int, email: str) -> None:
        self.nome = nome
        self.idade = idade
        self.email = email

Base.metadata.create_all(bind=db)
lista_usuarios = session.query(Usuario).all()


# FUNÇÕES

def carregando():
    os.system("cls || clear")
    print("Carregando.")
    time.sleep(2)
    os.system("cls || clear")

def menu_inicial_grafico():
    print("Menu: ")
    print("\n1. Registrar um novo estudante.")
    print("\n2. Ver registro dos estudantes.")
    print("\n3. Pesquisar um estudante.")
    print("\n4. Remover um estudante dos registros.")
    print("\n5. Encerrar.\n") # Vou trabalhar no final

def menu_inicial_funcional(resposta_menu):
    match resposta_menu:
        case 1:
            registrar_usuario(resposta_menu)
        case 2:
            registros_usuarios(resposta_menu)
        case 3:
            pesquisar_usuario(resposta_menu)
        case 4:
            deletar_usuario(resposta_menu)

def registrar_usuario(usuario):
    print("\nRegistrando um usuário: \n")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    email = input("Digite seu e-mail: ")
    usuario = Usuario(nome= nome, idade= idade, email= email)
    session.add(usuario)
    session.commit()


def registros_usuarios(usuario):
    print("\nRegistros de Usuários: \n")
    for usuario in lista_usuarios:
     lista_usuarios = session.query(Usuario).all()
     print(f"{usuario.id} - {usuario.nome} - {usuario.idade} - {usuario.email}")

def pesquisar_usuario(usuario):
    print("\nPesquisando usuários:\n")
    usuario_id = input("\nInforme o id: ")
    usuario = session.query(Usuario).filter_by(id = usuario_id).first()

    if usuario:
        print(f"\nInformações sobre usuário: {usuario.id} - {usuario.nome} - {usuario.idade} - {usuario.email}")
    else:
        print("Usuário não encontrado")

def deletar_usuario(usuario):
    print("\nExcluíndo usuário:\n")
    usuario_id = input("\nInforme um id: ")
    usuario = session.query(Usuario).filter_by(id = usuario_id).first()
    session.delete(usuario)
    session.commit()
    print("\nUsuário deletado")

### FUNCIONAL 

# COMEÇO

print("Bem vindo, aguarde.")

carregando()

menu_inicial_grafico()
resposta_menu = int(input("\nDigite a opção desejada: "))
menu_inicial_funcional(resposta_menu)
#carregando()



# print("R.A || Nome || Idade || E-mail")



# print("\nAtualizando os dados do usuário...")

# email_usuario = input("Informe o e-mail do usuário: ")

# session.commit()

# print("\nPesquisando um usuário pelo R.A: ")

