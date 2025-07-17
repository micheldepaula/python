## 🐍 `sorted.py

#python
# Lista de nomes com diferentes capitalizações
nomes = ['João', 'ana', 'Carlos']

# Ordenação ignorando maiúsculas/minúsculas
# A função lambda transforma cada nome para minúsculo antes da comparação
nomes_ordenados = sorted(nomes, key=lambda nome: nome.lower())

# Impressão da lista ordenada corretamente
print(nomes_ordenados) # Saída: ['ana', 'Carlos', 'João']

# ---------------------------------------------------------
# Explicação detalhada:
#
# sorted() retorna uma nova lista ordenada
# O argumento key=lambda nome: nome.lower() faz:
# - Cada nome virar minúsculo (ex: "João" → "joão")
# - Isso evita que letras maiúsculas fiquem "antes" na ordem
#
# Por padrão, 'Z' < 'a' em Python → ordenar sem .lower() pode dar resultados estranhos
#
# Resumo:
# - sorted(lista): ordena os itens
# - key=lambda x: x.lower(): ordena ignorando maiúsculas
#
# Dica:
# - Você também pode usar key=len para ordenar por tamanho
# - Ou key=lambda x: x.split()[-1] para ordenar por último nome
