---

# Aula — Modelagem de Dados: do Conceito à Implementação

## Slide 1 — Modelagem de Dados

### Os três níveis da modelagem

A modelagem de dados pode ser dividida em três níveis:

**1. Conceitual**
**2. Lógico**
**3. Físico**

Cada nível possui um objetivo diferente e aumenta progressivamente o nível de detalhamento.

---

## Slide 2 — Visão geral

```text
              MODELAGEM DE DADOS
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
   CONCEITUAL      LÓGICA       FÍSICA
```

### Em resumo:

* **Conceitual:** entender a realidade.
* **Lógica:** organizar os dados.
* **Física:** implementar no SGBD.

---

# 1. Modelagem Conceitual

## Slide 3 — O que é modelagem conceitual?

A **modelagem conceitual** é o primeiro nível da modelagem de dados.

Seu objetivo é compreender:

* Quais elementos existem no sistema?
* Quais informações são importantes?
* Como esses elementos se relacionam?

### Foco principal:

> **Entender a realidade que será representada no banco de dados.**

---

## Slide 4 — O que ainda não importa?

Na modelagem conceitual, **não estamos preocupados com detalhes de implementação**.

Ainda não precisamos definir:

* MySQL
* PostgreSQL
* SQL Server
* Tipos de dados
* Índices
* Armazenamento
* Configurações do SGBD

### O foco é:

**O que existe?**

**Como os elementos se relacionam?**

---

## Slide 5 — Exemplo: sistema de vendas

Imagine uma loja.

Precisamos representar:

```text
CLIENTE

PEDIDO

PRODUTO
```

Podemos identificar os relacionamentos:

```text
CLIENTE
   │
   │ realiza
   ↓
PEDIDO
   │
   │ contém
   ↓
PRODUTO
```

Neste momento, estamos apenas entendendo o funcionamento da loja.

---

## Slide 6 — Pergunta-chave da modelagem conceitual

A modelagem conceitual responde principalmente:

> **"O que existe nessa realidade e como esses elementos se relacionam?"**

Exemplo:

```text
CLIENTE ─── realiza ─── PEDIDO
```

Ainda não precisamos saber como isso será armazenado no banco.

---

# 2. Modelagem Lógica

## Slide 7 — O que é modelagem lógica?

Depois de compreender a realidade, começamos a detalhar o modelo.

Essa etapa é chamada de **modelagem lógica**.

Aqui definimos:

* Entidades
* Atributos
* Relacionamentos
* Cardinalidades
* Chaves
* Estrutura lógica dos dados

---

## Slide 8 — Exemplo de modelo lógico

### CLIENTE

```text
CLIENTE
- id_cliente
- nome
- cpf
- email
```

### PEDIDO

```text
PEDIDO
- id_pedido
- data_pedido
- valor_total
```

### PRODUTO

```text
PRODUTO
- id_produto
- nome
- preco
```

Agora o modelo está muito mais detalhado.

---

## Slide 9 — Conceitual × Lógico

| Conceitual                    | Lógico                             |
| ----------------------------- | ---------------------------------- |
| Mais abstrato                 | Mais detalhado                     |
| Identifica entidades          | Define atributos                   |
| Identifica relacionamentos    | Detalha relacionamentos            |
| Foca na realidade             | Foca na estrutura dos dados        |
| Independente da implementação | Mais próximo da estrutura do banco |

### Exemplo

**Conceitual:**

```text
CLIENTE ─── REALIZA ─── PEDIDO
```

**Lógico:**

```text
CLIENTE
- id_cliente
- nome
- cpf
- email

PEDIDO
- id_pedido
- data_pedido
- id_cliente
```

---

# 3. Modelagem Física

## Slide 10 — O que é modelagem física?

A **modelagem física** transforma o modelo lógico em uma implementação real.

Agora entram as características do **SGBD escolhido**.

Exemplos:

* MySQL
* PostgreSQL
* SQL Server
* Oracle

---

## Slide 11 — O que é definido na modelagem física?

