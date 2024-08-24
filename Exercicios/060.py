n1=int(input('Digite um numero para calcula o fatorial: '))
contador=n1-1
fatorial = n1

while contador > 0:
    fatorial = fatorial*contador
    contador-=1

print(f'O resultado fatorial do numero {n1} é {fatorial}')

#############################################################

n = int(input('Digite um numero para calcula o fatorial: '))
c = n
f = 1

print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f*=c
    c-=1
print(f'{f}')