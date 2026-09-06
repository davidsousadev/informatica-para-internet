# AULA 00 — PROCESSO FUNDAMENTAL DE TESTE DE SOFTWARE

**Curso:** Técnico em Informática para Internet
**Aula:** 00 — Introdução ao Processo Fundamental de Teste
**Duração:** 50 minutos
**Público:** Alunos do Curso Técnico em Informática para Internet
**Tema:** Processo Fundamental de Teste

---

## 1. OBJETIVOS DA AULA

Ao final desta aula, o aluno deverá ser capaz de:

* Compreender por que testes são importantes no desenvolvimento de software.
* Diferenciar **verificação** e **validação**.
* Reconhecer as principais etapas do processo fundamental de teste.
* Entender que teste não significa apenas "procurar erros".
* Perceber a relação entre testes, qualidade, segurança e confiança do usuário.
* Identificar situações do cotidiano em que um software deveria ser testado.

---

# 2. ABERTURA DA AULA — 0 A 5 MIN

## Pergunta inicial

Imagine que você acabou de desenvolver um site para uma escola.

O sistema possui:

* Cadastro de alunos;
* Login;
* Formulário de matrícula;
* Upload de documentos;
* Consulta de notas.

Antes de colocar esse sistema no ar, você faria o quê?

### Pergunte aos alunos:

> "Vocês colocariam o sistema diretamente nas mãos dos usuários sem testar?"

Depois pergunte:

> "O que poderia dar errado?"

Possíveis respostas:

* O login pode não funcionar.
* O formulário pode não enviar.
* O sistema pode aceitar dados inválidos.
* O usuário pode perder informações.
* Uma senha pode aparecer na tela.
* O sistema pode funcionar no computador, mas apresentar problemas no celular.
* Um botão pode não funcionar.
* O sistema pode ficar lento com muitos usuários.
* Um cadastro pode ser duplicado.
* O sistema pode permitir acesso indevido.

### Conexão com a aula

Explique:

> Testar software não é simplesmente procurar erros depois que o sistema está pronto.

O teste faz parte de um **processo organizado**, que ajuda a aumentar a qualidade, reduzir riscos e verificar se o software realmente atende às necessidades de quem vai utilizá-lo.

---

# 3. O QUE É TESTAR SOFTWARE? — 5 A 12 MIN

## Conceito fundamental

Teste de software é uma atividade **sistemática** utilizada para avaliar um software, identificar defeitos, reduzir riscos e aumentar a confiança de que o sistema atende aos requisitos e às necessidades dos usuários.

### Uma ideia importante:

> **Teste não é apenas encontrar bugs.**

Quando testamos um sistema, queremos descobrir, por exemplo:

* O sistema funciona?
* Ele faz aquilo que foi solicitado?
* Ele funciona em diferentes situações?
* Ele é seguro?
* É fácil de utilizar?
* Os dados são tratados corretamente?
* Ele continua funcionando quando aumenta a quantidade de usuários?
* O comportamento apresentado é o esperado?

---

## Exemplo simples

Imagine um formulário de cadastro:

```text
Nome: João
E-mail: joao@email.com
Senha: 123456

[ Cadastrar ]
```

Um teste básico poderia verificar:

### Entrada válida

```text
Nome: João
E-mail: joao@email.com
Senha: 123456
```

**Resultado esperado:**

```text
Cadastro realizado com sucesso.
```

Mas e se o usuário deixar o nome vazio?

```text
Nome:
E-mail: joao@email.com
Senha: 123456
```

**Resultado esperado:**

```text
O campo nome é obrigatório.
```

E se o usuário digitar um e-mail inválido?

```text
Nome: João
E-mail: joao
Senha: 123456
```

**Resultado esperado:**

```text
Informe um e-mail válido.
```

Perceba que testar significa verificar o comportamento do sistema em diferentes situações.

---

# 4. POR QUE TESTAR? — 12 A 17 MIN

Pergunte aos alunos:

> "Qual é o custo de um erro em um software?"

Dê exemplos:

### Aplicativo bancário

Um erro pode:

* Processar um pagamento incorretamente;
* Exibir um saldo errado;
* Permitir uma operação indevida;
* Causar perda financeira.

### Loja virtual

Um erro pode:

