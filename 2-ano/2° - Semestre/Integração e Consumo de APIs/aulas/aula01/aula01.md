# Aula 01 — Tipos e Arquitetura de APIs

**Curso:** Técnico em Informática para Internet
**Capítulo:** 1 — Introdução a APIs
**Aula:** 01 — Tipos e Arquitetura de APIs

---

# 1. Objetivos da aula

Ao final desta aula, o aluno deverá ser capaz de:

* Compreender que existem diferentes formas de construir APIs;
* Diferenciar REST, SOAP e GraphQL;
* Compreender as principais características do REST;
* Identificar os princípios fundamentais de uma API REST;
* Compreender o conceito de recurso;
* Compreender o conceito de endpoint;
* Relacionar endpoints aos recursos de uma API;
* Compreender a função dos métodos HTTP em APIs REST;
* Diferenciar JSON e XML como formatos de representação de dados;
* Compreender o conceito de API Gateway;
* Compreender a função do cache em APIs;
* Identificar os principais componentes da arquitetura de uma API;
* Escolher uma abordagem de API considerando as necessidades de um sistema.

---

# 2. Retomando a aula anterior

Na aula anterior, aprendemos que uma API permite que diferentes sistemas se comuniquem.

Vimos uma comunicação básica:

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

Também aprendemos que APIs podem ser utilizadas para:

* previsão do tempo;
* mapas;
* pagamentos;
* autenticação;
* sistemas empresariais;
* comunicação entre serviços.

Agora surge uma nova pergunta:

> **Todas as APIs funcionam da mesma maneira?**

A resposta é:

**Não.**

Existem diferentes formas de projetar e implementar APIs.

Nesta aula estudaremos três abordagens muito importantes:

```text
APIs
 │
 ├── REST
 │
 ├── SOAP
 │
 └── GraphQL
```

Além disso, vamos compreender os principais componentes que formam a arquitetura de uma API.

---

# 3. API não é uma única tecnologia

É importante entender que **API é um conceito geral**.

Uma API define uma forma de comunicação entre sistemas.

Porém, essa comunicação pode ser implementada utilizando diferentes tecnologias e estilos arquiteturais.

Por exemplo:

```text
             API
              │
      ┌───────┼────────┐
      ↓       ↓        ↓
     REST    SOAP    GraphQL
```

Essas abordagens possuem características diferentes.

Por isso, quando um desenvolvedor começa um projeto, pode surgir uma pergunta:

> **Qual abordagem de API é mais adequada para esse sistema?**

Para responder, precisamos conhecer as características de cada uma.

---

# 4. REST

## REST significa:

**Representational State Transfer**

Em português:

**Transferência de Estado Representacional**

REST é um **estilo arquitetural** utilizado para construir serviços e APIs, especialmente na Web.

Ele utiliza conceitos e padrões da própria Web, principalmente o protocolo HTTP.

É uma das abordagens mais utilizadas para APIs Web.

---

# 5. A ideia principal do REST

No REST, pensamos principalmente em **recursos**.

Um recurso representa alguma informação ou objeto importante para o sistema.

Exemplos:

```text
USUÁRIOS
PRODUTOS
PEDIDOS
CLIENTES
CURSOS
ALUNOS
LIVROS
```

Podemos imaginar:

```text
API
 │
 ├── Usuários
 ├── Produtos
 ├── Pedidos
 ├── Clientes
 └── Cursos
```

Cada recurso pode ser acessado por uma URL.

Por exemplo:

```text
/produtos
```

representa o recurso de produtos.

E:

```text
/clientes
```

representa o recurso de clientes.

---

# 6. O que é um recurso?

Um **recurso** é algo que a API disponibiliza para consulta ou manipulação.

Por exemplo, em uma API de uma loja podemos ter:

```text
Produto
Cliente
Pedido
Categoria
```

Esses elementos representam recursos do sistema.

Podemos pensar:

```text
RECURSO = algo que a API disponibiliza
```

Exemplo:

```text
/produtos
```

representa o conjunto de produtos.

Enquanto:

```text
/produtos/15
```

pode representar um produto específico.

```text
/produtos/15
       ↑
    ID = 15
```

---

# 7. O que é um endpoint?

Um **endpoint** é um ponto específico de acesso a uma API.

Normalmente é representado por uma URL associada a uma determinada operação ou recurso.

Por exemplo:

```text
GET /produtos
```

pode representar uma solicitação para consultar produtos.

Outro exemplo:

