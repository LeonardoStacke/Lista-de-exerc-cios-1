#Exercício 3 - a)

paginasVisitadas = []

paginasVisitadas.append('www.instagram.com')
paginasVisitadas.append('www.twitter.com')
paginasVisitadas.append('www.netflix.com')

def remover_ultima_pagina_visitada(paginasVisitadas):
    ultima_pagina_visitada = paginasVisitadas.pop()
    return ultima_pagina_visitada

remover_ultima_pagina_visitada(paginasVisitadas)

print(paginasVisitadas)
