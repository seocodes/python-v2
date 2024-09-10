def salariosFuncionarios():
        salarios_e_funcionarios = {}
        while True:
            nome = input("Digite o nome do funcionário (ou 'sair' para terminar): ")
            if nome.lower() == 'sair':
                break
            salario = float(input(f"Digite o salário para {nome}: "))
            salarios_e_funcionarios[nome] = salario
        return salarios_e_funcionarios

dict1 = salariosFuncionarios()
porc_aumento = int(input('Digite a porcentagem do aumento: '))

salarioMaiorQ3000 = dict(filter(lambda x: x[1] > 3000, dict1.items()))
aumento = dict(map(lambda x: (x[0], x[1] + (x[1] * (porc_aumento / 100))), salarioMaiorQ3000.items()))

for nome, novoSalario in aumento.items():
    dict1[nome] = novoSalario

print(dict1)