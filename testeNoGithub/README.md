# Teste no Github

## Gerando arquivo
O programa `fiboFact.py` gera um arquivo `arquivo-teste.data` que tem em sua estrutura:
```
# fact Fib
n fact(n) fibo(n)
```
para todas as linhas com um n

## Testando arquivos
O programa `testador.py` verifica a existência, lê e compara dois arquivos pré-carregados: `arquivo-1.data` e `arquivo-2.data`.
Considerando o `arquivo-1.data` como o gabarito do esperado, verifica a existência do arquivo `arquivo-teste.data` e o compara com o nosso gabarito.
Caso os resultados não retornem o valor esperado, é retornada uma lista `linhas_erradas` que possui os inteiros cujos valores não conferem.