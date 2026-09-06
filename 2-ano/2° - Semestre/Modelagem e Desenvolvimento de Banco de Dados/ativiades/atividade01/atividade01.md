# ATIVIDADE — MODELAGEM DE DADOS

## Modelagem Conceitual, Entidades, Atributos e Relacionamentos

### Orientações

Leia atentamente cada situação-problema antes de responder.

As respostas devem ser **discursivas e justificadas**. Não basta apenas listar entidades ou atributos: explique suas decisões sempre que solicitado.

Nas atividades em que for necessário criar atributos, procure escolher informações que sejam **realmente relevantes para o funcionamento do sistema**.

---

# ATIVIDADE 01 — SISTEMA DE BIBLIOTECA

Uma biblioteca deseja desenvolver um sistema para controlar seu acervo e os empréstimos realizados pelos usuários.

O sistema deverá armazenar informações sobre os livros disponíveis, os usuários cadastrados e os empréstimos realizados.

Um usuário pode realizar vários empréstimos ao longo do tempo. Cada empréstimo registra a retirada de um livro e deve permitir identificar quando o livro foi emprestado e quando foi devolvido.

### Responda:

**a)** Quais entidades você identificaria nesse sistema?

**b)** Desenvolva pelo menos **5 atributos para cada entidade** que você identificou.

**c)** Explique por que os atributos escolhidos são importantes para o sistema.

**d)** Identifique os relacionamentos existentes entre as entidades.

**e)** Qual é a cardinalidade entre `USUARIO` e `EMPRESTIMO`? Justifique.

**f)** Explique por que `EMPRESTIMO` pode ser considerado importante na representação dessa realidade.

**g)** Faça uma representação simples do modelo conceitual utilizando entidades e relacionamentos.

---

# ATIVIDADE 02 — SISTEMA DE VENDAS

Uma loja deseja desenvolver um sistema para controlar seus clientes, produtos e pedidos.

Um cliente pode realizar vários pedidos. Cada pedido possui uma data e está associado a um cliente.

Um pedido pode conter vários produtos. Um produto pode aparecer em diferentes pedidos.

### Responda:

**a)** Identifique as principais entidades do cenário.

**b)** Desenvolva pelo menos **5 atributos para `CLIENTE`**.

**c)** Desenvolva pelo menos **5 atributos para `PRODUTO`**.

**d)** Desenvolva pelo menos **4 atributos para `PEDIDO`**.

**e)** Explique quais relacionamentos existem entre essas entidades.

**f)** Identifique a cardinalidade entre `CLIENTE` e `PEDIDO`.

**g)** Identifique a cardinalidade entre `PEDIDO` e `PRODUTO`.

**h)** Explique com suas palavras por que o relacionamento entre `PEDIDO` e `PRODUTO` é do tipo N:N.

**i)** Proponha uma entidade associativa para representar o relacionamento entre pedido e produto.

**j)** Desenvolva pelo menos **3 atributos para essa entidade associativa** e explique a finalidade de cada um.

---

# ATIVIDADE 03 — SISTEMA ACADÊMICO

Uma instituição de ensino deseja desenvolver um sistema para controlar seus alunos, professores, cursos e disciplinas.

Cada aluno possui informações pessoais e está vinculado a um curso.

Os professores ministram disciplinas.

Um aluno pode cursar várias disciplinas e uma disciplina pode ser cursada por vários alunos.

### Responda:

**a)** Identifique pelo menos quatro entidades presentes no cenário.

**b)** Desenvolva atributos para cada entidade identificada.

Utilize pelo menos:

* 5 atributos para `ALUNO`;
* 4 atributos para `PROFESSOR`;
* 4 atributos para `CURSO`;
* 4 atributos para `DISCIPLINA`.

**c)** Explique quais atributos representam características próprias de cada entidade.

**d)** Identifique os principais relacionamentos.

**e)** Qual é a cardinalidade entre `ALUNO` e `CURSO` considerando o cenário apresentado? Justifique sua resposta.

**f)** Qual é a cardinalidade entre `ALUNO` e `DISCIPLINA`?

**g)** Explique por que essa relação pode exigir uma entidade associativa.

**h)** Proponha um nome para essa entidade associativa.

**i)** Desenvolva pelo menos 4 atributos para a entidade associativa.

