// MODEL
let nome = "";


// CONTROLLER
function controller() {

    nome = document.getElementById("nome").value;

    view();
}


// VIEW
function view() {

    document.getElementById("resultado").innerText = "Olá, " + nome;
}