import mysql.connector

conexao_banco = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'carros'
)

cursor = conexao_banco.cursor()
id_carro = 0

def cadastrarCarros():
    marca = input('Marca do carro: ').lower().capitalize()
    modelo =  input('Modelo do carro: ').lower().capitalize()
    ano = int(input('Ano: '))
    cor = input('Cor do carro: ').lower().capitalize()
    insertSQL = f'INSERT INTO carro(id,marca,modelo,ano,cor) VALUES {id_carro} , "{marca}" , "{modelo}", {ano} , "{cor}"'
    cursor.execute(insertSQL)
    conexao_banco.commit()
    id_carro += 1

def excluirCarros():
    viewSQL = f'SELECT * FROM carro'
    cursor.execute(viewSQL)
    global read_table 
    read_table = cursor.fetchall()
    for linha in read_table:
        print(f'ID: {linha[0]} - Marca: {linha[1]} - Modelo: {linha[2]} - Ano: {linha[3]} - Cor: {linha[4]}')
    idDelete = input('Digite o ID do carro que você quer excluir?\n').strip()
    deleteSQL = f'DELETE FROM carro WHERE id = {idDelete}'
    cursor.execute(deleteSQL)
    conexao_banco.commit()

def pesquisarCarros():
    print('''
          ID - Pesquisar por ID
          ANO - Pesquisar por ANO
          COR - Pesquisar por COR\n''')
    pesquisa = input('Qual campo você quer pesquisar?\n').strip().upper()
    if pesquisa == 'ID':
        idPesquisa = input('Digite o ID que quer procurar: ')
        for linha in read_table:
            if linha[0] == idPesquisa:
                print(f'ID: {linha[0]} - Marca: {linha[1]} - Modelo: {linha[2]} - Ano: {linha[3]} - Cor: {linha[4]}')
    if pesquisa == 'ANO':
        anoPesquisa = input('Digite o ano que quer procurar: ')
        for linha in read_table:
            if linha[3] == idPesquisa:
                print(f'ID: {linha[0]} - Marca: {linha[1]} - Modelo: {linha[2]} - Ano: {linha[3]} - Cor: {linha[4]}')
    if pesquisa == 'COR':
        corPesquisa = input('Digite a cor: ').lower().capitalize()
        for linha in read_table:
            if linha[4] == corPesquisa:
                print(f'ID: {linha[0]} - Marca: {linha[1]} - Modelo: {linha[2]} - Ano: {linha[3]} - Cor: {linha[4]}0')

def sair():
    exit()

while True:
    print('''MENU OPÇÕES
          C - Cadastrar carro
          E - Excluir carro 
          P - Pesquisar carro
          S - Sair\n''')
    opcao = input('Digite a opção que deseja: ').upper().strip()
    if opcao == 'C':
        cadastrarCarros()
    elif opcao == 'E':
        excluirCarros()
    elif opcao == 'P':
        pesquisarCarros()
    elif opcao == 'S':
        sair()

#TA COM PROBLEMA NO ID CARRO!!!