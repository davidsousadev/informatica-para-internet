async function buscarDados() {
    try {
        const response = await fetch("https://api-buy-tech.vercel.app/produtos", {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        });

        const dados = await response.json();

        document.getElementById("texto").textContent =
            JSON.stringify(dados, null, 2);

    } catch (error) {
        console.log(error);
    }
}

buscarDados();