const express = require('express');
const app = express();
app.use(express.json());
// Rota inicial
app.get('/', (req, res) => {
    res.json({
        mensagem: 'Minha API Express está funcionando!' }); });
// Listar usuários
app.get('/usuarios', (req, res) => {
    res.json([{ id: 1, nome: 'João' }, { id: 2, nome: 'Maria' } ]); });
// Cadastrar usuário
app.post('/usuarios', (req, res) => { const usuario = req.body;
    res.status(201).json({ mensagem: 'Usuário cadastrado!', usuario
    }); });
// Iniciar servidor
app.listen(3000, () => { console.log('API rodando em http://localhost:3000'); });