empresa = {}
while True:
    print('''C - Cadastrar
          A - Alterar
          E - Excluir
          P - Pesquisar
          S - Sair''')
    op = (input('Opção > ')).upper()
    
    if op == 'C':
        newName = input('Novo funcionário > ').lower().title()
        newCargo = input('Cargo do novo funcionário > ').lower().title()
        empresa.update({newName: newCargo})
        print(empresa)
    if op == 'A':
        print(empresa)
        funcionario = input('Qual funcionário aquer alterar? ').lower().title()
        if funcionario in empresa:
            print("O que deseja alterar?")
            print("1 - Nome do funcionário")
            print("2 - Cargo do funcionário")
            escolha = int(input("Escolha uma opção: "))
            if escolha == 1:
                nome_subst = input('Qual o novo nome? ').lower().title()
                empresa[nome_subst] = empresa.pop(newName)   #Ao atribuir o resultado de pop() à chave nome_subst, 
                #estamos criando um novo item no dicionário com a chave nome_subst e valor igual
                #ao cargo do funcionário que foi removido com pop()
            elif escolha == 2:
                cargo_subst = input('Qual o nome do novo cargo > ').lower().title()
                empresa[funcionario] = cargo_subst  #Aqui é mais de boas, eu puxo o nome da pessoa
                #que botei lá em cima e atribuo um novo cargo (como esse nome já tá no dicionário,
                #só substitui o valor)
            print(empresa)
        else:
            print('Esse blud não existe.')
            continue 
    if op == 'E':
        del_check = input('Qual funcionário deseja excluir? ').lower().title()
        if del_check in empresa:
            empresa.pop(del_check)
        else:
            print('Não existe esse bosta!')
        print(empresa)
    if op == 'P':
        for chave, valor in empresa.items():
            print(f'{chave}: {valor}')
        print(f'A lista tem {len(empresa.items())} funcionários')
        print('Lista em ordem alfabética:\n')
        for nome in sorted(empresa.keys()):
            print(f'{nome}')
    if op == 'S':
        exit()
        