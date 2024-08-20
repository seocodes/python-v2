contatos = []

def add_contact():
    newContact = input('Novo contato: ').lower().title()
    contatos.append(newContact)

def view():
    for contato in contatos:
            print(contato)

def update():
    print('Contatos: ')
    for contato in contatos:
            print(contato)
    change = int(input('Digite o número do contato a ser atualizado: ')) - 1
    newName = input('Digite o novo nome: ').lower().title()
    contatos[change] = newName

def delete():
    for contato in contatos:
            print(contato)
    delete = input('Digite o contato que quer deletar: ').lower().title()
    contatos.remove(delete)

while True: 
        print('''Gerenciador de Contatos
      1 - Adicionar contato
      2 - Visualizar
      3 - Atualizar contato
      4 - Excluir contato
      5 - Sair''')
        op = int(input('Digite a operação escolhida: '))
    
        if op == 1:
            add_contact()
    
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