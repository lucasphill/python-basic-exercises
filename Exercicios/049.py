n1=int(input('Digite um numero para mostrar a tabuada: '))

i=0
print('-'*13)
for i in range(1,11):
    print(f'{n1} * {i:2} = {n1*i}')
print('-'*13)