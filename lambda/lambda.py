# O nome lambda vem da matemática, mais precisamente da lambda calculus (cálculo lambda), 
# uma formalização da computação criada por Alonzo Church nos anos 1930. 
# Esse sistema matemático descreve como funções podem ser definidas e aplicadas — sem usar nomes.
# 
# - Por que Python usa esse nome?
# Python adota lambda como uma referência direta ao cálculo lambda, para indicar:
# - Que está criando uma função anônima (sem def e sem nome fixo).
# - Que essa função tem apenas uma expressão (simples, rápida, funcional).
# Sintaxe:
# lambda argumentos: expressão
# lambda: 2 + 3
#
# 📌 Explicando:
# - lambda x, y: x + y cria uma função anônima.
# 
# - soma = lambda x, y: x + y cria uma função anônima e atribui a variavel.
#
# - soma(4, 6) executa essa função.
#
# - print(...) mostra o resultado da execução.

soma = lambda x, y: x + y
print(soma(4, 6)) # Saída: 10

# Isso é o mesmo que escrever:
def soma(x, y):
 return x + y
print(soma(6, 12)) # Saída: 18

# 📌 Explicando:
# - (lambda: 2 + 3) cria uma função anônima.
#
# - () executa essa função imediatamente.
#
# - print(...) mostra o resultado da execução.

print((lambda: 2 + 3)()) # Saída: 5
 
# Onde o lambda é mais usado:
# Em funções como map(), filter() e sorted().
# 
# Para callbacks simples.
# 
# Quando não vale a pena criar uma função com def só para uma lógica curta.
# 
# Exemplo com sorted():

nomes = ['João', 'ana', 'Carlos']
nomes_ordenados = sorted(nomes, key=lambda nome: nome.lower())
print(nomes_ordenados) # Saída: ['ana', 'Carlos', 'João']