* Impedir uma compra;
* Calcular o frete errado;
* Aplicar um desconto incorreto;
* Registrar o pedido de forma errada.

### Sistema escolar

Um erro pode:

* Apagar informações;
* Registrar uma nota incorretamente;
* Impedir uma matrícula;
* Exibir informações para o usuário errado.

### Site

Um erro pode:

* Impedir o envio de um formulário;
* Quebrar uma página;
* Não funcionar no celular;
* Prejudicar a experiência do usuário.

---

## Conclusão

Quanto maior o impacto de um erro, maior é a necessidade de um processo de teste adequado.

> **Qualidade de software está diretamente relacionada à confiança do usuário.**

---

# 5. VERIFICAÇÃO X VALIDAÇÃO — 17 A 25 MIN

Este é um dos conceitos mais importantes da aula.

## VERIFICAÇÃO

A verificação responde:

> **"Estamos construindo o software da maneira correta?"**

Ela verifica se o desenvolvimento está seguindo:

* Requisitos;
* Especificações;
* Padrões;
* Documentação;
* Regras técnicas;
* Boas práticas.

### Exemplo

O requisito diz:

> "A senha deve possuir no mínimo 8 caracteres."

O sistema permite:

```text
Senha: 1234
```

Nesse caso, precisamos verificar se o software está sendo construído de acordo com o requisito.

---

## VALIDAÇÃO

A validação responde:

> **"Estamos construindo o software certo?"**

Aqui o foco está no:

* Usuário;
* Negócio;
* Contexto real;
* Uso do sistema;
* Necessidades do usuário;
* Experiência de utilização.

### Exemplo

Imagine que o sistema possui um botão:

```text
CONFIRMAR
```

Tecnicamente, o botão funciona.

Porém, os usuários não entendem o que ele faz.

Então podemos ter um problema de validação.

O sistema pode estar funcionando tecnicamente, mas não estar atendendo adequadamente ao usuário.

---

## RESUMO

| Conceito    | Pergunta principal                 | Foco                                         |
| ----------- | ---------------------------------- | -------------------------------------------- |
| Verificação | Estamos construindo corretamente?  | Requisitos, especificações e desenvolvimento |
| Validação   | Estamos construindo a coisa certa? | Usuário, necessidade e contexto real         |

### Frase para memorizar

> **Verificação = construir corretamente.**
> **Validação = construir o que realmente precisa ser construído.**

---

# 6. PROCESSO FUNDAMENTAL DE TESTE — 25 A 35 MIN

O teste não acontece de maneira improvisada.

Existe um processo organizado.

Podemos pensar nele como um ciclo:

```text
PLANEJAMENTO
      ↓
DESENHO DOS TESTES
      ↓
EXECUÇÃO
      ↓
MONITORAÇÃO E CONTROLE
      ↓
AVALIAÇÃO DOS RESULTADOS
      ↓
AJUSTES / NOVOS TESTES
      ↺
```

Agora vamos entender cada etapa.

---

## 6.1 PLANEJAMENTO

Antes de testar, precisamos decidir:

* O que será testado?
* Por que será testado?
* Quem realizará os testes?
* Quando os testes serão realizados?
* Quais recursos serão necessários?
* Quais são os riscos?
* Quais critérios serão utilizados?

### Exemplo

Uma equipe está desenvolvendo uma loja virtual.

No planejamento, pode decidir:

```text
Funcionalidade:
Login

Objetivo:
Verificar se os usuários conseguem acessar suas contas.

Riscos:
- Login permitir acesso indevido.
- Senha incorreta ser aceita.
- Usuário não conseguir recuperar a senha.
```

---

# 6.2 DESENHO DOS TESTES

Agora precisamos definir **como o teste será realizado**.

Criamos:

* Casos de teste;
* Cenários;
* Roteiros;
* Dados de entrada;
* Resultados esperados.

### Exemplo

```text
Caso de teste: Login com dados válidos

Entrada:
E-mail: aluno@email.com
Senha: 12345678

Ação:
Clicar no botão "Entrar".

Resultado esperado:
Usuário deve ser direcionado para a página inicial.
```

Outro caso:

```text
Caso de teste: Login com senha incorreta

Entrada:
E-mail: aluno@email.com
Senha: senhaerrada

Ação:
Clicar no botão "Entrar".

Resultado esperado:
O sistema deve informar que os dados são inválidos.
```

