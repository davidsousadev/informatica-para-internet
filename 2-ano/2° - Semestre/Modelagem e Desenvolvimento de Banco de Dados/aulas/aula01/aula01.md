# MODELAGEM E DESENVOLVIMENTO DE BANCO DE DADOS

## Aula 01 — Modelagem de Dados: Conceitos, Níveis e Diagrama Entidade-Relacionamento

---

## 1. RELEMBRANDO A AULA ANTERIOR

Na aula anterior, estudamos os conceitos fundamentais de Banco de Dados.

Vimos que:

* Banco de Dados é uma coleção organizada de dados relacionados.
* O SGBD é o software responsável por gerenciar o Banco de Dados.
* CRUD representa as principais operações realizadas sobre os dados.
* Existem diferentes tipos de Banco de Dados.
* Bancos de Dados relacionais organizam os dados principalmente em tabelas.
* A modelagem de dados é utilizada antes da implementação do Banco de Dados.

Podemos representar esse processo da seguinte forma:

```text
REALIDADE
   ↓
ANÁLISE
   ↓
MODELAGEM
   ↓
BANCO DE DADOS
   ↓
SISTEMA
```

Nesta aula, vamos aprofundar justamente a etapa de **MODELAGEM**.

---

# 2. O QUE É MODELAGEM DE DADOS?

**Modelagem de dados** é o processo de representar, de forma organizada, os dados e as regras de uma realidade que será utilizada por um sistema.

Em outras palavras:

> Modelar dados significa transformar uma realidade do mundo real em uma estrutura que possa ser compreendida e posteriormente armazenada em um Banco de Dados.

Imagine uma escola.

Na realidade, temos:

* Alunos
* Professores
* Cursos
* Disciplinas
* Matrículas
* Notas

O sistema precisa representar essas informações.

Porém, não podemos simplesmente colocar "a escola inteira" dentro do Banco de Dados.

Precisamos analisar a realidade e identificar:

* O que precisa ser armazenado?
* Quais informações descrevem cada elemento?
* Quais elementos possuem relação?
* Quais regras precisam ser respeitadas?

É justamente essa organização que chamamos de **modelagem de dados**.

---

# 3. POR QUE FAZER MODELAGEM?

Uma dúvida comum é:

> "Por que não criar as tabelas diretamente?"

Porque criar tabelas sem entender previamente os dados pode gerar diversos problemas.

Uma modelagem inadequada pode resultar em:

* Dados duplicados
* Informações inconsistentes
* Relacionamentos incorretos
* Dificuldade de manutenção
* Consultas complexas
* Problemas de desempenho
* Dificuldade para realizar alterações futuras

Podemos pensar na modelagem como o **projeto de uma construção**.

Antes de construir uma casa, normalmente fazemos um projeto.

```text
PROJETO DA CASA
      ↓
  CONSTRUÇÃO
```

Da mesma forma:

```text
MODELAGEM DO BANCO
       ↓
IMPLEMENTAÇÃO
```

A modelagem funciona como um planejamento da estrutura que será construída.

---

# 4. MODELAGEM E REALIDADE

Um Banco de Dados representa uma determinada parte da realidade.

Por exemplo:

```text
REALIDADE
   ↓
ESCOLA
```

Na escola existem diversos elementos.

```text
ESCOLA
 ├── ALUNOS
 ├── PROFESSORES
 ├── CURSOS
 ├── DISCIPLINAS
 ├── TURMAS
 └── NOTAS
```

O sistema não precisa necessariamente representar tudo o que existe na escola.

Ele representa aquilo que é **relevante para os objetivos do sistema**.

Por exemplo, um sistema acadêmico pode precisar armazenar:

* Nome do aluno
* CPF
* Data de nascimento
* Curso
* Disciplinas
* Notas

Mas talvez não seja necessário armazenar informações como:

* Cor favorita do aluno
* Música favorita
* Filme favorito

Isso depende dos **requisitos e das regras de negócio**.

---

# 5. REGRAS DE NEGÓCIO

As **regras de negócio** são condições ou regras que representam como determinada organização ou sistema funciona.

Exemplos:

```text
Um aluno pode estar matriculado em várias disciplinas.

Uma disciplina pode possuir vários alunos.

Um pedido pertence a um cliente.

Um pedido pode possuir vários produtos.

Um produto possui um preço.

Um funcionário pertence a um departamento.
```

