#Exercício 3 - b)

lista = []

def push(lista, numero):
    lista.append(numero)

def pop(lista):
    if len(lista) == 0:
        print("A pilha está vazia.")
    else:
        lista.pop()