receitas = []
despesas = []

while True:
    receita = float(input('Digite a receita desse mês: '))
    despesa = float(input('Digite a despesa desse mês: '))
    receitas.append(receita)
    despesas.append(despesa)
    op = input('Deseja continuar? ').strip().lower()
    if op == 's':
        continue
    else: 
        break
    
lucro_meses = list(map(lambda x,y: x-y , receitas,despesas))
lucro_medioAnual = sum(lucro_meses)/len(lucro_meses)
print(lucro_meses)

# S

