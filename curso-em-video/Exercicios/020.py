from random import sample,shuffle

nome1=input('Digite o nome do primeiro aluno: ')
nome2=input('Digite o nome do segundo aluno: ')
nome3=input('Digite o nome do terceiro aluno: ')
nome4=input('Digite o nome do quarto aluno: ')

lista=[nome1,nome2,nome3,nome4]

print(f'A ordem de apresentação será: {sample(lista,k=4)}') #sorteia a lista para apresentar

shuffle(lista) #randomiza a lista, depois apresenta
print(f'A ordem de apresentação será:')
print(lista)