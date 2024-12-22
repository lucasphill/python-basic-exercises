n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo numero: '))

if n1>n2:
    print(f'O primeiro numero é maior {n1} do que o segundo {n2}')
elif n2>n1:
    print(f'O segundo numero é maior {n2} do que o primeiro {n1}')
else:
    print('Os dois valores são iguais.')