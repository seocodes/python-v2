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

salarioMaiorQ3000 = {nome: salario for nome, salario in dict1.items() if salario > 3000}
aumento = {nome: salario + (salario * (porc_aumento / 100)) for nome, salario in salarioMaiorQ3000.items()}

for nome, novoSalario in aumento.items():
    dict1[nome] = novoSalario

print(dict1)