---

# 6.3 EXECUÇÃO DOS TESTES

Agora colocamos o teste em prática.

O testador pode:

* Executar testes manualmente;
* Utilizar ferramentas automatizadas;
* Registrar resultados;
* Comparar resultado obtido com resultado esperado;
* Registrar defeitos encontrados.

### Exemplo

Esperado:

```text
Senha incorreta.
```

Obtido:

```text
Erro 500 - Internal Server Error
```

Temos uma diferença entre o resultado esperado e o resultado obtido.

Esse comportamento deve ser analisado e registrado.

---

# 6.4 MONITORAÇÃO E CONTROLE

Os testes também precisam ser acompanhados.

Podemos observar:

* Quantos testes foram planejados;
* Quantos foram executados;
* Quantos passaram;
* Quantos falharam;
* Quantos defeitos foram encontrados;
* Qual a cobertura dos testes;
* Quais riscos continuam existentes;
* Se o cronograma está sendo cumprido.

### Exemplo

```text
Testes planejados: 100

Executados: 80

Aprovados: 65

Falharam: 15

Pendentes: 20
```

Essas informações ajudam a equipe a entender o estado atual da qualidade do sistema.

---

# 6.5 AVALIAÇÃO DOS RESULTADOS

Depois da execução, precisamos analisar os resultados.

Perguntas importantes:

* Os testes planejados foram realizados?
* Os critérios de aceitação foram atingidos?
* Existem defeitos críticos?
* É necessário corrigir o sistema?
* É necessário executar novos testes?
* O software pode avançar para a próxima etapa?
* O risco restante é aceitável?

### Importante

Um sistema não é considerado pronto simplesmente porque:

> "Não encontramos nenhum erro."

Pode ser que:

* Poucos testes tenham sido realizados;
* Os testes tenham sido mal planejados;
* Algumas funcionalidades não tenham sido testadas;
* Existam riscos ainda não avaliados.

---

# 7. ATIVIDADE RÁPIDA — 35 A 43 MIN

## Desafio: Testando um formulário

Imagine que a turma está testando um formulário de login:

```text
--------------------------------
             LOGIN
--------------------------------

E-mail: _______________________

Senha:  _______________________

[ ENTRAR ]

--------------------------------
```

Em grupos ou individualmente, os alunos devem pensar em **5 situações diferentes para testar esse login**.

### Exemplos

```text
1. E-mail e senha corretos.

2. E-mail correto e senha incorreta.

3. E-mail incorreto e senha correta.

4. Campos vazios.

5. E-mail em formato inválido.
```

Mas incentive os alunos a pensar além:

```text
6. Espaços antes ou depois do e-mail.

7. Senha muito longa.

8. Caracteres especiais.

9. Muitos caracteres no campo de e-mail.

10. Tentativa de login várias vezes.
```

---

## Pergunta para a turma

Para cada teste, pergunte:

> "Qual é o resultado esperado?"

Essa pergunta é fundamental.

Um teste não deve ser simplesmente:

> "Vou clicar e ver o que acontece."

Precisamos saber **o que deveria acontecer** antes de comparar com o resultado real.

---

# 8. DISCUSSÃO — 43 A 47 MIN

Apresente a seguinte situação:

> Um site de uma escola funciona perfeitamente no computador do desenvolvedor, mas os alunos reclamam que o formulário de matrícula não funciona corretamente no celular.

Pergunte:

### 1. O software foi testado?

Talvez sim.

### 2. Isso significa que o software está adequado?

Não necessariamente.

### 3. O que pode ter acontecido?

Possibilidades:

* O teste foi realizado apenas no computador.
* O celular não foi considerado no planejamento.
* O contexto real de uso não foi validado.
* O cenário dos usuários não foi considerado.

### Conclusão

Esse exemplo mostra por que testar envolve muito mais do que verificar se o código "funciona".

Precisamos considerar:

```text
Software
   +
Requisitos
   +
Ambiente
   +
Usuário
   +
Contexto real
   =
Qualidade
```

---

# 9. FECHAMENTO — 47 A 50 MIN

## Revisão rápida

Peça aos alunos para responderem oralmente:

### Pergunta 1

> O que é teste de software?

Resposta esperada:

> Uma atividade sistemática para avaliar o software, identificar defeitos, reduzir riscos e aumentar a confiança na qualidade do sistema.

### Pergunta 2

> Qual a diferença entre verificação e validação?

Resposta esperada:

```text
Verificação:
"Estamos construindo corretamente?"

Validação:
"Estamos construindo o software certo?"
```

### Pergunta 3

> Qual é a primeira etapa do processo fundamental de teste?

Resposta:

> Planejamento.

### Pergunta 4

> O que fazemos no desenho dos testes?

Resposta:

> Definimos casos de teste, cenários, entradas, ações e resultados esperados.

### Pergunta 5

> O teste termina quando encontramos um erro?

Resposta:

> Não. O processo é iterativo e os resultados podem gerar correções e novos testes.

---

# 10. MAPA MENTAL DA AULA

```text
                 TESTE DE SOFTWARE
                        │
        ┌───────────────┴────────────────┐
        │                                │
    QUALIDADE                           RISCO
        │                                │
        └───────────────┬────────────────┘
                        │
                PROCESSO DE TESTE
                        │
       ┌────────────────┼────────────────┐
       │                │                │
PLANEJAMENTO         DESENHO          EXECUÇÃO
       │                │                │
       └────────────────┼────────────────┘
                        │
               MONITORAÇÃO E CONTROLE
                        │
                        ↓
              AVALIAÇÃO DOS RESULTADOS
                        │
                        ↓
                 NOVOS TESTES
                        │
                        ↺

VERIFICAÇÃO → "Estamos construindo corretamente?"

VALIDAÇÃO   → "Estamos construindo o software certo?"
```

---

# 11. CONCEITO-CHAVE PARA LEVAR DA AULA

> **Testar software não é apenas procurar erros. É um processo sistemático para avaliar se o software está correto, atende aos requisitos, reduz riscos e realmente resolve o problema do usuário.**

---

# 12. CONEXÃO COM AS PRÓXIMAS AULAS

Nas próximas aulas, podemos aprofundar:

* Casos de teste;
* Cenários de teste;
* Técnicas de teste;
* Testes funcionais;
* Testes não funcionais;
* Testes manuais;
* Testes automatizados;
* Registro e classificação de defeitos;
* Critérios de entrada e saída;
* Testes de interface;
* Testes em aplicações web;
* Testes de usabilidade;
* Testes de desempenho;
* Testes de segurança;
* Ferramentas utilizadas no mercado.

---

# 13. ATIVIDADE PARA FINALIZAR

## "O que você testaria?"

Escolha uma aplicação que você utiliza frequentemente.

Pode ser:

* Um aplicativo bancário;
* Uma rede social;
* Um jogo;
* Uma loja virtual;
* Um sistema escolar;
* Um aplicativo de transporte;
* Um site.

Responda:

```text
1. Qual sistema você escolheu?

2. Qual funcionalidade você testaria?

3. Qual seria a entrada do teste?

4. Qual ação seria realizada?

5. Qual resultado você esperaria?

6. O que poderia dar errado?

7. Como você saberia que o teste passou?
```

### Exemplo

```text
Sistema:
Site de uma loja virtual.

Funcionalidade:
Adicionar produto ao carrinho.

Entrada:
Produto selecionado.

Ação:
Clicar em "Adicionar ao carrinho".

Resultado esperado:
O produto deve aparecer no carrinho.

Possível problema:
O produto não aparecer ou aparecer com quantidade incorreta.

Critério de aprovação:
O produto selecionado deve aparecer no carrinho com nome,
quantidade e preço corretos.
```

---

# RESUMO DA AULA

```text
TESTE DE SOFTWARE
        ↓
Não é apenas procurar bugs
        ↓
É uma atividade sistemática
        ↓
Ajuda a reduzir riscos
        ↓
Aumenta a confiança no software
        ↓
Precisa ser planejada
        ↓
Os testes precisam ser desenhados
        ↓
Os testes são executados
        ↓
Os resultados são monitorados
        ↓
Os resultados são avaliados
        ↓
O processo pode gerar novos testes
```

## FRASE FINAL

> **Um bom profissional de informática não pergunta apenas "o sistema funciona?". Ele também pergunta "funciona para quem, em quais condições, de acordo com quais requisitos e com quais riscos?"**
