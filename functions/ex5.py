import datetime as dt

def selectPlace():
    dest = input('Para onde quer viajar? ')
    return dest

def selectDate():
    dia = int(input('Dia > '))
    mes = int(input('Mês > '))
    ano = int(input('Ano > '))
    return ano, mes, dia

def selectPass():
    passageiros = int(input('Digite o número de passageiros: '))
    return passageiros

def verify():
    print(destino)
    print(data_viagem)
    print(passageiros)

while True:
    print('''SISTEMA DE RESERVAS
      1 - Selecionar destino
      2 - Selecionar data do vôo
      3 - Número de passageiros
      4 - Verificar (use somente ao colocar todos os dados)
      5 - Sair''')
    op = int(input('>> '))
    if op == 1:
        destino = selectPlace()
    elif op == 2:
        data = selectDate()
        ano, mes, dia = data
        data_viagem = dt.date(ano,mes,dia)
    elif op == 3:
        passageiros = selectPass()
    elif op == 4:
        verify()
    elif op == 5:
        exit()
    else:
        print('Operação não encontrada.')
