import mysql.connector

conexao_banco = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'vendas'
)

cursor = conexao_banco.cursor()

# CRUD
# CREATE - READ - UPDATE - DELETE

#CREATE
# nome = input('Digite o nome do produto: ')
# valor = float(input('Digite o valor do produto: '))
# comando_sql = f'INSERT INTO produtos(nome_produto , valor_produto) VALUES ("{nome}" , {valor})' #Lembra do bagulho de aspas simples e aspas duplas
# cursor.execute(comando_sql)
# conexao_banco.commit()

#READ
comando_sql4 = f'SELECT * FROM produtos'
cursor.execute(comando_sql4)
read_table = cursor.fetchall()
print(read_table)
print(read_table[1][1])  #Printa o nome do produto da segunda linha
print(read_table[0][0])  #Printa o ID do produto da primeira linha
print(read_table[2][2])  #Printa o valor do produto da terceira linha, pois [2] é para entrar na terceira linha, e [2] para ir nos valores

for linha in read_table:   #vai iterando em cada linha/tupla dentro daquela lista (read_table) com todos os produtos
    print(f'ID: {linha[0]:<5} Nome: {linha[1]:<10} Valor: {linha[2]:<10}')  #O linha[0] pega o ID da linha do loop, e vai indo assim

#UPDATE
id_change = int(input('Digite o ID do produto a ser mudado:  '))

for linha in read_table:
    if id_change == linha[0]:
        opcao = input('Digite N para trocar o nome e V para trocar o valor: ').upper().strip()
        if opcao == 'N':
            novo_nome = input('Digite o novo nome: ').lower().capitalize()
            comando_sql2 = f'UPDATE produtos SET nome_produto = "{novo_nome}" WHERE id_produtos = {id_change}'
            cursor.execute(comando_sql2)
            conexao_banco.commit()
        elif  opcao == 'V':
            novo_valor = float(input('Digite o novo valor: '))
            comando_sql9 = f'UPDATE produtos SET valor_produto = {novo_valor} WHERE id_produtos = {id_change}'
            cursor.execute(comando_sql9)
            conexao_banco.commit()
        else:
            print('Opção inválida')

# #DELETE
# id_delete = int(input('Digite o ID que quer deletar: '))
# comando_sql3 = f'DELETE FROM produtos  WHERE id_produtos = "{id_delete}"'
# cursor.execute(comando_sql3)
# conexao_banco.commit()

