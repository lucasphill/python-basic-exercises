import random
from time import sleep
from os import system

system('cls')
print('''Suas opções:
      
[0] - Pedra
[1] - Papel
[2] - Tesoura
''')

opcoes=['pedra','papel','tesoura']

while True:
    opcao=int(input('Selecione uma opção: '))
    if 0 < opcao < 3:
        break

user_op=opcoes[opcao]
pc_op=opcoes[random.randrange(0,2)]

system('cls')
print('Jooo...')
sleep(0.5)
system('cls')
print('Jooo...keen')
sleep(0.5)
system('cls')
print('Jooo...keen...pooo!\n')
sleep(0.5)

print(f'Eu escolhi {pc_op} e você escolheu {user_op}!\n')

if user_op == pc_op:
    print('Empate!')
elif user_op == 'pedra' and pc_op == 'tesoura':
    print('Você ganhou!')
elif user_op == 'pedra' and pc_op == 'papel':
    print('Você perdeu!')
elif user_op == 'papel' and pc_op == 'tesoura':
    print('Você perdeu!')
elif user_op == 'papel' and pc_op == 'pedra':
    print('Você ganhou!')
elif user_op == 'tesoura' and pc_op == 'pedra':
    print('Você perdeu!')
elif user_op == 'tesoura' and pc_op == 'papel':
    print('Você ganhou!')
