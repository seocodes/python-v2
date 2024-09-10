def cadastro():
    funcionarios = []
    while True:
        nome = input("Digite o nome do funcionário (ou 'sair' para terminar): ")
        if nome.lower() == 'sair':
            break
        idade = float(input(f"Digite a idade, {nome}: "))
        cidade = input(f'Digite o nome da sua cidade: ').title()
        funcionario = {
            'Nome': nome,
            'Idade': idade,
            'Cidade': cidade
        }
        funcionarios.append(funcionario)
    return funcionarios

funcionarios = cadastro()

pessoaDeSP = list(filter(lambda x: x['Cidade'] == 'São Paulo' , funcionarios))
pessoaDeMaior = list(filter(lambda x: x['Idade'] >= 18 , funcionarios))

nomesECidade_PessoaDeMaior = list(map(lambda x: x['Nome'] + ', ' + x['Cidade'] , pessoaDeMaior))
nomesECidade_PessoaDeSP = list(map(lambda x: x['Nome'] + ', ' + x['Cidade'] , pessoaDeSP))


print("Pessoas cadastradas que são de São Paulo:")
for pessoa in nomesECidade_PessoaDeSP:
    print(pessoa)

print("Pessoas cadastradas que são maiores de idade:")
for pessoa in nomesECidade_PessoaDeMaior:
    print(pessoa)

