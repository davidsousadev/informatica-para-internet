// Busca e exibe todos os usuários cadastrados
async function listarUsuarios() {
    try {
        console.log("Buscando usuários...");
        const resposta = await fetch("http://127.0.0.1:8000/usuarios");
        const usuarios = await resposta.json();
        console.log("Lista de usuários cadastrados:");
        usuarios.forEach(usuario => {
            console.log(usuario);
        })
    } catch (erro) {
        console.log("Erro ao buscar usuários:", erro);
    }
}

// Chama a função para executar
listarUsuarios();
