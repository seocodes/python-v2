cars = {
    'marca': 'Toyota',
    'modelo': 'Onix',
    'ano': 1999
        }
print(type(cars))

#acessando dados do dicionário de forma padrão
print(cars['marca'])
print(cars['modelo'])
print(cars['ano'])

#acessando dados do dicionário com o método get()
print(cars.get('marca'))
print(cars.get('placa', 'Chave inexistente.'))

#acessando todas as chaves do meu dict
print(cars.keys())

#acessando todos os valores
print(cars.values())

#acessando tudinho
print(cars.items())

#adicionando ou alterando um valor:
cars['ano'] = 2015 #alterei

cars['placa'] = 'A94QS3' #criando
print(cars.items())

#deletando itens no dicionários 
old_placa = cars.pop('placa')  #no método .pop, é possível armazenar dentro de uma variável
print(old_placa)   

del cars['ano']  #não é possível armazenar dentro de uma variável
print(cars.items())

#verificando se um item está no dicionário
print('Onix' in cars.values())
print('tracker' in cars.values())

#iterando sobre um dicionário
for chaves in cars.keys():
    print(chaves)

for valores in cars.values():
    print(valores)

for keys, values in cars.items():  #pra printar fofinho um do lado do outro, e LEMBRA DE USAR O FOR IN
    print(f'{keys}: {values}')  #pois o for está trabalhando diretamente com o dicionário
                                #o dict é uma coleção de chaves e valores, e o keys, values está iterando sobre esses

#####################################################################

#dicionário dentro de uma lista
filmes = [
    {'name': 'O Homem de Ferro', 'genre': 'Ficção'},
    {'name': 'Minions', 'genre': 'Animação'},
    {'name': 'Se beber não case', 'genre': 'Comédia'}
]

print(filmes)
print(filmes[1].items()) #printa todo o segundo dict
print(filmes[0]['genre']) #printa ficção
print(filmes[2]['name'])  #output: se beber nao case
print(filmes[0].values()) #output: homem de ferro de ficção
print(filmes[2].keys()) #output: name e genre

for i in filmes:
    print(i)  #output: todos os dicionários, 1 por vez pois está iterando a cada loop

# filmes = [
#     {'name': 'O Homem de Ferro', 'genre': 'Ficção'},
#     {'name': 'Minions', 'genre': 'Animação'},
#     {'name': 'Se beber não case', 'genre': 'Comédia'}
# ]

for i in filmes:   #loop que itera sobre cada dicionário na lista
    for chave, valor in i.items():  #imprime a chave e o valor correspondente, separados por dois pontos
        print(f'{chave}: {valor}')
#aqui, usamos i.items() em vez de apenas i porque queremos iterar sobre as chaves e valores do dicionário
#se usássemos apenas i, estaríamos iterando sobre as chaves do dicionário, mas não teríamos acesso aos valores

##############################################################
#criando dicionários com inputs
filmes2 = {}

nome = input('Nome do filme > ')
genero = input('Genero > ')
filmes2.update({'name': nome})
filmes2.update({'genre': genero})
print(filmes2)

#criando uma lista com dicionários com inputs. LEGAL!
locadora = []
for x in range(3):
    name = input('Nome do filme > ')
    genre = input('Genero > ')
    filmes3 = {}               #crio o dict dentro do for para criar 3 dicts ao total
    filmes3.update({'name': name})    #se o dict tivesse fora, os updates iam substituir os itens, pois tem o mesmo nome de chave
    filmes3.update({'genre': genre})
    locadora.append(filmes3)

print(locadora)