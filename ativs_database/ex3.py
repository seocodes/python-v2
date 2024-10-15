import mysql.connector

conexao_banco = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'inventario'
)

cursor = conexao_banco.cursor()

def cadastrar():
    viewSQL = f'SELECT * FROM produtos'
    cursor.execute(viewSQL)
    read = cursor.fetchall()
    id_prod = int(input('ID: '))
    nome = input('Digite o nome do produto: ')
    categoria = input('Digite o categoria: ')
    quantidade = int(input('Digite a quantidade: '))
    for linha in read:
        if linha[1] == nome or linha[2] == categoria:
            print('Já tá no banco seu noia.')
            return
    insertSQL = f'INSERT INTO produtos(id_produtos, nome, categoria, quantidade) VALUES ({id_prod}, "{nome}", "{categoria}", {quantidade})'
    cursor.execute(insertSQL)
    conexao_banco.commit()
    print("Produto cadastrado com sucesso!")

def alterar():
    viewSQL = f'SELECT * FROM produtos'
    cursor.execute(viewSQL)
    read = cursor.fetchall()
    for linha in read:
        print(f'ID: {linha[0]} - Nome: {linha[1]} -  Categoria: {linha[2]} - Quant.: {linha[3]}')
    id_change = int(input('Digite o ID que quer alterar: '))
    for linha in read:
        if linha[0] == id_change:
            nova_quant = input('Digite a nova quant: ')
            updateSQL = f'UPDATE produtos SET quantidade = "{nova_quant}" WHERE id_produtos = {id_change}'
            cursor.execute(updateSQL)
            conexao_banco.commit()
        else:
            print('O produto de ID {id_change} não foi encontrado.')

def excluir():
    viewSQL = f'SELECT * FROM produtos'
    cursor.execute(viewSQL)
    read = cursor.fetchall()
    for linha in read:
        print(f'ID: {linha[0]} - Nome: {linha[1]} -  Categoria: {linha[2]} - Quant.: {linha[3]}')
    id_delete = int(input('Digite o ID que quer excluir: '))
    for linha in read:
        if linha[0] == id_delete:
            deleteSQL = f'DELETE FROM produtos WHERE id_produtos = {id_delete}'
            cursor.execute(deleteSQL)
            conexao_banco.commit()
        else:
            print('Não encontrado...')

def pesquisar():
    viewSQL = f'SELECT * FROM produtos'
    cursor.execute(viewSQL)
    read = cursor.fetchall()
    for linha in read:
        print(f'ID: {linha[0]} - Nome: {linha[1]} -  Categoria: {linha[2]} - Quant.: {linha[3]}')

def sair():
    exit()

while True:
    print('''MENU OPÇÕES
          C - Cadastrar produtos
          A - Alterar produtos
          E - Excluir produtos 
          P - Pesquisar produtos
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

