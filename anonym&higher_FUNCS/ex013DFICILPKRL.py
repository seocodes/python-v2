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

salarioMaiorQ3000 = dict(filter(lambda x: x[1] > 3000, dict1.items()))  #Sim, isso retorna um dicionário com todos os nomes
#só retorna os dicionários que tem > 3000 (ainda em forma de dicionário pq usei o dict)

aumento = dict(map(lambda x: (x[0], x[1] + (x[1] * (porc_aumento / 100))), salarioMaiorQ3000.items()))
#a "," depois do x[0] é pra separar a chave do valor, não usar ":" em dict lambdas

for nome, novoSalario in aumento.items():
    dict1[nome] = novoSalario

print(dict1)