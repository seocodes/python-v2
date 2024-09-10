lucroMensal = []
receitas = []
despesas = []

while True:
    receita = float(input('Digite a receita desse mês: '))
    despesa = float(input('Digite as despesas desse mês: '))
    sair = input('Deseja sair? Digite S para sair: ')
    if sair.upper() == 'S':
        break
    receitas.append(receita)
    despesas.append(despesa)         
    lucro = list(map(lambda x,y: x-y , receitas ,despesas))   #ta errado eu acho


lucroAnual = sum(lucro)/len(lucro)
print(f'O lucro médio anual foi de: {lucroAnual}')