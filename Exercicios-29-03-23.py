comando = 0
while comando != 4:
    comando = int(input('\n-=-=-=-=-=-=-=-=-=-\n1 - Registrar nota;\n2 - Registrar nota de exame;\n3 - Resultado final;\n4 - Sair.\n-=-=-=-=-=-=-=-=-=-\n'))

    if comando == 1:
        nome = str(input('Nome do aluno: '))
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        nota3 = float(input('Nota 3: '))

        with open("notas.txt", "a") as arquivo:
            arquivo.write(f'{nome},{nota1},{nota2},{nota3}\n')

        media = float((nota1+nota2+nota3)/3)
        if media >= 7:
            with open("aprovados.txt", "a") as arquivo:
                arquivo.write(f'{nome},{media},Aprovado\n')
        if (media >= 5) and (media < 7):
            with open("exame.txt", "a") as arquivo:
                nota_exame = float(0)
                arquivo.write(f'{nome},{media},{nota_exame},Exame\n')
        if media < 5:
            with open("reprovados.txt", "a") as arquivo:
                arquivo.write(f'{nome},{media},Reprovado\n')
    if comando == 2:
        while True:
            nomeAluno = str(input('Nome do aluno: '))
            with open("exame.txt", "r") as arquivo:
                conteudo = arquivo.read()
                if nomeAluno in conteudo:
                    break
                else:
                    print('Aluno não encontrado.')


        notaExame = float(input('Nota no exame: '))
        registros = []
        with open("exame.txt", "r") as arquivo:
            for linha in arquivo:
                nome, media, notaexame,situacao = linha.split(",")
                registro = {"nome": nome, "media": float(media), "notaexame": float(notaexame),"situacao": situacao}
                registros.append(registro)
            for registro in registros:
                if nomeAluno == nome:
                    registro["notaexame"] = notaExame
                    mediaFinal = float((notaExame + registro["media"])/2)
                    if mediaFinal >= 5:
                        registro["situacao"] = "Aprovado após exame"
                        with open("aprovados.txt", "a") as arquivo:
                            arquivo.write(f'{registro["nome"]},{mediaFinal},{registro["situacao"]}\n')
                    else:
                        registro["situacao"] = "Reprovado após exame"
                        with open("reprovados.txt", "a") as arquivo:
                            arquivo.write(f'{registro["nome"]},{mediaFinal},{registro["situacao"]}\n')
    if comando == 3:
        print('\n\033[32mAlunos aprovados:\033[0m\n')
        with open("aprovados.txt", "r") as arquivo:
            for linha in arquivo:
                nome, media, situacao = linha.split(",")
                mediaArred = float(round(float(media), 2))
                print(f'Nome: {nome} | Média: {mediaArred}' )
        print("\n\033[31mAlunos reprovados:\033[0m\n")
        with open("reprovados.txt", "r") as arquivo:
            for linha in arquivo:
                nome, media, situacao = linha.split(",")
                mediaArred = float(round(float(media),2))
                print(f'Nome: {nome} | Média: {mediaArred}')


