import random

def generateRandom():
    num = random.randint(1,100)
    return num

while True:
    guess = int(input('Adivinhe o número secreto (1 a 100): '))
    numero_secreto = generateRandom()
    if guess == numero_secreto:
        print('BOA SEU BOSTA')
        break
    else:
        print('Tente novamente!\n')