nums = []

while True:      #Fazendo uma com o input do usuário pelo menos
    num = int(input('Digite um número: '))
    nums.append(num)
    op = input('Quer sair? Digite S para sair: ').upper()
    if op == 'S':
        break

double_oddNums = list(map(lambda x: x*2 if x%2 != 0 else x, nums))
print(double_oddNums)