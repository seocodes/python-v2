import mysql.connector

conexao_banco = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'funcionarios'
)

cursor = conexao_banco.cursor()

def cadastrar():
    id_funcionario = int(input('Digite o ID do funcionário: '))
    nome = input('Digite o nome do funcionário: ')
    cargo = input('Digite o cargo: ')
    insertSQL = f'INSERT INTO funcionarios(id_func , nome , cargo) VALUES ({id_funcionario} , "{nome}"  , "{cargo}")'
    cursor.execute(insertSQL)
    conexao_banco.commit()

def alterar():
    viewSQL = f'SELECT * FROM funcionarios'
    cursor.execute(viewSQL)
    read = cursor.fetchall()
    for linha in read:
        print(f'ID: {linha[0]} - Nome: {linha[1]} -  Cargo: {linha[2]}')
    id_change = int(input('Digite o ID que quer alterar: '))
    for linha in read:
        if linha[0] == id_change:
            novo_Cargo = input('Digite o novo cargo: ')
            updateSQL = f'UPDATE funcionarios SET cargo = "{novo_Cargo}" WHERE id_func = {id_change}'
            cursor.execute(updateSQL)
            conexao_banco.commit()
        else:
            print('O funcionário de ID {id_change} não foi encontrado.')

def excluir():
    viewSQL = f'SELECT * FROM funcionarios'
    cursor.execute(viewSQL)
    read = cursor.fetchall()
    for linha in read:
        print(f'ID: {linha[0]} - Nome: {linha[1]} -  Cargo: {linha[2]}')
    id_delete = int(input('Digite o ID que quer excluir: '))
    for linha in read:
        if linha[0] == id_delete:
            deleteSQL = f'DELETE FROM funcionarios WHERE id_func = {id_delete}'
            cursor.execute(deleteSQL)
            conexao_banco.commit()
        else:
            print('Não encontrado...')

def pesquisar():
    viewSQL = f'SELECT * FROM funcionarios'
    cursor.execute(viewSQL)
    read = cursor.fetchall()
    op = input('Desja pesquisar por nome ou cargo? ').lower().strip()
    if op == 'nome':
        nome = input('Digite o nome do funcionário: ')
        for linha in read:
            if linha[1] ==  nome:
                print(f'ID: {linha[0]} - Nome: {linha[1]} -  Cargo: {linha[2]}')
            else:
                print('Nome não está no banco de dados.')
    elif op ==  'cargo':
        cargo = input('Digite o cargo do funcionário: ')
        for linha in read:
            if linha[2] == cargo:
                print(f'ID: {linha[0]} - Nome: {linha[1]} -  Cargo: {linha[2]}')
            else:
                print('Não encontrado.')
    else:
        print('Opção inválida.')

    
def sair():
    exit()

while True:
    print('''MENU OPÇÕES
          C - Cadastrar funcionário
          A - Alterar funcionário
          E - Excluir funcionário 
          P - Pesquisar funcionário
          S - Sair\n''')
    opcao = input('Digite a opção que deseja: ').upper().strip()
    if opcao == 'C':
        cadastrar()
    elif opcao == 'A':
        alterar()
    elif opcao == 'E':
        excluir()
    elif opcao == 'P':
        pesquisar()
    elif opcao == 'S':
        sair()

