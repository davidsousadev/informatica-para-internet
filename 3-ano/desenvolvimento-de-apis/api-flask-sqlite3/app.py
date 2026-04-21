# importa o Flask (framework web), request (dados da requisição) e jsonify (retorno JSON)
from flask import Flask, request, jsonify

# importa o SQLite (banco de dados leve embutido no Python)
import sqlite3

# importa o Swagger automático
from flasgger import Swagger

# cria a aplicação Flask
app = Flask(__name__)

# ativa o Swagger (gera interface web automática)
swagger = Swagger(app)

# função que cria conexão com o banco SQLite
def get_db():
    # conecta (ou cria) o arquivo banco.db
    conn = sqlite3.connect('banco.db')
    
    # faz com que cada linha retornada seja tipo dicionário
    conn.row_factory = sqlite3.Row
    
    # retorna a conexão
    return conn

# função para criar tabela automaticamente
def criar_tabela():
    # abre conexão
    conn = get_db()
    
    # executa SQL para criar tabela se não existir
    conn.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT,                            
            idade INTEGER                         
        )
    ''')
    # id automático
    # nome texto
    # idade número
    
    # fecha conexão
    conn.close()

# chama a função ao iniciar (garante que a tabela exista)
criar_tabela()

# rota inicial
@app.route('/')
def home():
    return "API rodando com SQLite + Swagger!"

# rota para criar usuário
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    """
    Criar usuário
    ---
    tags:
      - Usuários
    parameters:
      - name: body
        in: body
        required: true
        schema:
          properties:
            nome:
              type: string
              example: João
            idade:
              type: integer
              example: 25
    responses:
      200:
        description: Usuário criado com sucesso
    """
    
    # pega JSON enviado na requisição
    dados = request.get_json()
    
    # extrai nome
    nome = dados.get('nome')
    
    # extrai idade
    idade = dados.get('idade')

    # abre conexão com banco
    conn = get_db()
    
    # insere dados usando proteção contra SQL injection
    conn.execute(
        'INSERT INTO usuarios (nome, idade) VALUES (?, ?)',
        (nome, idade)
    )
    
    # salva alterações
    conn.commit()
    
    # fecha conexão
    conn.close()

    # retorna resposta em JSON
    return jsonify({"msg": "Usuário criado!"})

# rota para listar usuários
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    """
    Listar usuários
    ---
    tags:
      - Usuários
    responses:
      200:
        description: Lista de usuários
    """
    
    # abre conexão
    conn = get_db()
    
    # executa SELECT e pega todos resultados
    usuarios = conn.execute('SELECT * FROM usuarios').fetchall()
    
    # fecha conexão
    conn.close()

    # converte cada linha em dicionário
    lista = [dict(u) for u in usuarios]
    
    # retorna JSON com lista
    return jsonify(lista)

# roda o servidor acessível na rede
app.run(host='0.0.0.0', port=5000)