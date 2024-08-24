n1=int(input('Digite um numero: '))

cont=0
for i in range(1,n1+1):
    if n1%i==0:
        print(f'\033[0;31;40m{i}\033[m',end=' ')
        cont+=1
    else:
        print(i,end=' ')
print('FIM\n')

if cont==2:
    print(f'Seu numero {n1} foi divisível 2 vezes por isso ele é PRIMO')
else:
    print(f'Seu numero {n1} foi divisivel {cont} vezes')
    