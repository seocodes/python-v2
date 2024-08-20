def subt(a,b):
    print(a-b)


def add(a,b):
    print(a+b)


def mult(a,b):
    print(a*b)


def div(a,b):
    print(f'{a/b:.2f}')

print('''CALCULADORA
      1 - Adição
      2 - Subtração
      3 - Multiplicação
      4 - Divisão''')
op = int(input('Digite a opção desejada da calculadora: '))

if op == 1:
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    add(a,b)

elif op == 2:
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    subt(a,b)

elif op == 3: 
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    mult(a,b)

elif op == 4:
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    div(a,b)

else:
    print('Não funfa!')
