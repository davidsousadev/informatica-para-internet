# Atividade 03 - Formulários, Input e Multimídia

**Disciplina:** Programação para Front-End
**Curso:** Técnico em Informática para Internet
**Professor:** David Sousa

---

## 1. Formulários HTML

Formulários são utilizados em páginas HTML para **coletar informações dos usuários**, como nome, e-mail, senha, idade, arquivos e outras informações.

A estrutura básica de um formulário utiliza a tag:

```html
<form>
    <!-- campos do formulário -->
</form>
```

### Principais atributos do `<form>`

#### `action`

Define o endereço para onde os dados do formulário serão enviados.

```html
<form action="processamento.php">
```

#### `method`

Define como os dados serão enviados.

Os principais métodos são:

* **GET:** envia os dados pela URL.
* **POST:** envia os dados no corpo da requisição.

Exemplo:

```html
<form action="processamento.php" method="POST">

</form>
```

### GET x POST

**GET**

* Os dados ficam visíveis na URL.
* Pode ser utilizado em pesquisas e filtros.
* Não é indicado para informações sensíveis.

**POST**

* Os dados são enviados no corpo da requisição.
* É mais adequado para informações sensíveis e grandes volumes de dados.

---

## 2. Campos de entrada - `<input>`

A tag `<input>` permite criar diferentes tipos de campos para receber informações do usuário.

Exemplo:

```html
<input type="text">
```

O atributo `type` define o tipo de campo.

### Principais tipos de `input`

| Tipo       | Função                         |
| ---------- | ------------------------------ |
| `text`     | Campo de texto                 |
| `email`    | Campo para e-mail              |
| `password` | Campo de senha                 |
| `number`   | Campo para números             |
| `date`     | Seleção de data                |
| `time`     | Seleção de horário             |
| `color`    | Seleção de cor                 |
| `file`     | Seleção de arquivo             |
| `checkbox` | Caixa de seleção               |
| `radio`    | Seleção de uma opção           |
| `range`    | Seletor de intervalo           |
| `search`   | Campo de pesquisa              |
| `tel`      | Número de telefone             |
| `url`      | Endereço de site               |
| `submit`   | Botão para enviar o formulário |
| `reset`    | Botão para limpar o formulário |
| `button`   | Botão comum                    |

### Exemplo

```html
<input type="text" name="nome">
<input type="email" name="email">
<input type="password" name="senha">
<input type="number" name="idade">
```

---

## 3. Atributos `name` e `value`

O atributo `name` identifica o campo quando os dados são enviados.

```html
<input type="text" name="nome">
```

O atributo `value` define um valor para o campo.

```html
<input type="text" name="nome" value="David">
```

---

## 4. Formulário completo

Exemplo de um formulário simples:

```html
<form action="processamento.php" method="POST">

    <input type="text" name="nome">

    <input type="email" name="email">

    <input type="password" name="senha">

    <input type="submit" value="Enviar">

</form>
```

Nesse exemplo:

* `form` cria o formulário;
* `action` define para onde os dados serão enviados;
* `method` define como os dados serão enviados;
* `input` cria os campos;
* `type` define o tipo do campo;
* `name` identifica o campo;
* `submit` cria o botão de envio.

---

## 5. Imagens

Para inserir uma imagem em uma página HTML, utilizamos a tag:

```html
<img src="leao.jpg">
```

O atributo `src` indica o local onde está o arquivo da imagem.

A imagem pode estar na mesma pasta do arquivo HTML:

```text
projeto/
├── index.html
└── leao.jpg
```

### Alterando o tamanho

Podemos utilizar `width` para definir a largura:

```html
<img src="leao.jpg" width="300px">
```

Ou `height` para definir a altura:

```html
<img src="leao.jpg" height="200px">
```

### Atenção

Alterar `width` e `height` ao mesmo tempo pode causar **distorção da imagem**.

---

## 6. Áudio

Para adicionar áudio a uma página HTML, utilizamos a tag `<audio>`.

```html
<audio controls>
    <source src="minha_musica.mp3" type="audio/mp3">
</audio>
```

O atributo `controls` permite que o usuário tenha acesso aos controles de reprodução.

O arquivo de áudio deve estar disponível no caminho indicado.

Exemplo de estrutura:

```text
projeto/
├── index.html
└── minha_musica.mp3
```

---

## 7. Vídeo

Para adicionar vídeos, utilizamos a tag `<video>`.

```html
<video width="380" height="240" controls>
    <source src="video.mp4" type="video/mp4">
</video>
```

Nesse exemplo:

* `width` define a largura;
* `height` define a altura;
* `controls` exibe os controles do vídeo;
* `source` indica o arquivo de vídeo;
* `type` informa o formato do arquivo.

Exemplo de estrutura:

```text
projeto/
├── index.html
└── video.mp4
```

---

## 8. Prática no VS Code

Durante a atividade, foram praticados no **Visual Studio Code**:

* Criação de formulários HTML;
* Utilização da tag `<form>`;
* Utilização dos atributos `action` e `method`;
* Criação de campos com `<input>`;
* Utilização de diferentes tipos de `input`;
* Utilização dos atributos `name` e `value`;
* Criação de botões de envio e redefinição;
* Inserção de imagens com `<img>`;
* Alteração de largura e altura de imagens;
* Inserção de áudio com `<audio>`;
* Inserção de vídeo com `<video>`;
* Organização dos arquivos HTML, imagens, áudios e vídeos em um projeto.

---

## Atividade prática

Crie no VS Code uma página HTML contendo:

1. Um formulário para cadastro de usuário;
2. Campos para nome, e-mail e senha;
3. Um campo para idade;
4. Uma opção de seleção utilizando `radio`;
5. Uma opção utilizando `checkbox`;
6. Um campo para selecionar um arquivo;
7. Um botão para enviar o formulário;
8. Uma imagem;
9. Um áudio;
10. Um vídeo.

### Objetivo

Praticar a criação de **formulários, campos de entrada e elementos multimídia utilizando HTML**.
