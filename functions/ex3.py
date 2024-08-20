manager = []

def add_task():
    newTask = input('Nova tarefa: ').lower().title()
    manager.append(newTask)

def view():
    for tarefa in manager:
            print(tarefa)

def update():
    print('Tarefas:')
    for tarefa in manager:
            print(tarefa)
    change = int(input('Digite a numeração da tarefa qual deseja alterar: ')) - 1
    newName = input('Digite a nova tarefa: ').lower().title()
    manager[change] = newName

def delete():
    for tarefa in manager:
            print(tarefa)
    delete = input('Digite o item que quer deletar: ').lower().title()
    manager.remove(delete)
while True:
    print('''Gerenciador de Tarefas
      1 - Adicionar tarefa
      2 - Visualizar
      3 - Atualizar tarefa
      4 - Excluir tarefa
      5 - Sair''')
    op = int(input('Digite a operação escolhida: '))
    
    if op == 1:
        add_task()
    
    elif op == 2:
        view()
    
    elif op == 3:
        update()

    elif op == 4: 
        delete()

    elif op == 5:
        exit()
    
    else:
        print('Essa operação não existe.')