Essas regras são importantes porque ajudam a determinar como os dados deverão ser organizados.

Por exemplo:

> Um cliente pode realizar vários pedidos.

Podemos representar:

```text
CLIENTE
   │
   │ realiza
   ↓
PEDIDO
```

Essa informação será importante posteriormente para definir o relacionamento entre as entidades.

---

# 6. OS TRÊS NÍVEIS DA MODELAGEM

A modelagem de dados pode ser dividida em três níveis principais:

```text
MODELAGEM
    │
    ├── CONCEITUAL
    │
    ├── LÓGICA
    │
    └── FÍSICA
```

Cada nível possui uma finalidade diferente.

---

# 7. MODELAGEM CONCEITUAL

A **modelagem conceitual** é o primeiro nível da modelagem.

Neste momento, estamos preocupados principalmente em entender:

* Quais são os principais elementos do sistema?
* Quais informações são importantes?
* Como esses elementos se relacionam?

Ainda não estamos preocupados com detalhes específicos de um SGBD.

Por exemplo, imagine um sistema de vendas.

Podemos identificar:

```text
CLIENTE

PEDIDO

PRODUTO
```

E seus relacionamentos:

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

Nesse momento, ainda não estamos pensando em:

* MySQL
* PostgreSQL
* tipos de dados
* índices
* armazenamento físico

O objetivo é compreender a realidade.

---

# 8. EXEMPLO DE MODELAGEM CONCEITUAL

Imagine a seguinte situação:

> Uma loja possui clientes. Um cliente pode realizar vários pedidos. Cada pedido pode possuir vários produtos.

Podemos identificar três entidades:

```text
CLIENTE

PEDIDO

PRODUTO
```

E os relacionamentos:

```text
CLIENTE
   │
   │ realiza
   ↓
PEDIDO
   │
   │ possui
   ↓
PRODUTO
```

A modelagem conceitual responde principalmente:

> "O que existe nessa realidade e como esses elementos se relacionam?"

---

# 9. MODELAGEM LÓGICA

Depois de compreender a realidade, podemos detalhar o modelo.

Essa etapa é chamada de **modelagem lógica**.

Aqui começamos a definir:

* Entidades
* Atributos
* Relacionamentos
* Cardinalidades
* Chaves
* Estrutura lógica dos dados

Por exemplo:

```text
CLIENTE
- id_cliente
- nome
- cpf
- email
```

```text
PEDIDO
- id_pedido
- data_pedido
- valor_total
```

```text
PRODUTO
- id_produto
- nome
- preco
```

Agora a representação está mais detalhada.

---

# 10. CONCEITUAL × LÓGICA

Podemos comparar os dois níveis.

| Modelagem Conceitual          | Modelagem Lógica                   |
| ----------------------------- | ---------------------------------- |
| Mais abstrata                 | Mais detalhada                     |
| Identifica entidades          | Define atributos                   |
| Identifica relacionamentos    | Detalha relacionamentos            |
| Foca na realidade             | Foca na estrutura dos dados        |
| Independente da implementação | Mais próxima da estrutura do banco |

Exemplo:

### Conceitual

```text
CLIENTE ─── REALIZA ─── PEDIDO
```

### Lógica

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

# 11. MODELAGEM FÍSICA

A **modelagem física** é a etapa em que o modelo lógico é transformado em uma implementação real.

Aqui entram questões relacionadas ao SGBD escolhido.

Por exemplo:

* MySQL
* PostgreSQL
* SQL Server
* Oracle

Agora precisamos pensar em detalhes como:

* Tipos de dados
* Índices
* Restrições
* Armazenamento
* Desempenho
* Particionamento
* Configurações específicas do SGBD

Por exemplo:

```sql
CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(11),
    email VARCHAR(150)
);
```

Nesse ponto, já estamos trabalhando com uma implementação concreta.

---

# 12. OS TRÊS NÍVEIS JUNTOS

Podemos resumir:

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

### Conceitual

```text
O QUE EXISTE?
```

### Lógica

```text
COMO OS DADOS SERÃO ORGANIZADOS?
```

### Física

```text
COMO ISSO SERÁ IMPLEMENTADO?
```

