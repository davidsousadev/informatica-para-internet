# Guia da API RESTful Flask

## Visão Geral

Esta API foi desenvolvida utilizando Flask e segue os princípios RESTful para comunicação entre clientes e servidores através de HTTP.

**Base URL:**

```text
http://localhost:5000/api/v1
```

---

## Tecnologias Utilizadas

* Python 3.11+
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Flask-JWT-Extended
* PostgreSQL/MySQL/SQLite
* Marshmallow (Serialização)

---

## Estrutura do Projeto

```text
project/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── config.py
│   └── __init__.py
│
├── migrations/
├── tests/
├── requirements.txt
├── run.py
└── README.md
```

---

## Autenticação

A API utiliza JWT (JSON Web Token).

### Login

**Endpoint**

```http
POST /auth/login
```

**Request**

```json
{
  "email": "usuario@email.com",
  "password": "senha123"
}
```

**Response**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs..."
}
```

### Uso do Token

Enviar no cabeçalho:

```http
Authorization: Bearer SEU_TOKEN
```

---

# Recursos

## Usuários

### Listar usuários

```http
GET /users
```

**Response**

```json
[
  {
    "id": 1,
    "name": "João Silva",
    "email": "joao@email.com"
  }
]
```

---

### Buscar usuário por ID

```http
GET /users/{id}
```

**Exemplo**

```http
GET /users/1
```

**Response**

```json
{
  "id": 1,
  "name": "João Silva",
  "email": "joao@email.com"
}
```

---

### Criar usuário

```http
POST /users
```

**Request**

```json
{
  "name": "João Silva",
  "email": "joao@email.com",
  "password": "123456"
}
```

**Response**

```json
{
  "id": 1,
  "message": "Usuário criado com sucesso"
}
```

---

### Atualizar usuário

```http
PUT /users/{id}
```

**Request**

```json
{
  "name": "João Atualizado"
}
```

**Response**

```json
{
  "message": "Usuário atualizado com sucesso"
}
```

---

### Remover usuário

```http
DELETE /users/{id}
```

**Response**

```json
{
  "message": "Usuário removido com sucesso"
}
```

---

# Códigos de Status HTTP

| Código | Descrição             |
| ------ | --------------------- |
| 200    | OK                    |
| 201    | Created               |
| 204    | No Content            |
| 400    | Bad Request           |
| 401    | Unauthorized          |
| 403    | Forbidden             |
| 404    | Not Found             |
| 409    | Conflict              |
| 422    | Unprocessable Entity  |
| 500    | Internal Server Error |

---

# Paginação

Exemplo:

```http
GET /users?page=1&per_page=10
```

**Response**

```json
{
  "items": [],
  "page": 1,
  "per_page": 10,
  "total": 100,
  "pages": 10
}
```

---

# Filtros

Exemplo:

```http
GET /users?name=joao
```

---

# Ordenação

Exemplo:

```http
GET /users?sort=name&order=asc
```

---

# Tratamento de Erros

Formato padrão:

```json
{
  "error": true,
  "message": "Descrição do erro"
}
```

Exemplo:

```json
{
  "error": true,
  "message": "Usuário não encontrado"
}
```

---

# Health Check

```http
GET /health
```

**Response**

```json
{
  "status": "ok"
}
```

---

# Boas Práticas

* Utilizar nomes de recursos no plural.
* Retornar códigos HTTP adequados.
* Validar todos os dados de entrada.
* Utilizar autenticação JWT para rotas protegidas.
* Implementar logs e monitoramento.
* Versionar a API (`/api/v1`).
* Documentar endpoints com Swagger/OpenAPI.

---

# Exemplo de Curl

```bash
curl -X GET \
  http://localhost:5000/api/v1/users \
  -H "Authorization: Bearer TOKEN"
```

---

# Licença

Este projeto está licenciado sob a licença MIT.
