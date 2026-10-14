Vamos instalar o **MariaDB no Termux**, que é compatível com o MySQL e funciona bem no Android. Assim, você poderá criar bancos de dados, tabelas e executar comandos SQL diretamente pelo celular, sem precisar instalar o phpMyAdmin.

## 1. Atualize o Termux

Abra o Termux e execute:

```bash
pkg update && pkg upgrade -y
```

Aguarde a atualização terminar.

## 2. Instale o MariaDB

Execute:

```bash
pkg install mariadb -y
```

Verifique se foi instalado corretamente:

```bash
mariadb --version
```

Deverá aparecer a versão do MariaDB.

> **Importante:** o MariaDB é uma alternativa compatível com o MySQL. Os comandos SQL básicos são praticamente os mesmos.

## 3. Inicialize o banco de dados

Execute:

```bash
mariadb-install-db
```

Esse comando prepara os arquivos necessários para o funcionamento do banco de dados.

Se a inicialização terminar sem erros, avance para a próxima etapa.

## 4. Inicie o servidor

Execute:

```bash
mariadbd-safe &
```

Aguarde alguns segundos para que o servidor inicie.

Para verificar se o processo está ativo:

```bash
pgrep -af mariadbd
```

Se aparecer um processo relacionado ao MariaDB, provavelmente o servidor está funcionando.

## 5. Acesse o banco de dados

Execute:

```bash
mariadb
```

Se tudo estiver correto, você verá algo semelhante a:

```text
Welcome to the MariaDB monitor.
MariaDB [(none)]>
```

Pronto! Você já está dentro do banco de dados.

Para sair, utilize:

```sql
EXIT;
```

## 6. Crie seu primeiro banco de dados

Entre novamente, caso tenha saído:

```bash
mariadb
```

Agora, crie um banco chamado `biblioteca`:

```sql
CREATE DATABASE biblioteca;
```

Confira se ele foi criado:

```sql
SHOW DATABASES;
```

Você deverá encontrar o banco `biblioteca` na lista.

## 7. Crie uma tabela

Selecione o banco:

```sql
USE biblioteca;
```

Crie uma tabela para armazenar livros:

```sql
CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    ano_publicacao INT
);
```

Confira a estrutura:

```sql
DESCRIBE livros;
```

## 8. Insira e consulte dados

Insira um livro:

```sql
INSERT INTO livros (titulo, autor, ano_publicacao)
VALUES ('Introdução a Banco de Dados', 'Carlos Silva', 2025);
```

Consulte os registros:

```sql
SELECT * FROM livros;
```

Para atualizar um registro:

```sql
UPDATE livros
SET ano_publicacao = 2026
WHERE id = 1;
```

Para excluir um registro:

```sql
DELETE FROM livros
WHERE id = 1;
```

**Atenção:** o comando `DELETE` remove o registro selecionado. Sempre confira a condição `WHERE` antes de executar.

## 9. Como iniciar o MySQL/MariaDB quando abrir o Termux

Se o servidor não estiver em execução, utilize:

```bash
mariadbd-safe &
```

Depois, conecte-se:

```bash
mariadb
```

Para encerrar uma sessão SQL:

```sql
EXIT;
```

Isso encerra sua conexão com o banco, mas não necessariamente o servidor.

---

## Resumo dos comandos

| Ação | Comando |
|---|---|
| Instalar | `pkg install mariadb -y` |
| Inicializar | `mariadb-install-db` |
| Iniciar o servidor | `mariadbd-safe &` |
| Entrar no banco | `mariadb` |
| Listar bancos | `SHOW DATABASES;` |
| Selecionar banco | `USE biblioteca;` |
| Listar tabelas | `SHOW TABLES;` |
| Consultar dados | `SELECT * FROM livros;` |
| Sair | `EXIT;` |

### Uma recomendação para seus projetos

Como você desenvolve aplicações web e APIs com Python, FastAPI e outras tecnologias, o MariaDB instalado no Termux pode servir como banco de dados para seus testes.

**Comece executando estes três comandos, um de cada vez:**

```bash
pkg update && pkg upgrade -y
```

```bash
pkg install mariadb -y
```

```bash
mariadb-install-db
```

Depois, execute `mariadbd-safe &` e `mariadb` para iniciar o servidor e acessar o banco.

Se algum comando apresentar erro, envie a mensagem completa para que eu possa orientar a correção sem fazer você reinstalar tudo desnecessariamente.