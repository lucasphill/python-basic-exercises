import random
import os

os.system('cls')
print('Eu pensei em um numero de 0 a 10! Tente adivinhar!')
n1 = int(input('Digite seu palpite:'))
tentativas=0
while True:
    tentativas+=1
    n2=random.randint(0,10)
    if n1 == n2:
        print(f'Você acertou! Eu pensei em {n2} e você também! Foram necessárias {tentativas} tentativas.')
        break
    else:
        print(f'Você errou! Eu pensei em {n2} e você {n1}. Tente novamente, vou pensar em outro numero...')
        n1=int(input('Digite seu palpite: '))