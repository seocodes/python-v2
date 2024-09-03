from functools import reduce

nums = []

while True:      #Fazendo uma com o input do usuário
    num = int(input('Digite um número: '))
    nums.append(num)
    op = input('Quer sair? Digite S para sair: ').upper()
    if op == 'S':
        break

produto = reduce(lambda x,y: x*y , nums)
print(f"O produto de todos os números inputados é de: {produto}")