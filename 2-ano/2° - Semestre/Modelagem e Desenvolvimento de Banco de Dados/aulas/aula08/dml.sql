-- 2 - Cria uma tabela de alunos

CREATE TABLE IF NOT EXISTS alunos (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    nota DECIMAL(4,2),
    ativo BOOLEAN,
    data_cadastro DATE
);

INSERT INTO alunos (
    id, 
    nome, 
    idade, 
    nota, 
    ativo, 
    data_cadastro) 
VALUES
(1, 'David Sousa', 19, 10, TRUE, 2026-04-08),
(2, 'Wallas Silva', 22, 9.5, FALSE, 2025-01-01);




-- Maria do Amparo

INSERT INTO professores (id, cpf, nome, telefone) VALUES
(1, '001.001.001-10', 'Maria do Amparo', '99 9.9999-9999');

-- Vitor Gabriel

INSERT INTO comentarios (id, nome, texto, data_comentario) VALUES
(11213, 'jef007', 'Aluno nota 10', 2026-11-03)

-- Anderson Lima

INSERT INTO livros (id, nome, valor, numero_de_paginas) VALUES
(15, 'As 48 leis do poder', 180.00, 450);