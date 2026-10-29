async function carregarUsuarios() {
    const resposta = await fetch(
        "https://jsonplaceholder.typicode.com/users"
    );
    const usuarios = await resposta.json();
    const lista = document.getElementById("lista");
    usuarios.forEach(usuario => {
        const item = document.createElement("li");
        item.textContent = usuario.name;
        lista.appendChild(item);
    });
}



