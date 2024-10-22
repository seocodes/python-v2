import mysql.connector

# Conexão com o banco de dados
conexao_banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="biblioteca"
)
cursor = conexao_banco.cursor()

# Função para cadastrar um livro
def create():
    id = int(input('Digite o ID do livro: '))
    titulo = input('Digite o título do livro: ')
    autor = input('Digite o autor do livro: ')

    # Verifica se o livro já existe
    comando_sql = f'SELECT * FROM livros WHERE id = {id} OR (titulo = "{titulo}" AND autor = "{autor}")'
    cursor.execute(comando_sql)
    dados_livro = cursor.fetchall()

    if len(dados_livro) <= 0:
        ano_publicacao = int(input('Digite o ano de publicação do livro: '))
        disponivel = True  # Livro é disponível por padrão

        comando_sql = f'INSERT INTO livros (id, titulo, autor, ano_publicacao, disponivel) VALUES ({id}, "{titulo}", "{autor}", {ano_publicacao}, {disponivel})'
        cursor.execute(comando_sql)
        conexao_banco.commit()
        print('Livro cadastrado com sucesso!')
    else:
        print('Livro já cadastrado ou ID já existe.')
        for livro in dados_livro:
            print(f'ID: {livro[0]} Título: {livro[1]} Autor: {livro[2]} Ano de Publicação: {livro[3]} Disponível: {livro[4]}')

# Função para alterar o status de disponibilidade de um livro
def update():
    id = int(input('Digite o ID do livro: '))

    comando_sql = f'SELECT * FROM livros WHERE id = {id}'
    cursor.execute(comando_sql)
    dados_livro = cursor.fetchall()

    if len(dados_livro) > 0:
        print(f'Título: {dados_livro[0][1]} Autor: {dados_livro[0][2]} Ano de Publicação: {dados_livro[0][3]} Disponível: {dados_livro[0][4]}')
        troca = not dados_livro[0][4]
        comando_sql = f'UPDATE livros SET disponivel = {troca} WHERE id = {id}'
        cursor.execute(comando_sql)
        conexao_banco.commit()
        print('Status de disponibilidade alterado!')
    else:
        print('ID não localizado.')

# Função para excluir um livro
def delete():
    id = int(input('Digite o ID do livro: '))

    comando_sql = f'SELECT * FROM livros WHERE id = {id}'
    cursor.execute(comando_sql)
    dados_livro = cursor.fetchall()

    if len(dados_livro) > 0:
        print(f'Título: {dados_livro[0][1]} Autor: {dados_livro[0][2]} Ano de Publicação: {dados_livro[0][3]} Disponível: {dados_livro[0][4]}')

        comando_sql = f'DELETE FROM livros WHERE id = {id}'
        cursor.execute(comando_sql)
        conexao_banco.commit()
        print('Livro excluído!')
    else:
        print('ID não localizado.')

# Função para pesquisar um livro
def read():
    escolha = input('Escolha:\nT - Título\nA - Autor\n:').upper()
    if escolha == 'T':
        titulo = input('Digite o título do livro: ')
        comando_sql = f'SELECT * FROM livros WHERE titulo LIKE "{titulo}"'
        cursor.execute(comando_sql)
        dados = cursor.fetchall()

        if len(dados) <= 0:
            print('Título não encontrado!')
        else:
            for i in dados:
                print(f'ID: {i[0]} Título: {i[1]} Autor: {i[2]} Ano de Publicação: {i[3]} Disponível: {i[4]}')

    elif escolha == 'A':
        autor = input('Digite o autor do livro: ')
        comando_sql = f'SELECT * FROM livros WHERE autor LIKE "%{autor}%"'
        cursor.execute(comando_sql)
        dados = cursor.fetchall()

        if len(dados) <= 0:
            print('Autor não encontrado!')
        else:
            for i in dados:
                print(f'ID: {i[0]}')