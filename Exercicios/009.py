n1=int(input('Digite um numero para mostrar a tabuada: '))

i=0
print('-'*13)
while i <= 10:
    print(f'{n1} * {i:2} = {n1*i}')
    i+=1
print('-'*13)