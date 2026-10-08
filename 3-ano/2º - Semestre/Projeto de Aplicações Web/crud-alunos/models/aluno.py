import os
import sqlite3

import mysql.connector

from dotenv import load_dotenv


load_dotenv()


BANCO = os.getenv("DATABASE", "sqlite")


# CONEXÃO COM O BANCO
def conectar():

    if BANCO == "mysql":

        return mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            port=int(os.getenv("MYSQL_PORT", 3306)),
            database=os.getenv("MYSQL_DATABASE"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD")
        )

    return sqlite3.connect(
        os.getenv("SQLITE_DATABASE", "banco.db")
    )


# CRIAR TABELA
def criar_banco():

    conexao = conectar()

    cursor = conexao.cursor()


    if BANCO == "mysql":

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL,
                idade INT NOT NULL
            )
        """)

    else:

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                idade INTEGER NOT NULL
            )
        """)


    conexao.commit()

    cursor.close()
    conexao.close()


# LISTAR
def listar():

    conexao = conectar()

    if BANCO == "mysql":

        cursor = conexao.cursor(dictionary=True)

    else:

        conexao.row_factory = sqlite3.Row

        cursor = conexao.cursor()


    cursor.execute("""
        SELECT id, nome, email, idade
        FROM alunos
        ORDER BY id
    """)


    alunos = cursor.fetchall()


    if BANCO == "sqlite":

        alunos = [dict(aluno) for aluno in alunos]


    cursor.close()
    conexao.close()


    return alunos


# ADICIONAR
def adicionar(nome, email, idade):

    conexao = conectar()

    cursor = conexao.cursor()


    cursor.execute("""
        INSERT INTO alunos (nome, email, idade)
        VALUES (%s, %s, %s)
    """ if BANCO == "mysql" else """
        INSERT INTO alunos (nome, email, idade)
        VALUES (?, ?, ?)
    """, (nome, email, idade))


    conexao.commit()

    cursor.close()
    conexao.close()


# ATUALIZAR
def atualizar(id, nome, email, idade):

    conexao = conectar()

    cursor = conexao.cursor()


    cursor.execute("""
        UPDATE alunos
        SET nome = %s, email = %s, idade = %s
        WHERE id = %s
    """ if BANCO == "mysql" else """
        UPDATE alunos
        SET nome = ?, email = ?, idade = ?
        WHERE id = ?
    """, (nome, email, idade, id))


    conexao.commit()

    cursor.close()
    conexao.close()


# EXCLUIR
def excluir(id):

    conexao = conectar()

    cursor = conexao.cursor()


    cursor.execute("""
        DELETE FROM alunos
        WHERE id = %s
    """ if BANCO == "mysql" else """
        DELETE FROM alunos
        WHERE id = ?
    """, (id,))


    conexao.commit()

    cursor.close()
    conexao.close()


criar_banco()