**j)** Explique o que aconteceria com a modelagem se o relacionamento entre aluno e disciplina fosse simplesmente ignorado.

---

# ATIVIDADE 04 — SISTEMA DE CLÍNICA

Uma clínica médica deseja desenvolver um sistema para controlar pacientes, médicos e consultas.

Um paciente pode realizar várias consultas.

Um médico pode realizar consultas com vários pacientes.

Cada consulta deve registrar informações sobre o atendimento realizado.

### Responda:

**a)** Quais são as principais entidades desse sistema?

**b)** Desenvolva pelo menos **6 atributos para `PACIENTE`**.

**c)** Desenvolva pelo menos **6 atributos para `MEDICO`**.

**d)** Desenvolva pelo menos **6 atributos para `CONSULTA`**.

**e)** Explique por que `CONSULTA` não deve ser tratada apenas como um atributo de `PACIENTE`.

**f)** Identifique os relacionamentos existentes.

**g)** Determine a cardinalidade entre `PACIENTE` e `CONSULTA`.

**h)** Determine a cardinalidade entre `MEDICO` e `CONSULTA`.

**i)** Explique como a entidade `CONSULTA` ajuda a representar corretamente a realidade da clínica.

**j)** Crie uma representação conceitual simplificada do cenário.

---

# ATIVIDADE 05 — SISTEMA DE RESTAURANTE

Um restaurante deseja criar um sistema para controlar seus clientes, mesas, funcionários, pedidos e produtos vendidos.

Um cliente pode realizar pedidos.

Um pedido pode conter vários produtos.

Cada pedido deve registrar a data e o horário em que foi realizado.

Os funcionários são responsáveis pelo atendimento dos pedidos.

### Responda:

**a)** Identifique as entidades presentes no cenário.

**b)** Desenvolva pelo menos **5 atributos para cada entidade**.

**c)** Explique a diferença entre uma entidade e um atributo utilizando dois exemplos retirados do cenário.

**d)** Identifique os relacionamentos entre as entidades.

**e)** Determine as cardinalidades dos relacionamentos identificados.

**f)** Existe algum relacionamento N:N nesse cenário? Explique.

**g)** Caso exista, proponha uma entidade associativa.

**h)** Desenvolva atributos para essa entidade associativa.

**i)** Escolha três relacionamentos identificados e explique por que eles são importantes para representar a realidade do restaurante.

---

# ATIVIDADE 06 — IDENTIFICANDO ENTIDADES E ATRIBUTOS

Leia o texto:

> Uma empresa possui diversos funcionários. Cada funcionário possui nome, CPF, telefone, e-mail e data de nascimento. Os funcionários trabalham em departamentos. Cada departamento possui um nome, um código e uma localização. A empresa também possui projetos. Um funcionário pode participar de vários projetos e um projeto pode possuir vários funcionários.

### Responda:

**a)** Identifique todas as entidades que você considera necessárias.

**b)** Desenvolva pelo menos 5 atributos para cada entidade.

**c)** Explique por que cada elemento escolhido é uma entidade e não apenas um atributo.

**d)** Identifique os relacionamentos.

**e)** Determine as cardinalidades.

**f)** Existe algum relacionamento N:N? Explique.

**g)** Caso exista, proponha uma entidade associativa.

**h)** Desenvolva atributos para a entidade associativa.

---

# ATIVIDADE 07 — O QUE ESTÁ ERRADO NA MODELAGEM?

Um aluno apresentou a seguinte proposta para um sistema de vendas:

```text
CLIENTE
- nome
- cpf
- telefone
- produto
- preço
- pedido
- data
```

O aluno afirmou:

> "Não precisamos criar outras entidades porque todas as informações podem ficar dentro de CLIENTE."

### Responda:

**a)** Você concorda com essa modelagem? Justifique.

**b)** Quais elementos apresentados poderiam representar entidades?

**c)** Quais elementos poderiam representar atributos?

**d)** Que informações estão sendo misturadas nessa proposta?

**e)** Proponha uma nova organização para esse modelo.

**f)** Desenvolva atributos para cada entidade que você propôs.

**g)** Explique quais relacionamentos deveriam existir.

**h)** Explique por que uma modelagem inadequada pode causar problemas no desenvolvimento e na manutenção do sistema.

---

# ATIVIDADE 08 — DO TEXTO PARA O MODELO