```text
GET /produtos/15
```

pode representar uma solicitação para consultar o produto de identificador 15.

Podemos pensar:

```text
API
 │
 ├── /produtos
 │
 ├── /produtos/15
 │
 ├── /clientes
 │
 └── /pedidos
```

Esses pontos de acesso fazem parte da interface disponibilizada pela API.

---

# 8. Recurso × Endpoint

É importante não confundir os conceitos.

### Recurso

Representa o objeto ou conjunto de dados.

```text
PRODUTO
```

### Endpoint

É o ponto de acesso utilizado para interagir com esse recurso.

```text
/produtos
```

Podemos simplificar:

```text
RECURSO
   ↓
PRODUTO

ENDPOINT
   ↓
/produtos
```

Outro exemplo:

```text
RECURSO
   ↓
CLIENTE

ENDPOINT
   ↓
/clientes
```

---

# 9. REST e métodos HTTP

Uma das características mais importantes do REST é utilizar os métodos HTTP para indicar a ação desejada sobre um recurso.

Os principais métodos que estudaremos são:

```text
GET
POST
PUT
DELETE
```

Podemos associá-los inicialmente às seguintes operações:

| Método | Ideia principal      |
| ------ | -------------------- |
| GET    | Consultar            |
| POST   | Criar                |
| PUT    | Atualizar/substituir |
| DELETE | Excluir              |

---

# 10. GET

O método **GET** é utilizado para solicitar informações.

Exemplo:

```text
GET /produtos
```

A aplicação está dizendo:

> "Quero consultar os produtos."

Podemos imaginar:

```text
CLIENTE
   │
   │ GET /produtos
   ↓
  API
   │
   ↓
SERVIDOR
   │
   ↓
DADOS
```

A API pode retornar:

```json
[
  {
    "id": 1,
    "nome": "Notebook",
    "preco": 3500
  },
  {
    "id": 2,
    "nome": "Mouse",
    "preco": 80
  }
]
```

O JSON será estudado com mais profundidade posteriormente.

Neste momento, é suficiente compreender que ele é um formato muito utilizado para representar os dados enviados pela API.

---

# 11. POST

O método **POST** é normalmente utilizado para enviar dados ao servidor e solicitar a criação de um novo recurso.

Exemplo:

```text
POST /produtos
```

O cliente poderia enviar:

```json
{
  "nome": "Teclado",
  "preco": 120
}
```

A API recebe os dados e pode criar um novo produto.

Fluxo:

```text
CLIENTE
   │
   │ POST /produtos
   │
   │ dados do produto
   ↓
  API
   ↓
SERVIDOR
   ↓
BANCO DE DADOS
   ↓
NOVO PRODUTO
```

---

# 12. PUT

O método **PUT** é utilizado para atualizar ou substituir uma representação de um recurso.

Exemplo:

```text
PUT /produtos/15
```

O cliente está indicando:

> "Quero atualizar o produto 15."

Podemos imaginar:

```text
CLIENTE
   ↓
PUT /produtos/15
   ↓
API
   ↓
SERVIDOR
   ↓
PRODUTO 15 ATUALIZADO
```

Neste momento, o objetivo é compreender a função geral do método.

As diferenças entre `PUT` e `PATCH` serão aprofundadas posteriormente.

---

# 13. DELETE

O método **DELETE** é utilizado para solicitar a remoção de um recurso.

Exemplo:

```text
DELETE /produtos/15
```

A solicitação significa:

> "Quero remover o produto 15."

Fluxo:

```text
CLIENTE
   ↓
DELETE /produtos/15
   ↓
API
   ↓
SERVIDOR
   ↓
RECURSO REMOVIDO
```

---

# 14. REST e CRUD

Podemos relacionar os métodos HTTP com o conceito de CRUD estudado anteriormente.

| CRUD   | Operação  | Método HTTP |
| ------ | --------- | ----------- |
| Create | Criar     | POST        |
| Read   | Consultar | GET         |
| Update | Atualizar | PUT         |
| Delete | Excluir   | DELETE      |

Podemos visualizar:

```text
CRUD
 │
 ├── CREATE → POST
 ├── READ   → GET
 ├── UPDATE → PUT
 └── DELETE → DELETE
```

Essa associação será muito importante quando começarmos a desenvolver APIs.

---

# 15. REST: princípio Cliente-Servidor

Um dos princípios do REST é a separação entre **cliente** e **servidor**.

O cliente é responsável pela interface e pela interação com o usuário.

