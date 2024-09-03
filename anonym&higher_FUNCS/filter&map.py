#### FUNÇÃO FILTER ####
numbers = [4,5,8,9,10]

even_numbers = list(filter(lambda x: x%2 == 0 , numbers))  #Função filter requer uma função e um conjunto de dados, separados por VÍRGULA
#Numbers é como se fosse o parâmetro/valor dado à função lambda (x), e os itens da lista vão sendo iterados e se tornando x
#O conjunto de dados é FILTRADO PELA FUNÇÃO, ou seja, TEM QUE TER UMA CONDIÇÃO/VERIFICAÇÃO (sem o if), e o que resultar True dessa função de verificar, é adicionado no filter
print(even_numbers)

##########################################################################################

names = ['augusto', 'mariane', 'alice', 'pedro', 'jow']

nomes_letra_a = list(filter(lambda x: 'a' in x, names))
print(nomes_letra_a)
#a função lambda pode ser pensada como:
# def tem_a(x):
#     return 'a' in x     sendo x a lista numbers

##########################################################################################

#### FUNÇÃO MAP ####
numbers = [4,5,8,9,10]
squared = list(map(lambda x: x**2, numbers))   #APLICA uma função à um conjunto de dados
#Lembrando que numbers é o que vai ser iterado e aplicado a função
print(squared)

names = ['augusto', 'mariane', 'alice', 'pedro', 'jow']
capitalized = list(map(lambda x: x.capitalize(), names))   #names é iterado e vai se tornando x, e capitalizado
#Todos são capitalizados, pois se trata de uma função map
print(capitalized)

lengthPalavra = list(map(lambda x: len(x), names))
print(lengthPalavra)

##########################################################################################

#### FUNÇÃO REDUCE ####
from functools import reduce

numbers = [5,7,12,9,1,22]

sum_num = reduce(lambda x,y: x+y , numbers)     #Reduce retorna apenas UM VALOR, não precisa transformar em lista
#A função reduce() engloba todos os elementos do conjunto e faz alguma função, retornando apenas um valor
print(sum_num)

min_num = reduce(lambda x,y: x if x<y else y, numbers)   #Retorna x se (...), se não, y
print(min_num)