Na modelagem física podemos definir:

* Tipos de dados
* Índices
* Restrições
* Armazenamento
* Desempenho
* Particionamento
* Configurações específicas do SGBD

### Agora a pergunta é:

> **Como isso será implementado?**

---

## Slide 12 — Exemplo de implementação

Um modelo lógico como:

```text
CLIENTE
- id_cliente
- nome
- cpf
- email
```

pode ser transformado em SQL:

```sql
CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(11),
    email VARCHAR(150)
);
```

Agora temos uma implementação concreta.

---

# 4. Os três níveis juntos

## Slide 13 — Do mundo real ao banco

```text
REALIDADE
    ↓
MODELAGEM CONCEITUAL
    ↓
MODELAGEM LÓGICA
    ↓
MODELAGEM FÍSICA
    ↓
BANCO DE DADOS IMPLEMENTADO
```

Cada etapa aumenta o nível de detalhamento.

---

## Slide 14 — Uma forma simples de lembrar

### CONCEITUAL

> **O QUE EXISTE?**

Identificamos os principais elementos e seus relacionamentos.

### LÓGICA

> **COMO OS DADOS SERÃO ORGANIZADOS?**

Definimos atributos, chaves e estrutura.

### FÍSICA

> **COMO ISSO SERÁ IMPLEMENTADO?**

Definimos tabelas, tipos de dados, índices e outras características do SGBD.

---

# 5. Entidades

## Slide 15 — O que é uma entidade?

Uma **entidade** representa algo relevante para o sistema.

Pode representar:

* Pessoa
* Objeto
* Lugar
* Evento
* Conceito

### Exemplos:

```text
ALUNO
PROFESSOR
CURSO
PRODUTO
CLIENTE
PEDIDO
FUNCIONÁRIO
DEPARTAMENTO
```

---

## Slide 16 — Como identificar uma entidade?

Uma pergunta simples ajuda:

> **"O sistema precisa armazenar informações sobre isso?"**

### Exemplo

Uma loja precisa armazenar informações sobre:

```text
CLIENTES
PRODUTOS
PEDIDOS
```

Portanto:

```text
CLIENTE
PRODUTO
PEDIDO
```

podem ser entidades do sistema.

---

## Slide 17 — O que torna algo uma entidade?

Uma entidade deve representar algo que tenha **importância para o sistema**.

Por exemplo:

### Sistema de uma loja

```text
CLIENTE       → importante
PRODUTO       → importante
PEDIDO        → importante
```

Já algo sem necessidade de armazenamento ou identificação própria provavelmente não será uma entidade.

### Regra prática:

> Se precisamos manter informações sobre algo, esse elemento pode ser candidato a entidade.

---

# 6. Atributos

## Slide 18 — O que são atributos?

As entidades representam os elementos.

Os **atributos** representam as características desses elementos.

### Exemplo

```text
CLIENTE
```

Pode possuir:

```text
Nome
CPF
E-mail
Telefone
Data de nascimento
```

Essas informações são **atributos** da entidade CLIENTE.

---

## Slide 19 — Entidade e atributos

Podemos representar:

```text
CLIENTE
 ├── Nome
 ├── CPF
 ├── E-mail
 ├── Telefone
 └── Data de nascimento
```

### Entidade

```text
CLIENTE
```

### Atributos

```text
Nome
CPF
E-mail
Telefone
Data de nascimento
```

---

## Slide 20 — Entidade × atributo

Não confunda:

### ENTIDADE

Representa o objeto ou conceito.

```text
CLIENTE
```

### ATRIBUTO

Descreve esse objeto.

```text
Nome
CPF
E-mail
Telefone
```

### Uma forma fácil de lembrar:

> **Entidade = o que é**

> **Atributo = o que descreve**

---

## Slide 21 — Exemplo: Produto

Considere a entidade:

```text
PRODUTO
```

Quais informações podem descrevê-la?

```text
PRODUTO
 ├── Nome
 ├── Descrição
 ├── Preço
 ├── Código
 └── Estoque
```

