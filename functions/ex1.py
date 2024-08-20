def calcularCirculo(raio):
    return raio**2*3.14


def calcularTriangulo(base,altura):
    return (base*altura)/2

                                                    #ao inves de return, tu pode só voltar um print e chamar a função com os parametros la embaixo
def calcularRetangulo(base,altura):
    return base*altura


print('''Menu de OPÇÕES:
      1 - Círculo
      2 - Triângulo
      3 - Retângulo\n''')
op = int(input('Digite a opção desejada > '))

if op == 1:
    raio = float(input('Digite o raio do círculo: '))
    resultado = calcularCirculo(raio)
    print(f'A área do círculo é: {resultado}')

elif op == 2:
    base = float(input('Digite a base do triângulo: '))
    altura = float(input('Digite a altura do triângulo: '))
    resultado = calcularTriangulo(base,altura)
    print(f'A área do triângulo é: {resultado}')

elif op == 3:
        base = float(input('Digite a base do retângulo: '))
        altura = float(input('Digite a altura do retângulo: '))
        resultado = calcularRetangulo(base,altura)
        print(f'A área do retângulo é: {resultado}')

else:
     print('Opção não disponível.')