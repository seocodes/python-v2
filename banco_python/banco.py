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

#UPDATE
id_change = int(input('Digite o ID do produto a ser mudado:  '))
nove_nome = input('Digite o novo nome do produto: ')

comando_sql2 = f'UPDATE produtos SET nome_produto = "{nove_nome}" WHERE id_produtos = {id_change}'
cursor.execute(comando_sql2)
conexao_banco.commit()