### Classificação

* **PRODUTO** → entidade
* **Nome** → atributo
* **Descrição** → atributo
* **Preço** → atributo
* **Código** → atributo
* **Estoque** → atributo

---

# 7. Relacionamentos

## Slide 22 — O que é um relacionamento?

As entidades não existem isoladamente.

Em um sistema, elas normalmente possuem relações.

Um **relacionamento** representa uma associação entre entidades.

### Exemplo

```text
CLIENTE ─── realiza ─── PEDIDO
```

Temos:

* CLIENTE → entidade
* PEDIDO → entidade
* REALIZA → relacionamento

---

## Slide 23 — Outros exemplos

### Escola

```text
ALUNO ─── cursa ─── DISCIPLINA
```

### Empresa

```text
FUNCIONÁRIO ─── pertence ─── DEPARTAMENTO
```

### Loja

```text
CLIENTE ─── realiza ─── PEDIDO
```

O relacionamento descreve **como as entidades estão associadas**.

---

# 8. Entidades + atributos + relacionamentos

## Slide 24 — Os três elementos fundamentais

Uma parte fundamental da modelagem envolve:

### 1. Entidades

```text
CLIENTE
PEDIDO
PRODUTO
```

### 2. Atributos

```text
CLIENTE
- nome
- CPF
- email
```

### 3. Relacionamentos

```text
CLIENTE ─── realiza ─── PEDIDO
```

---

## Slide 25 — Visualizando juntos

```text
┌─────────────┐
│   CLIENTE   │
├─────────────┤
│ id_cliente  │
│ nome        │
│ cpf         │
│ email       │
└─────────────┘
       │
       │ realiza
       │
       ↓
┌─────────────┐
│    PEDIDO   │
├─────────────┤
│ id_pedido   │
│ data        │
│ valor       │
└─────────────┘
```

---

# 9. Cardinalidade

## Slide 26 — O que é cardinalidade?

Depois de identificar os relacionamentos, precisamos descobrir:

> **Quantas ocorrências de uma entidade podem estar relacionadas a outra?**

Essa informação é chamada de **cardinalidade**.

---

## Slide 27 — Exemplo de cardinalidade

### Regra do sistema:

> Um cliente pode realizar vários pedidos.

Representação:

```text
CLIENTE 1 ───────── N PEDIDO
```

Isso significa:

* Um cliente pode ter vários pedidos.
* Cada pedido está associado a um cliente.

---

## Slide 28 — Outro exemplo

### Regra:

> Um departamento possui vários funcionários.

Representação:

```text
DEPARTAMENTO 1 ───────── N FUNCIONÁRIO
```

### Interpretação

Um departamento:

```text
        ┌── FUNCIONÁRIO
        ├── FUNCIONÁRIO
DEPARTAMENTO
        └── FUNCIONÁRIO
```

pode estar associado a vários funcionários.

---

# 10. Principais cardinalidades

## Slide 29 — Tipos mais comuns

As principais cardinalidades são:

```text
1 : 1
1 : N
N : N
```

Também podemos encontrar representações equivalentes como:

```text
1:1
1:N
N:N
```

---

## Slide 30 — Relacionamento 1:1

### Um para um

Uma ocorrência de uma entidade está relacionada a apenas uma ocorrência de outra entidade.

### Exemplo:

```text
PESSOA 1 ───────── 1 PASSAPORTE
```

Considerando a regra:

> Uma pessoa possui um único passaporte e um passaporte pertence a uma única pessoa.

---

## Slide 31 — Relacionamento 1:N

### Um para muitos

Uma ocorrência de uma entidade pode estar relacionada a várias ocorrências de outra.

### Exemplo:

```text
CLIENTE 1 ───────── N PEDIDO
```

Um cliente pode realizar vários pedidos.

```text
CLIENTE
   │
   ├──── PEDIDO
   ├──── PEDIDO
   └──── PEDIDO
```

---

## Slide 32 — Relacionamento N:N

