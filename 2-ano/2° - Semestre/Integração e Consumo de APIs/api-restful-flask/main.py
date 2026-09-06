# uvicorn main:app --reload

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import sqlite3
import math


app = FastAPI(
    title="API de Produtos",
    description="API RESTful para gerenciamento de produtos",
    version="2.0.0"
)

DATABASE = "produtos.db"


# ============================================================
# BANCO DE DADOS
# ============================================================

def conectar_banco():
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    conexao = conectar_banco()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL,
            categoria TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


# ============================================================
# MODELOS
# ============================================================

class Produto(BaseModel):
    nome: str
    preco: float
    estoque: int
    categoria: str


class ProdutoAtualizacao(BaseModel):
    nome: str | None = None
    preco: float | None = None
    estoque: int | None = None
    categoria: str | None = None


# ============================================================
# GET - LISTAR PRODUTOS
#
# Exemplos:
#
# GET /produtos
#
# GET /produtos?busca=note
#
# GET /produtos?categoria=eletronicos
#
# GET /produtos?pagina=2&limite=5
#
# GET /produtos?busca=note&categoria=eletronicos
#                       &pagina=1&limite=10
# ============================================================

@app.get("/produtos")
def listar_produtos(
    busca: str | None = Query(
        default=None,
        description="Termo utilizado para buscar pelo nome do produto"
    ),

    categoria: str | None = Query(
        default=None,
        description="Categoria dos produtos"
    ),

    pagina: int = Query(
        default=1,
        ge=1,
        description="Número da página"
    ),

    limite: int = Query(
        default=10,
        ge=1,
        le=100,
        description="Quantidade de produtos por página"
    )
):

    conexao = conectar_banco()

    # ========================================================
    # CONSTRUÇÃO DOS FILTROS
    # ========================================================

    filtros = []
    parametros = []

    # --------------------------------------------------------
    # BUSCA POR TERMO
    # --------------------------------------------------------
    #
    # O LIKE permite procurar parte do nome.
    #
    # Exemplo:
    #
    # ?busca=note
    #
    # encontrará:
    #
    # Notebook
    # Notebook Pro
    # Suporte para Notebook
    #
    # O % significa "qualquer quantidade de caracteres".
    # --------------------------------------------------------

    if busca:
        filtros.append("nome LIKE ?")
        parametros.append(f"%{busca}%")

    # --------------------------------------------------------
    # FILTRO POR CATEGORIA
    # --------------------------------------------------------

    if categoria:
        filtros.append("categoria = ?")
        parametros.append(categoria)

    # ========================================================
    # WHERE
    # ========================================================

    where = ""

    if filtros:
        where = "WHERE " + " AND ".join(filtros)

    # ========================================================
    # CONTAGEM TOTAL
    # ========================================================

    consulta_total = f"""
        SELECT COUNT(*) AS total
        FROM produtos
        {where}
    """

    resultado_total = conexao.execute(
        consulta_total,
        parametros
    ).fetchone()

    total = resultado_total["total"]

    # ========================================================
    # PAGINAÇÃO
    # ========================================================

    # Exemplo:
    #
    # página 1, limite 10
    # offset = (1 - 1) * 10
    # offset = 0
    #
    # página 2, limite 10
    # offset = (2 - 1) * 10
    # offset = 10
    #
    # página 3, limite 10
    # offset = (3 - 1) * 10
    # offset = 20

    offset = (pagina - 1) * limite

    # ========================================================
    # BUSCAR OS PRODUTOS
    # ========================================================

    consulta = f"""
        SELECT *
        FROM produtos
        {where}
        ORDER BY id
        LIMIT ? OFFSET ?
    """

    parametros_consulta = parametros + [
        limite,
        offset
    ]

    produtos = conexao.execute(
        consulta,
        parametros_consulta
    ).fetchall()

    conexao.close()

    # ========================================================
    # CALCULAR TOTAL DE PÁGINAS
    # ========================================================

    total_paginas = math.ceil(total / limite) if total > 0 else 0

    # ========================================================
    # RESPOSTA
    # ========================================================

    return {
        "pagina": pagina,
        "limite": limite,
        "total": total,
        "total_paginas": total_paginas,
        "dados": [
            dict(produto)
            for produto in produtos
        ]
    }


