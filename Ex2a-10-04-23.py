#Exercício 2 - a)

from collections import deque

fila = deque(['João', 'Maria', 'Pedro', 'Julia'])

def remover_primeira_pessoa():
    if len(fila) > 0:
        pessoaRemovida = fila.popleft()
        print(f'A pessoa removida foi: {pessoaRemovida}')
    else:
        print('A fila está vazia.')

remover_primeira_pessoa()
print(fila)
