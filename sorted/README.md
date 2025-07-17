# Ordenação com `sorted` e `lambda`

```python

nomes = ['João', 'ana', 'Carlos']
nomes_ordenados = sorted(nomes, key=lambda nome: nome.lower())
print(nomes_ordenados) # Saída: ['ana', 'Carlos', 'João']

```

<br>

## Explicação do código Python:

```python

nomes = ['João', 'ana', 'Carlos']

```

<br>

No código acima foi criada uma lista chamada nomes com três strings. Elas têm **diferenças de capitalização**:

- `João`   → começa com J maiúsculo

- `ana`    → tudo minúsculo

- `Carlos` → começa com C maiúsculo

<br>

***

<br>
<br>

```python

nomes_ordenados = sorted(nomes, key=lambda nome: nome.lower())

```

Aqui vem a parte mais importante:

 🔹 `sorted(...)`
- É uma função embutida do Python que **retorna** uma nova lista com os elementos **ordenados**.

🔹 `key=lambda nome: nome.lower()`
- Isso diz ao `sorted` que, para fins de ordenação, cada `nome` deve ser  
**convertido para minúsculas `(lower())` antes de comparar**.

- Assim, evita que  letras maiúsculas tenham **prioridade na ordem**
(por padrão, `'Z' < 'a'` no Python).

<br>

***

<br>

🔡 Comparação de strings:  

<br>

Sem o `key=...`, a ordenação padrão considera **valores Unicode**, e letras maiúsculas vêm antes das minúsculas.

Com o `key=lambda nome: nome.lower()`, você torna a ordenação **case-insensitive** (sem diferenciar maiúsculas e minúsculas).

<br>

```python

print(nomes_ordenados) # Saída: ['ana', 'Carlos', 'João']

```

Essa é a **ordem alfabética, ignorando diferença entre maiúsculas e minúscula** das 
letras  

<br>

***

<br>

✅ Resumo

| Parte | Explica |
| ------------------------- | -------------------------------------------------- |
| `sorted(lista)`           | Ordena os itens de uma lista                       |
| `key=lambda x: x.lower()` | Converte cada item para minúsculo antes de ordenar |
| `print(...)`              | Exibe o resultado final                            |