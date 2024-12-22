print('Gerador de Progressão Aritimética')

n1=int(input('Digite o primeiro numero: '))
razao=int(input('Digite a razão da PA: '))
c=1
#2-7-12-17-22-27...
while c <= 10:
    print(f'{n1} +' if c < 10 else f'{n1} =',end=' ')
    n1 = n1 + razao
    c+=1
print('FIM')