O servidor é responsável pelo processamento e pelos dados.

```text
┌──────────────┐
│    CLIENTE   │
│              │
│ Site / App   │
└──────┬───────┘
       │
       │ HTTP
       ↓
┌──────────────┐
│    SERVIDOR  │
│              │
│ API + Dados  │
└──────────────┘
```

Essa separação permite que diferentes clientes utilizem a mesma API.

Por exemplo:

```text
             API
              │
       ┌──────┼──────┐
       ↓      ↓      ↓
     SITE    APP   SISTEMA
```

Todos podem utilizar os mesmos serviços disponibilizados pela API.

---

# 16. REST: Stateless

Outro princípio importante é o conceito de **stateless**.

A ideia é que cada requisição deve conter as informações necessárias para que o servidor consiga processá-la.

O servidor não deve depender de uma memória de sessão específica para interpretar a requisição seguinte.

Exemplo simplificado:

```text
REQUISIÇÃO 1
   ↓
Servidor consegue processar

REQUISIÇÃO 2
   ↓
Servidor consegue processar
```

Cada requisição deve possuir as informações necessárias para ser compreendida.

Isso favorece a escalabilidade e simplifica determinados aspectos da arquitetura.

---

# 17. REST: Cacheável

Outro princípio é a possibilidade de utilizar **cache**.

Cache é uma área utilizada para armazenar temporariamente informações que podem ser reutilizadas.

Imagine:

```text
CLIENTE
   ↓
GET /produtos
   ↓
SERVIDOR
   ↓
RESPOSTA
```

Se a mesma informação for solicitada repetidamente, algumas respostas podem ser armazenadas temporariamente em cache.

```text
           ┌────────────┐
           │   CLIENTE  │
           └─────┬──────┘
                 │
                 ↓
              CACHE
                 │
          ┌──────┴──────┐
          │             │
       Encontrou     Não encontrou
          │             │
          ↓             ↓
       Resposta      SERVIDOR
```

O cache pode reduzir:

* tempo de resposta;
* processamento;
* tráfego;
* carga no servidor.

---

# 18. REST: Interface Uniforme

REST também trabalha com o princípio de uma **interface uniforme**.

Isso significa que a comunicação deve seguir padrões consistentes.

Por exemplo:

```text
GET /produtos
GET /produtos/10
POST /produtos
PUT /produtos/10
DELETE /produtos/10
```

O desenvolvedor consegue perceber uma lógica consistente na utilização dos recursos.

Essa padronização facilita o entendimento e o consumo da API.

---

# 19. Representação dos dados

Uma API precisa enviar dados utilizando algum formato.

Dois formatos muito conhecidos são:

```text
JSON
XML
```

---

# 20. JSON

JSON significa:

**JavaScript Object Notation**

É um formato leve e muito utilizado em APIs Web.

Exemplo:

```json
{
  "id": 10,
  "nome": "Notebook",
  "preco": 3500
}
```

Observe que os dados são organizados em pares:

```text
"chave": "valor"
```

Por exemplo:

```text
"nome": "Notebook"
```

---

# 21. XML

XML significa:

**Extensible Markup Language**

Também pode ser utilizado para representar dados.

Exemplo:

```xml
<produto>
    <id>10</id>
    <nome>Notebook</nome>
    <preco>3500</preco>
</produto>
```

Podemos observar uma estrutura baseada em elementos e marcações.

---

# 22. JSON × XML

| JSON                                 | XML                                                                 |
| ------------------------------------ | ------------------------------------------------------------------- |
| Estrutura mais compacta              | Estrutura mais verbosa                                              |
| Muito utilizado em APIs Web modernas | Muito utilizado em sistemas corporativos e integrações tradicionais |
| Fácil de ler                         | Estrutura baseada em marcações                                      |
| Comum em REST                        | Muito associado ao SOAP                                             |

Isso não significa que REST só pode utilizar JSON ou que SOAP só pode utilizar XML.

Essas associações são comuns, mas não são regras absolutas.

---

# 23. SOAP

SOAP significa:

**Simple Object Access Protocol**

SOAP é um **protocolo** utilizado para troca de informações estruturadas entre sistemas.

Uma de suas principais características é o uso de **XML** para estruturar as mensagens.

Exemplo conceitual:

```text
CLIENTE
   ↓
Mensagem SOAP
   ↓
SERVIDOR
   ↓
Processamento
   ↓
Resposta SOAP
   ↓
CLIENTE
```

---

# 24. SOAP e XML