### Muitos para muitos

Várias ocorrências de uma entidade podem estar relacionadas a várias ocorrências de outra.

### Exemplo:

```text
ALUNO N ───────── N DISCIPLINA
```

Um aluno pode cursar várias disciplinas.

Uma disciplina pode possuir vários alunos.

---

## Slide 33 — Exemplo visual do N:N

```text
ALUNO
 ├──── DISCIPLINA
 ├──── DISCIPLINA
 └──── DISCIPLINA

DISCIPLINA
 ├──── ALUNO
 ├──── ALUNO
 └──── ALUNO
```

### Importante

O relacionamento **N:N** terá um papel importante na transformação para o modelo relacional.

---

# 11. Diagrama Entidade-Relacionamento

## Slide 34 — O que é um DER?

O **Diagrama Entidade-Relacionamento (DER)** é uma representação gráfica do modelo de dados.

Ele permite visualizar:

* Entidades
* Atributos
* Relacionamentos
* Cardinalidades

---

## Slide 35 — Exemplo de DER

```text
┌─────────────┐
│   CLIENTE   │
├─────────────┤
│ id_cliente  │
│ nome        │
│ cpf         │
│ email       │
└─────────────┘
       │
       │ realiza
       │
       N
       │
       │
       1
┌─────────────┐
│    PEDIDO   │
├─────────────┤
│ id_pedido   │
│ data        │
│ valor       │
└─────────────┘
```

> A representação visual pode variar de acordo com a notação utilizada.

---

## Slide 36 — Para que serve o DER?

O DER ajuda a:

* Visualizar a estrutura do sistema.
* Identificar entidades.
* Identificar atributos.
* Identificar relacionamentos.
* Identificar cardinalidades.
* Encontrar possíveis problemas na modelagem.
* Facilitar a comunicação entre a equipe.
* Servir como base para a implementação do banco.

### Pense no DER como:

> **Um mapa do Banco de Dados.**

---

# 12. Exemplo completo — Sistema de vendas

## Slide 37 — Cenário

Imagine a seguinte situação:

> **Uma loja possui clientes. Os clientes realizam pedidos. Cada pedido pode conter produtos.**

Nosso objetivo é transformar essa descrição em um modelo de dados.

---

## Slide 38 — Passo 1: identificar as entidades

A partir do problema, identificamos:

```text
CLIENTE
PEDIDO
PRODUTO
```

Esses são os principais elementos do sistema.

---

## Slide 39 — Passo 2: identificar os atributos

### CLIENTE

```text
- id_cliente
- nome
- cpf
- email
```

### PEDIDO

```text
- id_pedido
- data_pedido
- valor_total
```

### PRODUTO

```text
- id_produto
- nome
- preco
```

---

## Slide 40 — Passo 3: identificar os relacionamentos

A descrição diz:

> Clientes realizam pedidos.

Então:

```text
CLIENTE ─── realiza ─── PEDIDO
```

Também diz:

> Pedidos podem conter produtos.

Então:

```text
PEDIDO ─── possui ─── PRODUTO
```

---

## Slide 41 — Passo 4: identificar as cardinalidades

### Cliente e pedido

Um cliente pode realizar vários pedidos:

```text
CLIENTE 1 ───────── N PEDIDO
```

### Pedido e produto

Um pedido pode possuir vários produtos.

Um produto pode aparecer em vários pedidos.

```text
PEDIDO N ───────── N PRODUTO
```

---

# 13. O problema do N:N

## Slide 42 — Por que o N:N precisa de atenção?

Temos:

```text
PEDIDO N ───────── N PRODUTO
```

Isso significa:

* Um pedido pode possuir vários produtos.
* Um produto pode aparecer em vários pedidos.

No modelo relacional, normalmente precisamos de uma **estrutura intermediária**.

---

## Slide 43 — Entidade associativa

Podemos criar:

```text
PEDIDO
   │
   │
   ↓
ITEM_PEDIDO
   ↑
   │
   │
PRODUTO
```

