palavras = ['augusto', 'maçã', 'ogro', 'melancia', 'a', 'b', 'c']
palavras_maisq3 = list(filter(lambda x: len(x) > 3, palavras))
palavras_len =  list(map(lambda x: len(x) , palavras_maisq3))

for palavra in palavras_maisq3:
    print(palavra)
print(palavras_len)
