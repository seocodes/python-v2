pessoa = {}

nome = input('Nome > ')
idade = int(input('Idade > '))
telefone = int(input('Telefone > '))
endereco = input('Endereço > ')
pessoa.update({'nome': nome})
pessoa.update({'idade': idade})
pessoa.update({'telefone': telefone})
pessoa.update({'endereco': endereco})

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')