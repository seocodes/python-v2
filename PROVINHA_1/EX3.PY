tarefas = {}
tarefaId = 1

def cadastro(tarefaId,tarefa):
    tarefas[tarefaId] = tarefa

def alterar(ident):
    if ident not in tarefas.keys():
        print('ID não encontrado.\n')
    else:
        novaTarefa = input('Digite a nova tarefa: ')
        tarefas[ident] = novaTarefa

def excluir(ident):
    if ident not in tarefas.keys():
        print('ID não encontrado.\n')
    else:
        tarefas.pop(ident)

def pesquisar():
    for chave,tarefa in tarefas.items():
        print(f'{chave}: {tarefa}')
    print(f'Ordem alfabética: {sorted(tarefas.values())} ')


def sair():
    print('ENCERRANDO...')
    exit()

while True:
    print('''1 - Cadastrar
          2 - Alterar
          3 - Excluir
          4 - Pesquisar
          5 - Sair''')
    op = int(input('Digite a opção desejada: '))
    match op:
        case 1:
            tarefa = input('Digite a tarefa: ')
            cadastro(tarefaId,tarefa)
            tarefaId += 1
        case 2:
            for chave,tarefa in tarefas.items():
                print(f'{chave}: {tarefa}')
            ident = int(input('Digite o ID no qual deseja mudar a tarefa: '))
            alterar(ident)
        case 3:
            for chave,tarefa in tarefas.items():
                print(f'{chave}: {tarefa}')
            ident = int(input('Digite o ID que deseja excluir: '))
            excluir(ident)
        case 4:
            pesquisar()
        case 5:
            sair()
        case __:
            print('Opção inválida.\n')
            continue
