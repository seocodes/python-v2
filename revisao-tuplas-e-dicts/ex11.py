pessoas = []
for i in range(3):
    nome = input('Nome > ')
    idade = int(input('Idade > '))
    cpf = input('CPF > ')
    pessoa = {
        'nome': nome,
        'idade': idade,
        'cpf': cpf
    }
    pessoas.append(pessoa)
for dicionario in pessoas:
    if dicionario['idade'] < 18:
        print(f'{dicionario['nome']} é menor de idade!')    #pega o nome de cada 1 pois 
                                            #'dicionario' está iterando a cada loop, o mesmo serve para
                                            #os outros usos do dicionario

