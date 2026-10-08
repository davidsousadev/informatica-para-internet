let alunoEditando = null;


// LISTAR
async function listarAlunos() {
    const resposta = await fetch("/api/alunos");
    const alunos = await resposta.json();

    const lista = document.getElementById("listaAlunos");

    lista.innerHTML = "";

    alunos.forEach(aluno => {
        lista.innerHTML += `
            <tr>
                <td>${aluno.id}</td>
                <td>${aluno.nome}</td>
                <td>${aluno.email}</td>
                <td>${aluno.idade}</td>
                <td>
                    <button
                        class="btn-editar"
                        onclick="editarAluno(${aluno.id})">
                        Editar
                    </button>

                    <button
                        class="btn-excluir"
                        onclick="excluirAluno(${aluno.id})">
                        Excluir
                    </button>
                </td>
            </tr>
        `;
    });
}


// ADICIONAR / ATUALIZAR
document
    .getElementById("formAluno")
    .addEventListener("submit", async function (event) {

        event.preventDefault();


        const nome =
            document.getElementById("nome").value;

        const email =
            document.getElementById("email").value;

        const idade =
            document.getElementById("idade").value;


        const dados = {
            nome: nome,
            email: email,
            idade: idade
        };


        // ATUALIZAR
        if (alunoEditando !== null) {

            await fetch(
                `/api/alunos/${alunoEditando}`,
                {
                    method: "PUT",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify(dados)
                }
            );

            cancelarEdicao();

            listarAlunos();

            return;
        }


        // ADICIONAR
        await fetch(
            "/api/alunos",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify(dados)
            }
        );


        document
            .getElementById("formAluno")
            .reset();


        listarAlunos();

    });


// EDITAR
async function editarAluno(id) {
    const resposta = await fetch(`/api/alunos`);
    const alunos = await resposta.json();

    const aluno = alunos.find(aluno => aluno.id === id);

    if (!aluno) {
        alert("Aluno não encontrado!");
        return;
    }

    alunoEditando = aluno.id;

    document.getElementById("nome").value = aluno.nome;
    document.getElementById("email").value = aluno.email;
    document.getElementById("idade").value = aluno.idade;

    document.getElementById("botao").textContent = "Atualizar";
    document.getElementById("cancelar").hidden = false;
}


// CANCELAR
function cancelarEdicao() {

    alunoEditando = null;

    document
        .getElementById("formAluno")
        .reset();

    document.getElementById("botao")
        .textContent = "Adicionar";

    document.getElementById("cancelar")
        .hidden = true;
}


// EXCLUIR
async function excluirAluno(id) {

    const confirmar = confirm(
        "Deseja realmente excluir este aluno?"
    );


    if (!confirmar) {
        return;
    }


    await fetch(
        `/api/alunos/${id}`,
        {
            method: "DELETE"
        }
    );


    listarAlunos();
}


// INICIAR
listarAlunos();