Leia o cenário:

> Uma escola deseja criar um sistema para controlar suas turmas. Cada turma pertence a um curso. Um curso possui várias disciplinas. Professores podem ministrar disciplinas. Alunos são matriculados em turmas. Uma turma possui vários alunos.

### Desenvolva a modelagem conceitual.

Sua resposta deverá apresentar:

**a)** As entidades identificadas.

**b)** Pelo menos 4 atributos para cada entidade.

**c)** Os relacionamentos.

**d)** As cardinalidades.

**e)** As possíveis entidades associativas.

**f)** Uma explicação das principais decisões tomadas durante a modelagem.

**g)** Uma representação gráfica ou textual do modelo.

---

# ATIVIDADE 09 — CRIE OS ATRIBUTOS

Para cada entidade abaixo, desenvolva **pelo menos 6 atributos** que você considera adequados para um sistema de informação.

Depois, explique a finalidade de **três atributos escolhidos em cada entidade**.

### Entidade 1

```text
CLIENTE
```

### Entidade 2

```text
PRODUTO
```

### Entidade 3

```text
FUNCIONARIO
```

### Entidade 4

```text
ALUNO
```

### Entidade 5

```text
VEICULO
```

### Entidade 6

```text
LIVRO
```

### Atenção

Não basta criar atributos aleatórios.

Os atributos devem fazer sentido para a entidade.

Por exemplo, ao criar atributos para `PRODUTO`, pense:

* Que informações identificam o produto?
* Que informações descrevem o produto?
* Que informações são importantes para o sistema?

---

# ATIVIDADE 10 — ENTIDADE OU ATRIBUTO?

Analise os elementos abaixo considerando um sistema de vendas:

```text
Cliente
Nome
CPF
Endereço
Pedido
Data do pedido
Produto
Preço
Quantidade
Categoria
```

### Responda:

**a)** Quais elementos você classificaria como entidades?

**b)** Quais elementos você classificaria como atributos?

**c)** Escolha dois elementos cuja classificação possa gerar dúvida e explique sua decisão.

**d)** Explique por que a classificação correta entre entidade e atributo é importante para a modelagem.

**e)** Para cada entidade identificada, desenvolva pelo menos 4 atributos adicionais.

---

# ATIVIDADE 11 — MODELANDO UMA REALIDADE

Você foi contratado para modelar um sistema de uma **academia**.

A academia precisa controlar:

* alunos;
* professores;
* planos;
* modalidades;
* pagamentos;
* aulas.

Um aluno pode contratar um plano.

Um plano pode ser contratado por vários alunos.

Um professor pode ministrar várias aulas.

Uma modalidade pode possuir várias aulas.

### Sua tarefa

Desenvolva uma proposta de modelagem conceitual.

Sua resposta deve conter:

**a)** Entidades.

**b)** Atributos de cada entidade.

**c)** Relacionamentos.

**d)** Cardinalidades.

**e)** Entidades associativas, caso sejam necessárias.

**f)** Regras de negócio identificadas.

**g)** Justificativa das principais decisões da modelagem.

---

# ATIVIDADE 12 — DESAFIO DE MODELAGEM

Uma empresa deseja desenvolver um sistema de comércio eletrônico.

O sistema deverá permitir:

* cadastro de clientes;
* cadastro de produtos;
* cadastro de categorias;
* realização de pedidos;
* acompanhamento dos pedidos;
* registro dos produtos presentes em cada pedido.

Considere que:

* um cliente pode realizar vários pedidos;
* um pedido pertence a um cliente;
* um pedido possui vários produtos;
* um produto pode aparecer em vários pedidos;
* um produto pertence a uma categoria;
* uma categoria pode possuir vários produtos.

### Desenvolva o modelo conceitual.

Sua resposta deve apresentar:

1. Todas as entidades identificadas.
2. Pelo menos 5 atributos para cada entidade.
3. Os relacionamentos.
4. As cardinalidades.
5. As entidades associativas necessárias.
6. Os atributos das entidades associativas.
7. As principais regras de negócio.
8. Uma representação gráfica ou textual do modelo.
9. Uma justificativa para as principais decisões tomadas.

---

# ATIVIDADE 13 — REFLEXÃO SOBRE MODELAGEM

Responda de forma discursiva:

### a)

Por que a modelagem de dados deve ser realizada antes da implementação do Banco de Dados?

