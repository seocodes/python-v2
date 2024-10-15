import mysql.connector

conexao_banco = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'hotel'
)

cursor = conexao_banco.cursor()

def cadastrar():
    viewSQL = f'SELECT * FROM reservas'
    cursor.execute(viewSQL)
    read = cursor.fetchall()
    nome_cli = input('Nome do cliente: ').lower().capitalize()
    quarto = int(input('Quarto: '))
    data_checkin = input('Data check-in: ').replace(" ", "-")
    data_checkout = input('Data checkout: ').replace(" ", "-")
    for linha in read:
        if linha[3] == data_checkin or linha[4] ==  data_checkout:  #ESSE IF NAO FUNCIONA!
            print('Data de check-in ou checkout já está ocupada.')
            return
    insertSQL = f'INSERT INTO reservas(nome_cliente, quarto, data_checkin, data_checkout) VALUES ("{nome_cli}", {quarto}, "{data_checkin}", "{data_checkout}")'
    cursor.execute(insertSQL)
    conexao_banco.commit()

def alterar():
    viewSQL = f'SELECT * FROM reservas'
    cursor.execute(viewSQL)
    read = cursor.fetchall()
    for linha in read:
        print(f'ID: {linha[0]} - Nome cliente: {linha[1]} -  Quarto: {linha[2]} - Check-in: {linha[3]} - Checkout {linha[4]}')
    id_change = int(input('Digite o ID a ser mudado: '))
    for linha in read:
        if linha[0] == id_change:
            op = input('Mudar data de CHECKIN ou CHECKOUT').upper().strip()
            if op == 'CHECKIN':
                new_checkin = input('Novo check-in: ').replace(" ", "-")
                updateSQL = f'UPDATE reservas SET data_checkin = "{new_checkin}" WHERE id_reserva = {id_change}'
                cursor.execute(updateSQL)
                conexao_banco.commit()
            elif op == 'CHECKOUT':
                new_checkout = input('Novo checkout: ').replace(" ", "-")
                updateSQL = f'UPDATE reservas SET data_checkout = "{new_checkout}" WHERE id_reserva = {id_change}'
                cursor.execute(updateSQL)
                conexao_banco.commit()
            else:
                print('Inválido...')
        else:
            print('ID não existente.')

def excluir():
    viewSQL = f'SELECT * FROM reservas'
    cursor.execute(viewSQL)
    read = cursor.fetchall()
    for linha in read:
        print(f'ID: {linha[0]} - Nome cliente: {linha[1]} -  Quarto: {linha[2]} - Check-in: {linha[3]} - Checkout {linha[4]}')
    id_del = int(input('ID a ser deletado: '))
    for linha in read:
        if linha[0] == id_del:
            deleteSQL = f'DELETE FROM reservas WHERE id_reserva = {id_del}'
            cursor.execute(deleteSQL)
            conexao_banco.commit()
        else:
            print('ID não reconhecido.\n')

def pesquisar():
    viewSQL = f'SELECT * FROM reservas'
    cursor.execute(viewSQL)
    read = cursor.fetchall()
    op = input('Desja pesquisar por nome do cliente ou quarto? ').lower().strip()
    if op ==  'nomedocliente':
        nome = input('Nome do cliente a ser pesquisado: ').lower().capitalize()
        for linha in read:
            if linha[1] == nome:
                print(f'ID: {linha[0]} - Nome cliente: {linha[1]} -  Quarto: {linha[2]} - Check-in: {linha[3]} - Checkout {linha[4]}')
            else:
                print('Nome não encontrado...\n')
    elif op == 'quarto':
        quarto = int(input('Quarto a ser pesquisado: '))
        for linha in read:
            if linha[2] == quarto:
                print(f'ID: {linha[0]} - Nome cliente: {linha[1]} -  Quarto: {linha[2]} - Check-in: {linha[3]} - Checkout {linha[4]}')
            else:
                print('Quarto inexistente.\n')
    else:
        print('Inválido...')

def sair():
    exit()

while True:
    print('''MENU OPÇÕES
          C - Cadastrar reservas
          A - Alterar reservas
          E - Excluir reservas 
          P - Pesquisar reservas
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