---

# 13. ENTIDADES

Um dos conceitos mais importantes da modelagem é o conceito de **entidade**.

Uma entidade representa um objeto, pessoa, lugar, evento ou conceito relevante para o sistema.

Exemplos:

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

Uma entidade deve representar algo que tenha importância para o sistema.

---

# 14. COMO IDENTIFICAR UMA ENTIDADE?

Uma boa pergunta para identificar entidades é:

> "O sistema precisa armazenar informações sobre isso?"

Por exemplo:

> Uma loja precisa armazenar informações sobre seus clientes.

Então:

```text
CLIENTE
```

pode ser uma entidade.

A loja também precisa armazenar informações sobre os produtos:

```text
PRODUTO
```

E sobre os pedidos:

```text
PEDIDO
```

Temos:

```text
CLIENTE
PRODUTO
PEDIDO
```

Esses elementos podem fazer parte do modelo do sistema.

---

# 15. ATRIBUTOS

As entidades representam os elementos.

Os **atributos** representam as características desses elementos.

Por exemplo:

```text
CLIENTE
```

pode possuir:

```text
Nome
CPF
E-mail
Telefone
Data de nascimento
```

Essas informações são atributos da entidade CLIENTE.

Podemos representar:

```text
CLIENTE
 ├── Nome
 ├── CPF
 ├── E-mail
 ├── Telefone
 └── Data de nascimento
```

---

# 16. ENTIDADE × ATRIBUTO

É importante não confundir os dois conceitos.

### Entidade

Representa o objeto ou conceito.

```text
CLIENTE
```

### Atributos

Descrevem esse objeto.

```text
Nome
CPF
E-mail
Telefone
```

Portanto:

```text
CLIENTE
   │
   ├── Nome
   ├── CPF
   ├── E-mail
   └── Telefone
```

Uma forma simples de lembrar:

> **Entidade é "o que é".**

> **Atributo é "o que descreve".**

---

# 17. OUTRO EXEMPLO

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

Nesse caso:

* PRODUTO → entidade
* Nome → atributo
* Descrição → atributo
* Preço → atributo
* Código → atributo
* Estoque → atributo

---

# 18. RELACIONAMENTOS

As entidades não existem isoladamente.

Em um sistema, elas normalmente possuem relações.

Um **relacionamento** representa uma associação entre entidades.

Exemplo:

```text
CLIENTE ─── realiza ─── PEDIDO
```

Nesse caso:

* CLIENTE é uma entidade.
* PEDIDO é uma entidade.
* REALIZA é o relacionamento.

Outro exemplo:

```text
ALUNO ─── cursa ─── DISCIPLINA
```

Outro:

```text
FUNCIONÁRIO ─── pertence ─── DEPARTAMENTO
```

---

# 19. ENTIDADES + ATRIBUTOS + RELACIONAMENTOS

Esses três elementos formam uma parte fundamental da modelagem.

```text
        RELACIONAMENTO
              │
              ↓
        ┌───────────┐
        │  CLIENTE  │
        └───────────┘
          │  │  │
          ↓  ↓  ↓
        Nome CPF Email
```

E podemos relacionar CLIENTE com PEDIDO:

```text
┌───────────┐       ┌───────────┐
│  CLIENTE  │───────│   PEDIDO  │
└───────────┘ realiza└───────────┘
```

---

# 20. CARDINALIDADE

Depois de identificar os relacionamentos, precisamos entender **quantas ocorrências de uma entidade podem estar relacionadas a outra**.

Essa informação é chamada de **cardinalidade**.

Exemplo:

> Um cliente pode realizar vários pedidos.

Podemos representar:

```text
CLIENTE 1 ───────── N PEDIDO
```

Isso significa:

* Um cliente pode ter vários pedidos.
* Cada pedido está associado a um cliente.

Outro exemplo:

> Um departamento possui vários funcionários.

```text
DEPARTAMENTO 1 ───────── N FUNCIONÁRIO
```

---

# 21. PRINCIPAIS CARDINALIDADES

As cardinalidades mais comuns são:

```text
1 : 1
1 : N
N : N
```

---

## 21.1 UM PARA UM — 1:1

Uma ocorrência de uma entidade está relacionada a apenas uma ocorrência de outra entidade.

