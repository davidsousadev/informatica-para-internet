# 🐍 Funções e Módulos em Python

## 📌 1. Funções em Python

Funções são blocos de código reutilizáveis.

---

### ✨ Função simples

```python
def saudacao():
    print("Olá! Bem-vindo ao Python.")
```

### ▶️ Uso:

```python
saudacao()
```

---

### ✨ Função com parâmetros

```python
def saudacao(nome):
    print(f"Olá, {nome}!")
```

### ▶️ Uso:

```python
saudacao("Carlos")
saudacao("Maria")
```

---

### ✨ Função com retorno

```python
def soma(a, b):
    return a + b
```

### ▶️ Uso:

```python
resultado = soma(5, 3)
print(resultado)
```

---

## 🧩 2. Módulos em Python

Um módulo é um arquivo `.py` com funções reutilizáveis.

---

### 📂 Exemplo de módulo (meu_modulo.py)

```python
def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b
```

---

### 📥 Usando o módulo

```python
import meu_modulo

print(meu_modulo.soma(10, 5))
print(meu_modulo.subtrai(10, 5))
```

---

### 📥 Importando função específica

```python
from meu_modulo import soma

print(soma(10, 5))
```

---

## 📦 3. Módulos nativos do Python

### 🔢 math

```python
import math

print(math.sqrt(16))
print(math.pi)
```

---

### 🎲 random

```python
import random

print(random.randint(1, 10))
```

---

### 📅 datetime

```python
import datetime

print(datetime.datetime.now())
```

---

## 🚀 4. Resumo

- Funções → reutilizam código
- Módulos → organizam funções em arquivos
- Python já tem módulos prontos
```