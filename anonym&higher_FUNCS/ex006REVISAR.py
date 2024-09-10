names = ['augusto', 'mariane', 'alice', 'pedro', 'jow']

nome_ordem = sorted(names, key=lambda x: len(x))   #quando usa key o parametro é na frente
print(nome_ordem)               #key define o que vai ordenar a lista

#dava pra fazer key=len 