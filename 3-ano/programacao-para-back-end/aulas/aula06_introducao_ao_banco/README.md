# Manipulando SQLite pelo Terminal (.db)

## 1. Abrir o banco de dados
```bash
sqlite3 banco.db
```
Se o arquivo não existir, ele será criado automaticamente.

---

## 2. Comandos básicos no SQLite

### Ver tabelas
```sql
.tables
```

### Criar tabela
```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER
);
```

---

## 3. CRUD no terminal

### ➕ INSERT (Criar)
```sql
INSERT INTO usuarios (nome, idade) VALUES ('Ana', 25);
```

### 🔍 SELECT (Ler)
```sql
SELECT * FROM usuarios;
```

### ✏️ UPDATE (Atualizar)
```sql
UPDATE usuarios
SET idade = 30
WHERE nome = 'Ana';
```

### ❌ DELETE (Excluir)
```sql
DELETE FROM usuarios
WHERE nome = 'Ana';
```

---

## 4. Melhorar visualização

```sql
.headers on
.mode column
```

---

## 5. Sair do SQLite
```sql
.exit
```

---

## 6. Rodar arquivo .sql

Crie um arquivo `script.sql` e execute:

```bash
sqlite3 banco.db < script.sql
```

---

## Resumo
- sqlite3 banco.db → abre o banco
- SQL direto → CRUD completo
- .tables → lista tabelas
- .headers / .mode → formatação
- .exit → sair