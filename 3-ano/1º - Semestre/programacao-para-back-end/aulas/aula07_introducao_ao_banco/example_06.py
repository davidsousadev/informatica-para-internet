# 6. CRUD com menu (while + sqlite3)
import sqlite3

def conectar():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
    """)

    conn.commit()
    return conn, cursor


def inserir(cursor, conn):
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
    conn.commit()
    print("✔ Usuário inserido!")


def listar(cursor):
    cursor.execute("SELECT * FROM usuarios")
    dados = cursor.fetchall()

    print("\n📋 Usuários:")
    for d in dados:
        print(d)


def atualizar(cursor, conn):
    id_user = int(input("ID do usuário: "))
    novo_nome = input("Novo nome: ")
    nova_idade = int(input("Nova idade: "))

    cursor.execute(
        "UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?",
        (novo_nome, nova_idade, id_user)
    )
    conn.commit()
    print("✔ Usuário atualizado!")


def deletar(cursor, conn):
    id_user = int(input("ID para deletar: "))

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_user,))
    conn.commit()
    print("✔ Usuário deletado!")


def menu():
    conn, cursor = conectar()

    while True:
        print("\n====== MENU CRUD ======")
        print("1 - Inserir usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Deletar usuário")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            inserir(cursor, conn)

        elif opcao == "2":
            listar(cursor)

        elif opcao == "3":
            atualizar(cursor, conn)

        elif opcao == "4":
            deletar(cursor, conn)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("❌ Opção inválida!")

    conn.close()


menu()