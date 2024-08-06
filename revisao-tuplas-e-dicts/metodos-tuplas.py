#sintaxe de uma tupla (imutável)
my_tuple = (1, 1.6, 'Augusto', True)
my_tuple2 = (7, 'Ni-', 3.14, False)
print(type(my_tuple))

#acessando valores de uma tupla
#acessando o primeiro valor:
print(my_tuple[0])
#acessando ultimo valor:
print(my_tuple[-1]) #podia ser simplesmente o [3]

#acessando somente os 2 primeiros valores de uma tupla
#ou chamamos de FATIAMENTO DE TUPLA
print(my_tuple[:2]) #acessa o index 0 e 1 (antes do 2)

print(my_tuple[-2:]) #acessa o index do -1 e -2

print(my_tuple[:-2]) #é o mesmo que acessar o index 0 e 1, pois acessa o index do -2 pra frente, ou seja, (1 e 1.6)
#significa "comece do final da tupla e vá até o índice especificado". começa no índice -2 (o segundo último elemento) e vai até o final da tupla

#concatenação de tuplas:
new_tuple = my_tuple + my_tuple2
print(new_tuple)

#replicar tupla:
replicated_tuple = my_tuple*2
print(replicated_tuple)

#valor minimo e maximo de tuplas
nums_tuple = (1, 3.14, 99, 56, 4.2, 3)
max_value = max(nums_tuple)
min_value = min(nums_tuple)    #obs: não precisava declarar a variável se for printar assim apenas uma vez, apenas se for reutilizar
    #mas atribuir à variaveis é uma boa pratica
print(min_value)
print(max_value)

#percorrer a tupla
for i in my_tuple:  #i = iteração (i é o valor atual que está sendo processado). a cada iteração, i assume o valor do próximo item da tupla
    print(f'Itens da minha tupla: {i}')  #printa todos por vez até percorrer todos itens
    # imprime o valor atual de i

    #o mesmo que falar   for x in range(4)
for x in range (len(my_tuple)):                #for i in my_tuple trabalha com os valores da tupla e imprime os itens da tupla.
    print(x)                                    #for x in range(len(my_tuple)) trabalha com uma sequência de números e imprime os números da sequência.
#Se você quiser imprimir os itens da tupla usando o range(), pode fazer isso usando o índice da tupla: print(my_tuple[x]).


#desempactamento/unpacking de tuplas - IMPORTANTE
coordinate_tuple = (5,7)
var_x , var_y = coordinate_tuple
print(var_x)
print(var_y)

age_tuple = (10, 18, 56)
age1, age2, age3 = age_tuple
print(age1, age2, age3)

#função enumerate()
fruits_tuple = ('maçã', 'banana', 'kiwi', 'uva', 'melancia')
for index, fruit in enumerate(fruits_tuple):    #tem umas explicação daora no meu notion!
    print(f'{index}: {fruit}')
