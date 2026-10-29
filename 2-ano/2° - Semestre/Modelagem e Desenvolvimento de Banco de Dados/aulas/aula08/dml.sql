-- Comparação: maior, menor, diferente
1. SELECT *
2. FROM tecnicos
3. WHERE id_tecnico > 1;

-- Vários critérios — AND / OR
1. SELECT *
2. FROM tecnicos
3. WHERE nome_tecnico LIKE '%Silva%'
4.   AND id_tecnico <= 5;

-- Ordem crescente (padrão)
1. SELECT *
2. FROM tecnicos
3. ORDER BY nome_tecnico ASC;

-- Ordem decrescente
1. SELECT *
2. FROM tecnicos
3. ORDER BY id_tecnico DESC;

-- Remover repetições de resultados
1. SELECT DISTINCT nome_tecnico
2. FROM tecnicos;

-- Pegar apenas os 3 primeiros registros
1. SELECT *
2. FROM tecnicos
3. ORDER BY id_tecnico
4. LIMIT 3;

-- Paginação: pular 2 registros, pegar 2
1. SELECT *
2. FROM tecnicos
3. ORDER BY id_tecnico
4. LIMIT 2 OFFSET 2;

-- Contar total de registros
1. SELECT COUNT(*) AS total_tecnicos
2. FROM tecnicos;

-- Valor máximo / mínimo
1. SELECT MAX(id_tecnico) AS maior_id,
2.        MIN(id_tecnico) AS menor_id
3. FROM tecnicos;

-- Contar e agrupar
1. SELECT COUNT(*) AS quantidade
2. FROM tecnicos
3. GROUP BY id_tecnico;

-- Renomear coluna no resultado
1. SELECT nome_tecnico AS Nome,
2.        telefone AS Contato
3. FROM tecnicos;