Exemplo:

```text
PESSOA 1 ───────── 1 PASSAPORTE
```

Considerando uma determinada regra do sistema:

> Uma pessoa possui um único passaporte e um passaporte pertence a uma única pessoa.

---

## 21.2 UM PARA MUITOS — 1:N

Uma ocorrência de uma entidade pode estar relacionada a várias ocorrências de outra entidade.

Exemplo:

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

## 21.3 MUITOS PARA MUITOS — N:N

Várias ocorrências de uma entidade podem estar relacionadas a várias ocorrências de outra entidade.

Exemplo:

```text
ALUNO N ───────── N DISCIPLINA
```

Um aluno pode cursar várias disciplinas.

Uma disciplina pode possuir vários alunos.

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

Esse tipo de relacionamento será especialmente importante quando estudarmos a implementação do modelo relacional.

---

# 22. DIAGRAMA ENTIDADE-RELACIONAMENTO

O **Diagrama Entidade-Relacionamento (DER ou ERD)** é uma representação gráfica do modelo de dados.

Ele permite visualizar:

* Entidades
* Atributos
* Relacionamentos
* Cardinalidades

Em vez de analisar apenas textos, podemos representar graficamente a estrutura.

Exemplo simplificado:

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

O formato visual pode variar conforme a notação utilizada.

---

# 23. PARA QUE SERVE O DER?

O Diagrama Entidade-Relacionamento ajuda a:

* Visualizar a estrutura do sistema.
* Identificar entidades.
* Identificar atributos.
* Identificar relacionamentos.
* Identificar cardinalidades.
* Encontrar possíveis problemas na modelagem.
* Facilitar a comunicação entre membros da equipe.
* Servir como base para a implementação do Banco de Dados.

Podemos pensar no DER como uma espécie de **mapa do Banco de Dados**.

---

# 24. EXEMPLO COMPLETO — SISTEMA DE VENDAS

Vamos construir um exemplo passo a passo.

Imagine a seguinte situação:

> Uma loja possui clientes. Os clientes realizam pedidos. Cada pedido pode conter produtos.

### Passo 1 — Identificar as entidades

```text
CLIENTE
PEDIDO
PRODUTO
```

### Passo 2 — Identificar os atributos

```text
CLIENTE
- id_cliente
- nome
- cpf
- email
```

```text
PEDIDO
- id_pedido
- data_pedido
- valor_total
```

```text
PRODUTO
- id_produto
- nome
- preco
```

### Passo 3 — Identificar os relacionamentos

```text
CLIENTE realiza PEDIDO
```

```text
PEDIDO possui PRODUTO
```

### Passo 4 — Identificar as cardinalidades

```text
CLIENTE 1 ───────── N PEDIDO
```

Um cliente pode realizar vários pedidos.

E:

```text
PEDIDO N ───────── N PRODUTO
```

Um pedido pode possuir vários produtos e um produto pode aparecer em vários pedidos.

---

# 25. UMA OBSERVAÇÃO IMPORTANTE SOBRE N:N

O relacionamento:

```text
PEDIDO N ───────── N PRODUTO
```

é comum em sistemas de vendas.

Porém, em um Banco de Dados relacional, normalmente precisamos criar uma estrutura intermediária para representar esse relacionamento.

Podemos ter:

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

A entidade associativa `ITEM_PEDIDO` pode armazenar informações como:

```text
ITEM_PEDIDO
- quantidade
- preco_unitario
```

Assim conseguimos representar:

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

Esse assunto será aprofundado posteriormente, quando estudarmos a transformação do modelo conceitual e lógico para estruturas relacionais.

---

# 26. DO PROBLEMA REAL AO MODELO

Podemos resumir o processo de modelagem com um exemplo.

### Problema

> Uma escola precisa de um sistema para controlar alunos e cursos.

### Análise

Identificamos:

```text
ALUNO
CURSO
```

### Relacionamento

```text
ALUNO ─── pertence ─── CURSO
```

### Atributos

```text
ALUNO
- nome
- CPF
- data_nascimento
- email
```

```text
CURSO
- nome
- duração
- descrição
```

### Modelo

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
       │
       ↓
