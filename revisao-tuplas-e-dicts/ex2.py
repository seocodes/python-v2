tabela = ("Palmeiras",
    "Flamengo",
    "Internacional",
    "Grêmio",
    "São Paulo",
    "Atlético Mineiro",
    "Athletico Paranaense",
    "Cruzeiro",
    "Botafogo",
    "Santos",
    "Bahia",
    "Fluminense",
    "Corinthians",
    "Bragantino",
    "Ceará",
    "Vasco da Gama",
    "Sport",
    "Vitória",
    "Paraná",
    "América Mineiro")

print(f'5 primeiros colocados são: {tabela[:5]}')
print(f'4 últimos da tabela: {tabela[-4:]}')
print(f'Ordem alfabética: {sorted(tabela)}')
if 'Chapecoense' in tabela:
    print(f'Chapecoense está na posição: {tabela.index('Chapecoense')+1}')
