import random

numeros = ()

for i in range(5):
    num=(random.randint(0,50),)
    numeros+=num

print(f'Os numeros sorteados são: {numeros}')
print(f'O maior numero é: {max(numeros)}')
print(f'O menor numero é: {min(numeros)}')