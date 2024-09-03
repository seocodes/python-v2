i = 0
prices = []

while i < 3:
    preco = float(input('Digite o preço do produto: '))
    prices.append(preco)
    i = i+1

def discount(precos):
    desconto = int(input('Porcentagem de desconto: '))
    listaComDesconto = list(map(lambda x: x-(x*(desconto/100)) , precos))
    return listaComDesconto

lista_desconto = discount(prices)
print(lista_desconto)






