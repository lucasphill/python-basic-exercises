from random import randrange, randint
from time import sleep
from os import system

system('cls')
print('Vou pensar em um numero de 0 a 5. Tente adivinhar....')
n1=int(input('Digite seu palpite: '))
n2=randrange(0,6)
# n2=randint(0,6)

system('cls')
print('Você.')
sleep(0.5)
system('cls')
print('Você..')
sleep(0.5)
system('cls')
print('Você...')
sleep(0.5)

system('cls')
if n1 == n2:
    print(f'Você... ACERTOU! Eu pensei em {n2}!')
else:
    print(f'Você... ERROU! Eu pensei em {n2}! Tente novamente!')