Uma mensagem SOAP possui uma estrutura definida.

Exemplo simplificado:

```xml
<soap:Envelope>
    <soap:Body>
        <ConsultarCliente>
            <id>10</id>
        </ConsultarCliente>
    </soap:Body>
</soap:Envelope>
```

A estrutura é mais detalhada do que um JSON simples.

Por isso, SOAP pode parecer mais complexo inicialmente.

---

# 25. Características do SOAP

Entre suas características estão:

* Uso de XML;
* Estrutura formal de mensagens;
* Contratos bem definidos;
* Recursos voltados para ambientes corporativos;
* Suporte a padrões avançados de segurança;
* Suporte a operações e cenários complexos.

SOAP é encontrado principalmente em sistemas corporativos e integrações que possuem requisitos específicos de segurança, confiabilidade e transações.

---

# 26. WS-Security

SOAP pode utilizar padrões como **WS-Security**.

Esses padrões permitem implementar mecanismos relacionados à segurança das mensagens.

Em ambientes corporativos, isso pode ser importante quando existem requisitos rigorosos relacionados a:

* autenticação;
* integridade;
* confidencialidade;
* assinatura de mensagens.

Por isso, SOAP continua sendo utilizado em determinados setores e sistemas.

---

# 27. Desvantagens do SOAP

SOAP também possui algumas desvantagens.

Entre elas:

* Mensagens mais verbosas;
* Maior complexidade;
* Maior quantidade de padrões;
* Curva de aprendizado mais elevada;
* Estrutura geralmente mais pesada que uma API REST simples.

Podemos resumir:

```text
SOAP
 │
 ├── Estrutura formal
 ├── XML
 ├── Segurança avançada
 ├── Operações complexas
 └── Maior complexidade
```

---

# 28. REST × SOAP

Podemos comparar as duas abordagens:

| REST                        | SOAP                                              |
| --------------------------- | ------------------------------------------------- |
| Estilo arquitetural         | Protocolo                                         |
| Utiliza HTTP com frequência | Pode utilizar diferentes protocolos de transporte |
| Geralmente mais simples     | Geralmente mais complexo                          |
| JSON é muito comum          | XML é obrigatório nas mensagens SOAP              |
| Muito utilizado em APIs Web | Muito utilizado em sistemas corporativos          |
| Mais flexível               | Mais formal e padronizado                         |

Uma forma simples de lembrar:

```text
REST
→ simplicidade
→ recursos
→ HTTP
→ flexibilidade

SOAP
→ contrato
→ XML
→ padrões
→ operações corporativas complexas
```

---

# 29. GraphQL

Agora vamos conhecer outra abordagem.

**GraphQL** é uma linguagem de consulta para APIs e também um runtime utilizado para executar essas consultas.

Foi criado originalmente pelo Facebook, atualmente Meta.

Sua principal característica é permitir que o **cliente especifique exatamente quais dados deseja receber**.

---

# 30. O problema do excesso de dados

Imagine uma API:

```text
GET /clientes/10
```

A API retorna:

```json
{
  "id": 10,
  "nome": "Ana",
  "email": "ana@email.com",
  "telefone": "99999-9999",
  "endereco": "Rua A",
  "dataNascimento": "2000-01-10",
  "cidade": "Timon"
}
```

Mas imagine que a aplicação só precisava:

```text
nome
email
```

Nesse caso, foram recebidas informações que não eram necessárias.

Esse problema é chamado de:

**Overfetching**

---

# 31. Overfetching

**Overfetching** ocorre quando a aplicação recebe mais dados do que realmente precisa.

Exemplo:

```text
CLIENTE SOLICITA:

nome
email

API DEVOLVE:

nome
email
telefone
endereço
cidade
dataNascimento
...
```

O cliente recebeu dados adicionais.

```text
NECESSÁRIO
   ↓
nome
email

RECEBIDO
   ↓
nome
email
telefone
endereço
cidade
dataNascimento
```

---

# 32. Underfetching

O problema oposto é o **underfetching**.

Nesse caso, a aplicação recebe menos dados do que precisa.

Por exemplo:

```text
CLIENTE PRECISA:

nome
email
telefone
endereço

API DEVOLVE:

nome
email
```

O cliente precisa realizar outra solicitação para conseguir as informações restantes.

```text
REQUISIÇÃO 1
    ↓
Dados insuficientes
    ↓
REQUISIÇÃO 2
    ↓
Mais dados
```

---