A entidade associativa será responsável por representar a relação entre pedido e produto.

---

## Slide 44 — ITEM_PEDIDO

Além de relacionar pedido e produto, `ITEM_PEDIDO` pode armazenar informações específicas da relação.

### Exemplo:

```text
ITEM_PEDIDO
- quantidade
- preco_unitario
```

Isso é importante porque a quantidade comprada e o preço praticado pertencem ao **item do pedido**, e não simplesmente ao produto.

---

## Slide 45 — Transformando N:N

Em vez de:

```text
PEDIDO N ───────── N PRODUTO
```

Podemos representar:

```text
PEDIDO
   │
   │ 1:N
   ↓
ITEM_PEDIDO
   ↑
   │ N:1
   │
PRODUTO
```

Assim, o relacionamento N:N é dividido em dois relacionamentos:

```text
PEDIDO 1 ─── N ITEM_PEDIDO
```

e

```text
PRODUTO 1 ─── N ITEM_PEDIDO
```

---

# 14. Do problema real ao modelo

## Slide 46 — Exemplo: sistema escolar

### Problema

> Uma escola precisa de um sistema para controlar alunos e cursos.

---

## Slide 47 — Análise do problema

Identificamos as entidades:

```text
ALUNO
CURSO
```

E podemos identificar um relacionamento:

```text
ALUNO ─── pertence ─── CURSO
```

---

## Slide 48 — Atributos

### ALUNO

```text
- nome
- CPF
- data_nascimento
- email
```

### CURSO

```text
- nome
- duração
- descrição
```

---

## Slide 49 — Modelo visual

```text
┌─────────────┐
│    ALUNO    │
├─────────────┤
│ nome        │
│ CPF         │
│ nascimento  │
│ email       │
└─────────────┘
       │
       │ pertence
       ↓
┌─────────────┐
│    CURSO    │
├─────────────┤
│ nome        │
│ duração     │
│ descrição   │
└─────────────┘
```

Esse modelo ainda poderá ser refinado.

---

# 15. Do modelo conceitual ao banco

## Slide 50 — O processo completo

```text
                 REALIDADE
                    │
                    ↓
          ┌─────────────────────┐
          │ MODELAGEM CONCEITUAL│
          │                     │
          │ Entidades           │
          │ Relacionamentos     │
          └─────────────────────┘
                    │
                    ↓
             ┌──────────────┐
             │    LÓGICA    │
             │              │
             │ Atributos    │
             │ Chaves       │
             │ Cardinalidade│
             └──────────────┘
                    │
                    ↓
             ┌──────────────┐
             │    FÍSICA    │
             │              │
             │ Tabelas      │
             │ Tipos        │
             │ Índices      │
             │ Restrições   │
             └──────────────┘
                    │
                    ↓
              BANCO DE DADOS
```

---

# 16. Exemplo de transformação

## Slide 51 — Realidade

Imagine:

> **Uma loja possui clientes. Um cliente realiza pedidos.**

A informação ainda está em linguagem natural.

```text
Cliente realiza Pedido
```

---

## Slide 52 — Modelo conceitual

Transformamos a realidade em entidades e relacionamento:

```text
CLIENTE 1 ───────── N PEDIDO
```

Neste nível, estamos interessados principalmente no significado.

---

## Slide 53 — Modelo lógico

Agora detalhamos os dados:

### CLIENTE

```text
- id_cliente
- nome
- cpf
```

### PEDIDO

```text
- id_pedido
- data
- id_cliente
```

Observe que `id_cliente` aparece em PEDIDO para representar a associação com CLIENTE.

---

## Slide 54 — Modelo físico

Finalmente, podemos implementar no SGBD:

```sql
CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(11)
);

CREATE TABLE pedido (
    id_pedido INT PRIMARY KEY,
    data_pedido DATE,
    id_cliente INT,
    FOREIGN KEY (id_cliente)
        REFERENCES cliente(id_cliente)
);
```

Agora temos uma estrutura concreta de banco de dados.

---