# ============================================================
# GET - BUSCAR PRODUTO PELO ID
#
# GET /produtos/10
# ============================================================

@app.get("/produtos/{id}")
def buscar_produto(id: int):

    conexao = conectar_banco()

    produto = conexao.execute(
        """
        SELECT *
        FROM produtos
        WHERE id = ?
        """,
        (id,)
    ).fetchone()

    conexao.close()

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    return dict(produto)


# ============================================================
# POST - CRIAR PRODUTO
# ============================================================

@app.post("/produtos", status_code=201)
def criar_produto(produto: Produto):

    conexao = conectar_banco()

    cursor = conexao.execute(
        """
        INSERT INTO produtos
        (
            nome,
            preco,
            estoque,
            categoria
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            produto.nome,
            produto.preco,
            produto.estoque,
            produto.categoria
        )
    )

    conexao.commit()

    id_produto = cursor.lastrowid

    conexao.close()

    return {
        "id": id_produto,
        "nome": produto.nome,
        "preco": produto.preco,
        "estoque": produto.estoque,
        "categoria": produto.categoria
    }


# ============================================================
# PUT - ATUALIZAR PRODUTO COMPLETAMENTE
# ============================================================

@app.put("/produtos/{id}")
def atualizar_produto(
    id: int,
    produto: Produto
):

    conexao = conectar_banco()

    existente = conexao.execute(
        """
        SELECT *
        FROM produtos
        WHERE id = ?
        """,
        (id,)
    ).fetchone()

    if existente is None:
        conexao.close()

        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    conexao.execute(
        """
        UPDATE produtos
        SET
            nome = ?,
            preco = ?,
            estoque = ?,
            categoria = ?
        WHERE id = ?
        """,
        (
            produto.nome,
            produto.preco,
            produto.estoque,
            produto.categoria,
            id
        )
    )

    conexao.commit()
    conexao.close()

    return {
        "id": id,
        "nome": produto.nome,
        "preco": produto.preco,
        "estoque": produto.estoque,
        "categoria": produto.categoria
    }


# ============================================================
# PATCH - ATUALIZAÇÃO PARCIAL
# ============================================================

@app.patch("/produtos/{id}")
def atualizar_parcialmente(
    id: int,
    produto: ProdutoAtualizacao
):

    conexao = conectar_banco()

    existente = conexao.execute(
        """
        SELECT *
        FROM produtos
        WHERE id = ?
        """,
        (id,)
    ).fetchone()

    if existente is None:
        conexao.close()

        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    # ========================================================
    # MANTER O VALOR ANTIGO QUANDO O CAMPO NÃO FOR ENVIADO
    # ========================================================

    nome = (
        produto.nome
        if produto.nome is not None
        else existente["nome"]
    )

    preco = (
        produto.preco
        if produto.preco is not None
        else existente["preco"]
    )

    estoque = (
        produto.estoque
        if produto.estoque is not None
        else existente["estoque"]
    )

    categoria = (
        produto.categoria
        if produto.categoria is not None
        else existente["categoria"]
    )

    # ========================================================
    # ATUALIZAÇÃO
    # ========================================================

    conexao.execute(
        """
        UPDATE produtos
        SET
            nome = ?,
            preco = ?,
            estoque = ?,
            categoria = ?
        WHERE id = ?
        """,
        (
            nome,
            preco,
            estoque,
            categoria,
            id
        )
    )

    conexao.commit()
    conexao.close()

    return {
        "id": id,
        "nome": nome,
        "preco": preco,
        "estoque": estoque,
        "categoria": categoria
    }


# ============================================================
# DELETE - EXCLUIR PRODUTO
# ============================================================

@app.delete("/produtos/{id}")
def excluir_produto(id: int):

    conexao = conectar_banco()

    produto = conexao.execute(
        """
        SELECT *
        FROM produtos
        WHERE id = ?
        """,
        (id,)
    ).fetchone()

    if produto is None:
        conexao.close()

        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    conexao.execute(
        """
        DELETE FROM produtos
        WHERE id = ?
        """,
        (id,)
    )

    conexao.commit()
    conexao.close()

    return {
        "mensagem": "Produto excluído com sucesso"
    }


# ============================================================
# INICIALIZAÇÃO
# ============================================================

criar_tabela()