# 33. Como GraphQL trabalha?

No GraphQL, o cliente pode especificar os campos que deseja.

Exemplo conceitual:

```graphql
query {
  cliente(id: 10) {
    nome
    email
  }
}
```

A API pode responder:

```json
{
  "data": {
    "cliente": {
      "nome": "Ana",
      "email": "ana@email.com"
    }
  }
}
```

O cliente pediu:

```text
nome
email
```

E recebeu:

```text
nome
email
```

Essa é uma das principais ideias do GraphQL.

---

# 34. Tipagem forte no GraphQL

GraphQL utiliza um **schema** que define os tipos e campos disponíveis.

Por exemplo:

```graphql
type Cliente {
  id: ID!
  nome: String!
  email: String!
}
```

Isso permite que a API conheça a estrutura dos dados disponíveis.

A tipagem ajuda a:

* validar consultas;
* documentar a API;
* detectar erros;
* melhorar ferramentas de desenvolvimento.

---

# 35. REST × GraphQL

Podemos comparar:

| REST                                         | GraphQL                                           |
| -------------------------------------------- | ------------------------------------------------- |
| Trabalha fortemente com recursos e endpoints | Trabalha com consultas e um schema                |
| Cliente utiliza URLs e métodos HTTP          | Cliente especifica os campos desejados            |
| Pode haver múltiplos endpoints               | Frequentemente utiliza um endpoint para consultas |
| Pode ocorrer overfetching                    | Permite solicitar campos específicos              |
| Pode exigir várias requisições               | Pode buscar dados relacionados em uma consulta    |

Isso não significa que GraphQL seja sempre melhor que REST.

A escolha depende do problema que estamos tentando resolver.

---

# 36. REST × SOAP × GraphQL

Agora podemos comparar as três abordagens:

| Característica           | REST                                                           | SOAP                                | GraphQL                            |
| ------------------------ | -------------------------------------------------------------- | ----------------------------------- | ---------------------------------- |
| Natureza                 | Estilo arquitetural                                            | Protocolo                           | Linguagem de consulta + runtime    |
| Dados                    | JSON, XML e outros                                             | XML                                 | JSON é comum nas respostas         |
| Comunicação              | HTTP é muito comum                                             | Pode utilizar diferentes protocolos | Normalmente HTTP                   |
| Organização              | Recursos                                                       | Operações/mensagens                 | Schema e consultas                 |
| Flexibilidade            | Alta                                                           | Menor                               | Alta                               |
| Complexidade             | Geralmente menor                                               | Maior                               | Moderada                           |
| Consultas personalizadas | Limitadas ao desenho da API                                    | Não é o foco                        | É um dos principais objetivos      |
| Segurança avançada       | Pode utilizar mecanismos externos e próprios da infraestrutura | Possui padrões como WS-Security     | Depende da implementação           |
| Uso comum                | APIs Web                                                       | Sistemas corporativos               | Aplicações com consultas complexas |

---

# 37. Quando utilizar cada abordagem?

Não existe uma única resposta para todos os projetos.

## REST

Pode ser uma boa escolha quando:

* queremos uma API Web simples;
* precisamos trabalhar com recursos;
* queremos utilizar HTTP de forma natural;
* buscamos facilidade de implementação;
* precisamos de uma arquitetura amplamente conhecida.

---

## SOAP

Pode ser adequado quando:

* existem requisitos corporativos específicos;
* há necessidade de padrões formais;
* existem transações complexas;
* segurança de mensagens é um requisito importante;
* o ambiente já utiliza tecnologias baseadas em SOAP.

---

## GraphQL

Pode ser interessante quando:

* o cliente precisa de dados muito específicos;
* existem consultas complexas;
* diferentes clientes precisam de diferentes conjuntos de dados;
* queremos reduzir overfetching e underfetching;
* precisamos consultar dados relacionados de maneira flexível.

---

# 38. Arquitetura de uma API

Agora que conhecemos diferentes abordagens, precisamos compreender como uma API pode ser estruturada.

Uma arquitetura simplificada pode ser:

```text
CLIENTE
   ↓
API
   ↓
SERVIDOR
   ↓
BANCO DE DADOS
```

Mas uma aplicação real pode possuir vários outros componentes.

```text
                 CLIENTE
                    │
                    ↓
              API GATEWAY
                    │
          ┌─────────┼─────────┐
          ↓         ↓         ↓
       SERVIÇO   SERVIÇO   SERVIÇO
       USUÁRIO   PEDIDO    PRODUTO
          │         │         │
          └─────────┼─────────┘
                    ↓
               BANCO DE DADOS
```

