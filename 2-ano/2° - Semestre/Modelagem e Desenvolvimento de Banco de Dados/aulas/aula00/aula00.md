# MODELAGEM E DESENVOLVIMENTO DE BANCO DE DADOS

## Aula 00 — Introdução a Banco de Dados

---

## 1. O QUE É BANCO DE DADOS?

**Banco de Dados (BD)** é uma coleção organizada de **dados relacionados**, armazenados para facilitar:

- Armazenamento
- Consulta
- Atualização
- Exclusão
- Gerenciamento

**Exemplo: Banco de Dados de uma Escola**

- Alunos
- Cursos
- Professores
- Disciplinas
- Notas

---

## 2. POR QUE USAR BANCO DE DADOS?

Muitos dados  
↓  
Organização  
↓  
Armazenamento  
↓  
Consulta  
↓  
Atualização  
↓  
Controle

**Onde encontramos?**

- Escolas
- Hospitais
- Bancos
- Comércio
- Redes sociais
- Sistemas públicos

---

## 3. SGBD

**SGBD = Sistema Gerenciador de Banco de Dados**

É o **software responsável por gerenciar o Banco de Dados**.

**Funcionamento:**

USUÁRIO / SISTEMA  
↓  
SGBD  
↓  
BANCO DE DADOS

**Exemplos:**

- MySQL
- PostgreSQL
- SQL Server
- Oracle
- SQLite
- MongoDB

---

## 4. CRUD

Principais operações realizadas em um Banco de Dados:

**C → CREATE → CRIAR**

**R → READ → CONSULTAR**

**U → UPDATE → ATUALIZAR**

**D → DELETE → EXCLUIR**

---

## 5. TIPOS DE BANCO DE DADOS

### Relacional

- Organiza os dados em **tabelas**.
- Possui relações entre os dados.
- Utiliza chaves.
- Exemplos: MySQL e PostgreSQL.

### Não Relacional — NoSQL

- Possui estrutura mais flexível.
- Pode utilizar documentos, grafos ou chave-valor.
- Exemplo: MongoDB.

### Distribuído

- Dados armazenados em **diferentes servidores ou locais**.

---

## 6. RELACIONAL × NoSQL

| Relacional           | NoSQL                             |
| -------------------- | --------------------------------- |
| Tabelas              | Documentos, grafos ou chave-valor |
| Estrutura definida   | Estrutura flexível                |
| Relações entre dados | Maior flexibilidade               |
| MySQL                | MongoDB                           |

---

## 7. MODELAGEM DE DADOS

**Modelagem de dados** é o processo de representar uma parte da realidade que será armazenada no Banco de Dados.

REALIDADE  
↓  
ANÁLISE  
↓  
MODELAGEM  
↓  
BANCO DE DADOS  
↓  
SISTEMA

**Exemplo:**

ESCOLA

ALUNO ───────── CURSO

**ALUNO**

- Nome
- CPF
- E-mail
- Data de nascimento

---

# RESUMO

DADOS  
↓  
BANCO DE DADOS  
↓  
SGBD  
↓  
CRUD  
↓  
MODELAGEM  
↓  
SISTEMA

**Antes de criar um Banco de Dados, precisamos entender e modelar os dados que queremos armazenar.**