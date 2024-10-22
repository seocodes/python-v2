"""Desenvolva um sistema de gerenciamento de funcionários de uma empresa usando MySQL e Python.
Banco de Dados:
Tabela funcionarios com as colunas: id (INT, chave primária), nome (VARCHAR), cargo (VARCHAR).
Menu de Opções:
a)Cadastrar Funcionário: Insira um novo funcionário na tabela. Verifique se o funcionário já existe (baseado no id) antes de cadastrar.
b)Alterar Funcionário: Permita ao usuário alterar o cargo de um funcionário com base no id informado.
c)Excluir Funcionário: Exclua o funcionário com base no id fornecido.
d)Pesquisar Funcionário: Permita pesquisar por nome ou cargo. Exiba o total de funcionários cadastrados.
e)Sair: Encerre o programa."""

import mysql.connector

conexao_banco = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password = "1234",
    database = "empresa_2137"
)
cursor = conexao_banco.cursor()

#a
def create():
    id = int(input('Digite o ID do funcionário: '))

    #1 forma com o select
    comando_sql = f'SELECT * FROM funcionarios WHERE idfuncionarios = {id}'
    cursor.execute(comando_sql)
    dados_funcionario = cursor.fetchall()

    if len(dados_funcionario) <= 0:
        nome = input('Digite o nome do funcionário: ')
        cargo = input('Digite o cargo do funcionário: ')

        comando_sql = f'INSERT INTO funcionarios (idfuncionarios, nome, cargo) VALUES ({id}, "{nome}", "{cargo}")'
        cursor.execute(comando_sql)
        conexao_banco.commit()
    else:
        print('Funcionário já cadastrado')
        print(dados_funcionario)
        print(f'ID: {dados_funcionario[0][0]} NOME:  {dados_funcionario[0][1]}  CARGO: {dados_funcionario[0][2]}   ')

#b
def update():
    id = int(input('Digite o ID: '))

    comando_sql = f'SELECT * FROM funcionarios WHERE idfuncionarios = {id}'
    cursor.execute(comando_sql)
    dados_funcionario = cursor.fetchall()

    if len(dados_funcionario) > 0:
        print(f'ID: {dados_funcionario[0][0]}\nNome: {dados_funcionario[0][1]}\nCargo: {dados_funcionario[0][2]}')

        escolha = input('Alteração:\nN - nome\nC - cargo').upper()
        if escolha == 'N':
            nome = input('Nome: ')
            comando = f'UPDATE funcionarios SET nome = "{nome}" WHERE idfuncionarios = {id}'
            cursor.execute(comando)
            conexao_banco.commit()
        elif escolha == 'C':
            cargo = input('Cargo: ')
            comando = f'UPDATE funcionarios SET cargo = "{cargo}" WHERE idfuncionarios = {id}'
            cursor.execute(comando)
            conexao_banco.commit()
        else:
            print('Escolha inválida!')
    else:
        print('ID não localizado.')

#c
def delete():
    id = int(input('Digite o ID: '))

    comando_sql = f'SELECT * FROM funcionarios WHERE idfuncionarios = {id}'
    cursor.execute(comando_sql)
    dados_funcionario = cursor.fetchall()

    if len(dados_funcionario) > 0:
        print(f'ID: {dados_funcionario[0][0]}\nNome: {dados_funcionario[0][1]}\nCargo: {dados_funcionario[0][2]}')
    
        comando = f'DELETE FROM funcionarios WHERE idfuncionarios = {id}'
        cursor.execute(comando)
        conexao_banco.commit()
        print('funcionario deletado!')
    else:
        print('ID não localizado.')

def read():
    escolha = input('Escolha:\nN - nome\nC - cargo\nT - Todos\n:').upper()
    if escolha == 'N':
        nome = input('Digite o nome: ')
        comando = f'SELECT * FROM funcionarios WHERE nome like "%{nome}%"'
        cursor.execute(comando)
        dados = cursor.fetchall()

        if len(dados) <= 0:
            print('Nome não encontrado!')
        else:
            for i in dados:
                print(f'ID:{i[0]}   Nome: {i[1]} Cargo: {i[2]}')

    elif escolha == 'C':
        cargo = input('Digite o cargo: ')
        comando = f'SELECT * FROM funcionarios WHERE cargo like "%{cargo}%"'
        cursor.execute(comando)
        dados = cursor.fetchall()

        if len(dados) <= 0:
            print('cargo não encontrado!')
        else:
            for i in dados:
                print(f'ID:{i[0]}   Nome: {i[1]} Cargo: {i[2]}')

    elif escolha == 'T':
        comando = f'SELECT * FROM funcionarios'
        cursor.execute(comando)
        dados = cursor.fetchall()
        if len(dados) <= 0:
            print('nenhum funcionário encontrado!')
        else:
            for i in dados:
                print(f'ID:{i[0]}   Nome: {i[1]} Cargo: {i[2]}')
    else: 
        print('escolha inválida!')
    

while True:
    menu = input('-- Controle de cadastro --\n1 - Cadastrar\n2 - Alterar\n3 - Deletar\n4 - Pesquisar\n5 - Sair\n: ')

    if menu == '1':
        create()
    elif menu == '2':
        update()
    elif menu == '3':
        delete()
    elif menu == '4':
        read()
    elif menu == '5':
        print('Saindo do programa... ')
        break
    else:
        print('Opção inválida!')