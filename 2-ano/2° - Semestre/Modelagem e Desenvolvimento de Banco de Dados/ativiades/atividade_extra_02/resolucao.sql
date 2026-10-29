-- 1- Cria um banco de dados para uma escola

CREATE DATABASE IF NOT EXISTS escola;

CREATE DATABASE IF NOT EXISTS comercio;
CREATE DATABASE IF NOT EXISTS academia;
CREATE DATABASE IF NOT EXISTS cinema;
CREATE DATABASE IF NOT EXISTS hotel;

-- 2 - Cria uma tabela de alunos

CREATE TABLE IF NOT EXISTS alunos (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    nota DECIMAL(4,2),
    ativo BOOLEAN,
    cadastro DATE
);

CREATE TABLE IF NOT EXISTS professores(
    id_professor INT PRIMARY KEY,
    nome_professor VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS vaga(
    id_vaga INT PRIMARY KEY,
    ocupada BOOLEAN
);

CREATE TABLE IF NOT EXISTS filmes(
    id_filme INT PRIMARY KEY,
    duracao TIME
);

CREATE TABLE IF NOT EXISTS posts(
    id_post INT PRIMARY KEY,
    conteudo TEXT
);

CREATE TABLE IF NOT EXISTS cortes(
    id INT PRIMARY KEY
);

-- 3 - Renomeia o atributo nome para nome_completo

ALTER TABLE alunos RENAME COLUMN nome TO nome_aluno;
ALTER TABLE alunos RENAME COLUMN id TO id_aluno;
ALTER TABLE cortes RENAME COLUMN id TO id_corte;

-- 4 - Adiciona o atributo email

ALTER TABLE alunos ADD COLUMN email VARCHAR(100);
ALTER TABLE cortes ADD COLUMN preco DECIMAL;
ALTER TABLE cortes ADD COLUMN modelo VARCHAR(100);

-- 5 - Altera o tamanho do campo nome_aluno
ALTER TABLE alunos MODIFY COLUMN nome_aluno VARCHAR(150);
ALTER TABLE cortes MODIFY COLUMN modelo VARCHAR(50);
ALTER TABLE cortes MODIFY COLUMN preco INT;
