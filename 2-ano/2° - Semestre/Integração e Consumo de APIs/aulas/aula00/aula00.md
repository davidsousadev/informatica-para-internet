# Aula 00 — Introdução às APIs

**Curso:** Técnico em Informática para Internet
**Capítulo:** 1 — Introdução a APIs
**Duração:** 50 minutos
**Aula:** 00 — Primeiros conceitos sobre APIs

---

## 1. Objetivos da aula

Ao final desta aula, o aluno deverá ser capaz de:

* Entender o que é uma API;
* Identificar a função de uma API na comunicação entre sistemas;
* Compreender o conceito de **cliente** e **servidor**;
* Reconhecer exemplos de APIs presentes no cotidiano;
* Diferenciar APIs privadas e públicas;
* Relacionar APIs com:

  * Redes de Computadores;
  * Segurança da Informação;
  * Sistemas Distribuídos;
* Perceber a importância das APIs no desenvolvimento de aplicações web.

---

# 2. Roteiro da aula — 50 minutos

| Tempo     | Etapa         | Atividade                                        |
| --------- | ------------- | ------------------------------------------------ |
| 0–5 min   | Abertura      | Pergunta-problema e contextualização             |
| 5–15 min  | Conceito      | O que é uma API?                                 |
| 15–25 min | Como funciona | Cliente, servidor, requisição e resposta         |
| 25–32 min | Evolução      | APIs privadas e públicas                         |
| 32–40 min | Exemplos      | Clima, mapas, login e pagamentos                 |
| 40–46 min | Relações      | APIs + redes + segurança + sistemas distribuídos |
| 46–50 min | Revisão       | Quiz rápido e fechamento                         |

---

# 3. Abertura — 0 a 5 minutos

## Pergunta para iniciar

> **Como um site consegue descobrir a previsão do tempo, mostrar um mapa ou permitir login com uma conta do Google sem possuir todos esses dados dentro dele?**

Deixe os alunos levantarem hipóteses.

Possíveis respostas:

* "Ele acessa outro site."
* "Ele busca na internet."
* "Existe um banco de dados."
* "Usa algum serviço externo."

### Condução do professor

Explique:

> Muitas aplicações não precisam desenvolver tudo do zero. Elas podem utilizar funcionalidades e dados oferecidos por outros sistemas.

É nesse ponto que entram as **APIs**.

---

# 4. O que é uma API? — 5 a 15 minutos

## API significa:

**Application Programming Interface**

Em português:

**Interface de Programação de Aplicações**

De forma simples:

> **Uma API é uma forma padronizada para que um sistema possa conversar com outro sistema.**

Uma API funciona como uma **ponte de comunicação** entre aplicações.

### Exemplo simples

Imagine um restaurante.

Você:

* escolhe o prato;
* faz o pedido;
* recebe o pedido.

Você não precisa entrar na cozinha e preparar a comida.

Existe uma interface entre você e a cozinha:

```text
CLIENTE
   ↓
PEDIDO
   ↓
ATENDENTE
   ↓
COZINHA
   ↓
PEDIDO PRONTO
   ↓
CLIENTE
```

Em uma aplicação:

```text
APLICAÇÃO
    ↓
   API
    ↓
OUTRO SISTEMA
    ↓
   DADOS
    ↓
   API
    ↓
APLICAÇÃO
```

A API é responsável por estabelecer **como essa comunicação deve acontecer**.

---

# 5. API não é apenas "um programa"

Uma API não deve ser entendida simplesmente como um aplicativo.

Ela define **regras de comunicação**.

Por exemplo:

* Qual endereço deve ser utilizado?
* Qual informação deve ser enviada?
* Qual método deve ser utilizado?
* Qual formato os dados devem possuir?
* Qual resposta será devolvida?
* O usuário precisa estar autenticado?

Podemos imaginar:

```text
CLIENTE

"Quero saber a temperatura de Timon."

        ↓

       API

        ↓

SERVIDOR DE CLIMA

        ↓

       API

        ↓

"Temperatura: 31 °C"
```

---

# 6. Cliente e servidor

Para compreender APIs, precisamos conhecer dois conceitos importantes.

## Cliente

É quem **faz uma solicitação**.

Pode ser:

* um navegador;
* um aplicativo de celular;
* um site;
* um sistema empresarial;
* outro servidor.

## Servidor

É quem **recebe a solicitação e fornece uma resposta**.

Exemplo:

```text
NAVEGADOR
   |
   | requisição
   ↓
SERVIDOR
   |
   | resposta
   ↓
NAVEGADOR
```

Uma API normalmente participa dessa comunicação.

---

# 7. O ciclo básico de uma API

Podemos representar uma comunicação assim:

```text
┌──────────────┐
│    CLIENTE   │
│ Site / App   │
└──────┬───────┘
       │
       │ 1. Requisição
       ↓
┌──────────────┐
│     API      │
└──────┬───────┘
       │
       │ 2. Processamento
       ↓
┌──────────────┐
│   SERVIDOR   │
│ Banco / Dados│
└──────┬───────┘
       │
       │ 3. Resultado
       ↓
┌──────────────┐
│     API      │
└──────┬───────┘
       │
       │ 4. Resposta
       ↓
┌──────────────┐
│    CLIENTE   │
└──────────────┘
```

### Resumindo

```text
REQUISIÇÃO → API → SERVIDOR → API → RESPOSTA
```

---

# 8. APIs e Internet

Grande parte das APIs utilizadas na Internet utiliza o protocolo:

**HTTP — Hypertext Transfer Protocol**

O HTTP permite a comunicação entre clientes e servidores.

Por exemplo:

```text
Cliente
   ↓
HTTP Request
   ↓
API
   ↓
Servidor
   ↓
HTTP Response
   ↓
Cliente
```

Isso conecta o estudo de APIs diretamente com a disciplina de:

## Redes de Computadores

Para uma API funcionar pela Internet, precisamos de comunicação entre máquinas.

Por isso, conhecimentos de:

* IP;
* portas;
* DNS;
* HTTP;
* HTTPS;
* cliente/servidor;

serão importantes durante o estudo de APIs.

---

# 9. Um exemplo do mundo real

Imagine um site de comércio eletrônico.

O site precisa realizar um pagamento.

O desenvolvedor poderia criar todo um sistema financeiro do zero.

Mas existe outra possibilidade:

```text
┌──────────────────┐
│    E-commerce    │
└────────┬─────────┘
         │
         │ Solicita pagamento
         ↓
┌──────────────────┐
│ API de Pagamento │
└────────┬─────────┘
         │
         ↓
┌──────────────────┐
│Sistema Financeiro│
└────────┬─────────┘
         │
         ↓
     Pagamento
     aprovado
         │
         ↓
┌──────────────────┐
│ E-commerce       │
└──────────────────┘
```

A API permite que o e-commerce utilize um serviço especializado.

---

# 10. Evolução das APIs — 25 a 32 minutos

As APIs evoluíram junto com os sistemas de software.

## APIs privadas

São utilizadas dentro de uma empresa ou organização.

Exemplo:

Uma empresa possui:

```text
Sistema de Vendas
       ↓
       API
       ↓
Sistema de Estoque
```

Quando uma venda acontece, o sistema pode utilizar uma API para informar ao sistema de estoque:

> "O produto X foi vendido."

O estoque então pode atualizar a quantidade disponível.

### Exemplo

```text
Produto: Notebook
Quantidade antes: 10

Venda realizada

Quantidade depois: 9
```

---

# 11. APIs públicas

São APIs disponibilizadas para que desenvolvedores externos possam utilizar determinados serviços.

Exemplos de funcionalidades que podem ser oferecidas:

* mapas;
* localização;
* previsão do tempo;
* pagamentos;
* autenticação;
* redes sociais;
* tradução;
* envio de mensagens.

A ideia é permitir que outros sistemas aproveitem funcionalidades existentes.

---

# 12. Exemplo: login com Google

Imagine que um site ofereça:

```text

┌─────────────────────────────┐
│      ENTRAR NO SISTEMA      │
│                             │
│  [ E-mail ]                 │
│  [ Senha  ]                 │
│                             │
│  [ Entrar com Google ]      │
└─────────────────────────────┘

```

Ao clicar em:

**"Entrar com Google"**

o site pode utilizar serviços de autenticação disponibilizados pelo Google.

O fluxo pode ser representado de forma simplificada:

```text
Usuário
   ↓
Site
   ↓
API/Serviço de autenticação
   ↓
Google
   ↓
Autenticação
   ↓
Site
   ↓
Usuário conectado
```

O site não precisa necessariamente criar sozinho todo o sistema de autenticação.

---

# 13. Exemplos práticos de APIs

## 13.1 API de clima

Uma aplicação pode consultar uma API de clima para obter:

* temperatura;
* umidade;
* previsão;
* velocidade do vento;
* condições climáticas.

Exemplo conceitual:

```text
Aplicação
   ↓
"Qual o clima em Timon?"
   ↓
API de clima
   ↓
Servidor
   ↓
Dados meteorológicos
   ↓
Aplicação
```

---

## 13.2 API de mapas

Uma aplicação pode utilizar uma API de mapas para disponibilizar:

* mapas;
* localização;
* rotas;
* endereços;
* pontos de interesse;
* informações de trânsito.

Por exemplo, um aplicativo de entrega pode utilizar serviços de mapas para ajudar a determinar uma rota.

```text
Aplicativo de entrega
        ↓
       API
        ↓
Serviço de mapas
        ↓
   Rota calculada
        ↓
Aplicativo
```

---

## 13.3 API de pagamentos

Uma loja virtual pode utilizar uma API para conversar com um serviço de pagamento.

```text
Cliente
   ↓
Loja virtual
   ↓
API de pagamento
   ↓
Serviço financeiro
   ↓
Resultado
   ↓
Loja virtual
```

O resultado poderia ser:

```text
Pagamento aprovado
```

ou:

```text
Pagamento recusado
```

---

# 14. APIs e Segurança da Informação — 32 a 40 minutos

APIs frequentemente trabalham com informações importantes.

Exemplos:

* dados pessoais;
* dados de clientes;
* informações de pedidos;
* informações financeiras;
* credenciais;
* informações de localização.

Por isso, **segurança é fundamental**.

---

## Autenticação

A autenticação responde:

> **"Quem é você?"**

Exemplo:

```text
Usuário
   ↓
Login
   ↓
Senha / Token
   ↓
Servidor
   ↓
Usuário identificado
```

---

## Autorização

A autorização responde:

> **"O que você pode fazer?"**

Por exemplo:

Um usuário comum pode:

```text
✓ Visualizar seus pedidos
✓ Alterar seus dados
```

Mas talvez não possa:

```text
✗ Excluir outros usuários
✗ Alterar preços
✗ Acessar dados administrativos
```

---

# 15. APIs e Sistemas Distribuídos

Imagine uma aplicação grande dividida em vários serviços:

```text
             SISTEMA
                │
     ┌──────────┼──────────┐
     ↓          ↓          ↓
 Usuários    Pedidos    Estoque
     │          │          │
     └────── API ──────────┘
```

Cada serviço pode possuir uma responsabilidade específica.

Esse tipo de arquitetura aparece em:

* sistemas distribuídos;
* arquiteturas orientadas a serviços;
* microsserviços.

As APIs permitem que esses diferentes componentes se comuniquem.

---

# 16. APIs conectam várias áreas

As APIs não são um assunto isolado.

