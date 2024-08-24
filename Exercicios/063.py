quant = int(input('Digite quantos fatores quer mostrar: '))
contador=0

n1=0
n2=1
n3=0

while contador < quant-1:
    n3=n1+n2
    print(f'0 -> 1 -> 1 -> ' if contador == 0 else f'{n3} -> ', end='')
    n1=n2
    n2=n3
    contador+=1
print('FIM')

#####################################################################

n=int(input('Digite quantos fatores quer mostrar: '))
t1=0
t2=1
print(f'{t1} -> {t2}', end='')
cont=3
while cont <= n:
    t3=t1+t2
    print(f' -> {t3}', end='')
    t1=t2
    t2=t3
    cont+=1
print(' -> FIM')