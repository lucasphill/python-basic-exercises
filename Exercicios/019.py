import random

nome1=input('Digite o nome do primeiro aluno: ')
nome2=input('Digite o nome do segundo aluno: ')
nome3=input('Digite o nome do terceiro aluno: ')
nome4=input('Digite o nome do quarto aluno: ')

lista=[nome1,nome2,nome3,nome4]

print(f'O aluno escolhido foi {random.choice(lista)}') #utilizando random choice()
print(f'O aluno escolhido foi {lista[random.randrange(0,4)]}') #utilizando randrange()