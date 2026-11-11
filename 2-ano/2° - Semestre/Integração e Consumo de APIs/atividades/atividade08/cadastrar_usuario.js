fetch("http://127.0.0.1:8000/usuarios",
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nome: "David",
            email: "david@gmail.com"
        })
    }
);