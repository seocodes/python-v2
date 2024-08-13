tupla = ('banana', 5.00, 'maçã', 4.00, 'leite', 8.00, 'aaaa', 9.00)
print('------------------\n')
print('Preços:\n')
for i in range (1, len(tupla), 2):  #primeiro numero é onde começa, depois é a length do for
    print(f'{tupla[i]}')            #e o ultimo numero é quantos indices ele pula a cada iteração
print('------------------')