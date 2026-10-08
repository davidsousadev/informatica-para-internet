from flask import Blueprint, request, jsonify

from models import aluno


aluno_controller = Blueprint(
    "aluno",
    __name__
)


# LISTAR
@aluno_controller.route("/api/alunos", methods=["GET"])
def listar_alunos():

    alunos = aluno.listar()

    return jsonify(alunos)


# ADICIONAR
@aluno_controller.route("/api/alunos", methods=["POST"])
def adicionar_aluno():

    dados = request.json

    aluno.adicionar(
        dados["nome"],
        dados["email"],
        dados["idade"]
    )

    return jsonify({
        "mensagem": "Aluno adicionado com sucesso!"
    })


# ATUALIZAR
@aluno_controller.route("/api/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):

    dados = request.json

    aluno.atualizar(
        id,
        dados["nome"],
        dados["email"],
        dados["idade"]
    )

    return jsonify({
        "mensagem": "Aluno atualizado com sucesso!"
    })


# EXCLUIR
@aluno_controller.route("/api/alunos/<int:id>", methods=["DELETE"])
def excluir_aluno(id):

    aluno.excluir(id)

    return jsonify({
        "mensagem": "Aluno excluído com sucesso!"
    })
