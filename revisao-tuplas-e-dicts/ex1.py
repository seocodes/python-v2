tupla = ("zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    num = int(input('Digite um número a ser mostrado de 0 a 20\n'))
    if num >= 0 and num <= 10:
        for i in range (len(tupla)):
            if i == num:
                print(tupla[i].title())
    else:
        break