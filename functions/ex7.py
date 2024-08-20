import math

def teoremaPitagoras(co,ca):
    h = co**2+ca**2
    resultado = math.sqrt(h)
    return resultado

a = float(input('CATETO 1 > '))
b = float(input('CATETO 2 > '))

hipotenusa = teoremaPitagoras(a,b)
print(f'A hipotenusa é: {hipotenusa:.2f}')
