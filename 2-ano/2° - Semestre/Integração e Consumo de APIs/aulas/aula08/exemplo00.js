fetch("https://exemplo.com/usuarios", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        nome: "David",
        email: "david@email.com"
    })
});