# 17. Resumo da aula

## Slide 55 — O que aprendemos?

Nesta aula, vimos:

### Modelagem de dados

Possui três níveis:

```text
CONCEITUAL
LÓGICO
FÍSICO
```

### Conceitual

* Entende a realidade.
* Identifica entidades.
* Identifica relacionamentos.

### Lógico

* Define atributos.
* Define chaves.
* Define cardinalidades.
* Organiza a estrutura dos dados.

### Físico

* Implementa o modelo.
* Define tipos de dados.
* Cria tabelas.
* Define índices e restrições.
* Considera características do SGBD.

---

## Slide 56 — Conceitos fundamentais

```text
ENTIDADE
     ↓
representa algo importante
para o sistema

ATRIBUTO
     ↓
descreve uma entidade

RELACIONAMENTO
     ↓
associa entidades

CARDINALIDADE
     ↓
define quantas ocorrências
podem estar relacionadas

DER
     ↓
representa graficamente
o modelo
```

---

## Slide 57 — Cardinalidades

| Cardinalidade | Significado        | Exemplo             |
| ------------- | ------------------ | ------------------- |
| **1:1**       | Um para um         | Pessoa ↔ Passaporte |
| **1:N**       | Um para muitos     | Cliente → Pedidos   |
| **N:N**       | Muitos para muitos | Aluno ↔ Disciplina  |

### Atenção:

Relacionamentos **N:N** normalmente precisam de uma estrutura intermediária no modelo relacional.

---

# 18. Atividade em sala

## Slide 58 — Atividade 1: identificar entidades

Considere:

> Uma biblioteca possui livros, autores e leitores. Um leitor pode realizar vários empréstimos. Cada empréstimo está relacionado a um livro.

### Pergunta:

**Quais são as possíveis entidades?**

---

## Slide 59 — Atividade 2: identificar atributos

Para cada entidade identificada, pense em possíveis atributos.

### LIVRO

```text
?
?
?
```

### LEITOR

```text
?
?
?
```

### AUTOR

```text
?
?
?
```

---

## Slide 60 — Atividade 3: identificar relacionamentos

Analise:

> Um leitor realiza empréstimos. Um empréstimo está relacionado a um livro.

Identifique os relacionamentos:

```text
LEITOR ─── ? ─── EMPRÉSTIMO

EMPRÉSTIMO ─── ? ─── LIVRO
```

---

## Slide 61 — Atividade 4: identificar cardinalidades

Determine as cardinalidades:

```text
LEITOR ? ───────── ? EMPRÉSTIMO

LIVRO ? ───────── ? EMPRÉSTIMO
```

### Justifique sua resposta.

---

# 19. Perguntas para revisão

## Slide 62 — Revisão

### 1. Quais são os três níveis da modelagem de dados?

### 2. Qual é o objetivo da modelagem conceitual?

### 3. Qual é a diferença entre entidade e atributo?

### 4. O que é um relacionamento?

### 5. O que representa uma cardinalidade?

### 6. Qual a diferença entre 1:1, 1:N e N:N?

### 7. O que é um DER?

### 8. Por que relacionamentos N:N normalmente precisam de uma estrutura intermediária?

---

# 20. Slide final — Para memorizar

## Slide 63 — A ideia principal

```text
             REALIDADE
                 ↓
        ┌────────────────┐
        │   CONCEITUAL   │
        │   O que existe?│
        └────────────────┘
                 ↓
        ┌────────────────┐
        │     LÓGICO     │
        │ Como organizar?│
        └────────────────┘
                 ↓
        ┌────────────────┐
        │     FÍSICO     │
        │ Como implementar│
        └────────────────┘
                 ↓
           BANCO DE DADOS
```

### Conceitos para guardar:

**Entidade** → o que existe.

**Atributo** → o que descreve.

**Relacionamento** → como se relacionam.

**Cardinalidade** → quantos podem se relacionar.

**DER** → representação visual.

**Conceitual → Lógico → Físico** → caminho da realidade até a implementação.
