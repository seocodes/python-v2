aluno = {}
name = input('Nome > ')
media = float(input('Média anual > '))
aluno.update({name: media})

for i, y in aluno.items():
    if y >= 7:
        print(f'{name} foi aprovado!')
    else:
        print(f'{name} foi reprovado. :(')
