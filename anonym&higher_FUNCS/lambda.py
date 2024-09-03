print((lambda x: x**2) (8))  #Passa o valor 8 como x.
#Depois dos dois pontos é o que vai ser executado por essa função anônima


def  quadrado(x):
    return x**2       #Forma convencional de se fazer, menos prática de se fazer se não for chamada muitas vezes
print(quadrado(8))


quadradoLambda = (lambda x: x**2) (8)    #Atribuindo a função anônima à uma variável
print(quadradoLambda)


print((lambda x,y: x**y) (5,3))  #Função lambda com 2 valores sendo utilizados

###################################################################################################################

lista = [
    lambda x: x*2,
    lambda x: x**2,    #Lista com funções anônimas, podem ser chamadas e usadas por meio de um for, pois itera sobre os itens da lista
    lambda x: x**3
]

num = float(input("Digite um número: "))

for i in lista:
    print(i(num))     #Nesse caso, o "i" são as funções lambda (vão sendo iteradas), assumem o valor inputado e são printadas

###################################################################################################################

name_Age = lambda x,y: print(f"{x} possui {y} anos.\n")
name_Age("Augusto", 18)    #Não precisa printar pois já printa dentro da função

name = input("Digite seu nome: ")
age = int(input('Digite sua idade: '))
name_Age(name,age)    #Atribuindo valores, os valores são os inputs do usuário

###################################################################################################################

lambda x,y: print(f"{x} possui {y} anos.\n") ((input('Digite seu nome: ')),(int(input('Digite sua idade'))))  
#Nesse caso, os inputs são os valores que são atribuídos, assim como mostrado no início desse aruivo, onde podemos atribuir itens se *botarmos entre parênteses*