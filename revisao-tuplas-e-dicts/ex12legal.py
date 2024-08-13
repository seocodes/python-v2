Carros = { 1 : [ "fiat", "palio", "ano 2022", "prata"], 
        2 : [ "ford", "fiesta", "ano 2023", "branca"],
        3 : [ "honda", "fit", "ano 2024", "preta"]
            }
while True:
    print('''1 - Cadastrar
          2 - Excluir
          3 - Pesquisar
          4 - Sair''')
    op = int(input('Opção > '))
    if op == 1:
        cod_check = int(input('Qual o código que deseja inserir? '))
        if cod_check in Carros:
            print('Já existe vlw flw')
            continue
        else:
            newCar = []
            marca = input('Marca: ')
            modelo = input('Modelo: ')
            ano = input('Ano: ')
            cor = input('Cor: ')
            newCar.append(marca)
            newCar.append(modelo)
            newCar.append(ano)
            newCar.append(cor)
            Carros.update({cod_check: newCar})
            print(Carros)
    if op == 2:
        del_check = int(input('Qual o código do carro que deseja deletar? '))
        if del_check in Carros:
            Carros.pop(del_check)
            print(Carros)
        else:
            print('Código inexistente!')
            continue
    if op == 3:
        check = int(input('Código do carro que quer pesquisar: '))
        if check in Carros:
            print(Carros[check])
        else:
            print('Não existe noob.')
            continue
    if op == 4:
        exit()