┌─────────────┐
│    CURSO    │
├─────────────┤
│ nome        │
│ duração     │
│ descrição   │
└─────────────┘
```

Esse modelo poderá posteriormente ser refinado e transformado em uma estrutura lógica e, depois, em uma implementação física.

---

# 27. CONCEITUAL → LÓGICO → FÍSICO

Vamos visualizar todo o processo:

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
             │   LÓGICA     │
             │              │
             │ Atributos    │
             │ Chaves       │
             │ Cardinalidade│
             └──────────────┘
                    │
                    ↓
             ┌──────────────┐
             │   FÍSICA     │
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

# 28. EXEMPLO DE TRANSFORMAÇÃO

Imagine que na realidade temos:

```text
Uma loja possui clientes.
Um cliente realiza pedidos.
```

### Realidade

```text
Cliente realiza Pedido
```

### Modelo conceitual

```text
CLIENTE 1 ───────── N PEDIDO
```

### Modelo lógico

```text
CLIENTE
- id_cliente
- nome
- cpf

PEDIDO
- id_pedido
- data
- id_cliente
```

### Modelo físico

A estrutura pode ser implementada em um SGBD utilizando SQL:

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

Observe que cada etapa possui um nível diferente de detalhe.

---

# 29. O PAPEL DA MODELAGEM NO DESENVOLVIMENTO

A modelagem não existe apenas para criar um desenho bonito.

Ela possui uma função prática no desenvolvimento.

Uma boa modelagem ajuda a:

```text
COMPREENDER O PROBLEMA
        ↓
ORGANIZAR OS DADOS
        ↓
DEFINIR RELACIONAMENTOS
        ↓
IDENTIFICAR REGRAS
        ↓
EVITAR INCONSISTÊNCIAS
        ↓
FACILITAR A IMPLEMENTAÇÃO
        ↓
FACILITAR A MANUTENÇÃO
```

Por isso, modelar corretamente antes da implementação pode reduzir problemas futuros.

---

# 30. ERROS COMUNS NA MODELAGEM

Alguns erros aparecem com frequência durante a criação de modelos.

## 30.1 Confundir entidade com atributo

Exemplo:

```text
CLIENTE
 ├── Nome
 ├── CPF
 └── Endereço
```

Nesse caso, CLIENTE é uma entidade.

Nome, CPF e Endereço são atributos.

---

## 30.2 Criar entidades sem necessidade

Nem tudo que aparece no sistema precisa necessariamente virar uma entidade.

É necessário analisar os requisitos e entender se aquele elemento realmente precisa ser representado e armazenado.

---

## 30.3 Ignorar relacionamentos

Não basta identificar:

```text
CLIENTE
PEDIDO
PRODUTO
```

Também precisamos entender:

```text
CLIENTE realiza PEDIDO

PEDIDO possui PRODUTO
```

---

## 30.4 Não definir cardinalidades

Não basta dizer que:

```text
CLIENTE está relacionado com PEDIDO
```

Precisamos entender:

> Um cliente pode ter quantos pedidos?

> Um pedido pertence a quantos clientes?

Essas perguntas ajudam a determinar a cardinalidade.

---

# 31. CHECKLIST DE MODELAGEM

Antes de considerar um modelo pronto, podemos fazer algumas perguntas:

### Entidades

* Quais são os principais objetos ou conceitos?
* Todas as entidades necessárias foram identificadas?

### Atributos

* Quais informações descrevem cada entidade?
* Os atributos realmente pertencem à entidade correta?

### Relacionamentos

* Como as entidades se relacionam?
* Todos os relacionamentos importantes foram identificados?

### Cardinalidades

* Uma entidade pode se relacionar com quantas ocorrências da outra?
* O relacionamento é 1:1, 1:N ou N:N?

### Regras de negócio

* Existem regras que precisam ser representadas?
* Existem restrições importantes?

### Implementação

* O modelo poderá ser transformado em uma estrutura lógica?
* A implementação atenderá aos requisitos do sistema?

---

# 32. ATIVIDADE DE FIXAÇÃO

Considere o seguinte cenário:

> Uma biblioteca possui livros e usuários. Um usuário pode realizar vários empréstimos. Cada empréstimo está relacionado a um livro.

## Questão 1

Quais são as possíveis entidades?

---

## Questão 2

Quais atributos poderiam existir na entidade `USUARIO`?

---

## Questão 3

Quais atributos poderiam existir na entidade `LIVRO`?

---

## Questão 4

Qual é o relacionamento entre `USUARIO` e `EMPRESTIMO`?

---

## Questão 5

Qual é a possível cardinalidade entre `USUARIO` e `EMPRESTIMO`?

---

## Questão 6

Crie uma representação simples do modelo:

```text
ENTIDADE ─── RELACIONAMENTO ─── ENTIDADE
```

---

# 33. DESAFIO

Considere o seguinte cenário:

> Uma universidade possui alunos e disciplinas. Um aluno pode cursar várias disciplinas e uma disciplina pode ser cursada por vários alunos.

Identifique:

1. As entidades.
2. Os principais atributos.
3. O relacionamento.
4. A cardinalidade.
5. Se existe um relacionamento N:N.
6. Como esse relacionamento poderia ser representado em um modelo relacional.

Tente representar graficamente:

```text
┌─────────────┐
│             │
│    ALUNO    │
│             │
└─────────────┘
       │
       │
       ?
       │
       │