---

# 39. Componentes principais

Podemos identificar:

```text
CLIENTE
SERVIDOR
ENDPOINT
RECURSO
MÉTODO HTTP
REPRESENTAÇÃO
BANCO DE DADOS
API GATEWAY
CACHE
```

Cada componente possui uma função.

---

# 40. Cliente

O **cliente** inicia a comunicação.

Pode ser:

* navegador;
* aplicativo mobile;
* aplicação JavaScript;
* sistema empresarial;
* outro servidor.

Exemplo:

```text
Navegador
   ↓
GET /produtos
```

---

# 41. Servidor

O servidor recebe e processa as requisições.

Ele pode:

* validar dados;
* executar regras de negócio;
* consultar o banco;
* realizar cálculos;
* autenticar usuários;
* retornar respostas.

Podemos imaginar:

```text
CLIENTE
   ↓
REQUISIÇÃO
   ↓
SERVIDOR
   ↓
PROCESSAMENTO
   ↓
RESPOSTA
```

---

# 42. Endpoint

O endpoint representa um ponto de acesso da API.

Exemplos:

```text
GET /clientes
GET /clientes/10

GET /produtos
GET /produtos/20

POST /pedidos
```

Os endpoints são definidos pela API para disponibilizar seus recursos e operações.

---

# 43. Recursos

Os recursos representam os elementos que a API disponibiliza.

Exemplo:

```text
/clientes
/produtos
/pedidos
/cursos
/alunos
```

Podemos pensar:

```text
API
 │
 ├── Clientes
 ├── Produtos
 ├── Pedidos
 ├── Cursos
 └── Alunos
```

---

# 44. Métodos HTTP

Os métodos indicam a intenção da requisição.

```text
GET
   ↓
Consultar

POST
   ↓
Criar

PUT
   ↓
Atualizar/Substituir

DELETE
   ↓
Excluir
```

Eles serão estudados detalhadamente nas próximas aulas.

---

# 45. Representação

Os dados precisam ser representados em algum formato.

Os mais conhecidos neste contexto são:

```text
JSON
XML
```

Exemplo JSON:

```json
{
  "nome": "Carlos",
  "idade": 20
}
```

Exemplo XML:

```xml
<aluno>
    <nome>Carlos</nome>
    <idade>20</idade>
</aluno>
```

---

# 46. Banco de Dados

Muitas APIs precisam consultar ou alterar dados armazenados em um Banco de Dados.

Podemos ter:

```text
CLIENTE
   ↓
API
   ↓
SERVIDOR
   ↓
BANCO DE DADOS
```

Por exemplo:

```text
GET /clientes/10
```

Pode resultar em:

```text
API
 ↓
Consulta banco
 ↓
Cliente 10 encontrado
 ↓
Monta resposta
 ↓
Retorna ao cliente
```

É importante lembrar que o cliente normalmente **não acessa diretamente o banco de dados**.

A API atua como uma camada intermediária.

---

# 47. API Gateway

Em arquiteturas mais complexas, pode existir um componente chamado:

**API Gateway**

Ele atua como intermediário entre os clientes e os serviços internos.

```text
CLIENTE
   ↓
API GATEWAY
   ↓
┌───────────────┐
│               │
↓               ↓
USUÁRIOS      PEDIDOS
│               │
↓               ↓
BANCO         BANCO
```

---

# 48. Funções do API Gateway

Um API Gateway pode ser responsável por:

* receber requisições;
* encaminhar requisições;
* autenticar clientes;
* controlar autorização;
* aplicar políticas;
* limitar requisições;
* registrar informações;
* realizar roteamento;
* integrar diferentes serviços.

Em uma arquitetura com vários serviços, ele pode funcionar como uma porta de entrada.

---

# 49. API Gateway na prática

Imagine uma aplicação com:

```text
SERVIÇO DE USUÁRIOS
SERVIÇO DE PEDIDOS
SERVIÇO DE PRODUTOS
SERVIÇO DE PAGAMENTOS
```

O cliente não precisa necessariamente conhecer todos os serviços internos.

Pode existir:

```text
                  CLIENTE
                     ↓
                API GATEWAY
                     ↓
        ┌────────────┼────────────┐
        ↓            ↓            ↓
    USUÁRIOS       PEDIDOS     PRODUTOS
```

O Gateway recebe a requisição e decide para onde ela deve ser encaminhada.

