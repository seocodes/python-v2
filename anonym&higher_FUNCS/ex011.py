palavras = ['augusto', 'maçã', 'ogro', 'melancia', 'a', 'b', 'c']
palavras_maisq3 = list(filter(lambda x: len(x) >= 3, palavras))

print(palavras_maisq3)
for palavra in palavras_maisq3:
    print(len(palavra))

