#Exercício 1 - a)

paises = ['Argentina', 'Brasil', 'Chile', 'Espanha', 'Estados Unidos', 'França', 'Itália', 'México', 'Portugal', 'Uruguai']

def posicao_do_pais(nome_do_pais):
    if nome_do_pais in paises:
        return paises.index(nome_do_pais) + 1
    else:
        return 'País não encontrado.'