#Exercício 2 - b)

from collections import deque

fila = deque()

def remover_primeiro_numero():
    if len(fila) > 0:
        numeroRemovido = fila.popleft()
        print(f'O numero removido foi: {numeroRemovido}')
    else:
        print('A fila está vazia.')

def adicionar_ultimo_numero():
        numeroAdicionado = int()
        fila.append(numeroAdicionado)
        print(f'O numero adicionado foi: {numeroAdicionado}')

remover_primeiro_numero()
adicionar_ultimo_numero()
print(fila)

