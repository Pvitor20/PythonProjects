# database.py
import sqlite3
from pathlib import Path
from datetime import datetime

# Caminho para o diretório do arquivo atual
ROOT_PATH = Path(__file__).parent
con = sqlite3.connect(ROOT_PATH / 'DBRP.sqlite')
cursor = con.cursor()

# Criação das tabelas, se ainda não existirem
cursor.execute('''
CREATE TABLE IF NOT EXISTS Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome VARCHAR(100), 
    cpf VARCHAR(11), 
    email VARCHAR(100), 
    senha VARCHAR(100)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Relatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    user_id INTEGER, 
    localizacao TEXT,
    denuncia TEXT,
    foto TEXT,
    data_hora TIMESTAMP,
    resolvido BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES Usuarios(id) 
)
''')

# Funções CRUD
def adicionar_usuario(nome, cpf, email, senha):
    data_user = (nome, cpf, email, senha)
    try:
        cursor.execute("INSERT INTO Usuarios (nome, cpf, email, senha) VALUES (?, ?, ?, ?);", data_user)
        con.commit()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        con.rollback()

def check_login(email, senha):
    cursor.execute("SELECT * FROM Usuarios WHERE email = ? AND senha = ?", (email, senha))
    return cursor.fetchone()

def registrar_denuncia(user_id, localizacao, denuncia_texto, foto_path=None):
    data_denuncia = (user_id, localizacao, denuncia_texto, foto_path, datetime.now(), False)
    cursor.execute('''
        INSERT INTO Relatos (user_id, localizacao, denuncia, foto, data_hora, resolvido) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', data_denuncia)
    con.commit()

def listar_denuncias(user_id):
    cursor.execute('''SELECT data_hora, localizacao, denuncia, resolvido FROM Relatos WHERE user_id = ?''', (user_id,))
    return cursor.fetchall()

# Fecha a conexão ao encerrar
def fechar_conexao():
    con.close()
