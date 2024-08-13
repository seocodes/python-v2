words = ('acento', 'banana', 'arara', 'seila', 'augusto')
vogais = ('a', 'e', 'i', 'o', 'u')
for i in range (len(words)):
    print(f'Palavra: {words[i]}')
    print('Vogais: ')
    for caractere in words[i]:
        if caractere in vogais:
            print(caractere)