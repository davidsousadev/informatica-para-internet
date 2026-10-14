async function usuarios() {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/users");
        const dados = await response.json();

        console.log(JSON.stringify(dados[0]["name"], null, 2));

    } catch (error) {
        console.log(error);
    }
}

usuarios();