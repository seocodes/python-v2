agenda = []
for i in range (5):
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu CPF: ')
    idade = int(input('Digite sua idade: '))
    telefone = int(input('Telefone: '))

    usuario = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'telefone': telefone }
    
    agenda.append(usuario)    # SABER SE PODE ISSO AQ OU TEM OUTRO JEITO DE FAZER


for i in range (len(agenda)):
    print(f'Agenda do usuário{i+1}:')
    print(f'Nome: {agenda[i]['nome']}')
    print(f'CPF: {agenda[i]['cpf']}')
    print(f'Idade: {agenda[i]['idade']}')
    print(f'Telefone: {agenda[i]['telefone']}\n')
