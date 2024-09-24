funcionarios = {}
funcionarioId = 1


while True:
    print('''1 - Cadastrar
          2 - Alterar
          3 - Excluir
          4 - Pesquisar
          5 - Sair''')
    op = int(input('Digite a opção desejada: '))
    if op == 1:
        dados = []
        nome = input('Digite o nome do funcionário: ')
        cargo = input('Digite o cargo do funcionário: ')
        dados.append(nome)
        dados.append(cargo)
        funcionarios[funcionarioId] = dados
        funcionarioId += 1

    elif op == 2:
        for identificacao,dados in funcionarios.items():
            print(f'{identificacao}: {dados}')
        change = int(input('Digite o ID da pessoa que quer ter as informações mudadas: '))
        if change in funcionarios.keys():
            opcao = int(input('Digite 1 para mudar o nome e 2 para mudar o cargo: '))
            if opcao == 1:
                newName = input('Digite o novo nome: ')
                funcionarios[change][0] = newName 
            elif opcao == 2:
                newJob = input('Digite o novo cargo: ')
                funcionarios[change][1] = newJob
            else:
                print('Opção inválida.')
                continue
        else:
            print('ID não encontrado.')
            continue
        

    elif op == 3:
        for identificacao,dados in funcionarios.items():
            print(f'{identificacao}: {dados}')
        delete = int(input('Digite o ID da pessoa que quer excluir do dicionário: '))
        if delete in funcionarios.keys():
            funcionarios.pop(delete)
        else:
            print('ID não encontrado.\n')
            continue

    elif op == 4:
        for identificacao,dados in funcionarios.items():
            print(f'{identificacao}: {dados}')     
        print(f'Ordem alfabética: {sorted(funcionarios.values())}')
        print(f'Total de funcionários cadastrados: {len(funcionarios)}')

    elif op == 5:
        print('ENCERRANDO O SISTEMA...')
        exit()
    
    else:
        print('Operação inválida.\n')