### b)

Qual é a diferença entre modelagem conceitual, lógica e física?

### c)

Explique com suas palavras a diferença entre:

```text
ENTIDADE
ATRIBUTO
RELACIONAMENTO
CARDINALIDADE
```

### d)

Por que não devemos escolher atributos simplesmente porque eles "parecem interessantes"?

### e)

Como as regras de negócio influenciam a criação dos relacionamentos?

### f)

Explique como uma modelagem inadequada pode prejudicar um sistema no futuro.

---

# ATIVIDADE 14 — SITUAÇÃO-PROBLEMA

Leia:

> Uma universidade deseja criar um sistema para controlar seus cursos. Cada curso possui disciplinas. Os alunos pertencem a um curso e podem cursar várias disciplinas. Professores ministram disciplinas. A universidade precisa saber quais alunos estão cursando cada disciplina e quais professores são responsáveis por cada disciplina.

### Desenvolva uma proposta completa de modelagem.

Você deverá:

* identificar as entidades;
* desenvolver os atributos;
* identificar os relacionamentos;
* definir as cardinalidades;
* identificar possíveis entidades associativas;
* desenvolver atributos para as entidades associativas;
* representar o modelo;
* explicar suas decisões.

### Pergunta principal

> Como você transformaria essa realidade em uma estrutura organizada de dados?

---

# ATIVIDADE 15 — PRODUÇÃO INDIVIDUAL

Escolha **um dos seguintes sistemas**:

* Sistema de escola
* Sistema de biblioteca
* Sistema de hospital
* Sistema de loja
* Sistema de restaurante
* Sistema de academia
* Sistema de transporte
* Sistema de hotel

Depois, desenvolva uma proposta de modelagem conceitual.

Sua atividade deve conter:

## 1. Descrição da realidade

Explique brevemente como funciona o sistema escolhido.

## 2. Entidades

Identifique pelo menos **5 entidades**.

## 3. Atributos

Desenvolva pelo menos **5 atributos para cada entidade**.

## 4. Relacionamentos

Explique como as entidades se relacionam.

## 5. Cardinalidades

Defina as cardinalidades dos relacionamentos.

## 6. Regras de negócio

Identifique pelo menos **3 regras de negócio** presentes no sistema.

## 7. Entidades associativas

Verifique se existe algum relacionamento N:N.

Caso exista, proponha uma entidade associativa e seus atributos.

## 8. Modelo

Apresente uma representação gráfica ou textual do modelo.

## 9. Justificativa

Explique as principais decisões tomadas durante a modelagem.

---

# CRITÉRIOS DE AVALIAÇÃO

As atividades podem ser avaliadas considerando os seguintes critérios:

| Critério                   | O que será observado                                            |
| -------------------------- | --------------------------------------------------------------- |
| Identificação de entidades | Capacidade de reconhecer elementos relevantes da realidade      |
| Definição de atributos     | Capacidade de escolher informações adequadas para cada entidade |
| Relacionamentos            | Capacidade de identificar associações entre entidades           |
| Cardinalidade              | Compreensão das relações 1:1, 1:N e N:N                         |
| Regras de negócio          | Capacidade de interpretar as regras apresentadas no cenário     |
| Entidades associativas     | Capacidade de tratar relacionamentos N:N                        |
| Justificativa              | Capacidade de explicar as decisões tomadas                      |
| Representação              | Capacidade de organizar e representar o modelo                  |
| Coerência                  | Modelo consistente com a realidade apresentada                  |

---

# ORIENTAÇÃO FINAL AO ALUNO

Nas atividades de modelagem, não existe apenas uma forma possível de representar uma realidade.

O mais importante é que sua proposta seja:

* coerente com o cenário;
* organizada;
* justificável;
* consistente com as regras apresentadas;
* capaz de representar adequadamente os dados necessários ao sistema.

**Não escolha atributos aleatoriamente.**

Antes de criar um atributo, pergunte:

> **"Essa informação é realmente necessária para descrever ou controlar essa entidade dentro do sistema?"**

Antes de criar um relacionamento, pergunte:

> **"Como esses elementos se relacionam na realidade?"**

E antes de definir uma cardinalidade, pergunte:

> **"Quantas ocorrências de uma entidade podem estar relacionadas a uma ocorrência da outra?"**