┌─────────────┐
│             │
│ DISCIPLINA  │
│             │
└─────────────┘
```

---

# 34. RESUMO DA AULA

Nesta aula aprendemos que **modelagem de dados** é o processo de representar de maneira organizada uma realidade que será utilizada por um sistema.

Aprendemos também os três níveis principais:

```text
CONCEITUAL
     ↓
LÓGICO
     ↓
FÍSICO
```

### Modelagem conceitual

Foca na compreensão da realidade.

```text
ENTIDADES
RELACIONAMENTOS
```

### Modelagem lógica

Detalha a estrutura dos dados.

```text
ENTIDADES
ATRIBUTOS
RELACIONAMENTOS
CARDINALIDADES
CHAVES
```

### Modelagem física

Transforma o modelo em uma implementação real.

```text
TABELAS
TIPOS DE DADOS
ÍNDICES
RESTRIÇÕES
ARMAZENAMENTO
```

Também estudamos:

```text
ENTIDADE
   ↓
representa algo relevante

ATRIBUTO
   ↓
descreve uma entidade

RELACIONAMENTO
   ↓
associa entidades

CARDINALIDADE
   ↓
define quantas ocorrências podem participar do relacionamento

DER / ERD
   ↓
representa graficamente o modelo
```

---

# 35. MAPA MENTAL DA AULA

```text
                    MODELAGEM DE DADOS
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ↓                ↓                ↓
    CONCEITUAL          LÓGICA           FÍSICA
          │                │                │
          ↓                ↓                ↓
     Entidades         Atributos         Tabelas
     Relações          Chaves            Tipos
                       Cardinalidade     Índices
                                         Restrições
          │
          ↓
        DER
          │
          ├── Entidades
          ├── Atributos
          ├── Relacionamentos
          └── Cardinalidades
```

---

# 36. CONCLUSÃO

A modelagem de dados é uma etapa fundamental para o desenvolvimento de um Banco de Dados.

Antes de pensar em tabelas e comandos SQL, precisamos compreender a realidade que será representada.

O processo pode ser resumido assim:

```text
REALIDADE
   ↓
ANÁLISE
   ↓
ENTIDADES
   ↓
ATRIBUTOS
   ↓
RELACIONAMENTOS
   ↓
CARDINALIDADES
   ↓
MODELO CONCEITUAL
   ↓
MODELO LÓGICO
   ↓
MODELO FÍSICO
   ↓
BANCO DE DADOS
```

A ideia central desta aula é:

> **Antes de implementar um Banco de Dados, precisamos entender o problema, identificar os dados relevantes e definir como eles se relacionam.**

Uma boa modelagem serve como base para um Banco de Dados mais organizado, consistente, compreensível e adequado às necessidades do sistema.

---

# PRÓXIMA ETAPA

Na próxima etapa, podemos avançar no estudo da modelagem e aprofundar conceitos como:

* Chaves primárias
* Chaves estrangeiras
* Cardinalidade
* Participação nos relacionamentos
* Relacionamentos 1:1, 1:N e N:N
* Entidades associativas
* Construção detalhada de Diagramas Entidade-Relacionamento
* Transformação do modelo conceitual em modelo lógico
