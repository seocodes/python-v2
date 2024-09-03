palavras = ['augusto', 'maçã', 'ogro', 'melancia']
vogais = 'aeiou'

ordenarPorVogal = lambda palavra: sum(1 for letra in palavra if letra in vogais)
nova_lista = sorted(palavras, key=ordenarPorVogal)
print(f'Lista de palavras de acrdo com o número de vogais (menor p/ maior): {nova_lista}')