Elas conectam diferentes áreas da Tecnologia da Informação.

```text
                 APIs
                  │
      ┌───────────┼───────────┐
      ↓           ↓           ↓
   REDES       SEGURANÇA   SISTEMAS
      │           │        DISTRIBUÍDOS
      │           │           │
     HTTP      OAuth/Tokens  Serviços
      │           │           │
      └───────────┼───────────┘
                  ↓
            APLICAÇÕES WEB
```

Por isso, aprender APIs ajuda o aluno a compreender melhor o funcionamento de aplicações modernas.

---

# 17. Atividade rápida — 40 a 46 minutos

## Desafio: "Onde existe uma API?"

Apresente as situações abaixo aos alunos.

### Situação 1

Um aplicativo mostra a previsão do tempo.

**Pergunta:**

De onde provavelmente vêm os dados?

---

### Situação 2

Um aplicativo de entrega mostra um mapa e calcula uma rota.

**Pergunta:**

O aplicativo precisou criar todo o sistema de mapas do zero?

---

### Situação 3

Uma loja virtual oferece:

> "Pagar com cartão"

**Pergunta:**

Como o site pode conversar com um serviço de pagamento?

---

### Situação 4

Um site permite:

> "Entrar com Google"

**Pergunta:**

Como o site consegue utilizar a autenticação de outra plataforma?

---

## Resposta esperada

Em todos os casos, uma possibilidade é a utilização de uma **API**.

---

# 18. Quiz final — 46 a 50 minutos

### 1. O que é uma API?

**A)** Um banco de dados.
**B)** Uma interface que permite a comunicação entre aplicações.
**C)** Um sistema operacional.
**D)** Um computador.

**Resposta:** B

---

### 2. Qual protocolo é muito utilizado pelas APIs na Internet?

**A)** HTTP
**B)** HDMI
**C)** USB
**D)** SATA

**Resposta:** A

---

### 3. O que é uma API privada?

**A)** Uma API utilizada internamente por uma organização.
**B)** Uma API que não possui servidor.
**C)** Uma API exclusiva para celulares.
**D)** Uma API sem segurança.

**Resposta:** A

---

### 4. Qual situação pode utilizar uma API?

**A)** Consulta de previsão do tempo.
**B)** Integração com mapas.
**C)** Processamento de pagamentos.
**D)** Todas as alternativas.

**Resposta:** D

---

### 5. Por que segurança é importante em APIs?

**A)** Porque APIs podem trabalhar com informações sensíveis.
**B)** Porque APIs não utilizam redes.
**C)** Porque APIs substituem o sistema operacional.
**D)** Porque APIs funcionam apenas offline.

**Resposta:** A

---

# 19. Fechamento da aula

## A ideia principal

> **Uma API permite que diferentes sistemas possam se comunicar seguindo regras previamente definidas.**

Podemos resumir:

```text
API = comunicação entre sistemas
```

E uma comunicação típica pode ser representada como:

```text
CLIENTE
   ↓
REQUISIÇÃO
   ↓
API
   ↓
SERVIDOR
   ↓
PROCESSAMENTO
   ↓
RESPOSTA
   ↓
CLIENTE
```

---

# 20. O que veremos nas próximas aulas?

Nas próximas aulas, vamos sair do conceito e começar a **utilizar APIs na prática**.

Vamos estudar conceitos como:

* HTTP;
* requisições e respostas;
* métodos HTTP;
* GET;
* POST;
* PUT;
* PATCH;
* DELETE;
* códigos de status;
* JSON;
* endpoints;
* parâmetros;
* autenticação;
* testes de APIs;
* ferramentas como Postman/Insomnia;
* consumo de APIs com JavaScript.

---

# 21. Frase para levar da aula

> **"Uma API é uma ponte que permite que sistemas diferentes conversem entre si."**

Essa ideia será a base para todo o nosso estudo de APIs.