---

# 50. Cache

O **cache** armazena temporariamente informações que podem ser reutilizadas.

Imagine uma API que recebe:

```text
GET /produtos
```

Milhares de vezes.

Se os dados não mudaram, talvez seja possível reutilizar uma resposta armazenada temporariamente.

```text
CLIENTE
   ↓
GET /produtos
   ↓
CACHE
   │
   ├── Encontrou → retorna resposta
   │
   └── Não encontrou
           ↓
        SERVIDOR
           ↓
        BANCO
```

---

# 51. Benefícios do cache

O uso adequado de cache pode:

* reduzir o tempo de resposta;
* diminuir consultas ao banco;
* reduzir a carga do servidor;
* diminuir o tráfego;
* melhorar a experiência do usuário.

Por exemplo:

```text
SEM CACHE

Cliente
  ↓
Servidor
  ↓
Banco
  ↓
Servidor
  ↓
Cliente
```

Com cache:

```text
COM CACHE

Cliente
  ↓
Cache
  ↓
Resposta
```

Quando a informação está disponível e pode ser reutilizada, evitamos processamento desnecessário.

---

# 52. Cuidado com o cache

Cache não significa simplesmente:

> "Guardar tudo."

É necessário definir:

* o que pode ser armazenado;
* por quanto tempo;
* quando o cache deve ser atualizado;
* quais informações não devem ser armazenadas.

Informações sensíveis ou que mudam constantemente exigem cuidados especiais.

---

# 53. Arquitetura completa simplificada

Podemos reunir todos os conceitos:

```text
                         CLIENTE
                            │
                            ↓
                     API GATEWAY
                            │
                   ┌────────┴────────┐
                   ↓                 ↓
                CACHE             SERVIDOR
                                     │
                           ┌─────────┼─────────┐
                           ↓         ↓         ↓
                       USUÁRIOS   PEDIDOS   PRODUTOS
                           │         │         │
                           └─────────┼─────────┘
                                     ↓
                              BANCO DE DADOS
```

O cliente envia uma requisição.

O Gateway pode receber e encaminhar.

O cache pode responder rapidamente quando possível.

O servidor processa a requisição.

Os serviços podem consultar ou alterar o banco.

Finalmente, a resposta retorna ao cliente.

---

# 54. Exemplo completo

Imagine uma aplicação de loja.

O cliente deseja consultar o produto de código 25.

A aplicação realiza:

```text
GET /produtos/25
```

Podemos representar:

```text
CLIENTE
   │
   │ GET /produtos/25
   ↓
API GATEWAY
   │
   ↓
SERVIÇO DE PRODUTOS
   │
   ↓
CACHE
   │
   ├── Produto encontrado
   │       ↓
   │    RESPOSTA
   │
   └── Produto não encontrado
           ↓
       BANCO DE DADOS
           ↓
       SERVIÇO
           ↓
       RESPOSTA
```

Uma possível resposta seria:

```json
{
  "id": 25,
  "nome": "Notebook",
  "preco": 3500
}
```

Observe quantos conceitos estão envolvidos:

```text
CLIENTE
ENDPOINT
MÉTODO HTTP
RECURSO
SERVIDOR
CACHE
BANCO DE DADOS
JSON
RESPOSTA
```

---

# 55. REST, SOAP e GraphQL em uma visão geral

Podemos guardar inicialmente estas ideias:

```text
REST
↓
Recursos + HTTP + URLs
```

```text
SOAP
↓
Mensagens XML + contratos + padrões corporativos
```

```text
GraphQL
↓
Consultas personalizadas + schema
```

Não devemos pensar:

> "Um é sempre melhor que o outro."

Devemos pensar:

> **"Qual abordagem atende melhor às necessidades do sistema?"**

---

# 56. Como escolher?

Podemos utilizar algumas perguntas:

### Pergunta 1

O sistema precisa de uma API Web simples e amplamente conhecida?

```text
→ REST pode ser uma boa opção.
```

### Pergunta 2

O sistema possui requisitos corporativos específicos, contratos formais e operações complexas?

```text
→ SOAP pode ser considerado.
```

### Pergunta 3

Diferentes clientes precisam solicitar diferentes conjuntos de dados?

```text
→ GraphQL pode ser interessante.
```

A escolha depende dos requisitos.

---

# 57. Exemplo de decisão

Imagine três projetos.

## Projeto A — Aplicativo de catálogo

Precisa:

* listar produtos;
* consultar produtos;
* criar produtos;
* atualizar produtos;
* excluir produtos.

Uma API REST pode atender muito bem.

```text
GET    /produtos
GET    /produtos/10
POST   /produtos
PUT    /produtos/10
DELETE /produtos/10
```

---

## Projeto B — Sistema corporativo complexo

Possui:

* transações complexas;
* regras corporativas;
* integração com sistemas legados;
* requisitos específicos de segurança.

SOAP pode ser uma opção adequada dependendo dos requisitos e da infraestrutura existente.

---

## Projeto C — Aplicativo com consultas complexas

Imagine um aplicativo que precisa consultar:

```text
Usuário
   ↓
Pedidos
   ↓
Produtos
   ↓
Categorias
```

E diferentes telas precisam de informações diferentes.

GraphQL pode ser uma alternativa interessante porque permite que o cliente especifique os dados necessários.

---

# 58. O que aprendemos?

Nesta aula estudamos que existem diferentes formas de construir APIs.

Aprendemos:

```text
REST
SOAP
GraphQL
```

Também estudamos os principais conceitos de uma arquitetura de API:

```text
CLIENTE
   ↓
API GATEWAY
   ↓
SERVIDOR
   ↓
BANCO DE DADOS
```

E:

```text
RECURSO
ENDPOINT
MÉTODO HTTP
REPRESENTAÇÃO
CACHE
```

---

# 59. Resumo dos conceitos

| Conceito    | Significado                                                    |
| ----------- | -------------------------------------------------------------- |
| API         | Interface para comunicação entre sistemas                      |
| REST        | Estilo arquitetural para sistemas distribuídos                 |
| SOAP        | Protocolo de troca de mensagens estruturadas                   |
| GraphQL     | Linguagem de consulta e runtime para APIs                      |
| Recurso     | Elemento disponibilizado pela API                              |
| Endpoint    | Ponto de acesso da API                                         |
| GET         | Consulta                                                       |
| POST        | Criação/envio                                                  |
| PUT         | Atualização/substituição                                       |
| DELETE      | Exclusão                                                       |
| JSON        | Formato de representação de dados                              |
| XML         | Linguagem/formato de marcação utilizado para representar dados |
| API Gateway | Intermediário entre clientes e serviços                        |
| Cache       | Armazenamento temporário de dados/respostas                    |

---

# 60. Mapa mental da aula

```text
                         APIs
                          │
            ┌─────────────┼─────────────┐
            ↓             ↓             ↓
          REST           SOAP        GraphQL
            │             │             │
            ↓             ↓             ↓
        Recursos         XML         Consultas
        HTTP             Contratos   Schema
        URLs             Segurança   Tipagem
        JSON             Transações  Flexibilidade
            │
            ↓
       ARQUITETURA
            │
      ┌─────┼──────────────┐
      ↓     ↓              ↓
   Cliente Servidor      Gateway
      │     │              │
      │     ↓              ↓
      │   Banco          Serviços
      │
      ↓
   Endpoint
      │
      ↓
Métodos HTTP
      │
 ┌────┼────┬──────┐
 ↓    ↓    ↓      ↓
GET POST PUT DELETE
      │
      ↓
Representação
   │        │
   ↓        ↓
 JSON      XML
      │
      ↓
    Cache
```

---

# 61. Pergunta para reflexão

Antes de finalizar, pense:

> **Se REST, SOAP e GraphQL são formas diferentes de construir APIs, por que não utilizar sempre a opção mais simples?**

A resposta está nos **requisitos do sistema**.

Uma tecnologia ou arquitetura não deve ser escolhida apenas porque é popular.

Devemos analisar:

* necessidade do sistema;
* complexidade;
* segurança;
* desempenho;
* integração;
* quantidade e tipo de clientes;
* manutenção;
* infraestrutura existente.

---

# 62. Preparação para a próxima aula

Agora que já conhecemos os principais tipos e componentes de APIs, podemos começar a estudar **como uma API REST é utilizada na prática**.

Na próxima etapa, vamos aprofundar:

```text
HTTP
 ↓
REQUISIÇÃO
 ↓
MÉTODO
 ↓
URL
 ↓
ENDPOINT
 ↓
PARÂMETROS
 ↓
HEADERS
 ↓
BODY
 ↓
RESPOSTA
 ↓
STATUS HTTP
```

A partir daí, o aluno começará a observar uma requisição de API não apenas como uma ideia abstrata, mas como uma comunicação real entre cliente e servidor.
