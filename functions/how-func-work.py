#SEM PARÂMETROS
def somar(a,b):   #Função com parâmetros (há coisas dentro do parênteses).
    return a+b
print(somar(3,4))   

def inicio():
    print('Hello, FDP!')
inicio()          #Executa a função inicio.

def cores():
    cor1 = input('Digite uma cor: ')
    cor2 = input('Digite outra cor: ')
    print(f'As cores escolhidas foram: {cor1} e {cor2}')
cores()       #Executa a função cores.

#PARÂMETRO
def nome(name):
    print(f'Seja bem-vindo {name}!')
nome('Augusto')  #Coloca o parâmetro como Augusto, por isso vai printar com meu nome

#MÚLTIPLOS PARÂMETROS
def somar(a,b):   
    soma = a+b
    print(f'A soma de {a} e {b} é: {soma}')
somar(3,4)


#PARÂMETROS VARIÁVEIS (QUANTOS QUISER) QUE VIRAM TUPLAS/*args
def soma(*args):  #O * na frente faz ser um tamanho variado
    somar = 0   #Declarando a var pra não dar pau
    for i in args:   #When you call a function with multiple arguments, 
#like my_function(1, 2, 3, 4, 5), Python collects all these arguments into a single tuple called args
        somar += i 
    print(f'O resultado da soma foi de {somar}')
soma(1,2,3,4,5)

def nomes(*names):    #lembrando que NAMES vira uma tupla com os valores/parametros atribuidos
    for i in range(len(names)):
        print(f'Nome: {names[i]}')
nomes('Oi', 'VOLTAPRACADOG\n')

#PARÂMETROS VARIÁVEIS QUE VIRAM DICIONÁRIOS/**kwargs
def pessoas(**dados):
    for chave,valor in dados.items():
        print(f'{chave}: {valor}')
pessoas(nome = 'Augusto', idade = 18, altura = '190cm')

#USANDO RETURN
def soma(a,b):
    soma = a+b
    return soma   #Salva o valor de soma

print(somar(2,5))   #Não posso printar 'soma', por exemplo, pois ela tá dentro da função
#e não pode ser executada a não ser que eu chame a função

def numeroPar(num):
    if num%2 == 0:
        return True
    else:
        return False
numero = int(input('Digite um número: '))
print(numeroPar(numero))

######################################################

def calculo(n1,n2):
    soma = n1+n2
    media = soma/2
    return soma, media      #QUANDO UMA FUNÇÃO RETORNA 2 VALORES, RETORNA COMO TUPLA

resultado = calculo(10,9)
soma, media = resultado         #DESEMPACOTAMENTO

print(f'A soma das notas é: {soma}, e a média: {media}.')

######

def cadastro():
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    endereco = input('Endereço: ')
    return nome, idade, endereco   #volta como tupla pois o return retorna mais de 1 coisa

    nome, idade, endereco = cadastro()  #Não preciso associar a uma variável pois os INPUTS já estão lá dentro
    #logo, a função já retorna os valores assim que roda o programa 

#ACESSANDO VARIÁVEIS DE UMA FUNÇÃO FORA DELA:
def somar(a,b):
    global soma   #Deixa acessar a variável fora do escopo da função
    soma = a+b
    return soma

somar(6,7)
print(soma)


################### BIBLIOTECAS #############################
from datetime import *

data_atual = date.today()

ano = data_atual.year
print(ano)

mes = data_atual.month
print(mes)
    

