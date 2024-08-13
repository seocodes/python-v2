alunos = []


for i in range (3):
    aluno = {}
    name = input('Nome > ')
    media = float(input('Média anual > '))
    aluno['nome'] = name
    aluno['media'] = media
    alunos.append(aluno)

# Iterar sobre a lista de dicionários (alunos)
for aluno in alunos:
    if aluno['media'] >= 7:
        print(f"{aluno['nome']} foi aprovado!")
        # Note que aqui, "aluno" é o mesmo nome da variável do for, mas isso não interfere!
        # Isso ocorre porque "aluno" é um dicionário, e "aluno['nome']" está acessando um valor dentro desse dicionário
    else:
        print(f"{aluno['nome']} foi reprovado. :(")
